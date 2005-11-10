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
import UIXML
import os
import os.path
import ItemList
import time
import locale
import traceback
import encodings
import codecs
import sys

import psyco

class SCApp(B_SC):
    def __init__(self):
        self.nocalc = 1
	self.scroller = None
        self.totals = { }
        self.capTotals = { }
        self.currentPieceTab = None
        self.extraSlotsOpen = False
        self.recentFiles = []
        self.effectlists = {
            'Unused' : UnusedList,
            'Stat'   : StatList, 
            'Resist' : ResistList, 
            'Hits'   : HitsList, 
            'Power'  : PowerList,
            'Skill'  : [],
            'Focus'  : []
        }
        self.dropeffectlists = self.effectlists.copy()
        self.dropeffectlists['Stat'] =         DropStatList
        self.dropeffectlists['Cap Increase'] = CapIncreaseList
        self.dropeffectlists['PvE Bonus'] =    PvEBonusList
        self.dropeffectlists['Other Bonus'] =  OtherBonusList
        # for the moment, every other ability will be Unique
        self.dropeffectlists['Other Ability'] = ("Unique Ability...",)

        for effect in EffectItemNames.keys():
            self.effectlists[effect] =     EffectItemNames[effect][0]
            self.dropeffectlists[effect] = EffectItemList

        self.reportFile = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                                       'reports', 'Default_Config_Report.xml')
        self.coop = False

        B_SC.__init__(self,parent=None,name="SpellCraft Calulator",fl=Qt.WDestructiveClose)

        self.EffectWidths = [self.Effect_1.width(), self.Effect_5.width()]

        self.menuBar = QMenuBar(self)
        pal = QPalette(self.palette().copy())
        self.menuBar.setPalette(pal)

        self.scroller = QScrollView(self)
        self.scroller.enableClipper(True)
        self.scroller.setGeometry(QRect(0, self.menuBar.height(), self.width(), 
                                        self.height() - self.menuBar.height()))
        self.scroller.resizeContents(self.width() - 2, 
                                     self.height() - self.menuBar.height())
        self.setGeometry(self.x(), self.y(), self.width() + 2,
			 self.height() + 1)

        # Dummy widget, makes things look nicer on X-Windows
        q = QWidget(self.scroller)
        q.setGeometry(0, 0, 2000, 2000)
        self.scroller.addChild(q, 0, 0)

        for c in self.children():
            if isinstance(c, QTabBar) or isinstance(c, QGroupBox) \
                    or isinstance(c, QLabel):
                c.reparent(self.scroller.viewport(), c.pos(), 1)
                self.scroller.addChild(c, c.pos().x(), c.pos().y())
        self.scroller.show()

        self.PieceTab.setFocusPolicy(QWidget.StrongFocus)
        for tabname in PieceTabList:
            newtab = QTab(qApp.translate("B_SC",tabname,None))
            self.PieceTab.insertTab(newtab, row = 0)
        for tabname in JewelTabList:
            newtab = QTab(qApp.translate("B_SC",tabname,None))
            self.PieceTab.insertTab(newtab, row = 1)

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
	
        self.StrengthLabel = self.replaceLabel(self.StrengthLabel, 'Strength')
        self.ConstitutionLabel = self.replaceLabel(self.ConstitutionLabel, 'Constitution')
        self.DexterityLabel = self.replaceLabel(self.DexterityLabel, 'Dexterity')
        self.QuicknessLabel = self.replaceLabel(self.QuicknessLabel, 'Quickness')
        self.IntelligenceLabel = self.replaceLabel(self.IntelligenceLabel, 'Intelligence')
        self.PietyLabel = self.replaceLabel(self.PietyLabel, 'Piety')
        self.CharismaLabel = self.replaceLabel(self.CharismaLabel, 'Charisma')
        self.EmpathyLabel = self.replaceLabel(self.EmpathyLabel, 'Empathy')
        self.BodyLabel = self.replaceLabel(self.BodyLabel, 'Body')
        self.ColdLabel = self.replaceLabel(self.ColdLabel, 'Cold')
        self.HeatLabel = self.replaceLabel(self.HeatLabel, 'Heat')
        self.EnergyLabel = self.replaceLabel(self.EnergyLabel, 'Energy')
        self.MatterLabel = self.replaceLabel(self.MatterLabel, 'Matter')
        self.SpiritLabel = self.replaceLabel(self.SpiritLabel, 'Spirit')
        self.CrushLabel = self.replaceLabel(self.CrushLabel, 'Crush')
        self.ThrustLabel = self.replaceLabel(self.ThrustLabel, 'Thrust')
        self.SlashLabel = self.replaceLabel(self.SlashLabel, 'Slash')
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
        self.charclass = 'Armsman'
        self.crafterSkill = 1001
        self.showDoneInMatsList = 0
        self.noteText = ''
        self.includeRacials = True
        self.hideNonClassSkills = False
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
        self.nocalc = 0
        self.calculate()
        self.modified = 0
    
    def close(self, args):
        Options.Options(self).OK_pressed() # write out app config data to disk
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 'Some changes may not have been saved. Are you sure you want to quit?', 'Yes', 'No')
            if ret == 0:
                return QMainWindow.close(self, 1)
            else:
                return False
        else: return QMainWindow.close(self, 1)

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

        self.PieceTab.setCurrentTab(0)
        self.currentTab = self.PieceTab
        self.currentPieceTab = self.PieceTab.currentTab()
        self.currentTabLabel = string.strip(str(self.PieceTab.tab(0).text()))

        self.Equipped.setChecked(1)

        self.itemattrlist = { }
        for tab in TabList:
            self.itemattrlist[tab] = Item(tab)
        self.ItemLevel.setText('51')
        self.CharLevel.setText('50')

        self.extraSlots = []
        self.switchOnType = {'drop' : [], 'player' : [] }
        self.switchOnType['drop'].append(self.QualEdit)
        self.switchOnType['drop'].append(self.Amount_Edit_1)
        self.switchOnType['drop'].append(self.Amount_Edit_2)
        self.switchOnType['drop'].append(self.Amount_Edit_3)
        self.switchOnType['drop'].append(self.Amount_Edit_4)
        self.switchOnType['drop'].append(self.Amount_Edit_5)
        self.switchOnType['drop'].append(self.Amount_Edit_6)
        self.switchOnType['drop'].append(self.Amount_Edit_7)
        self.switchOnType['drop'].append(self.Amount_Edit_8)
        self.switchOnType['drop'].append(self.Amount_Edit_9)
        self.switchOnType['drop'].append(self.Amount_Edit_10)
        self.switchOnType['drop'].append(self.Gem_Label_5)
        self.switchOnType['drop'].append(self.Gem_Label_6)
        self.switchOnType['drop'].append(self.Gem_Label_7)
        self.switchOnType['drop'].append(self.Gem_Label_8)
        self.switchOnType['drop'].append(self.Gem_Label_9)
        self.switchOnType['drop'].append(self.Gem_Label_10)
        self.switchOnType['drop'].append(self.Type_5)
        self.switchOnType['drop'].append(self.Type_6)
        self.switchOnType['drop'].append(self.Type_7)
        self.switchOnType['drop'].append(self.Type_8)
        self.switchOnType['drop'].append(self.Type_9)
        self.switchOnType['drop'].append(self.Type_10)
        self.switchOnType['drop'].append(self.Effect_5)
        self.switchOnType['drop'].append(self.Effect_6)
        self.switchOnType['drop'].append(self.Effect_7)
        self.switchOnType['drop'].append(self.Effect_8)
        self.switchOnType['drop'].append(self.Effect_9)
        self.switchOnType['drop'].append(self.Effect_10)
        self.switchOnType['drop'].append(self.SaveItem)
        self.switchOnType['drop'].append(self.ItemName)

        self.switchOnType['player'].append(self.QualDrop)
        self.switchOnType['player'].append(self.Amount_Drop_1)
        self.switchOnType['player'].append(self.Amount_Drop_2)
        self.switchOnType['player'].append(self.Amount_Drop_3)
        self.switchOnType['player'].append(self.Amount_Drop_4)
        self.switchOnType['player'].append(self.Quality_Label)
        self.switchOnType['player'].append(self.Quality_1)
        self.switchOnType['player'].append(self.Quality_2)
        self.switchOnType['player'].append(self.Quality_3)
        self.switchOnType['player'].append(self.Quality_4)
        self.switchOnType['player'].append(self.Points_Label)
        self.switchOnType['player'].append(self.Points_1)
        self.switchOnType['player'].append(self.Points_2)
        self.switchOnType['player'].append(self.Points_3)
        self.switchOnType['player'].append(self.Points_4)
        self.switchOnType['player'].append(self.Cost_Label)
        self.switchOnType['player'].append(self.Cost_1)
        self.switchOnType['player'].append(self.Cost_2)
        self.switchOnType['player'].append(self.Cost_3)
        self.switchOnType['player'].append(self.Cost_4)
        self.switchOnType['player'].append(self.Name_1)
        self.switchOnType['player'].append(self.Name_2)
        self.switchOnType['player'].append(self.Name_3)
        self.switchOnType['player'].append(self.Name_4)
        self.switchOnType['player'].append(self.Imbue_Label)
        self.switchOnType['player'].append(self.Imbue)
        self.switchOnType['player'].append(self.Slash_Label)
        self.switchOnType['player'].append(self.Total_Imbue)
        self.switchOnType['player'].append(self.Overcharge_Label)
        self.switchOnType['player'].append(self.Overcharge)
        self.switchOnType['player'].append(self.ItemCost_Label)
        self.switchOnType['player'].append(self.ItemCost)
        self.switchOnType['player'].append(self.CraftButton)
        self.RealmChanged()
        #self.connect(self, SLOT('show()'), self.shown)

    def asXML(self):
        document = Document()
        rootnode = document.createElement('SCTemplate')
        document.appendChild(rootnode)
        namenode = document.createElement('Name')
        namenode.appendChild(document.createTextNode(str(self.CharName.text())))
        classnode = document.createElement('Class')
        classnode.appendChild(document.createTextNode(self.charclass))
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
    
    def PieceTabChanged(self,a0):
        if self.nocalc:
            return
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        self.storeItem(item)
        self.currentPieceTab = a0
        self.currentTabLabel = string.strip(str(self.PieceTab.tab(a0).text()))
        self.restoreItem(self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel)))

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
        item.loadAttr('Location', self.currentTabLabel)
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
            item.loadAttr('ItemQuality', unicode(self.QualEdit.text()))
        item.loadAttr('AFDPS', unicode(self.AFDPS_Edit.text()))
        item.loadAttr('Speed', unicode(self.Speed_Edit.text())) 
        item.loadAttr('Bonus', unicode(self.Bonus_Edit.text()))
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
        self.itemattrlist[self.currentTabLabel] = item

    def restoreItem(self, item):
        if item is None: return
        wascalc = self.nocalc
        self.nocalc = 1
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
        self.Equipped.setChecked(int(item.getAttr('Equipped')))
        for slot in range(1, toprng):
            typecombo = getattr(self, 'Type_%d' % slot)
            typecombo.clear()
            typecombo.insertStrList(list(typelist))
            gemtype = item.getSlotAttr(itemtype, slot-1, 'Type')
            gemeffect = item.getSlotAttr(itemtype, slot-1, 'Effect')
            typecombo.setCurrentItem(typelist.index(gemtype))
            self.UpdateCombo(slot)
            effcombo = getattr(self, 'Effect_%d' % slot)
            if self.Drop.isChecked():
                if not gemeffect in self.dropeffectlists[gemtype]:
                    if not isinstance(self.dropeffectlists[gemtype], list):
                        self.dropeffectlists[gemtype] = list(self.dropeffectlists[gemtype])
                    self.dropeffectlists[gemtype].append(gemeffect)
                    effcombo.insertStrList( [gemeffect] )
                effectlist = self.dropeffectlists[gemtype]
            else:
                if not gemeffect in self.effectlists[gemtype]:
                    if not isinstance(self.effectlists[gemtype], list):
                        self.effectlists[gemtype] = list(self.effectlists[gemtype])
                    self.effectlists[gemtype].append(gemeffect)
                    effcombo.insertStrList( [gemeffect] )
                effectlist = self.effectlists[gemtype]
            effcombo.setCurrentItem(effectlist.index(gemeffect))
            if itemtype == 'drop':
                am = item.getSlotAttr(itemtype, slot-1, 'Amount')
                amedit = getattr(self, 'Amount_Edit_%d' % slot)
                amedit.setText(am)
            else:
                gemamount = item.getSlotAttr(itemtype, slot-1, 'Amount')
                amountlist = ValuesLists[gemtype]
                if gemamount in amountlist:
                    getattr(self, 'Amount_Drop_%d' % slot).setCurrentItem(
                            amountlist.index(gemamount))
                quacombo = getattr(self, 'Quality_%d' % slot)
                gemqua = item.getSlotAttr(itemtype, slot-1, 'Qua')
                if gemqua in QualityValues:
                    if quacombo.count() > 0:
                        quacombo.setCurrentItem(QualityValues.index(gemqua))
        self.AFDPS_Edit.setText(item.getAttr('AFDPS'))
        self.Speed_Edit.setText(item.getAttr('Speed'))
        self.Bonus_Edit.setText(item.getAttr('Bonus'))
        if itemtype == 'drop':
            self.QualEdit.setText(item.getAttr('ItemQuality'))
            self.ItemName.setText(item.getAttr('ItemName'))
        else:
            if item.getAttr('ItemQuality') in QualityValues:
                self.QualDrop.setCurrentItem(
                    QualityValues.index(item.getAttr('ItemQuality')))
        self.save = 1
        self.nocalc = wascalc
        self.calculate()

    def calculate(self):
        if self.nocalc:
            return
        self.nocalc = 1
        focusnum = 1
        charleveltext = str(self.CharLevel.text())
        if charleveltext == '': 
            charlevel = 1
        else:
            charlevel = max(min(50, int(charleveltext)), 1)
        self.CharLevel.setText(str(charlevel))
        self.totals = { }
        self.capTotals = { }
        for effect in ResistList:
            self.totals[effect] = 0
        for effect in StatList:
            self.totals[effect] = 0
            self.capTotals[effect] = 0
        self.totals['Hits'] = 0
        self.totals['Power'] = 0
        self.capTotals['Hits'] = 0
        self.capTotals['Power'] = 0
        self.capTotals['AF'] = 0
        skillTotals = {}
        otherTotals = {}
        self.Focus_1.setText('')
        self.Focus_2.setText('')
        self.Focus_3.setText('')
        self.Focus_4.setText('')
        self.DupErrorString.setText('')
        self.OcErrorString.setText('')
        totalutility = 0.0
        totalcost = 0
        for key, item in self.itemattrlist.items():
            utility = 0.0
            itemtype = item.getAttr('ActiveState')
            itemcost = 0
            if itemtype == 'player':
                toprng = 4
            else:
                toprng = 10
            gemeffects = []
            for i in range(0, toprng):
                gemtype = item.getSlotAttr(itemtype, i, 'Type')
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
                    costindex = ValuesLists[gemtype].index(str(amount))
                    cost = GemCosts[costindex]
                    remakecost = RemakeCosts[costindex] * int(item.getSlotAttr(itemtype, i, 'Remakes'))
                    if effect[0:4] == 'All ':
                        cost += 60 * costindex
                        cost = cost * 3
                        if remakecost > 0:
                            remakecost += 180 * costindex
                        if effect != 'All Spell Lines' and amount > 1:
                            self.DupErrorString.setText('Invalid ' + effect + ' on ' + key)
                    elif gemtype == 'Resist' or gemtype == 'Focus':
                        cost += 60 * costindex
                        if remakecost > 0:
                            remakecost += 60 * costindex
                    itemcost += cost + remakecost
                if itemtype == 'player' and key == self.currentTabLabel:
                    getattr(self, 'Cost_%d' % (i+1)).setText(SC.formatCost(cost+remakecost))
                if gemtype == 'Skill':
                    if effect == 'All Magic Skills'\
                        or effect == 'All Melee Weapon Skills'\
                        or effect == 'All Dual Wield Skills'\
                        or effect == 'All Archery Skills':

                        if effect == 'All Melee Combat Skills':
                            utility += amount * 5
                        for e in AllBonusList[self.realm][self.charclass][effect]:
                            if effect == 'All Magic Skills'\
                                or effect == 'All Dual Wield Skills'\
                                or effect == 'All Archery Skills':
                                utility += amount * 5
                            if item.getAttr('Equipped') == '1':
                                if not skillTotals.has_key(e):
                                    skillTotals[e] = amount
                                else:
                                    skillTotals[e] += amount
                    else:           
                        utility += amount * 5
                        if item.getAttr('Equipped') == '1':
                            if self.hideNonClassSkills:
                                if not AllBonusList[self.realm][self.charclass]['Skills Hash'].has_key(effect):
                                    continue
                            if not skillTotals.has_key(effect):
                                skillTotals[effect] = amount
                            else:
                                skillTotals[effect] += amount
                elif gemtype == 'Focus':
                    utility += 1
                    if item.getAttr('Equipped') == '1':
                        if effect == 'All Spell Lines':
                            for f in AllBonusList[self.realm][self.charclass][effect]:
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
                        self.totals[effect] += amount
                elif gemtype == 'Stat':
                    if effect == 'Acuity':
                        for e in AllBonusList[self.realm][self.charclass][effect]:
                            utility += amount * 2.0 / 3.0
                            if item.getAttr('Equipped') == '1':
                                self.totals[e] += amount
                    else:
                        utility += amount * 2.0 / 3.0
                        if item.getAttr('Equipped') == '1':
                            self.totals[effect] += amount
                elif gemtype == 'Other Bonus' or gemtype == 'PvE Bonus':
                    if item.getAttr('Equipped') == '1':
                        if not otherTotals.has_key(effect):
                            otherTotals[effect] = amount
                        else:
                            otherTotals[effect] += amount
                elif gemtype == 'Cap Increase':
                    if item.getAttr('Equipped') == '1':
                        oeffect = effect + ' Cap'
                        if effect == 'AF':
                          if not otherTotals.has_key(oeffect):
                              otherTotals[oeffect] = amount
                          else:
                              otherTotals[oeffect] += amount
                        elif effect == 'Acuity':
                            effect = AllBonusList[self.realm][self.charclass][effect]
                            if len(effect) == 0:
                                continue
                            effect = effect[0]
                        if not self.capTotals.has_key(effect):
                            self.capTotals[effect] = amount
                        else:
                            self.capTotals[effect] += amount
            if item.getAttr('Equipped') == '1':
                totalutility += utility
            totalcost += itemcost
            if itemtype == 'player':
                itemimbue = self.getItemImbue(item)
                imbue = self.calcImbue(item, key == self.currentTabLabel)
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
            if key == self.currentTabLabel:
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
                    if ResistTable.has_key(key):
                        rr = str(getattr(self, key+'RR').text())
                        if rr != '-':
                            val += int(rr[1:-1])
                if self.capTotals.has_key(key):
                  if self.capTotals[key] > 0:
                    getattr(self, key+'Cap').setText('('+str(self.capTotals[key])+')')
                  else:
                    getattr(self, key+'Cap').setText('-')
                getattr(self, key).setText(unicode(val))
            else:
                if HighCapBonusList.has_key(key):
                    capcalc = HighCapBonusList[key]
                elif Caps.has_key(key):
                    capcalc = HighCapBonusList[Caps[key]]
                else:
                    capcalc = HighCapBonusList['Other Bonus']
                basecap = int(charlevel * capcalc[0]) + capcalc[1]
                if self.capTotals.has_key(key):
                    if HighCapBonusList.has_key(key):
                        capcalc = HighCapBonusList[key + ' Cap']
                    else:
                        capcalc = HighCapBonusList['Cap']
                    addcap = int(charlevel * capcalc[0]) + capcalc[1]
                    capmod = self.capTotals[key]
                    capcap = addcap - capmod
                    if capmod > addcap:  capmod = addcap
                    getattr(self, key+'Cap').setText('('+unicode(int(capcap))+')')
                else:
                    capmod = 0
                getattr(self, key).setText(unicode(int(basecap + capmod) - val))
        self.TotalUtility.setText('%3.1f' % totalutility)
        self.TotalCost.setText(SC.formatCost(totalcost))
        self.SkillsList.clear()
        self.OtherBonusList.clear()
        for skill, amount in skillTotals.items():
            if self.TotalBonus.isChecked():
                self.SkillsList.insertItem('%d %s' % (amount, skill))
            else:
                capcalc = HighCapBonusList['Skill']
                thiscap = int(charlevel * capcalc[0]) + capcalc[1]
                self.SkillsList.insertItem('%d %s' % (thiscap - amount, skill))
        for bonus, amount in otherTotals.items():
            if self.TotalBonus.isChecked():
                self.OtherBonusList.insertItem('%d %s' % (amount, bonus))
            else:
                if HighCapBonusList.has_key(bonus):
                    capcalc = HighCapBonusList[bonus]
                else:
                    capcalc = HighCapBonusList['Other Bonus']
                cap = int(charlevel * capcalc[0]) + capcalc[1]
                if bonus == '% Power Pool' or bonus == 'AF':
                    key = bonus
                    if bonus == '% Power Pool': key = 'Power'
                    capcalc = HighCapBonusList[key + ' Cap']
                    addcap = int(charlevel * capcalc[0]) + capcalc[1]
                    capmod = self.capTotals[key]
                    if capmod > addcap:  capmod = addcap
                else:
                    capmod = 0
                self.OtherBonusList.insertItem('%d %s' % (cap + capmod - amount, bonus))        
        self.TotalPrice.setText(SC.formatCost(self.computePrice()))
        self.nocalc = 0

    def computePrice(self):
        price = 0
        cost = 0
        for key, item in self.itemattrlist.items():
            itemcost = 0
            itemtype = item.getAttr('ActiveState')
            if itemtype == 'drop': continue
            #if item.getAttr('Equipped') == '0': continue
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

    def UpdateCombo(self, num):
        effcombo = getattr(self, 'Effect_%d' % num)
        typecombo = getattr(self, 'Type_%d' % num)
        effcombo.clear()
        typetext = unicode(typecombo.currentText())
        if self.PlayerMade.isChecked():
            amountcombo = getattr(self, 'Amount_Drop_%d' % num)
        else:
            amountedit = getattr(self, 'Amount_Edit_%d' % num)
        if typetext != 'Unused':
            if self.Drop.isChecked():
                effectlist = self.dropeffectlists[typetext]
            else:
                effectlist = self.effectlists[typetext]
            if len(effectlist) > 0:
                effcombo.insertStrList(list(effectlist))
            if self.PlayerMade.isChecked():
                valueslist = ValuesLists[typetext]
                amountcombo.clear()
                amountcombo.insertStrList(list(valueslist))
            else:
                amountedit.setText('0')
        else:
            if self.PlayerMade.isChecked():
                amountcombo.clear()
            else:
                amountedit.clear()
        if self.PlayerMade.isChecked():
            qualcombo = getattr(self, 'Quality_%d' % num)
            qualcombo.clear()
            qualcombo.insertStrList(list(QualityValues))
            qualcombo.setCurrentItem(len(QualityValues)-2)

    def RaceChanged(self, a0):
        race = str(self.CharRace.currentText())
        for rt in ResistList:
            if Races['All'][race]['Resists'].has_key(rt):
              if self.includeRacials:
                getattr(self, rt + 'RR').setText('('+str(Races['All'][race]['Resists'][rt])+')')
              else:
                getattr(self, rt + 'RR').setText('+'+str(Races['All'][race]['Resists'][rt]))
            else:
                getattr(self, rt + 'RR').setText('-')
        self.calculate()

    def CharClassChanged(self,a0):
        self.charclass = str(self.CharClass.currentText())
        showrealm = self.realm
        if self.coop:
            showrealm = 'All'
        self.dropeffectlists['Skill'] = DropSkillList[showrealm]
        self.dropeffectlists['Focus'] = FocusList[showrealm]
        if self.hideNonClassSkills:
            self.effectlists['Skill'] = AllBonusList['All'][self.charclass]['All Skills']
            self.effectlists['Focus'] = AllBonusList['All'][self.charclass]['All Focus']
        else:
            self.effectlists['Skill'] = SkillList[showrealm]
            self.effectlists['Focus'] = FocusList[showrealm]
        race = str(self.CharRace.currentText())
        self.CharRace.clear()
        racelist = AllBonusList[self.realm][self.charclass]['Races']
        self.CharRace.insertStrList(list(racelist))
        if race in racelist:
          self.CharRace.setCurrentItem(racelist.index(race))
        self.RaceChanged('')
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        item.loadAttr('ActiveState','player')
        if self.save:
            self.restoreItem(item)
        self.calculate()

    def RealmChanged(self):
        self.CharClass.clear()
        self.CharClass.insertStrList(list(ClassList[self.realm]))
        if self.charclass in ClassList[self.realm]:
          self.CharClass.setCurrentItem(ClassList[self.realm].index(self.charclass))
        self.CharClassChanged('')
    
    def TypeChanged(self, index):
        wascalc = self.nocalc
        self.nocalc = 1
        self.modified = 1
        self.UpdateCombo(index)
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        self.storeItem(item)
        self.nocalc = wascalc
        self.calculate()

    def Type_1_Changed(self,a0):
        self.TypeChanged(1)
    def Type_2_Changed(self,a0):
        self.TypeChanged(2)
    def Type_3_Changed(self,a0):
        self.TypeChanged(3)
    def Type_4_Changed(self,a0):
        self.TypeChanged(4)
    def Type_5_Changed(self,a0):
        self.TypeChanged(5)
    def Type_6_Changed(self,a0):
        self.TypeChanged(6)
    def Type_7_Changed(self,a0):
        self.TypeChanged(7)
    def Type_8_Changed(self,a0):
        self.TypeChanged(8)
    def Type_9_Changed(self,a0):
        self.TypeChanged(9)
    def Type_10_Changed(self,a0):
        self.TypeChanged(10)


    def showWideEffects(self, wide):
        width = self.EffectWidths[wide]
        for num in range(1, 5):
          eff = getattr(self, 'Effect_%d' % num)
          eff.setGeometry(eff.x(), eff.y(), width, eff.height())

    def showDropWidgets(self):
        for w in self.switchOnType['player']:
            w.hide()
        for w in self.switchOnType['drop']:
            w.show()
        self.showWideEffects(1)
        self.Gem_Label_1.setEnabled(1)
        self.Gem_Label_2.setEnabled(1)
        self.Gem_Label_3.setEnabled(1)
        self.Gem_Label_4.setEnabled(1)

    def showPlayerWidgets(self):
        for w in self.switchOnType['player']:
            w.show()
        for w in self.switchOnType['drop']:
            w.hide()
        self.showWideEffects(0)

    def DropToggled(self,a0):
        self.modified = 1
        if not a0: 
            return
        self.showDropWidgets()
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        item.loadAttr('ActiveState','drop')
        if self.save:
            self.restoreItem(item)

    def PlayerToggled(self, a0):
        self.modified = 1
        if not a0: 
            return
        self.showPlayerWidgets()
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        item.loadAttr('ActiveState','player')
        if self.save:
            self.restoreItem(item)

    def AmountChanged(self,a0):
        self.modified = 1
        if self.save:
            item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
            self.storeItem(item)
        self.calculate()

    def recalculate(self,a0):
        self.modified = 1
        if self.save:
            item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
            self.storeItem(item)
        self.calculate()

    def ClearCurrentItem(self):
        item = Item(self.currentTabLabel)
        self.itemattrlist[self.currentTabLabel] = item
        self.restoreItem(item)

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
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        self.storeItem(item)
        ext = FileExt[self.currentTabLabel]
        if not isinstance(ext, types.StringType):
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
        ext = FileExt[self.currentTabLabel]
        extstr = ''
        if not isinstance(ext, types.StringType):
            for e in ext:
                extstr += '*%s.xml *.%s ' % (e, e)
            ext = ext[0]
        else:
            extstr = '*%s.xml *.%s' % (ext, ext)
        itemdir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'items', self.realm, ext)
        Qfd = QFileDialog(itemdir, "Items (%s)" % extstr, self, None, 1)
        Qfp = ItemList.ItemList(Qfd, self)
        Qfd.setMode(QFileDialog.ExistingFile)
        Qfd.setInfoPreviewEnabled(1)
        Qfd.setInfoPreview(Qfp, Qfp.preview)
        Qfd.setPreviewMode(QFileDialog.Info)
        ## Qfp is nested in a QWidgetStack within a QSplitter, which we will tweak:
        Qfp.parent().parent().setSizes([165, 150])
        if Qfd.exec_loop():
            filename = Qfd.selectedFile()
            if filename is not None and unicode(filename) != '':
                item = Item(self.currentTabLabel)
                item.loadAttr('Realm', self.realm)
                if item.load(unicode(filename)) == -1 : return
                if string.lower(item.getAttr('Realm')) != string.lower(self.realm)\
                    and string.lower(item.getAttr('Realm')) != 'all'\
                    and not self.coop:
                    QMessageBox.critical(None, 'Error!', 'You are trying to load an item for another realm!', 'OK')
                    return
                item.loadAttr('Location', self.currentTabLabel)
                self.itemattrlist[self.currentTabLabel] = item
                self.restoreItem(item)
                self.modified = 1

    def ItemLevelShow(self):
        level = self.ItemLevelWindow.exec_loop()
        if level != -1:
            self.ItemLevel.setText(str(level))

    def EquippedClicked(self):
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        self.storeItem(item)
        self.calculate()
    
    def newFile(self):
        wascalc = self.nocalc
        self.nocalc = 1
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 'Some changes may not have been saved. Are you sure you want to discard these changes?', 'Yes', 'No')
            if ret == 1:
                self.nocalc = wascalc
                return
        self.initialize()
        self.ClearCurrentItem()
        self.nocalc = wascalc
        self.calculate()
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
        wascalc = self.nocalc
        self.nocalc = 1
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
                charclass = XMLHelper.getText(child.childNodes)
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
        self.RealmChanged()
        if AllBonusList[self.realm].has_key(charclass):
            self.CharClass.setCurrentItem(ClassList[self.realm].index(charclass))
            self.CharClassChanged('')
        if racename in AllBonusList[self.realm][self.charclass]['Races']:
            self.CharRace.setCurrentItem(AllBonusList[self.realm][self.charclass]['Races'].index(racename))
            self.RaceChanged('')
        self.nocalc = wascalc
        self.restoreItem(self.itemattrlist.get(self.currentTabLabel))
        self.modified = 0
        
    def loadFromLela(self, scclines):
        wascalc = self.nocalc
        self.nocalc = 1
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
                self.realm, charclass = string.split(value, '_', 1)
                charclass = charclass[0]+string.lower(charclass[1:])
                if self.realm == 'HIB':
                    self.realm = 'Hibernia'
                elif self.realm == 'ALB':
                    self.realm = 'Albion'
                elif self.realm == 'MID':
                    self.realm = 'Midgard'
                self.RealmChanged()
                if AllBonusList[self.realm].has_key(charclass):
                   self.CharClass.setCurrentItem(ClassList[self.realm].index(charclass))
                   self.CharClassChanged('')

        for itemnum in range(0, 19):
            item = Item(TabList[itemnum])
            #item.loadAttr('Location', TabList[itemnum])
            item.loadLelaItemFromSCC(itemnum, scclines, self.realm)
            self.itemattrlist[item.getAttr('Location')] = item
        self.nocalc = wascalc
        self.restoreItem(self.itemattrlist.get(self.currentTabLabel))                        
        
    def openOptions(self):
        self.modified = 1
        self.nocalc = 1
        res = Options.Options(self, '', 1).exec_loop()
        if res == 2:
             self.RealmChanged()
        elif res == 1:
             self.CharClassChanged('')
        self.nocalc = 0
        self.calculate()

    def OpenCraftWindow(self):
        self.storeItem(self.itemattrlist.get(self.currentTabLabel))
        CW = CraftWindow.CraftWindow(self, '', 1)
        CW.loadItem(self.itemattrlist.get(self.currentTabLabel))
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
                elif effect in AllBonusList[self.realm][self.charclass].keys():
                    if effectstr in AllBonusList[self.realm][self.charclass][effect]:
                        locs.append([key, amount])

        DW = DisplayWindow.DisplayWindow(self, '', 1)
        DW.setCaption('Slots With %s' % effectstr)
        DW.loadLocations(locs)
        DW.exec_loop()

    def aboutBox(self):
        QMessageBox.information(None, "Kort's Spellcrafting Calculator", 
              "Verison " + ScVersion + "\n\n" 
            + "Official URI  http://kscraft.sf.net/\n"
            + "Project Home  http://sf.net/projects/kscraft\n\n"
            + "Report Bugs/Request Features on the project Users Forum", 'Close')

    def openCraftBars(self):
        CB = CraftBar.CraftBar(self.DaocPath, self, '', 1)
        CB.exec_loop()
        self.DaocPath = str(CB.DaocPath.text())

    def resizeEvent(self, e):
        sz = e.size()
        if self.scroller is not None:
            self.scroller.setGeometry(0, 0 + self.menuBar.height(), 
				      sz.width(), sz.height() - self.menuBar.height())
        QMainWindow.resizeEvent(self, e)

    def swapWith(self, part):
        cur = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        swap = self.itemattrlist.get(part, Item(part))
        self.itemattrlist[part] = cur
        self.itemattrlist[self.currentTabLabel] = swap
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def swapWithChest(self):
        self.swapWith('Chest')
    def swapWithArms(self):
        self.swapWith('Arms')
    def swapWithHead(self):
        self.swapWith('Head')
    def swapWithLegs(self):
        self.swapWith('Legs')
    def swapWithFeet(self):
        self.swapWith('Feet')
    def swapWithHands(self):
        self.swapWith('Hands')
    def swapWithRH(self):
        self.swapWith('Right Hand')
    def swapWithLH(self):
        self.swapWith('Left Hand')
    def swapWith2H(self):
        self.swapWith('2 Handed')
    def swapWithRanged(self):
        self.swapWith('Ranged')
    def swapWithSpare(self):
        self.swapWith('Spare')

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
    psyco.full()
    locale.setlocale(locale.LC_ALL, '')
    a = QApplication(sys.argv)
    QObject.connect(a,SIGNAL('lastWindowClosed()'),a,SLOT('quit()'))
    w = SCApp()
    a.setMainWidget(w)
    w.show()
    w.setCaption('Spellcrafting')
    a.exec_loop()
