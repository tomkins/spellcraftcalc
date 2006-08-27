# ScWindow.py: Dark Age of Camelot Spellcrafting Calculator (main Window)
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license


from qt import *
from B_ScWindow import *
from Item import *
from Character import *
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


class AboutScreen(QDialog):
    def __init__(self,parent = None,name = "About",modal = True,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)
        pixmap = QPixmap(parent.splashFile)
        self.setPaletteBackgroundPixmap(pixmap)
        self.resize(QSize(480,340).expandedTo(pixmap.size()))
        self.clearWState(Qt.WState_Polished)
        self.show()

    def mouseReleaseEvent(self, e):
        # a little lame, e should match a mouseDown event in our window
        self.close()

    def keyPressEvent(self, e):
        if len(e.text()):
            self.close()


class ScWindow(B_SC):
    def __init__(self):
        self.splashFile = None
        self.newcount = 0
        self.nocalc = 1
        self.totals = { }
        self.capTotals = { }
        self.currentPieceTab = None
        self.extraSlotsOpen = False
        self.recentFiles = []
        self.effectlists = GemLists['All'].copy()
        self.dropeffectlists = DropLists['All'].copy()

        self.reportFile = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                                       'reports', 'Default_Config_Report.xml')
        self.coop = False

        self.fixedtaborder = False

        B_SC.__init__(self,parent=None,name="Kort's Spellcrafting Calulator",
                      fl=Qt.WDestructiveClose|Qt.WStyle_Customize 
                        |Qt.WStyle_DialogBorder|Qt.WStyle_Title
                        |Qt.WStyle_SysMenu|Qt.WStyle_Minimize)

        self.fixtabs = True

        self.statusBar().setSizeGripEnabled(0)
        self.statusBar().hide()

        self.CharLevel.setValidator(QIntValidator(0, 99, self))
        self.ItemLevel.setValidator(QIntValidator(0, 99, self))
        self.QualEdit.setValidator(QIntValidator(0, 100, self))
        self.Bonus_Edit.setValidator(QIntValidator(0, 99, self))

        # This doesn't matter for tinctures, keep hidden
        self.Quality_5.hide()

        ## XXX not calculated yet - we must hide :)
        self.Cost_5.hide()
        self.ItemPriceLabel.hide()
        self.ItemPrice.hide()

        self.EffectWidths = [self.Effect_1.width(), self.Effect_10.width()]

        self.PieceTab.setFocusPolicy(QWidget.StrongFocus)
        for tabname in PieceTabList:
            newtab = QTab(qApp.translate("B_SC",tabname,None))
            self.PieceTab.insertTab(newtab, row = 0)
        for tabname in JewelTabList:
            newtab = QTab(qApp.translate("B_SC",tabname,None))
            self.PieceTab.insertTab(newtab, row = 1)

        size = self.PieceTab.size()
        size.setHeight(self.PieceTab.sizeHint().height())
        self.PieceTab.setFixedSize(size)

        self.GroupItemFrame.move(self.GroupItemFrame.pos().x(), self.PieceTab.geometry().bottom())

        self.Realm.insertStrList(list(Realms))
        self.QualDrop.insertStrList(list(QualityValues))

        self.GemLabel = []
        self.Type = []
        self.Effect = []
        self.AmountEdit = []
        self.AmountDrop = []
        self.Quality = []
        self.Points = []
        self.Cost = []
        self.Name = []

        editAmountValidator = QIntValidator(-999, +999, self)

        for i in range(0, 10):
            idx = i + 1
            self.GemLabel.append(getattr(self, 'Gem_Label_%d' % idx))
            self.Type.append(getattr(self, 'Type_%d' % idx))
            self.Effect.append(getattr(self, 'Effect_%d' % idx))
            self.Effect[i].setInsertionPolicy(QComboBox.BeforeCurrent)
            self.AmountEdit.append(getattr(self, 'Amount_Edit_%d' % idx))
            self.AmountEdit[i].setValidator(editAmountValidator)
            if i < 5:
                self.AmountDrop.append(getattr(self, 'Amount_Drop_%d' % idx))
                self.Quality.append(getattr(self, 'Quality_%d' % idx))
                self.Quality[i].insertStrList(list(QualityValues))
                self.Points.append(getattr(self, 'Points_%d' % idx))
                self.Cost.append(getattr(self, 'Cost_%d' % idx))
                self.Name.append(getattr(self, 'Name_%d' % idx))

        self.updateGeometry()
        self.centralWidget().setFixedSize(
             QSize(self.GroupItemFrame.frameGeometry().right() + 4, 
                   self.GroupItemFrame.frameGeometry().bottom() + 3))

        self.startup = 1
        self.pricingInfo = {}
	
        self.ItemLevelWindow = ItemLevel.ItemLevel(self, '', 1)
        self.DaocPath = ''
        self.realm = 'Albion'
        self.charclass = 'Armsman'
        self.crafterSkill = 1000
        self.showDoneInMatsList = 0
        self.noteText = ''
        self.capDistance = False
        self.includeRacials = False
        self.hideNonClassSkills = False
        OW = Options.Options(self, '', 0)
        OW.load()

        self.rf_menu = QPopupMenu(self, "Recent Files")
        self.updateRecentFiles(None)

        self.filemenu = QPopupMenu(self, 'FileMenu')
        self.filemenu.insertItem('&New', self.newFile, Qt.CTRL+Qt.Key_N)
        self.filemenu.insertItem('&Open...', self.openFile, Qt.CTRL+Qt.Key_O)
        self.filemenu.insertItem('&Save', self.saveFile, Qt.CTRL+Qt.Key_S)
        self.filemenu.insertItem('Save &As...', self.saveAsFile)
        self.filemenu.insertSeparator()
        self.filemenu.insertItem('Export &Quickbars...', self.openCraftBars)
        self.filemenu.insertItem('Export &UI XML (Beta)...', self.generateUIXML)
        self.filemenu.insertSeparator()
        self.filemenu.insertItem('&Recent Files', self.rf_menu)
        self.filemenu.insertSeparator()
        self.filemenu.insertItem('E&xit', self, SLOT('close()'), Qt.CTRL+Qt.Key_X)
        self.menuBar().insertItem('&File', self.filemenu)

        self.swapGems = QPopupMenu(self, "SwapGemsMenu")
        for piece in range(0,len(PieceTabList)):
            self.swapGems.insertItem(PieceTabList[piece], piece)
            self.swapGems.connectItem(piece, self.swapWith)
            self.swapGems.setItemParameter(piece, piece)

        self.editmenu = QPopupMenu(self, 'EditMenu')
        self.editmenu.insertItem('S&wap Gems With...', self.swapGems)
        self.editmenu.insertSeparator()
        self.editmenu.insertItem('&Options...', self.openOptions)
        self.menuBar().insertItem('&Edit', self.editmenu)

        self.viewmenu = QPopupMenu(self, 'ViewMenu')
        self.showcapmenuid = self.viewmenu.insertItem('Distance to &Cap', self.showCap)
        self.viewmenu.setItemChecked(self.showcapmenuid, self.capDistance)
        self.viewmenu.insertSeparator()
        self.viewmenu.insertItem('&Configuration', self.openConfigReport, Qt.CTRL+Qt.Key_C)
        self.viewmenu.insertItem('Choose Format...', self.chooseReportFile)
        self.viewmenu.insertSeparator()
        self.viewmenu.insertItem('&Materials', self.openMaterialsReport, Qt.CTRL+Qt.Key_M)
        self.menuBar().insertItem('&View', self.viewmenu)

        self.errorsmenu = QPopupMenu(self, "Errors")
        self.errorsmenu.insertSeparator()
        self.errorsmenuid = self.menuBar().insertItem('&Errors', self.errorsmenu)
        self.menuBar().setItemEnabled(self.errorsmenuid, False)

        self.helpmenu = QPopupMenu(self, 'HelpMenu')
        self.helpmenu.insertItem('&About', self.aboutBox)
        self.menuBar().insertItem('&Help', self.helpmenu)

        self.initialize()
        self.pricingInfo = OW.getPriceInfo()
        self.restoreItem(Item())
        self.nocalc = 0
        self.calculate()
        self.modified = 0

    def fix_taborder(self, line):
        if line > 4:
            prev = self.Effect[line - 1]
        elif line > 0:
            prev = self.Quality[line - 1]
        else: 
            prev = self.ItemName
        for i in range(line, 10):
            # Create the (sometimes used) edit boxes
            self.setTabOrder(prev,self.Type[i])
            self.setTabOrder(self.Type[i],self.AmountEdit[i])
            if i > 4:
                self.setTabOrder(self.AmountEdit[i],self.Effect[i])
                prev = self.Effect[i]
            else:
                self.setTabOrder(self.AmountEdit[i],self.AmountDrop[i])
                self.setTabOrder(self.AmountDrop[i],self.Effect[i])
                self.setTabOrder(self.Effect[i],self.Quality[i])
                prev = self.Quality[i]
        self.setTabOrder(prev,self.CraftButton)
        self.setTabOrder(self.CraftButton,self.LoadItem)
        self.setTabOrder(self.CraftButton,self.SaveItem)
        self.setTabOrder(self.SaveItem,self.ClearItem)
        self.setTabOrder(self.ClearItem,self.SkillsList)
        self.setTabOrder(self.SkillsList,self.OtherBonusList)

    def close(self, args):
        Options.Options(self).OK_pressed() # write out app config data to disk
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 'Some changes may not have been saved. Are you sure you want to quit?', 'Yes', 'No')
            if ret == 0:
                return QMainWindow.close(self, 1)
            else:
                return False
        else: return QMainWindow.close(self, 1)

    def initialize(self):

# Options passed over from the options box
        self.noteText = ''
        self.craftMultiplier = 6
        self.save = 1
        self.filename = None
        self.newcount = self.newcount + 1
        filetitle = unicode("Template" + str(self.newcount))
        self.setCaption(filetitle + " - Kort's Spellcrafting Calculator")

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
        self.switchOnType['drop'] = [ 
            self.QualEdit, self.SaveItem, self.ItemName,
            self.Amount_Edit_1, self.Amount_Edit_2,
            self.Amount_Edit_3, self.Amount_Edit_4,
            self.Amount_Edit_5, self.Amount_Edit_6,
            self.Amount_Edit_7, self.Amount_Edit_8,
            self.Amount_Edit_9, self.Amount_Edit_10,
            self.Gem_Label_6,
            self.Gem_Label_7, self.Gem_Label_8,
            self.Gem_Label_9, self.Gem_Label_10,
            self.Type_6, self.Type_7,
            self.Type_8, self.Type_9, self.Type_10,
            self.Effect_6, self.Effect_7,
            self.Effect_8, self.Effect_9, self.Effect_10,
        ]
        self.switchOnType['player'] = [
            self.QualDrop, self.CraftButton, 
            self.LabelGemQuality, self.LabelGemPoints, self.LabelGemCost,
            self.Amount_Drop_1, self.Amount_Drop_2,
            self.Amount_Drop_3, self.Amount_Drop_4,
            self.Amount_Drop_5,
            self.Quality_1, self.Quality_2, self.Quality_3, self.Quality_4,
            ## self.Quality_5, (doesn't matter for tinctures, keep hidden)
            self.Points_1, self.Points_2, self.Points_3, self.Points_4,
            self.Points_5,
            self.Cost_1, self.Cost_2, self.Cost_3, self.Cost_4,
            ## self.Cost_5, XXX not calculated yet
            self.Name_1, self.Name_2, self.Name_3, self.Name_4,
            self.Name_5,
            self.ItemImbueLabel, self.ItemImbue,
            self.ItemImbueSlashLabel, self.ItemImbueTotal,
            self.ItemOverchargeLabel, self.ItemOvercharge,
            self.ItemCostLabel, self.ItemCost,
            ## self.ItemPriceLabel, self.ItemPrice, XXX not calculated yet
        ]

        self.RealmChanged(self.realm)

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

    def PieceTabChanged(self,a0):
        if self.nocalc:
            return
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        self.storeItem(item)
        self.currentPieceTab = a0
        self.currentTabLabel = string.strip(str(self.PieceTab.tab(a0).text()))
        self.restoreItem(self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel)))

    def changePieceTab(self,a0):
        self.PieceTab.setCurrentTab(self.PieceTab.tab(a0))

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
            toprng = 10
            item.loadAttr('ItemName', unicode(self.ItemName.text())) 
            item.loadAttr('ItemQuality', unicode(self.QualEdit.text()))
        item.loadAttr('AFDPS', unicode(self.AFDPS_Edit.text()))
        item.loadAttr('Speed', unicode(self.Speed_Edit.text())) 
        item.loadAttr('Bonus', unicode(self.Bonus_Edit.text()))
        item.loadAttr('ActiveState', state)
        for slot in range(0, toprng):
            typectrl = self.Type[slot]
            effectctrl = self.Effect[slot]
            if state == 'drop':
                amountctrl = self.AmountEdit[slot]
                qua = '99'
                item.loadSlotAttrs(state, slot, 
                    typectrl.currentText(), 
                    amountctrl.text(),
                    effectctrl.currentText(), 
                    qua,
                    item.getSlotAttr(state, slot, 'Time'),
                    item.getSlotAttr(state, slot, 'Remakes'),
                    item.getSlotAttr(state, slot, 'Done'))
            else:
                amountctrl = self.AmountDrop[slot]
                qua = self.Quality[slot].currentText()
                item.loadSlotAttrs(state, slot, 
                    typectrl.currentText(), 
                    amountctrl.currentText(),
                    effectctrl.currentText(), 
                    qua,
                    item.getSlotAttr(state, slot, 'Time'),
                    item.getSlotAttr(state, slot, 'Remakes'),
                    item.getSlotAttr(state, slot, 'Done'))
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
            typelist = list(TypeList)
        else:
            self.Drop.setChecked(1)
            self.showDropWidgets()
            toprng = 10
            typelist = list(DropTypeList)
        self.ItemLevel.setText(item.getAttr('Level'))
        location = item.getAttr('Location')
        self.Equipped.setChecked(int(item.getAttr('Equipped')))
        for slot in range(0, toprng):
            typecombo = self.Type[slot]
            typecombo.clear()
            if slot == 4 and itemtype == 'player':
                typelist = list(EffectTypeList)
            gemtype = str(item.getSlotAttr(itemtype, slot, 'Type'))
            if not gemtype in typelist:
                typelist.append(gemtype)
            typecombo.insertStrList(typelist)
            typecombo.setCurrentItem(typelist.index(gemtype))
            self.UpdateCombo(0, slot)
            if gemtype == 'Unused':
                continue
            gemeffect = str(item.getSlotAttr(itemtype, slot, 'Effect'))
            self.Effect[slot].setCurrentText(gemeffect)
            self.UpdateCombo(1, slot)
            if itemtype == 'drop':
                am = item.getSlotAttr(itemtype, slot, 'Amount')
                amedit = self.AmountEdit[slot]
                amedit.setText(am)
            else:
                gemamount = item.getSlotAttr(itemtype, slot, 'Amount')
                if ValuesLists.has_key(gemtype):
                    if isinstance(ValuesLists[gemtype], tuple):
                        amountlist = ValuesLists[gemtype]
                    else:
                        if ValuesLists[gemtype].has_key(gemeffect):
                            amountlist = ValuesLists[gemtype][gemeffect]
                if gemamount in amountlist:
                    self.AmountDrop[slot].setCurrentItem(
                            amountlist.index(gemamount))
                quacombo = self.Quality[slot]
                gemqua = item.getSlotAttr(itemtype, slot, 'Qua')
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
        charleveltext = str(self.CharLevel.text())
        if charleveltext == '': 
            charlevel = 1
        else:
            charlevel = max(min(50, int(charleveltext)), 1)
        self.CharLevel.setText(str(charlevel))
        self.totals = { }
        self.capTotals = { }
        for effect in GemLists['All']['Resist']:
            self.totals[effect] = 0
        for effect in GemLists['All']['Stat']:
            self.totals[effect] = 0
            self.capTotals[effect] = 0
        self.totals['Hits'] = 0
        self.totals['Power'] = 0
        self.capTotals['Hits'] = 0
        self.capTotals['Power'] = 0
        self.capTotals['AF'] = 0
        skillTotals = {}
        otherTotals = {}
        errorcount = 0
        self.errorsmenu.clear()
        totalutility = 0.0
        totalcost = 0
        for key, item in self.itemattrlist.items():
            utility = 0.0
            itemtype = item.getAttr('ActiveState')
            itemcost = 0
            if itemtype == 'player':
                toprng = 5
            else:
                toprng = 10
            gemeffects = []
            for i in range(0, toprng):
                gemtype = item.getSlotAttr(itemtype, i, 'Type')
                if str(item.getSlotAttr(itemtype, i, 'Amount')) == '':
                    amount = 0
                else:
                    amount = re.sub('[^\d]', '', item.getSlotAttr(itemtype, i, 'Amount'))
                    if amount == '': amount = '0'
                    amount = int(amount)
                effect = item.getSlotAttr(itemtype, i, 'Effect')
                if effect != '' and [gemtype, effect] in gemeffects:
                    self.errorsmenu.insertItem('Two of same type of gem on %s' % key, errorcount)
                    self.errorsmenu.connectItem(errorcount, self.changePieceTab)
                    self.errorsmenu.setItemParameter(errorcount, TabList.index(key))
                    errorcount = errorcount + 1
                gemeffects.append([gemtype, effect])
                if itemtype == 'player':
                    if key == self.currentTabLabel:
                        self.Cost[i].setText('')
                    (cost, costindex) = SC.computeGemCost(item, i)
                    itemcost += cost
                    if key == self.currentTabLabel:
                        self.Cost[i].setText(SC.formatCost(cost))
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
                                skillTotals[f + ' Focus'] = amount
                        else:
                            skillTotals[effect + ' Focus'] = amount
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
                    self.errorsmenu.insertItem('Impossible Overcharge on %s' % key, errorcount)
                    self.errorsmenu.connectItem(errorcount, self.changePieceTab)
                    self.errorsmenu.setItemParameter(errorcount, TabList.index(key))
                    errorcount = errorcount + 1
                elif imbue > (itemimbue+0.5):
                    success = -OCStartPercentages[int(imbue-itemimbue)]
                    for i in range(0, 4):
                        if item.getSlotAttr(itemtype, i, 'Type') == 'Unused':
                            success += GemQualOCModifiers['94']
                        else:
                            success += GemQualOCModifiers[item.getSlotAttr(itemtype, i, 'Qua')]
                    success += ItemQualOCModifiers[str(self.QualDrop.currentText())]
                    skillbonus = (int(self.crafterSkill / 50) - 10) * 5
                    if skillbonus > 50: skillbonus = 50
                    success += skillbonus
            if key == self.currentTabLabel:
                self.ItemUtility.setText('%3.1f' % utility)
                if self.PlayerMade.isChecked():
                    self.ItemImbue.setText('%3.1f' % imbue)
                    self.ItemImbueTotal.setText(unicode(itemimbue))
                    self.ItemCost.setText(SC.formatCost(itemcost))
                    for i in range(0, 5):
                        n = self.Name[i]
                        n.setText(SC.getGemName(item, i))
                        if item.getSlotAttr(itemtype, i, 'Done') == '1':
                            self.GemLabel[i].setEnabled(0)
                        else:
                            self.GemLabel[i].setEnabled(1)
                    if (imbue - itemimbue) >= 6:
                        self.ItemOvercharge.setText('Impossible!')
                    elif imbue > (itemimbue+0.5):
                        if success < 0:
                            self.ItemOvercharge.setText('BOOM! (%d%%)' % success)
                        else:
                            self.ItemOvercharge.setText('%d%%' % success)
                    else:
                        self.ItemOvercharge.setText('None')
        for (key, val) in self.totals.items():
            if not self.capDistance:
                if self.includeRacials:
                    if GemTables['All']['Resist'].has_key(key):
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
        self.ItemTotalUtility.setText('%3.1f' % totalutility)
        self.TotalCost.setText(SC.formatCost(totalcost))
        self.SkillsList.clear()
        self.OtherBonusList.clear()
        for skill, amount in skillTotals.items():
            if not self.capDistance:
                self.SkillsList.insertItem('%d %s' % (amount, skill))
            else:
                if skill[-6:] == " Focus":
                    capcalc = HighCapBonusList['Focus']
                else:
                    capcalc = HighCapBonusList['Skill']
                thiscap = int(charlevel * capcalc[0]) + capcalc[1]
                self.SkillsList.insertItem('%d %s' % (thiscap - amount, skill))
        for bonus, amount in otherTotals.items():
            if not self.capDistance:
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
        self.menuBar().setItemEnabled(self.errorsmenuid, (errorcount > 0))

        self.nocalc = 0

    def computePrice(self):
        price = 0
        cost = 0
        for key, item in self.itemattrlist.items():
            itemcost = 0
            itemtype = item.getAttr('ActiveState')
            if itemtype == 'drop': continue
            for i in range(0, 5):
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
        try: itemlevel = int(item.getAttr('Level'))
        except: itemlevel = 0
        if itemlevel < 1 or itemlevel > 51:
            itemlevel = 1
            item.loadAttr('Level', '1')
        if (item.getAttr('Level') == item.getAttr('AFDPS')) \
                and (itemlevel % 2 == 1) and (itemlevel > 1) and (itemlevel != 51):
            itemlevel = itemlevel - 1
        try: itemqual = int(item.getAttr('ItemQuality')) - 94
        except: itemqual = -1
        if itemqual < 0 or itemqual >= len(ImbuePts[itemlevel - 1]):
            itemqual = 0
            item.loadAttr('ItemQuality', '94')
        itemimbue = ImbuePts[itemlevel - 1][itemqual]
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
                self.Points[i].setText('%3.1f' % mval)
            mvals.append(mval)
        maximbue = max(mvals)
        if display:
            for j in range(0, len(mvals)):
                if j != mvals.index(maximbue):
                    self.Points[j].setText('%3.1f' % (mvals[j] / 2.0))
                else:
                    self.Points[j].setText('%3.1f' % mvals[j])
        mvals.remove(maximbue)
        totalimbue = ((maximbue * 2 + sum(mvals)) / 2.0)
        return totalimbue
        
    def getMultiplier(self, type):
        return ImbueMultipliers[type]

    def UpdateCombo(self, type, num):
        typecombo = self.Type[num]
        typetext = str(typecombo.currentText())
        effcombo = self.Effect[num]
        efftext = str(effcombo.currentText())
        if self.PlayerMade.isChecked():
            amount = self.AmountDrop[num]
        else:
            amount = self.AmountEdit[num]
        if typetext == 'Unused':
            if type == 0:
                effcombo.clear()
                if effcombo.editable():
                    effcombo.setEditable(False)
                    self.fix_taborder(num)
                amount.clear()
                if self.PlayerMade.isChecked():
                    self.Quality[num].setCurrentItem(0)
        else:
            if self.PlayerMade.isChecked():
                effectlist = self.effectlists
            else:
                effectlist = self.dropeffectlists
            if effectlist.has_key(typetext):
                effectlist = effectlist[typetext]
            else:
                effectlist = list()
            if type == 0:
                effcombo.clear()
                if len(effectlist) > 0:
                    effcombo.insertStrList(list(effectlist))
                    effcombo.setCurrentItem(0)
            if type == 1:
                unique = (not efftext in effectlist) or (len(efftext) > 3 and efftext[-3:] == "...")
                if effcombo.editable() and not unique:
                    refocus = self.Effect[num].hasFocus()
                    effcombo.setEditable(False)
                    effcombo.setCurrentItem(effectlist.index(efftext))
                    self.fix_taborder(num)
                elif unique and not effcombo.editable():
                    refocus = self.Effect[num].hasFocus()
                    effcombo.setEditable(True)
                    effcombo.setCurrentText(efftext)
                    self.fix_taborder(num)
                else:
                    refocus = False
                if refocus:
                    flip = self.Effect[num].setFocus()
            if self.PlayerMade.isChecked():
                amtindex = amount.currentItem()
                amount.clear()
                if ValuesLists.has_key(typetext):
                    valueslist = ValuesLists[typetext]
                    efftext = str(effcombo.currentText())
                    if isinstance(valueslist, dict):
                        if valueslist.has_key(efftext):
                            valueslist = valueslist[efftext]
                        else:
                            valueslist = tuple()
                    elif efftext[0:5] == "All M":
                        valueslist = ("1",)
                    if len(valueslist) > 0:
                        amount.insertStrList(list(valueslist))
                    if amtindex < len(valueslist):
                        amount.setCurrentItem(amtindex)
                if type == 0:
                    self.Quality[num].setCurrentItem(len(QualityValues)-2)

    def RaceChanged(self, a0):
        race = str(self.CharRace.currentText())
        for rt in GemLists['All']['Resist']:
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
        self.dropeffectlists['Skill'] = DropLists[showrealm]['Skill']
        self.dropeffectlists['Focus'] = DropLists[showrealm]['Focus']
        if self.hideNonClassSkills:
            self.effectlists['Skill'] = AllBonusList['All'][self.charclass]['All Skills']
            self.effectlists['Focus'] = AllBonusList['All'][self.charclass]['All Focus']
        else:
            self.effectlists['Skill'] = GemLists[showrealm]['Skill']
            self.effectlists['Focus'] = GemLists[showrealm]['Focus']
        race = str(self.CharRace.currentText())
        self.CharRace.clear()
        racelist = AllBonusList[self.realm][self.charclass]['Races']
        self.CharRace.insertStrList(list(racelist))
        if race in racelist:
          self.CharRace.setCurrentItem(racelist.index(race))
        self.RaceChanged('')
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        if self.save:
            self.restoreItem(item)
        self.calculate()

    def RealmChanged(self,a0):
        self.realm = str(self.Realm.currentText())
        self.CharClass.clear()
        self.CharClass.insertStrList(list(ClassList[self.realm]))
        if self.charclass in ClassList[self.realm]:
          self.CharClass.setCurrentItem(ClassList[self.realm].index(self.charclass))
        self.CharClassChanged('')
    
    def TypeChanged(self, Value):
        index = self.focusWidget().name()[-2:]
        if index[0] == '_': index = index[1:]
        wascalc = self.nocalc
        self.nocalc = 1
        self.modified = 1
        self.UpdateCombo(0, int(index) - 1)
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        self.storeItem(item)
        self.nocalc = wascalc
        self.calculate()

    def EffectChanged(self, value):
        index = str(self.focusWidget().name())[-2:]
        if not index[-1].isdigit():
            index = str(self.focusWidget().parentWidget().name())[-2:]
        if not index[0].isdigit(): index = index[1:]
        wascalc = self.nocalc
        self.nocalc = 1
        self.modified = 1
        self.UpdateCombo(1, int(index) - 1)
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        self.storeItem(item)
        self.nocalc = wascalc
        self.calculate()

    def showWideEffects(self, wide):
        width = self.EffectWidths[wide]
        for num in range(0, 5):
          eff = self.Effect[num]
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
        self.Gem_Label_5.setEnabled(1)
        self.Gem_Label_5.setText('Gem 5:')

    def showPlayerWidgets(self):
        for w in self.switchOnType['player']:
            w.show()
        for w in self.switchOnType['drop']:
            w.hide()
        self.showWideEffects(0)
        self.Gem_Label_5.setText('Proc:')

    def DropToggled(self,a0):
        if self.nocalc:
            return
        if not a0: 
            return
        self.modified = 1
        self.showDropWidgets()
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        item.loadAttr('ActiveState','drop')
        if self.save:
            self.restoreItem(item)

    def PlayerToggled(self, a0):
        if self.nocalc:
            return
        if not a0: 
            return
        self.modified = 1
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
        Qfd.setViewMode(QFileDialog.List)
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
            self.AFDPS_Edit.setText(str(self.ItemLevelWindow.afdps))

    def EquippedClicked(self):
        item = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        self.storeItem(item)
        self.calculate()
    
    def newFile(self):
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 'Some changes may not have been saved. Are you sure you want to discard these changes?', 'Yes', 'No')
            if ret == 1:
                return
        wascalc = self.nocalc
        self.nocalc = 1
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
        filename = unicode(filename)
        while filename != '':
            if filename != '' and os.path.exists(filename):
                ret = QMessageBox.warning(self, 'Overwrite?', 'Do you want to overwrite the selected file?', 'Yes', 'No')
                if ret == 1:
                    filename = QFileDialog.getSaveFileName(filename, "Templates (*.xml)")
                    filename = unicode(filename)
                else:
                    break
            else: break
        if filename != '':
            if filename[-4:] != '.xml':
                filename += '.xml'
            try:
                f = open(filename, 'w')
                f.write(XMLHelper.writexml(self.asXML(), UnicodeStringIO(), '', '\t', '\n'))
                self.modified = 0
                f.close()
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + filename, 'OK')
                return
            self.filename = filename
            self.updateRecentFiles(filename)
            filetitle = os.path.basename(filename)
            self.setCaption(filetitle + " - Kort's Spellcrafting Calculator")
            

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
        filename = unicode(filename)
        if filename is not None and filename != '':
            try:
                f = open(filename, 'r')
            except IOError:
                traceback.print_exc()
                QMessageBox.critical(None, 'Error!', 
                    'Error opening file: ' + filename, 'OK')
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
            self.filename = filename
            self.updateRecentFiles(filename)
            filetitle = os.path.basename(filename)
            self.setCaption(filetitle + " - Kort's Spellcrafting Calculator")

    def updateRecentFiles(self, fn):
        if fn is not None:
            while fn in self.recentFiles:
                self.recentFiles.remove(fn)
            self.recentFiles.insert(0, fn)
        if len(self.recentFiles) > 5:
            del self.recentFiles[5:]
        self.rf_menu.clear()
        for count in range(0, len(self.recentFiles)):
            self.rf_menu.insertItem('&%d %s' % (count + 1, self.recentFiles[count]), count)
            self.rf_menu.connectItem(count, self.loadRecentFile)
            self.rf_menu.setItemParameter(count, count)

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
                self.charclass = XMLHelper.getText(child.childNodes)
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
        self.Realm.setCurrentItem(Realms.index(self.realm))
        self.RealmChanged(self.realm)
        if AllBonusList[self.realm].has_key(self.charclass):
            self.CharClass.setCurrentItem(ClassList[self.realm].index(self.charclass))
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
                self.charclass = charclass[0]+string.lower(charclass[1:])
                if self.realm == 'HIB':
                    self.realm = 'Hibernia'
                elif self.realm == 'ALB':
                    self.realm = 'Albion'
                elif self.realm == 'MID':
                    self.realm = 'Midgard'
                self.Realm.setCurrentItem(Realms.index(self.realm))
                self.RealmChanged(self.realm)
                if AllBonusList[self.realm].has_key(self.charclass):
                   self.CharClass.setCurrentItem(ClassList[self.realm].index(self.charclass))
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
        if res == 1:
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

    def aboutBox(self):
        splash = AboutScreen(parent=self,modal=True)
        splash.exec_loop()

    def openCraftBars(self):
        CB = CraftBar.CraftBar(self.DaocPath, self, '', 1)
        CB.exec_loop()
        self.DaocPath = str(CB.DaocPath.text())

    def DelveItemsDialog(self, find, findtype = None):
        locs = []
        for key, item in self.itemattrlist.items():
            activestate = item.getAttr('ActiveState')
            if activestate == 'drop':
                toprng = 10
            else:
                toprng = 5
            for slot in range(0, toprng):
                type = str(item.getSlotAttr(activestate, slot, 'Type'))
                if type == 'Unused': continue
                if (findtype and type != findtype) or \
                   (not findtype and type in ('Resist',)): continue
                effect = str(item.getSlotAttr(activestate, slot, 'Effect'))
                if effect != find: 
                    if find == 'Power' or find == '% Power Pool':
                       if effect != 'Power' and effect != '% Power Pool':
                           continue
                    elif effect == 'Acuity':
                       if not find in AllBonusList[self.realm][self.charclass][effect]:
                           continue
                    elif (type == 'Skill' or type == 'Focus') and effect[0:4] == 'All ' \
                            and effect in AllBonusList[self.realm][self.charclass].keys():
                        if not find in AllBonusList[self.realm][self.charclass][effect]:
                            continue
                    else:
                        continue
                amount = str(item.getSlotAttr(activestate, slot, 'Amount'))
                if type == 'Focus':
                    amount += ' Levels Focus'
                if effect != find: 
                    amount += ' ' + effect
                if type == 'Cap Increase':
                    amount += ' Cap'
                locs.append([key, amount])
        DW = DisplayWindow.DisplayWindow(self, modal = 1)
        if findtype:
            DW.setCaption('Slots With %s %s' % (find, findtype))
        else:
            DW.setCaption('Slots With %s' % find)
        DW.loadLocations(locs)
        DW.exec_loop()


    def gemClicked(self, item, slot):
        RW = ReportWindow.ReportWindow(self, '', 1)
        RW.setCaption('Materials')
        RW.materialsReport({item: self.itemattrlist[item]}, slot)
        RW.exec_loop()

    def mousePressEvent(self, e):
        if e is None: return
        child = self.childAt(e.pos(), False)
        if child is None: return
        if not isinstance(child, QLabel): return
        shortname = str(child.name())
        nameidx = 1
        while nameidx < len(shortname):
            if shortname[nameidx] < 'a' or shortname[nameidx] > 'z':
                shorttype = shortname[nameidx:]
                shortname = shortname[0:nameidx]
            nameidx += 1
        if shortname in ['Gem', 'Points', 'Cost', 'Name']:
            slot = child.name()[-2:]
            if str(slot[0:1]) == '_':
                slot = slot[1:]
            if self.PlayerMade.isChecked():
                self.gemClicked(self.currentTabLabel, int(slot))
            return
        if shortname in ['', 'Label', 'Total', 'Item']: return
        if child.parent().name() == 'GroupResists':
           self.DelveItemsDialog(shortname, 'Resist')
        else:
           self.DelveItemsDialog(shortname)

    def resizeEvent(self, e):
        sz = e.size()
        QMainWindow.resizeEvent(self, e)

    def SkillClicked(self,a0):
        if a0 is None: return
        if not ' ' in str(a0.text()): return
        amount, effect = string.split(str(a0.text()), ' ', 1)
        self.DelveItemsDialog(effect)

    def showCap(self):
        self.capDistance = not self.capDistance
        self.viewmenu.setItemChecked(self.showcapmenuid, self.capDistance)
        self.calculate()

    def swapWith(self, piece):
        part = TabList[piece]
        cur = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        swap = self.itemattrlist.get(part, Item(part))
        self.itemattrlist[part] = cur
        self.itemattrlist[self.currentTabLabel] = swap
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def loadRecentFile(self, index):
        self.openFile(self.recentFiles[index], True)

    def generateUIXML(self):
        UIXML.uixml(self)
