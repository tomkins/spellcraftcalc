#!/usr/bin/env python
# ScWindow.py: Dark Age of Camelot Spellcrafting Calculator (main Window)
# See http://sc.aod.net for updates

# Copyright (C) 2003, 2004  James Lamanna (jlamanna@ugcs.caltech.edu)

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.




from qt import *
from B_ScWindow import *
from Item import *
from constants import *
from xml.dom.minidom import *
from MyStringIO import UnicodeStringIO
import types
import re
import string
import ItemLevel
import Options
import SC
import CraftWindow
import ReportWindow
import ReportParser
import MouseLabel
import DisplayWindow
import CraftBar
import SearchingCombo
import os
import os.path
import ItemPreview
import time
import locale
import traceback
import encodings
import codecs
import sys

import UIXML


class SCApp(B_SC):
    def __init__(self,parent = None,name = None,fl = 0):
        self.scroller = None
        self.totals = { }
        self.currentPieceTab = None
        self.currentJewelTab = None
        self.currentTypeTab = None
        self.extraSlotsOpen = False
        B_SC.__init__(self,parent,name,fl)
        self.font().setPointSize(8)
        self.recentFiles = []
        self.scroller = QScrollView(self)
        self.scroller.enableClipper(True)
        self.scroller.setGeometry(QRect(0, 0, 781, 526))
        self.scroller.resizeContents(self.width(), self.height())
        self.setGeometry(self.x(), self.y(), 781, 526)
        self.reportFile = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                'reports', 'Default_Config_Report.xml')
        self.coop = False

        self.menuBar = QMenuBar(self)
        pal = QPalette(self.palette().copy())
        self.menuBar.setPalette(pal)

        # Dummy widget, makes things look nicer on linux
        q = QWidget(self.scroller)
        q.setGeometry(0, 0, 2000, 2000)
        self.scroller.addChild(q, 0, 0)

        for c in self.children():
            if isinstance(c, QTabWidget) or isinstance(c, QGroupBox) \
                    or isinstance(c, QMenuBar) or isinstance(c, QLabel):
                c.reparent(self.scroller.viewport(), c.pos(), 1)
                if not isinstance(c, QMenuBar):
                    self.scroller.addChild(c, c.pos().x(), c.pos().y() + (self.menuBar.height() - 18))
                else:
                    self.scroller.addChild(c, c.pos().x(), c.pos().y())
        self.scroller.show()
        self.TypeTab.setFocusPolicy(QWidget.StrongFocus)
        self.growWidget(self.TypeTab, -72)
        self.PieceTab.setFocusPolicy(QWidget.StrongFocus)
        self.growWidget(self.PieceTab, -72)
        self.JewelTab.setFocusPolicy(QWidget.StrongFocus)
        self.growWidget(self.JewelTab, -72)

        # Change text color to red for error strings
        pal = QPalette(self.OcErrorString.palette().copy())
        cg = QColorGroup(self.DupErrorString.colorGroup())
        cg.setColor(QColorGroup.Foreground, QColor(255, 0, 0))
        pal.setActive(cg)
        self.DupErrorString.setPalette(pal)
        pal = QPalette(self.OcErrorString.palette().copy())
        cg = QColorGroup(self.OcErrorString.colorGroup())
        cg.setColor(QColorGroup.Foreground, QColor(255, 0, 0))
        pal.setActive(cg)
        self.OcErrorString.setPalette(pal)


        self.startup = 1
        self.pricingInfo = {}


        self.StrLabel = self.replaceLabel(self.StrLabel, 'Strength')
        self.ConLabel = self.replaceLabel(self.ConLabel, 'Constitution')
        self.DexLabel = self.replaceLabel(self.DexLabel, 'Dexterity')
        self.QuiLabel = self.replaceLabel(self.QuiLabel, 'Quickness')
        self.IntLabel = self.replaceLabel(self.IntLabel, 'Intelligence')
        self.PieLabel = self.replaceLabel(self.PieLabel, 'Piety')
        self.ChaLabel = self.replaceLabel(self.ChaLabel, 'Charisma')
        self.EmpLabel = self.replaceLabel(self.EmpLabel, 'Empathy')
        self.BodyLabel = self.replaceLabel(self.BodyLabel, 'Body Resist')
        self.ColdLabel = self.replaceLabel(self.ColdLabel, 'Cold Resist')
        self.HeatLabel = self.replaceLabel(self.HeatLabel, 'Heat Resist')
        self.EnergyLabel = self.replaceLabel(self.EnergyLabel, 'Energy Resist')
        self.MatterLabel = self.replaceLabel(self.MatterLabel, 'Matter Resist')
        self.SpiritLabel = self.replaceLabel(self.SpiritLabel, 'Spirit Resist')
        self.CrushLabel = self.replaceLabel(self.CrushLabel, 'Crush Resist')
        self.ThrustLabel = self.replaceLabel(self.ThrustLabel, 'Thrust Resist')
        self.SlashLabel = self.replaceLabel(self.SlashLabel, 'Slash Resist')
        self.HitsLabel = self.replaceLabel(self.HitsLabel, 'Hits')
        self.PowerLabel = self.replaceLabel(self.PowerLabel, 'Power')
        self.Focus_1 = self.replaceLabel(self.Focus_1, '')
        self.Focus_2 = self.replaceLabel(self.Focus_2, '')
        self.Focus_3 = self.replaceLabel(self.Focus_3, '')
        self.Focus_4 = self.replaceLabel(self.Focus_4, '')

        self.Name_1 = self.replaceGemLabel(self.Name_1)
        self.Name_2 = self.replaceGemLabel(self.Name_2)
        self.Name_3 = self.replaceGemLabel(self.Name_3)
        self.Name_4 = self.replaceGemLabel(self.Name_4)

        self.ItemLevelWindow = ItemLevel.ItemLevel(self, '', 1)
        self.DaocPath = ''
        self.realm = 'Albion'
        self.crafterSkill = 1001
        self.showDoneInMatsList = 0
        self.noteText = ''
        self.includeRacials = True
        OW = Options.Options(self, '', 0)
        OW.load()

        self.filemenu = QPopupMenu(self, 'FileMenu')
        self.filemenu.insertItem('&New', self.newFile, Qt.CTRL+Qt.Key_N)
        self.filemenu.insertItem('&Open', self.openFile, Qt.CTRL+Qt.Key_O)
        self.filemenu.insertItem('&Save', self.saveFile, Qt.CTRL+Qt.Key_S)
        self.filemenu.insertItem('Save &As...', self.saveAsFile)
        self.rf_menu = QPopupMenu(self, "Recent Files")
        self.updateRecentFiles(None)
        self.filemenu.insertItem('&Recent Files', self.rf_menu)
        self.filemenu.insertItem('E&xit', self, SLOT('close()'), Qt.CTRL+Qt.Key_X)
        self.menuBar.insertItem('&File', self.filemenu)

        self.reportmenu = QPopupMenu(self, 'FileMenu')
        self.reportmenu.insertItem('Choose Config Format...', self.chooseReportFile)
        self.reportmenu.insertItem('&Configuration', self.openConfigReport, Qt.CTRL+Qt.Key_C)
        self.reportmenu.insertItem('&Materials', self.openMaterialsReport, Qt.CTRL+Qt.Key_M)
        self.reportmenu.insertItem('&Set up Craft Bars...', self.openCraftBars)
        self.reportmenu.insertItem('&Generate UI XML (Beta)', self.generateUIXML)
        self.menuBar.insertItem('&Reports', self.reportmenu)

        self.swapGems = QPopupMenu(self, "SwapGems")
        self.swapGems.insertItem('Chest', 0)
        self.swapGems.connectItem(0, self.swapWithChest)
        self.swapGems.insertItem('Arms', 1)
        self.swapGems.connectItem(1, self.swapWithArms)
        self.swapGems.insertItem('Head', 2)
        self.swapGems.connectItem(2, self.swapWithHead)
        self.swapGems.insertItem('Legs', 3)
        self.swapGems.connectItem(3, self.swapWithLegs)
        self.swapGems.insertItem('Hands', 4)
        self.swapGems.connectItem(4, self.swapWithHands)
        self.swapGems.insertItem('Feet', 5)
        self.swapGems.connectItem(5, self.swapWithFeet)
        self.swapGems.insertItem('Right Hand', 6)
        self.swapGems.connectItem(6, self.swapWithRH)
        self.swapGems.insertItem('Left Hand', 7)
        self.swapGems.connectItem(7, self.swapWithLH)
        self.swapGems.insertItem('2 Handed', 8)
        self.swapGems.connectItem(8, self.swapWith2H)
        self.swapGems.insertItem('Ranged', 9)
        self.swapGems.connectItem(9, self.swapWithRanged)
        self.swapGems.insertItem('Spare', 10)
        self.swapGems.connectItem(10, self.swapWithSpare)
        self.swapGems.setItemEnabled(0, False)
        self.toolsmenu = QPopupMenu(self, 'ToolsMenu')
        self.toolsmenu.insertItem('S&wap Gems With...', self.swapGems)
        self.toolsmenu.insertItem('&Options...', self.openOptions)
        self.menuBar.insertItem('&Tools', self.toolsmenu)

        self.helpmenu = QPopupMenu(self, 'HelpMenu')
        self.helpmenu.insertItem('&About', self.aboutBox)
        self.menuBar.insertItem('&Help', self.helpmenu)

        self.initialize()
        self.pricingInfo = OW.getPriceInfo()
        self.restoreItem(Item())
        self.modified = 0

    
    def close(self, args):
        Options.Options(self).OK_pressed() # write out app config data to disk
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 'Some changes may not have been saved. Are you sure you want to quit?', 'Yes', 'No')
            if ret == 0:
                return QMainWindow.close(self, 1)
            else:
                return False
        else: return QMainWindow.close(self, False)

    def replaceLabel(self, lbl, eff):
        ml = MouseLabel.MouseLabel(eff, self, '', lbl.parent())
        ml.setText(lbl.text())
        ml.setGeometry(lbl.x(), lbl.y(), lbl.width(), lbl.height())
        lbl.hide()
        ml.show()
        return ml

    def replaceGemLabel(self, lbl):
        ml = MouseLabel.GemLabel(None, 0, self, '', lbl.parent())
        ml.setText(lbl.text())
        ml.setGeometry(lbl.x(), lbl.y(), lbl.width(), lbl.height())
        lbl.hide()
        ml.show()
        return ml

    def initialize(self):

# Options passed over from the options box
        self.noteText = ''
        self.craftMultiplier = 6
        self.save = 1
        self.FileNameLabel.setText('Unnamed')
        self.filename = None

        self.PieceTab.setCurrentPage(0)
        self.currentPieceTab = self.PieceTab.currentPage()
        self.JewelTab.setCurrentPage(0)
        self.currentJewelTab = self.JewelTab.currentPage()
        self.TypeTab.setCurrentPage(0)
        self.currentTypeTab = self.TypeTab.currentPage()
        self.currentPage = self.PieceTab.currentPage()
        self.currentTab = self.PieceTab
        
        self.Equipped.setChecked(1)
        #self.Equipped.hide()

        self.itemattrlist = { }
        for tab in TabList:
            self.itemattrlist[tab] = Item(tab)
        self.ItemLevel.setText('51')
        self.CharLevel.setText('50')

        # move it around because i screwed up the UI file :)
        for child in self.currentJewelTab.children():
            child.reparent(self.currentPieceTab, 0, child.pos(), 1)

        self.extraSlots = []
        self.switchOnType = {'drop' : [], 'player' : [] }
        self.switchOnType['drop'].append(self.QualEdit)
        self.switchOnType['drop'].append(self.SaveItem)
        self.switchOnType['drop'].append(self.ItemName_Label)
        self.switchOnType['drop'].append(self.ItemName)
        self.switchOnType['drop'].append(self.AFDPS_Label)
        self.switchOnType['drop'].append(self.AFDPS_Edit)
        self.switchOnType['drop'].append(self.Speed_Label)
        self.switchOnType['drop'].append(self.Speed_Edit)
        self.switchOnType['drop'].append(self.Bonus_Label)
        self.switchOnType['drop'].append(self.Bonus_Edit)
        self.switchOnType['drop'].append(self.Amount_Edit_1)
        self.switchOnType['drop'].append(self.Amount_Edit_2)
        self.switchOnType['drop'].append(self.Amount_Edit_3)
        self.switchOnType['drop'].append(self.Amount_Edit_4)
        self.switchOnType['drop'].append(self.Amount_Edit_5)
        self.switchOnType['drop'].append(self.Amount_Edit_6)
        self.extraSlots.append(self.Amount_Edit_7)
        self.extraSlots.append(self.Amount_Edit_8)
        self.extraSlots.append(self.Amount_Edit_9)
        self.extraSlots.append(self.Amount_Edit_10)
        self.switchOnType['drop'].append(self.Gem_Label_5)
        self.switchOnType['drop'].append(self.Gem_Label_6)
        self.extraSlots.append(self.Gem_Label_7)
        self.extraSlots.append(self.Gem_Label_8)
        self.extraSlots.append(self.Gem_Label_9)
        self.extraSlots.append(self.Gem_Label_10)
        self.switchOnType['drop'].append(self.Type_5)
        self.switchOnType['drop'].append(self.Type_6)
        self.extraSlots.append(self.Type_7)
        self.extraSlots.append(self.Type_8)
        self.extraSlots.append(self.Type_9)
        self.extraSlots.append(self.Type_10)
        self.switchOnType['drop'].append(self.Effect_5)
        self.switchOnType['drop'].append(self.Effect_6)
        self.extraSlots.append(self.Effect_7)
        self.extraSlots.append(self.Effect_8)
        self.extraSlots.append(self.Effect_9)
        self.extraSlots.append(self.Effect_10)
        self.switchOnType['drop'].append(self.Quality_5)
        self.switchOnType['drop'].append(self.Quality_6)
        self.extraSlots.append(self.Quality_7)
        self.extraSlots.append(self.Quality_8)
        self.extraSlots.append(self.Quality_9)
        self.extraSlots.append(self.Quality_10)
        self.switchOnType['drop'].append(self.MoreSlots)

        self.switchOnType['player'].append(self.QualDrop)
        self.switchOnType['player'].append(self.Points_Label)
        self.switchOnType['player'].append(self.Cost_Label)
        self.switchOnType['player'].append(self.Name_Label)
        self.switchOnType['player'].append(self.Points_1)
        self.switchOnType['player'].append(self.Points_2)
        self.switchOnType['player'].append(self.Points_3)
        self.switchOnType['player'].append(self.Points_4)
        self.switchOnType['player'].append(self.Cost_1)
        self.switchOnType['player'].append(self.Cost_2)
        self.switchOnType['player'].append(self.Cost_3)
        self.switchOnType['player'].append(self.Cost_4)
        self.switchOnType['player'].append(self.Name_1)
        self.switchOnType['player'].append(self.Name_2)
        self.switchOnType['player'].append(self.Name_3)
        self.switchOnType['player'].append(self.Name_4)
        self.switchOnType['player'].append(self.Imbue)
        self.switchOnType['player'].append(self.Slash_Label)
        self.switchOnType['player'].append(self.Total_Imbue)
        self.switchOnType['player'].append(self.Imbue_Label)
        self.switchOnType['player'].append(self.Overcharge_Label)
        self.switchOnType['player'].append(self.Overcharge)
        self.switchOnType['player'].append(self.Amount_Drop_1)
        self.switchOnType['player'].append(self.Amount_Drop_2)
        self.switchOnType['player'].append(self.Amount_Drop_3)
        self.switchOnType['player'].append(self.Amount_Drop_4)
        self.switchOnType['player'].append(self.ItemCost_Label)
        self.switchOnType['player'].append(self.ItemCost)
        self.switchOnType['player'].append(self.CraftButton)

        self.CharClass.clear()
        self.CharClass.insertStrList(ClassList[self.realm])
        self.CharRace.clear()
        self.CharRace.insertStrList(Races[self.realm])
        self.RaceChanged('')
        #self.connect(self, SLOT('show()'), self.shown)
    
    def asXML(self):
        document = Document()
        rootnode = document.createElement('SCTemplate')
        document.appendChild(rootnode)
        namenode = document.createElement('Name')
        namenode.appendChild(document.createTextNode(str(self.CharName.text())))
        classnode = document.createElement('Class')
        classnode.appendChild(document.createTextNode(unicode(self.CharClass.currentText())))
        racenode = document.createElement('Race')
        racenode.appendChild(document.createTextNode(unicode(self.CharRace.currentText())))
        levelnode = document.createElement('Level')
        levelnode.appendChild(document.createTextNode(unicode(self.CharLevel.text())))
        realmnode = document.createElement('Realm')
        realmnode.appendChild(document.createTextNode(self.realm))
        craftnode = document.createElement('CraftMultiplier')
        craftnode.appendChild(document.createTextNode(str(self.craftMultiplier)))
        notesnode = document.createElement('Notes')
        notesnode.appendChild(document.createTextNode(str(self.noteText)))
        skillnode = document.createElement('CrafterSkill')
        skillnode.appendChild(document.createTextNode(str(self.crafterSkill)))
        coopnode = document.createElement('Coop')
        coopnode.appendChild(document.createTextNode(str(self.coop)))
        rootnode.appendChild(namenode)
        rootnode.appendChild(classnode)
        rootnode.appendChild(levelnode)
        rootnode.appendChild(racenode)
        rootnode.appendChild(realmnode)
        rootnode.appendChild(notesnode)
        rootnode.appendChild(skillnode)
        rootnode.appendChild(coopnode)

        for key, item in self.itemattrlist.items():
            # use firstChild here because item.asXML() constructs a Document()
            rootnode.appendChild(item.asXML().firstChild)
        return document

    def show(self):
        QMainWindow.show(self)
        self.PlayerMade.setChecked(1)
        if self.startup:
            # Kludge...major kludge.
            self.PlayerToggled(1)
            self.startup = 0
    
    def currentTabLabel(self):
        return str(self.currentTab.tabLabel(self.currentPage))

    def PieceTabChanged(self,a0):
        if self.currentPieceTab is None: return
        if self.currentTab != self.PieceTab: return
        self.swapGems.setItemEnabled(TabList.index(self.currentTabLabel()), True)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        for child in self.currentPieceTab.children():
            child.reparent(a0, 0, child.pos(), 1)
        #if str(self.PieceTab.tabLabel(a0)) == 'Right Hand' \
        #        or str(self.PieceTab.tabLabel(a0)) == 'Left Hand' \
        #        or str(self.PieceTab.tabLabel(a0)) == '2 Handed' \
        #        or str(self.PieceTab.tabLabel(a0)) == 'Ranged' \
        #        or str(self.PieceTab.tabLabel(a0)) == 'Spare':
        #    self.Equipped.show()
        #    self.Equipped.setChecked(0)
        #else:
        #    self.Equipped.hide()
        self.Equipped.show()
        self.currentPieceTab = a0
        self.currentPage = a0
        self.swapGems.setItemEnabled(TabList.index(self.currentTabLabel()), False)
        self.restoreItem(self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel())))
        self.calculate()
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        extraused = False
        if item.getAttr('ActiveState') == 'drop':
            for i in range(6, 10):
                if item.getSlotAttr('drop', i, 'Type') != 'Unused':
                    extraused = True
                    break
        if not extraused:
            if self.extraSlotsOpen:
                self.openMoreSlots()
            for w in self.extraSlots:
                w.hide()
        else:
            if not self.extraSlotsOpen:
                self.openMoreSlots()

    def JewelTabChanged(self,a0):
        if self.currentJewelTab is None: return
        if self.currentTab != self.JewelTab: return
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        for child in self.currentJewelTab.children():
            child.reparent(a0, 0, child.pos(), 1)
       #self.Equipped.hide()
        self.currentJewelTab = a0
        self.currentPage = a0
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.restoreItem(self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel())))
        self.calculate()

        extraused = False
        if item.getAttr('ActiveState') == 'drop':
            for i in range(6, 10):
                if item.getSlotAttr('drop', i, 'Type') != 'Unused':
                    extraused = True
                    break
        if not extraused:
            if self.extraSlotsOpen:
                self.openMoreSlots()
            for w in self.extraSlots:
                w.hide()
        else:
            if not self.extraSlotsOpen:
                self.openMoreSlots()

    def FixupItemLevel(self):
        if str(self.ItemLevel.text()) == '' \
                or re.compile('\D').search(str(self.ItemLevel.text())):
            itemimbue = 0
        else:
            itemlevel = int(str(self.ItemLevel.text()))
            if itemlevel > 51: itemlevel = 51
            if itemlevel < 1: itemlevel = 1
            self.ItemLevel.setText('%d' % itemlevel)

    def storeItem(self, item):
        if item is None: return
        self.FixupItemLevel()
        item.loadAttr('Location', self.currentTabLabel())
        item.loadAttr('Realm', self.realm)
        item.loadAttr('Level', unicode(self.ItemLevel.text()))
        if self.Equipped.isChecked():
            item.loadAttr('Equipped', '1')
        else:
            item.loadAttr('Equipped', '0')
        if self.PlayerMade.isChecked():
            state = 'player'
            toprng = 5
            item.loadAttr('ItemQuality', unicode(self.QualDrop.currentText()))
        else:
            state = 'drop'
            toprng = 11
            item.loadAttr('ItemName', unicode(self.ItemName.text())) 
            item.loadAttr('AFDPS', unicode(self.AFDPS_Edit.text()))
            item.loadAttr('Speed', unicode(self.Speed_Edit.text())) 
            item.loadAttr('Bonus', unicode(self.Bonus_Edit.text()))
            item.loadAttr('ItemQuality', unicode(self.QualEdit.text()))
        item.loadAttr('ActiveState', state)
        for slot in range(1, toprng):
            typectrl = getattr(self, 'Type_%d' % slot)
            effectctrl = getattr(self, 'Effect_%d' % slot)
            if state == 'drop':
                amountctrl = getattr(self, 'Amount_Edit_%d' % slot)
                qua = '99'
                item.loadSlotAttrs(state, slot-1, 
                    typectrl.currentText(), 
                    amountctrl.text(),
                    effectctrl.currentText(), 
                    qua,
                    item.getSlotAttr(state, slot-1, 'Time'),
                    item.getSlotAttr(state, slot-1, 'Remakes'),
                    item.getSlotAttr(state, slot-1, 'Done'))
            else:
                amountctrl = getattr(self, 'Amount_Drop_%d' % slot)
                qua = getattr(self, 'Quality_%d' % slot).currentText()
                item.loadSlotAttrs(state, slot-1, 
                    typectrl.currentText(), 
                    amountctrl.currentText(),
                    effectctrl.currentText(), 
                    qua,
                    item.getSlotAttr(state, slot-1, 'Time'),
                    item.getSlotAttr(state, slot-1, 'Remakes'),
                    item.getSlotAttr(state, slot-1, 'Done'))
        self.itemattrlist[self.currentTabLabel()] = item

    def restoreItem(self, item):
        if item is None: return
        self.save = 0
        itemtype = item.getAttr('ActiveState')
        if itemtype == 'player':
            self.PlayerMade.setChecked(1)
            self.showPlayerWidgets()
            toprng = 5
            typelist = TypeList
        else:
            self.Drop.setChecked(1)
            self.showDropWidgets()
            toprng = 11
            typelist = DropTypeList
        self.ItemLevel.setText(item.getAttr('Level'))
        location = item.getAttr('Location')
        #if location != 'Right Hand' \
        #        and location != 'Left Hand' \
        #        and location != '2 Handed' \
        #        and location != 'Ranged' \
        #        and location != 'Spare':
        #    item.loadAttr('Equipped', '1')
        #if self.Equipped.isVisible():
        self.Equipped.setChecked(int(item.getAttr('Equipped')))
        for slot in range(1, toprng):
            typecombo = getattr(self, 'Type_%d' % slot)
            quacombo = getattr(self, 'Quality_%d' % slot)
            typecombo.clear()
            typecombo.insertStrList(typelist)
            gemtype = item.getSlotAttr(itemtype, slot-1, 'Type')
            typecombo.setCurrentItem(typelist.index(gemtype))
            gemtype = re.sub(' ', '', gemtype)
            self.UpdateCombo(slot)
            if (gemtype == 'Skill' or gemtype == 'Focus' or gemtype == 'Stat') and itemtype == 'drop':
                effectlist = eval('Drop%sList' % gemtype, globals(), globals())
            else:
                effectlist = eval('%sList' % gemtype, globals(), globals())
            if type(effectlist) != types.ListType:
                effectlist = effectlist[self.realm]
            effectlist = map(lambda(x): x[0], effectlist)
            gemeffect = item.getSlotAttr(itemtype, slot-1, 'Effect')
            if gemeffect in effectlist:
                getattr(self, 'Effect_%d' % slot).setCurrentItem(effectlist.index(gemeffect))
                #eval('self.Effect_%d.setCurrentItem(%d)' % (slot, effectlist.index(gemeffect)))
                
            if itemtype == 'drop':
                am = item.getSlotAttr(itemtype, slot-1, 'Amount')
                amedit = getattr(self, 'Amount_Edit_%d' % slot)
                amedit.setText(am)
            else:
                gemamount = item.getSlotAttr(itemtype, slot-1, 'Amount')
                amountlist = eval('%sValues' % gemtype, globals(), globals())
                if gemamount in amountlist:
                    getattr(self, 'Amount_Drop_%d' % slot).setCurrentItem(
                            amountlist.index(gemamount))
                    #eval('self.Amount_Drop_%d.setCurrentItem(%d)' % (slot, 
                    #    amountlist.index(gemamount)))
            gemqua = item.getSlotAttr(itemtype, slot-1, 'Qua')
            if gemqua in QualityValues:
                if quacombo.count() > 0:
                    quacombo.setCurrentItem(QualityValues.index(gemqua))
        if itemtype == 'drop':
            self.AFDPS_Edit.setText(item.getAttr('AFDPS'))
            self.Speed_Edit.setText(item.getAttr('Speed'))
            self.Bonus_Edit.setText(item.getAttr('Bonus'))
            self.QualEdit.setText(item.getAttr('ItemQuality'))
            self.ItemName.setText(item.getAttr('ItemName'))
        else:
            if item.getAttr('ItemQuality') != '':
                self.QualDrop.setCurrentItem(
                    QualityValues.index(item.getAttr('ItemQuality')))
        self.save = 1

    def calculate(self):
        focusnum = 1
        charclass = unicode(self.CharClass.currentText())
        for effect, gem in ResistList:
            self.totals[effect[:string.find(effect, ' ')]] = 0
        for effect, gem in StatList:
            self.totals[effect[:3]] = 0
        self.totals['Hits'] = 0
        self.totals['Power'] = 0
        skillTotals = {}
        otherTotals = {}
        capTotals = {}
        self.Focus_1.setText('')
        self.Focus_2.setText('')
        self.Focus_3.setText('')
        self.Focus_4.setText('')
        self.DupErrorString.setText('')
        self.OcErrorString.setText('')
        totalutility = 0.0
        totalcost = 0
        for key, item in self.itemattrlist.items():
           # if key != '2 Handed' and \
           #         key != 'Right Hand' and \
           #         key != 'Left Hand' and \
           #         key != 'Ranged' and \
           #         key != 'Spare':
           #     item.loadAttr('Equipped', '1')
            utility = 0.0
            itemtype = item.getAttr('ActiveState')
            itemcost = 0
            if itemtype == 'player':
                toprng = 4
            else:
                toprng = 10
            gemeffects = []
            for i in range(0, toprng):
                gemtype = re.sub(' ', '', item.getSlotAttr(itemtype, i, 'Type'))
                if item.getSlotAttr(itemtype, i, 'Amount') == '':
                    amount = 0
                else:
                    amount = re.sub('[^\d]', '', item.getSlotAttr(itemtype, i, 'Amount'))
                    if amount == '': amount = '0'
                    amount = int(amount)
                effect = item.getSlotAttr(itemtype, i, 'Effect')
                if effect != '' and [gemtype, effect] in gemeffects:
                    self.DupErrorString.setText('Two of same type of gem on %s' % key)
                gemeffects.append([gemtype, effect])
                if amount == '' or gemtype == 'Unused' or amount == 0 or itemtype == 'drop':
                    cost = 0    
                    remakecost = 0
                else:
                    costindex = eval('%sValues' % gemtype, globals(), globals()).index(str(amount))
                    cost = GemCosts[costindex]
                    remakecost = RemakeCosts[costindex] * int(item.getSlotAttr(itemtype, i, 'Remakes'))
                    if 'All ' in effect:
                        cost += 60 * costindex
                        cost = cost * 3
                        if remakecost > 0:
                            remakecost += 180 * costindex
                        if effect != 'All Focus Bonus' and amount > 1:
                            self.DupErrorString.setText('Invalid ' + effect + ' on ' + key)
                    elif gemtype == 'Resist' or gemtype == 'Focus':
                        cost += 60 * costindex
                        if remakecost > 0:
                            remakecost += 60 * costindex
                    itemcost += cost + remakecost
                if itemtype == 'player' and key == self.currentTabLabel():
                    getattr(self, 'Cost_%d' % (i+1)).setText(SC.formatCost(cost+remakecost))
                    #eval('self.Cost_%d.setText("%s")' % (i+1, 
                    #    SC.formatCost(cost+remakecost)))
                if gemtype == 'Skill':
                        if effect == 'All Magic Skill Bonus'\
                            or effect == 'All Melee Skill Bonus'\
                            or effect == 'All Dual Wield Skill Bonus'\
                            or effect == 'Archery Skill Bonus':

                            if effect == 'All Melee Skill Bonus':
                                utility += amount * 5
                            for e in AllBonusList[charclass][effect]:
                                if effect == 'All Magic Skill Bonus'\
                                    or effect == 'All Dual Wield Skill Bonus'\
                                    or effect == 'Archery Skill Bonus':
                                    utility += amount * 5
                                if item.getAttr('Equipped') == '1':
                                    if not skillTotals.has_key(e):
                                        skillTotals[e] = amount
                                    else:
                                        skillTotals[e] += amount
                        else:           
                            utility += amount * 5
                            if item.getAttr('Equipped') == '1':
                                if not skillTotals.has_key(effect):
                                    skillTotals[effect] = amount
                                else:
                                    skillTotals[effect] += amount
                elif gemtype == 'Focus':
                    utility += 1
                    if item.getAttr('Equipped') == '1':
                        if effect == 'All Focus Bonus':
                            for f in AllBonusList[charclass][effect]:
                                if focusnum <= 4:
                                    getattr(self, 'Focus_%d' % focusnum).setText(
                                        '%s %s' % (amount, f)) 
                                    setattr(getattr(self, 'Focus_%d' % focusnum), 'effect', f)
                                    #exec('self.Focus_%d.effect = "%s"' 
                                    #    % (focusnum, f))
                                focusnum += 1
                        else:
                            if focusnum <= 4:
                                getattr(self, 'Focus_%d' % focusnum).setText(
                                    '%s %s' % (amount, effect)) 
                                setattr(getattr(self, 'Focus_%d' % focusnum), 'effect', effect)
                                #eval('self.Focus_%d.setText("%s %s")' 
                                #    % (focusnum, amount, effect))
                                #exec('self.Focus_%d.effect = "%s"' 
                                #    % (focusnum, effect))
                            focusnum += 1
                elif gemtype == 'Power':
                    utility += amount * 2
                    if item.getAttr('Equipped') == '1':
                        self.totals[gemtype] += amount
                elif gemtype == 'Hits':
                    utility += amount / 4.0
                    if item.getAttr('Equipped') == '1':
                        self.totals[gemtype] += amount
                elif gemtype == 'Resist':
                    utility += amount * 2
                    if item.getAttr('Equipped') == '1':
                        self.totals[effect[:string.find(effect, ' ')]] += amount
                elif gemtype == 'Stat':
                    if effect == 'Acuity':
                        for e in AllBonusList[charclass][effect]:
                            utility += amount * 2.0 / 3.0
                            if item.getAttr('Equipped') == '1':
                                self.totals[e[:3]] += amount
                    else:
                        utility += amount * 2.0 / 3.0
                        if item.getAttr('Equipped') == '1':
                            self.totals[effect[:3]] += amount
                elif gemtype == 'OtherBonus':
                    if item.getAttr('Equipped') == '1':
                        if not otherTotals.has_key(effect):
                            otherTotals[effect] = amount
                        else:
                            otherTotals[effect] += amount
                elif gemtype == 'CapIncrease':
                    if item.getAttr('Equipped') == '1':
                        oeffect = effect + ' Cap'
                        if not otherTotals.has_key(oeffect):
                            otherTotals[oeffect] = amount
                        else:
                            otherTotals[oeffect] += amount
                        if effect == 'Acuity':
                            effect = AllBonusList[charclass][effect]
                            if len(effect) == 0:
                                continue
                            effect = effect[0][:3]
                        elif effect != 'Hits' and effect != 'Power' and effect != 'AF':
                            effect = effect[:3]
                        if not capTotals.has_key(effect):
                            capTotals[effect] = amount
                        else:
                            capTotals[effect] += amount
                        if effect == 'Hits':
                            if capTotals['Hits'] > 200:
                                capTotals['Hits'] = 200 
                        elif capTotals[effect] > 25:
                            capTotals[effect] = 25
            if item.getAttr('Equipped') == '1':
                totalutility += utility
                totalcost += itemcost
            if itemtype == 'player':
                itemimbue = self.getItemImbue(item)
                imbue = self.calcImbue(item, key == self.currentTabLabel())
                if (imbue - itemimbue) >= 6:
                    self.OcErrorString.setText('Impossible Overcharge on %s' % key)
                elif imbue > (itemimbue+0.5):
                    success = -OCStartPercentages[int(imbue-itemimbue)]
                    for i in range(0, 4):
                        if item.getSlotAttr(itemtype, i, 'Type') == 'Unused':
                            success += GemQualOCModifiers['94']
                        else:
                            success += GemQualOCModifiers[item.getSlotAttr(itemtype, i, 'Qua')]
                    success += ItemQualOCModifiers[unicode(self.QualDrop.currentText())]
                    success += (self.crafterSkill - 500) / 10
                    if self.crafterSkill <= 50: success -= 450
            if key == self.currentTabLabel():
                self.Utility.setText('%3.1f' % utility)
                if self.PlayerMade.isChecked():
                    self.Total_Imbue.setText(unicode(itemimbue))
                    self.Imbue.setText('%3.1f' % imbue)
                    self.ItemCost.setText(SC.formatCost(itemcost))
                    for i in range(1, 5):
                        n = getattr(self, 'Name_%d' % i)
                        n.setText(SC.getGemName(item, i-1))
                        n.item = item
                        n.itemslot = i-1
                        if item.getSlotAttr(itemtype, i-1, 'Done') == '1':
                            getattr(self, 'Gem_Label_%d' % i).setEnabled(0)
                        else:
                            getattr(self, 'Gem_Label_%d' % i).setEnabled(1)
                    if (imbue - itemimbue) >= 6:
                        self.Overcharge.setText('Impossible!')
                    elif imbue > (itemimbue+0.5):
                        if success < 0:
                            self.Overcharge.setText('BOOM! (%d%%)' % success)
                        else:
                            self.Overcharge.setText('%d%%' % success)
                    else:
                        self.Overcharge.setText('None')
        for (key, val) in self.totals.items():
            if self.TotalBonus.isChecked():
                if self.includeRacials:
                    if key in map(lambda(x): x[0][:string.find(x[0], ' ')], ResistList):
                        rr = str(getattr(self, key+'RR').text())
                        if rr != '-':
                            val += int(rr[1:-1])
                getattr(self, key).setText(unicode(val))
            else:
                if capTotals.has_key(key):
                    capmod = capTotals[key]
                else:
                    capmod = 0
                capfunc = getattr(self, Caps[key])
                getattr(self, key).setText(unicode(int(capmod) + capfunc() - val))
        self.TotalUtility.setText('%3.1f' % totalutility)
        self.TotalCost.setText(SC.formatCost(totalcost))
        self.SkillsList.clear()
        self.OtherBonusList.clear()
        for skill, amount in skillTotals.items():
            if self.TotalBonus.isChecked():
                self.SkillsList.insertItem('%d %s' % (amount, skill))
            else:
                capfunc = getattr(self, Caps['Skill'])
                self.SkillsList.insertItem('%d %s' % (capfunc() - amount, skill))
        for bonus, amount in otherTotals.items():
            if self.TotalBonus.isChecked():
                self.OtherBonusList.insertItem('%d %s' % (amount, bonus))
            else:
                cap = 10
                if bonus[-3:] == 'Cap':
                    if bonus[:4] == 'Hits':
                        cap = 200
                    else:
                        cap = 25
                else:
                    if bonus in HighCapBonusList:
                        cap = 25
                self.OtherBonusList.insertItem('%d %s' % (cap - amount, bonus))
                
        self.TotalPrice.setText(SC.formatCost(self.computePrice()))
        
    def computePrice(self):
        price = 0
        cost = 0
        for key, item in self.itemattrlist.items():
            itemcost = 0
            itemtype = item.getAttr('ActiveState')
            if itemtype == 'drop': continue
            if item.getAttr('Equipped') == '0': continue
            for i in range(0, 4):
                gemcost, tierlvl = SC.computeGemCost(item, i)
                cost += gemcost
                itemcost += gemcost
                if gemcost > 0:
                    price += self.pricingInfo.get('PPGem', 0) * 10000
                    if self.pricingInfo.get('HourInclude', 0):
                        price += self.pricingInfo.get('Hour', 0) * 10000 * int(item.getSlotAttr(itemtype, i, 'Time')) / 60.0
                    if self.pricingInfo.get('TierInclude', 0):
                        tierp = self.pricingInfo.get('Tier', {})
                        price += float(tierp.get(str(tierlvl), 0)) * 10000
                    if self.pricingInfo.get('QualInclude', 0):
                        gemqual = item.getSlotAttr(itemtype, i, 'Qua')
                        qualp = self.pricingInfo.get('Qual', {})
                        price += (gemcost * float(qualp.get(gemqual, 0)) / 100.0)
            if self.pricingInfo.get('PPInclude', 0):
                imbuepts = self.calcImbue(item, 0)
                price += self.pricingInfo.get('PPImbue', 0) * 10000 * imbuepts
                price += self.pricingInfo.get('PPOC', 0) * 10000 \
                    * max(0, int(imbuepts - self.getItemImbue(item)))
                if itemcost > 0:
                    price += self.pricingInfo.get('PPLevel', 0) * 10000 * int(item.getAttr('Level'))
            if itemcost > 0:
                price += self.pricingInfo.get('PPItem', 0) * 10000
        price += self.pricingInfo.get('PPOrder', 0) * 10000
        price += cost * self.pricingInfo.get('General', 0) / 100.0
        if not self.pricingInfo.get('CostInPrice', 1):
            return int(price)
        else:
            return int(cost + price)

    def getItemImbue(self, item):
        itemlevel = item.getAttr('Level')
        if item.getAttr('ItemQuality') == '':
            item.loadAttr('ItemQuality', '94')
        if itemlevel == '':
            itemimbue = 0
        else:
            itemimbue = ImbuePts[int(itemlevel)-1]\
                    [int(item.getAttr('ItemQuality'))-94]

        return itemimbue
            

    def calcImbue(self, item, display):
        itemtype = item.getAttr('ActiveState')
        if itemtype == 'drop': return 0
        mvals = []
        for i in range(0, 4):
            type = item.getSlotAttr(itemtype, i, 'Type')
            amount = item.getSlotAttr(itemtype, i, 'Amount')
            if amount == '': 
                mval = 0.0
            elif type == 'Focus':
                mval = 1.0
            elif type == 'Unused':
                mval = 0.0
            elif type == 'Stat':
                mval = ((int(amount) - 1) / 3.0) * 2 + 1
            elif type == 'Resist' or type == 'Power':
                mval = (int(amount) - 1) * 2
                if mval == 0: mval = 1.0
            elif type == 'Hits':
                mval = int(amount) / 4.0
            elif type == 'Skill':
                mval = (int(amount) - 1) * 5.0
                if mval == 0: mval = 1.0    
            if display:
                getattr(self, 'Points_%d' % (i+1)).setText('%3.1f' % mval)
            mvals.append(mval)
        maximbue = max(mvals)
        if display:
            for j in range(0, len(mvals)):
                if j != mvals.index(maximbue):
                    getattr(self, 'Points_%d' % (j+1)).setText('%3.1f' % (mvals[j] / 2.0))
                else:
                    getattr(self, 'Points_%d' % (j+1)).setText('%3.1f' % mvals[j])
        mvals.remove(maximbue)
        totalimbue = ((maximbue * 2 + sum(mvals)) / 2.0)
        return totalimbue
        
    def getMultiplier(self, type):
        return ImbueMultipliers[type]

    def AttributeCap(self):
        cltext = str(self.CharLevel.text())
        if cltext == '': 
            level = 1
        else:
            level = max(min(50, int(cltext)), 1)
        self.CharLevel.setText(str(level))
        return int(level * 1.5)

    def ResistCap(self):
        cltext = str(self.CharLevel.text())
        if cltext == '': 
            level = 1
        else:
            level = max(min(50, int(cltext)), 1)
        self.CharLevel.setText(str(level))
        return (level / 2) + 1

    def SkillCap(self):
        cltext = str(self.CharLevel.text())
        if cltext == '': 
            level = 1
        else:
            level = max(min(50, int(cltext)), 1)
        self.CharLevel.setText(str(level))
        return (level / 5) + 1

    def HitsCap(self):
        cltext = str(self.CharLevel.text())
        if cltext == '': 
            level = 1
        else:
            level = max(min(50, int(cltext)), 1)
        self.CharLevel.setText(str(level))
        return level * 4

    def PowerCap(self):
        cltext = str(self.CharLevel.text())
        if cltext == '': 
            level = 1
        else:
            level = max(min(50, int(cltext)), 1)
        self.CharLevel.setText(str(level))
        return (level / 2) + 1

    def UpdateCombo(self, num):
        effcombo = getattr(self, 'Effect_%d' % num)
        typecombo = getattr(self, 'Type_%d' % num)
        qualcombo = getattr(self, 'Quality_%d' % num)
        effcombo.clear()
        qualcombo.clear()
        typetext = re.sub(' ', '', unicode(typecombo.currentText()))
        if self.PlayerMade.isChecked():
            amountcombo = getattr(self, 'Amount_Drop_%d' % num)
        else:
            amountedit = getattr(self, 'Amount_Edit_%d' % num)
        if typetext != 'Unused':
            if (typetext == 'Focus' or typetext == 'Skill' or typetext == 'Stat') and self.Drop.isChecked():
                listname = 'Drop%sList' % typetext
            else:
                listname = '%sList' % typetext
            valuesname = '%sValues' % typetext
            if type(eval(listname, globals(), globals())) == types.ListType:
                effcombo.insertStrList(map(lambda(x):x[0],eval(listname, globals(), globals())))
            else:
                effcombo.insertStrList(map(lambda(x):x[0],eval(listname, globals(), globals())[self.realm]))
            if self.PlayerMade.isChecked():
                amountcombo = getattr(self, 'Amount_Drop_%d' % num)
                amountcombo.clear()
                amountcombo.insertStrList(eval(valuesname, globals(), globals()))
            else:
                amountedit.setText('0')
        else:
            if self.PlayerMade.isChecked():
                amountcombo.clear()
            else:
                amountedit.clear()
        qualcombo.insertStrList(QualityValues)
        qualcombo.setCurrentItem(len(QualityValues)-2)

    def RaceChanged(self, a0, calc=True):
        race = str(self.CharRace.currentText())
        for r in ResistList:
            rt = r[0]
            rt = rt[:string.find(rt, ' ')]
            if RacialResists[race].has_key(rt):
                getattr(self, rt + 'RR').setText('('+str(RacialResists[race][rt])+')')
            else:
                getattr(self, rt + 'RR').setText('-')
        if calc:
            self.calculate()

    def Type_1_Changed(self,a0):
        self.modified = 1
        self.UpdateCombo(1)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        self.calculate()

    def Type_2_Changed(self,a0):
        self.modified = 1
        self.UpdateCombo(2)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        self.calculate()

    def Type_3_Changed(self,a0):
        self.modified = 1
        self.UpdateCombo(3)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        self.calculate()

    def Type_4_Changed(self,a0):
        self.modified = 1
        self.UpdateCombo(4)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        self.calculate()

    def Type_5_Changed(self,a0):
        self.modified = 1
        self.UpdateCombo(5)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        self.calculate()

    def Type_6_Changed(self,a0):
        self.modified = 1
        self.UpdateCombo(6)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        self.calculate()

    def Type_7_Changed(self,a0):
        self.modified = 1
        self.UpdateCombo(7)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        self.calculate()

    def Type_8_Changed(self,a0):
        self.modified = 1
        self.UpdateCombo(8)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        self.calculate()

    def Type_9_Changed(self,a0):
        self.modified = 1
        self.UpdateCombo(9)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        self.calculate()

    def Type_10_Changed(self,a0):
        self.modified = 1
        self.UpdateCombo(10)
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        self.calculate()

    def showDropWidgets(self):
        for w in self.switchOnType['player']:
            w.hide()
        for w in self.switchOnType['drop']:
            w.show()
        for i in range(1, 11):
            q = getattr(self, 'Quality_%d' % i)
            q.setEnabled(0)
        # By setting this to True and calling openMoreSlots() it will hide them
        if self.extraSlotsOpen:
            self.openMoreSlots()
        else:
            for w in self.extraSlots:
                w.hide()

    def showPlayerWidgets(self):
        for w in self.switchOnType['player']:
            w.show()
        for w in self.switchOnType['drop']:
            w.hide()
        for i in range(1, 5):
            q = getattr(self, 'Quality_%d' % i)
            q.setEnabled(1)
        if self.extraSlotsOpen:
            self.openMoreSlots()
        else:
            for w in self.extraSlots:
                w.hide()
        self.calculate()

    def DropToggled(self,a0):
        self.modified = 1
        if not a0: 
            return
        self.showDropWidgets()
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        item.loadAttr('ActiveState','drop')
        if self.save:
            self.restoreItem(item)
            self.calculate()


    def PlayerToggled(self, a0):
        self.modified = 1
        if not a0: 
            return
        self.showPlayerWidgets()
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        item.loadAttr('ActiveState','player')
        if self.save:
            self.restoreItem(item)
            self.calculate()

    def TypeTabChanged(self,a0):
        if (str(self.TypeTab.tabLabel(self.currentTypeTab)) == str(self.TypeTab.tabLabel(a0))) or self.currentTypeTab is None:
            return
        if str(self.TypeTab.tabLabel(self.currentTypeTab)) == 'Jewelry':
            curtab = self.JewelTab
            othertab = self.PieceTab
            for i in range(0, 11):
                self.swapGems.setItemEnabled(i, True)
        else:
            curtab = self.PieceTab
            othertab = self.JewelTab
            for i in range(0, 11):
                self.swapGems.setItemEnabled(i, False)

        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        for child in curtab.currentPage().children():
            child.reparent(othertab.currentPage(), 0, child.pos(), 1)
        self.currentTypeTab = a0
        self.currentPage = othertab.currentPage()
        self.currentTab = othertab
        if self.currentTab == self.JewelTab:
            #self.Equipped.hide()
            pass
        else:
            self.swapGems.setItemEnabled(TabList.index(self.currentTabLabel()), False)
            #if self.currentTabLabel() == 'Right Hand' \
            #        or self.currentTabLabel() == 'Left Hand' \
            #        or self.currentTabLabel() == '2 Handed' \
            #        or self.currentTabLabel() == 'Ranged' \
            #        or self.currentTabLabel() == 'Spare':
            #    self.Equipped.show()
            #    self.Equipped.setChecked(0)
            #else:
            #    self.Equipped.hide()
        self.Equipped.show()
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.restoreItem(item)
        if self.extraSlotsOpen:
            self.openMoreSlots()
        for w in self.extraSlots:
            w.hide()

    def AmountChanged(self,a0):
        self.modified = 1
        if self.save:
            item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
            self.storeItem(item)
        self.calculate()

    def recalculate(self,a0):
        self.modified = 1
        if self.save:
            item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
            self.storeItem(item)
        self.calculate()

    def ClearCurrentItem(self):
        item = Item(self.currentTabLabel())
        self.itemattrlist[self.currentTabLabel()] = item
        self.restoreItem(item)
        self.calculate()

    def DistanceCapSet(self):
        self.calculate()
    def TotalBonusSet(self):
        self.calculate()

    def Save_Item(self):
        itemname = unicode(self.ItemName.text())
        if itemname == '':
            QMessageBox.critical(None, 'Error!', 
                'Cannot save item - You must specifify a name!', 'OK')
            return
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        ext = FileExt[self.currentTabLabel()]
        if type(ext) == types.ListType:
            ext = ext[0]
        itemdir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'items', self.realm, ext)
        if not os.path.exists(itemdir):
            os.makedirs(itemdir)
        filename = os.path.join(itemdir, string.replace(itemname, ' ', '_') + '_' \
            + ext \
            + '.xml')
        item.save(filename)
        QMessageBox.information(None, 'Success!',
                '%s successfully saved!' % itemname, 'OK')
        
    def Load_Item(self):
        ext = FileExt[self.currentTabLabel()]
        extstr = ''
        if type(ext) == types.ListType:
            for e in ext:
                extstr += '*%s.xml *.%s ' % (e, e)
            ext = ext[0]
        else:
            extstr = '*%s.xml *.%s' % (ext, ext)
        itemdir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'items', self.realm, ext)
        Qfd = QFileDialog(itemdir, "Items (%s)" % extstr, self, None, 1)
        Qfp = ItemPreview.ItemPreview(Qfd, self) 
        Qfd.setInfoPreview(Qfp, Qfp.pu)
        Qfd.setInfoPreviewEnabled(1)
        Qfd.setPreviewMode(QFileDialog.Info)
        Qfd.setMode(QFileDialog.ExistingFile)
        Qfd.child('unnamed', 'QSplitter').setSizes([165, 150])
        if Qfd.exec_loop():
            filename = Qfd.selectedFile()
            if filename is not None and unicode(filename) != '':
                item = Item(self.currentTabLabel())
                item.loadAttr('Realm', self.realm)
                if item.load(unicode(filename)) == -1 : return
                if string.lower(item.getAttr('Realm')) != string.lower(self.realm)\
                    and string.lower(item.getAttr('Realm')) != 'all'\
                    and not self.coop:
                    QMessageBox.critical(None, 'Error!', 'You are trying to load an item for another realm!', 'OK')
                    return
                item.loadAttr('Location', self.currentTabLabel())
                self.itemattrlist[self.currentTabLabel()] = item
                self.restoreItem(item)
                self.modified = 1

    def ItemLevelShow(self):
        level = self.ItemLevelWindow.exec_loop()
        if level != -1:
            self.ItemLevel.setText(str(level))

    def EquippedClicked(self):
        item = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        self.storeItem(item)
        # Someone said this feature existed in Leladia's, but it doesn't seem to be....
        #if (self.currentTabLabel() == '2 Handed'\
        #       or self.currentTabLabel() == 'Ranged')\
        #       and self.Equipped.isChecked():
        #    i = self.itemattrlist.get('Left Hand', Item('Left Hand'))
        #    i.loadAttr('Equipped', '0')
        #    self.itemattrlist['Left Hand'] = i
        #    i = self.itemattrlist.get('Right Hand', Item('Right Hand'))
        #    i.loadAttr('Equipped', '0')
        #    self.itemattrlist['Right Hand'] = i
        #    if self.currentTabLabel() == '2 Handed':
        #        i = self.itemattrlist.get('Ranged', Item('Ranged'))
        #        i.loadAttr('Equipped', '0')
        #        self.itemattrlist['Ranged'] = i
        #    else:
        #        i = self.itemattrlist.get('2 Handed', Item('2 Handed'))
        #        i.loadAttr('Equipped', '0')
        #        self.itemattrlist['2 Handed'] = i
        #elif (self.currentTabLabel() == 'Right Hand'\
        #       or self.currentTabLabel() == 'Left Hand')\
        #       and self.Equipped.isChecked():
        #    i = self.itemattrlist.get('2 Handed', Item('2 Handed'))
        #    i.loadAttr('Equipped', '0')
        #    self.itemattrlist['2 Handed'] = i
        #    i = self.itemattrlist.get('Ranged', Item('Ranged'))
        #    i.loadAttr('Equipped', '0')
        #    self.itemattrlist['Ranged'] = i
        self.calculate()
    
    def newFile(self):
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 'Some changes may not have been saved. Are you sure you want to discard these changes?', 'Yes', 'No')
            if ret == 1:
                return
        self.initialize()
        self.ClearCurrentItem()
        self.modified = 0

    def saveFile(self):
        if self.filename is None:
            self.saveAsFile()
        else:
            try:
                f = open(self.filename, 'w')
                f.write(XMLHelper.writexml(self.asXML(), UnicodeStringIO(), '', '\t', '\n'))
                self.modified = 0
                f.close()
                self.FileNameLabel.setText(os.path.basename(self.filename))
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + self.filename, 'OK')
            self.updateRecentFiles(self.filename)


    def saveAsFile(self):
        if self.filename is None:
            templatedir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'templates')
            print templatedir
            filename = QFileDialog.getSaveFileName(
                    os.path.join(templatedir,str(self.CharName.text())+'_template.xml'), 
                    "Templates (*.xml)")
        else:
            filename = QFileDialog.getSaveFileName(self.filename, "Templates (*.xml)")
        while unicode(filename) != '':
            if unicode(filename) != '' and os.path.exists(unicode(filename)):
                ret = QMessageBox.warning(self, 'Overwrite?', 'Do you want to overwrite the selected file?', 'Yes', 'No')
                if ret == 1:
                    filename = QFileDialog.getSaveFileName(filename, "Templates (*.xml)")
                else:
                    break
            else: break
        if unicode(filename) != '':
            filename = unicode(filename)
            if filename[-4:] != '.xml':
                filename += '.xml'
            try:
                f = open(filename, 'w')
                f.write(XMLHelper.writexml(self.asXML(), UnicodeStringIO(), '', '\t', '\n'))
                self.modified = 0
                f.close()
                self.FileNameLabel.setText(os.path.basename(filename))
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + filename, 'OK')
        self.filename = filename
        self.updateRecentFiles(filename)

    def openFile(self, *args):
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 'Some changes may not have been saved. Are you sure you want to discard these changes?', 'Yes', 'No')
            if ret == 1:
                return
        if len(args) == 1:
            templatedir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'templates')
            filename = QFileDialog.getOpenFileName(templatedir, "Templates (*.xml *.scc)")
        else:
            filename = args[0]
        if filename is not None and unicode(filename) != '':
            try:
                f = open(unicode(filename), 'r')
            except IOError:
                traceback.print_exc()
                QMessageBox.critical(None, 'Error!', 
                    'Error opening file: ' + unicode(filename), 'OK')
                return
            try:
                docstr = f.read()
                if docstr[0:5] == '<?xml':
                    xmldoc = parseString(docstr)
                    template = xmldoc.getElementsByTagName('SCTemplate')
                    self.loadFromXML(template[0])
                elif docstr[0:5] == 'CHAR_':
                    f.seek(0)
                    self.loadFromLela(f.readlines())
                else:
                    QMessageBox.critical(None, 'Error!', 
                        'Unrecognized Template Type', 'OK')
                    f.close()
                    return
            except:
                traceback.print_exc()
                QMessageBox.critical(None, 'Error!', 
                    'Error loading template', 'OK')
                f.close()
                return
            self.FileNameLabel.setText(os.path.basename(unicode(filename)))
            self.updateRecentFiles(unicode(filename))
            self.filename = unicode(filename)

    def updateRecentFiles(self, fn):
        if len(self.recentFiles) > 5:
            l = len(self.recentFiles)
            del self.recentFiles[5:l]
        if fn is not None:
            if len(self.recentFiles) > 0:
                if self.recentFiles[0] != fn:
                    self.recentFiles.insert(0, fn)
                    if len(self.recentFiles) > 5:
                        l = len(self.recentFiles)
                        del self.recentFiles[5:l]
            else:
                self.recentFiles.insert(0, fn)
        self.rf_menu.clear()
        count = 1
        for f in self.recentFiles:
            if count < 6:
                self.rf_menu.insertItem('&%d %s' % (count, f), count-1)
                self.rf_menu.connectItem(count-1, getattr(self, 'recentFile%d' % count))
            count += 1

    def loadFromXML(self, template):
        self.initialize()
        self.ClearCurrentItem()
        racename = ''
        classname = ''
        for child in template.childNodes:
            if child.nodeType == Node.TEXT_NODE: continue
            if child.tagName == 'Name':
                self.CharName.setText(XMLHelper.getText(child.childNodes))
            elif child.tagName == 'Class':
                # defer for the moment
                classname = XMLHelper.getText(child.childNodes)
            elif child.tagName == 'Race':
                racename = XMLHelper.getText(child.childNodes)
            elif child.tagName == 'Realm':
                self.realm = XMLHelper.getText(child.childNodes)
            elif child.tagName == 'CraftMultiplier':
                self.craftMultiplier = int(XMLHelper.getText(child.childNodes))
            elif child.tagName == 'Level':
                self.CharLevel.setText(XMLHelper.getText(child.childNodes))
            elif child.tagName == 'Notes':
                self.noteText = XMLHelper.getText(child.childNodes)
            elif child.tagName == 'CrafterSkill':
                self.crafterSkill = int(XMLHelper.getText(child.childNodes))
            elif child.tagName == 'SCItem':
                newItem = Item()
                newItem.loadFromXML(child)
                self.itemattrlist[newItem.getAttr('Location')] = newItem
            elif child.tagName == 'Coop':
                self.coop = eval(XMLHelper.getText(child.childNodes), 
                                 globals(), globals())
        self.CharClass.clear()
        self.CharClass.insertStrList(ClassList[self.realm])
        if classname != '':
            self.CharClass.setCurrentItem(ClassList[self.realm].index(classname))
        self.CharRace.clear()
        self.CharRace.insertStrList(Races[self.realm])
        if racename != '':
            self.CharRace.setCurrentItem(Races[self.realm].index(racename))
            self.RaceChanged('', False)
        
        self.restoreItem(self.itemattrlist.get(self.currentTabLabel()))
        self.calculate()
        self.modified = 0
        
    def loadFromLela(self, scclines):
        self.initialize()
        self.ClearCurrentItem()
        sublines = filter(lambda(x): re.compile('^ITEM').match(x) is None, scclines)
        for line in sublines:
            line = string.strip(line, " \n\r")
            if line == '': continue
            attr, value = string.split(line, '=', 1)
            if attr == 'CHAR_NAME':
                self.CharName.setText(value)
            elif attr == 'CHAR_CLASS':
                realm, charclass = string.split(value, '_', 1)
                if realm == 'HIB':
                    self.realm = 'Hibernia'
                elif realm == 'ALB':
                    self.realm = 'Albion'
                elif realm == 'MID':
                    self.realm = 'Midgard'
                self.CharClass.clear()
                self.CharClass.insertStrList(ClassList[self.realm])
                self.CharClass.setCurrentItem(ClassList[self.realm].index(charclass[0]+string.lower(charclass[1:])))
                self.CharRace.clear()
                self.CharRace.insertStrList(Races[self.realm])

        for itemnum in range(0, 19):
            item = Item(TabList[itemnum])
            #item.loadAttr('Location', TabList[itemnum])
            item.loadLelaItemFromSCC(itemnum, scclines, self.realm)
            self.itemattrlist[item.getAttr('Location')] = item
        self.restoreItem(self.itemattrlist.get(self.currentTabLabel()))
        self.calculate()
                        
        
    def openOptions(self):
        self.modified = 1
        res = Options.Options(self, '', 1).exec_loop()
        if res == 2:
            self.newFile()
        elif res == 1:
            self.calculate()

    def OpenCraftWindow(self):
        self.storeItem(self.itemattrlist.get(self.currentTabLabel()))
        CW = CraftWindow.CraftWindow(self, '', 1)
        CW.loadItem(self.itemattrlist.get(self.currentTabLabel()))
        CW.ExpMultiplier.setValue(self.craftMultiplier)
        CW.exec_loop()
        self.craftMultiplier = int(CW.ExpMultiplier.value())
        self.calculate()
        self.modified = 1
    
    def openMaterialsReport(self):
        RW = ReportWindow.ReportWindow(self, '', 1)
        RW.materialsReport(self.itemattrlist)
        RW.exec_loop()

    def openConfigReport(self):
        RW = ReportWindow.ReportWindow(self, '', 1)
        RW.parseConfigReport(self.reportFile, self.itemattrlist)
        RW.exec_loop()

    def chooseReportFile(self):
	filename = QFileDialog.getOpenFileName('./reports', "Reports (*.xml *.rpt)")
        if filename is not None and str(filename) != '':
            self.reportFile = str(filename)

    def SkillClicked(self,a0):
        if a0 is None: return
        skilltext = str(a0.text())
        charclass = unicode(self.CharClass.currentText())
        num, effectstr = string.split(skilltext, ' ', 1)
        locs = []
        for key, item in self.itemattrlist.items():
            activestate = item.getAttr('ActiveState')
            if activestate == 'drop':
                toprng = 10
            else:
                toprng = 4
            for slot in range(0, toprng):
                effect = item.getSlotAttr(activestate, slot, 'Effect')
                amount = item.getSlotAttr(activestate, slot, 'Amount')
                if effectstr == effect:
                    locs.append([key, amount])
                elif effect in AllBonusList[charclass].keys():
                    if effectstr in AllBonusList[charclass][effect]:
                        locs.append([key, amount])

        DW = DisplayWindow.DisplayWindow(self, '', 1)
        DW.setCaption('Slots With %s' % effectstr)
        DW.loadLocations(locs)
        DW.exec_loop()

    def aboutBox(self):
        QMessageBox.information(None, "Kort's Spellcrafting Calculator", 
              "Verison " + ScVersion + "\n\n" 
            + "Homepage http://sc.aod.net\n"
            + "Author's Email kortsc@hotmail.com\n\n"
            + "Bugs/Features discussed on the IGN Trade Skill Forum\n"
            + "http://vnboards.ign.com/Trade_Skills/b20673/", 'Close')

    def openCraftBars(self):
        CB = CraftBar.CraftBar(self.DaocPath, self, '', 1)
        CB.exec_loop()
        self.DaocPath = str(CB.DaocPath.text())

    def resizeEvent(self, e):
        sz = e.size()
        if self.scroller is not None:
            self.scroller.setGeometry(0, 0, sz.width(), sz.height())
        QMainWindow.resizeEvent(self, e)

    def moveWidget(self, w, y):
        w.setGeometry(w.x(), w.y() + y, 
                w.width(), w.height())

    def growWidget(self, w, h):
        w.setGeometry(w.x(), w.y(), 
                w.width(), w.height() + h)

    def openMoreSlots(self):
        if self.extraSlotsOpen:
            for w in self.extraSlots:
                w.hide()
            self.growWidget(self.TypeTab, -72)
            self.growWidget(self.PieceTab, -72)
            self.growWidget(self.JewelTab, -72)
            #self.moveWidget(self.MoreSlots, -72)
            #self.moveWidget(self.SaveItem, -72)
            #self.moveWidget(self.LoadItem, -72)
            #self.moveWidget(self.ClearItem, -72)
            #self.moveWidget(self.ItemCost_Label, -72)
            #self.moveWidget(self.ItemCost, -72)
            self.extraSlotsOpen = False
            self.scroller.resizeContents(self.scroller.contentsWidth(), 
                    self.scroller.contentsHeight() - 72)
            self.MoreSlots.setText('View More Slots....')
        else:
            for w in self.extraSlots:
                w.show()
            self.growWidget(self.TypeTab, 72)
            self.growWidget(self.PieceTab, 72)
            self.growWidget(self.JewelTab, 72)
            #self.moveWidget(self.MoreSlots, 72)
            #self.moveWidget(self.SaveItem, 72)
            #self.moveWidget(self.LoadItem, 72)
            #self.moveWidget(self.ClearItem, 72)
            #self.moveWidget(self.ItemCost_Label, 72)
            #self.moveWidget(self.ItemCost, 72)
            self.extraSlotsOpen = True
            self.scroller.resizeContents(self.scroller.contentsWidth(), 
                    self.scroller.contentsHeight() + 75)
            self.MoreSlots.setText('Collapse Slots....')
            
    def swapWithChest(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        chest = self.itemattrlist.get('Chest', Item('Chest'))
        self.itemattrlist['Chest'] = cur
        self.itemattrlist[self.currentTabLabel()] = chest
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()

    def swapWithArms(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        arms = self.itemattrlist.get('Arms', Item('Arms'))
        self.itemattrlist['Arms'] = cur
        self.itemattrlist[self.currentTabLabel()] = arms
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()

    def swapWithHead(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        head = self.itemattrlist.get('Head', Item('Head'))
        self.itemattrlist['Head'] = cur
        self.itemattrlist[self.currentTabLabel()] = head
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()

    def swapWithLegs(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        legs = self.itemattrlist.get('Legs', Item('Legs'))
        self.itemattrlist['Legs'] = cur
        self.itemattrlist[self.currentTabLabel()] = legs
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()

    def swapWithFeet(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        feet = self.itemattrlist.get('Feet', Item('Feet'))
        self.itemattrlist['Feet'] = cur
        self.itemattrlist[self.currentTabLabel()] = feet
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()
        
    def swapWithHands(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        hands = self.itemattrlist.get('Hands', Item('Hands'))
        self.itemattrlist['Hands'] = cur
        self.itemattrlist[self.currentTabLabel()] = hands
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()

    def swapWithRH(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        rh = self.itemattrlist.get('Right Hand', Item('Right Hand'))
        self.itemattrlist['Right Hand'] = cur
        self.itemattrlist[self.currentTabLabel()] = rh
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()

    def swapWithLH(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        lh = self.itemattrlist.get('Left Hand', Item('Left Hand'))
        self.itemattrlist['Left Hand'] = cur
        self.itemattrlist[self.currentTabLabel()] = lh
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()

    def swapWith2H(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        th = self.itemattrlist.get('2 Handed', Item('2 Handed'))
        self.itemattrlist['2 Handed'] = cur
        self.itemattrlist[self.currentTabLabel()] = th
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()

    def swapWithRanged(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        ranged = self.itemattrlist.get('Ranged', Item('Ranged'))
        self.itemattrlist['Ranged'] = cur
        self.itemattrlist[self.currentTabLabel()] = ranged
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()

    def swapWithSpare(self):
        cur = self.itemattrlist.get(self.currentTabLabel(), Item(self.currentTabLabel()))
        spare = self.itemattrlist.get('Spare', Item('Spare'))
        self.itemattrlist['Spare'] = cur
        self.itemattrlist[self.currentTabLabel()] = spare
        self.restoreItem(self.itemattrlist[self.currentTabLabel()])
        self.calculate()

    def recentFile1(self):
        self.openFile(self.recentFiles[0], True)
    def recentFile2(self):
        self.openFile(self.recentFiles[1], True)
    def recentFile3(self):
        self.openFile(self.recentFiles[2], True)
    def recentFile4(self):
        self.openFile(self.recentFiles[3], True)
    def recentFile5(self):
        self.openFile(self.recentFiles[4], True)

    def generateUIXML(self):
        UIXML.uixml(self)

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, '')
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL('lastWindowClosed()'),a,SLOT('quit()'))
    w = SCApp()
    a.setMainWidget(w)
    w.show()
    w.setCaption('Spellcrafting')
    a.exec_loop()
