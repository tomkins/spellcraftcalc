# ScWindow.py: Dark Age of Camelot Spellcrafting Calculator (main Window)
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtCore import *
from PyQt4.QtGui import *
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
import MultiTabBar4
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
    def __init__(self,parent = None,name = "About",modal = True,
                 fl = Qt.SplashScreen|Qt.MSWindowsFixedSizeDialogHint):
        QDialog.__init__(self,parent,fl)
        self.setModal(modal)
        self.setObjectName(name)
        pixmap = QPixmap(parent.splashFile)
        self.palette().setBrush(self.backgroundRole(), QBrush(pixmap))
        self.resize(QSize(480,340).expandedTo(pixmap.size()))
        self.show()
        if not self.hasFocus():
            self.setFocus(Qt.ActiveWindowFocusReason)

    def mouseReleaseEvent(self, e):
        # a little lame, e should match a mouseDown event in our window
        self.close()

    def keyPressEvent(self, e):
        if len(e.text()):
            self.close()


class ScWindow(QMainWindow, Ui_B_SC):
    def __init__(self):
        self.splashFile = None
        self.newcount = 0
        self.startup = 1
        self.nocalc = 1
        self.totals = { }
        self.capTotals = { }
        self.recentFiles = []
        self.effectlists = GemLists['All'].copy()
        self.dropeffectlists = DropLists['All'].copy()
        self.itemeffectlists = CraftedLists['All'].copy()

        self.fixedtaborder = False

        QMainWindow.__init__(self,None,Qt.Window)
        self.setAttribute(Qt.WA_DeleteOnClose)
        Ui_B_SC.setupUi(self,self)
        self.statusBar().hide()
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            self.sizegrip = QSizeGrip(self)
            self.sizegrip.move(self.width() - 15, self.height() - 15)

        self.initLayout()
        self.initControls()
        self.updateGeometry()

        self.ItemLevelWindow = ItemLevel.ItemLevel(self.window(), '', 1)
        self.DaocPath = ''
        self.ItemPath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "items")
        self.TemplatePath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "templates")
        self.reportFile = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                                       'reports', 'Default_Config_Report.xml')
        self.realm = 'Albion'
        self.charclass = 'Armsman'
        self.crafterSkill = 1000
        self.showDoneInMatsList = 0
        self.coop = False
        self.noteText = ''
        self.capDistance = False
        self.includeRacials = False
        self.hideNonClassSkills = False
        self.pricingInfo = {}
        OW = Options.Options(self)
        OW.load()
        self.initMenu()
        self.pricingInfo = OW.getPriceInfo()
        self.updateRecentFiles(None)
        self.initialize(0)
        
    def initLayout(self):
        testfont = QFontMetrics(QApplication.font())

        self.switchOnType = {'drop' : [], 'player' : [] }
        self.switchOnType['drop'] = [ 
            self.QualEdit, self.LabelRequirement,
        ]
        self.switchOnType['player'] = [
            self.QualDrop,
            self.LabelGemQuality, self.LabelGemPoints,
            self.LabelGemCost, self.LabelGemName,
            self.ItemImbueLabel, self.ItemImbue, self.ItemImbueTotal,
            self.ItemOverchargeLabel, self.ItemOvercharge,
            self.ItemCostLabel, self.ItemCost,
            self.ItemPriceLabel, self.ItemPrice,
            self.LabelRequirement2,
        ]

        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            edheight = self.CharName.sizeHint().height() - 1
            cbheight = self.Realm.sizeHint().height()
        else:
            edheight = min(self.CharName.minimumSizeHint().height(),
                           self.Realm.minimumSizeHint().height()) - 2
            cbheight = edheight

        amtcbwidth = self.QualDrop.getMinimumWidth(['100'])
        # minSizeHint includes one char, test 19.9 width...
        amtedwidth = self.ItemLevel.minimumSizeHint().width()
        amtedwidth += testfont.size(Qt.TextSingleLine, "19.").width()

        self.StatLabel = {}
        self.StatValue = {}
        self.StatCap = {}
        self.StatBonus = {}

        for stat in (GemLists['All']['Stat'] + ('Power', 'Hits',)):
            self.StatLabel[stat] = getattr(self, stat + 'Label')
            self.StatValue[stat] = getattr(self, stat)
            self.StatCap[stat] = getattr(self, stat + 'Cap')
        width = testfont.size(Qt.TextSingleLine, "400").width()
        self.GroupStats.layout().setColumnMinimumWidth(1,width)
        width = testfont.size(Qt.TextSingleLine, " (400)").width()
        self.GroupStats.layout().setColumnMinimumWidth(2,width)

        for stat in (GemLists['All']['Resist']):
            self.StatLabel[stat] = getattr(self, stat + 'Label')
            self.StatValue[stat] = getattr(self, stat)
            self.StatBonus[stat] = getattr(self, stat + 'RR')
        width = testfont.size(Qt.TextSingleLine, "26").width()
        self.GroupResists.layout().setColumnMinimumWidth(1,width)
        width = testfont.size(Qt.TextSingleLine, " (5)").width()
        self.GroupResists.layout().setColumnMinimumWidth(2,width)

        skillmodel = QStandardItemModel(0,1,self.SkillsList)
        self.SkillsList.setModel(skillmodel)
        palette = QPalette(self.SkillsList.palette())
        palette.setColor(QPalette.Base, palette.color(QPalette.Window))
        palette.setBrush(QPalette.Base, palette.window())
        self.SkillsList.setPalette(palette)
        self.GroupSkillsList.layout().setColumnStretch(0, 1)
        self.ScWinFrame.layout().setColumnStretch(6, 1)

        cbwidth = self.CharClass.getMinimumWidth(['Necromancer'])
        self.CharName.setFixedSize(QSize(cbwidth, edheight + 2))
        self.Realm.setFixedSize(QSize(cbwidth, cbheight + 2))
        self.CharClass.setFixedSize(QSize(cbwidth, cbheight + 2))
        self.CharRace.setFixedSize(QSize(cbwidth, cbheight + 2))
        self.CharLevel.setFixedSize(QSize(amtedwidth, edheight + 2))

        self.Realm.insertItems(0, list(Realms))
        self.QualDrop.insertItems(0, list(QualityValues))

        self.CharLevel.setValidator(QIntValidator(0, 99, self))
        self.ItemLevel.setValidator(QIntValidator(0, 99, self))
        self.QualEdit.setValidator(QIntValidator(0, 100, self))
        self.Bonus_Edit.setValidator(QIntValidator(0, 99, self))

        self.GroupItemFrame.layout().itemAt(0).changeSize(1, 
                                    self.PieceTab.baseOverlap(),
                                    QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.GemLabel = []
        self.Type = []
        self.Effect = []
        self.AmountEdit = []
        self.AmountDrop = []
        self.Quality = []
        self.Points = []
        self.Cost = []
        self.Requirement = []
        self.Name = []

        self.ItemLevel.setFixedSize(QSize(amtedwidth, edheight))
        self.ItemLevelButton.setFixedSize(
            QSize(self.ItemLevelButton.width(), edheight))
        self.QualDrop.setFixedSize(QSize(amtcbwidth, cbheight))
        self.QualEdit.setFixedSize(QSize(amtcbwidth, edheight))
        self.Bonus_Edit.setFixedSize(QSize(amtedwidth, edheight))
        self.AFDPS_Edit.setFixedSize(QSize(amtedwidth, edheight))
        self.Speed_Edit.setFixedSize(QSize(amtedwidth, edheight))
        self.ItemNameCombo.setFixedHeight(cbheight)

        self.GroupItemFrame.layout().setColumnStretch(8, 1)
        width = testfont.size(Qt.TextSingleLine, " Slot 10:").width()
        self.GroupItemFrame.layout().setColumnMinimumWidth(0,width)
        width = testfont.size(Qt.TextSingleLine, " Points").width()
        self.GroupItemFrame.layout().setColumnMinimumWidth(5,width)
        reqwidth = width
        width = testfont.size(Qt.TextSingleLine, "  999g 00s 00c").width()
        self.GroupItemFrame.layout().setColumnMinimumWidth(6,width)
        reqwidth += width + amtcbwidth

        typewidth = self.Type_1.getMinimumWidth(list(DropTypeList))
        l = reduce(lambda x, y: x+y, [ list(x) for x in GemLists['All'].values() ])
        effectwidth = self.Effect_1.getMinimumWidth(l)

        editAmountValidator = QIntValidator(-999, +999, self)

        for i in range(0, 12):
            idx = i + 1

            self.GemLabel.append(getattr(self, 'Gem_Label_%d' % idx))
            self.Type.append(getattr(self, 'Type_%d' % idx))
            self.Type[i].setFixedSize(QSize(typewidth, cbheight))
            self.connect(self.Type[i],SIGNAL("activated(int)"),
                         self.TypeChanged)
            self.GemLabel[i].setBuddy(self.Type[i])

            self.AmountEdit.append(getattr(self, 'Amount_Edit_%d' % idx))
            self.AmountEdit[i].setFixedSize(QSize(amtcbwidth, edheight))
            self.AmountEdit[i].setValidator(editAmountValidator)
            self.switchOnType['drop'].append(self.AmountEdit[i])
            self.connect(self.AmountEdit[i],SIGNAL("textChanged(const QString&)"),
                         self.AmountsChanged)

            self.Effect.append(getattr(self, 'Effect_%d' % idx))
            self.Effect[i].setFixedSize(QSize(effectwidth, cbheight))
            self.Effect[i].setInsertPolicy(QComboBox.NoInsert)
            self.connect(self.Effect[i],SIGNAL("activated(int)"),
                         self.EffectChanged)
            self.connect(self.Effect[i],SIGNAL("editTextChanged(const QString&)"),
                         self.EffectChanged)

            self.Requirement.append(getattr(self, 'Requirement_%d' % idx))
            self.Requirement[i].setFixedSize(QSize(reqwidth, edheight))
            self.switchOnType['drop'].append(self.Requirement[i])
            self.connect(self.Requirement[i],SIGNAL("textChanged(const QString&)"),
                         self.AmountsChanged)

            if i < 6:
                self.AmountDrop.append(getattr(self, 'Amount_Drop_%d' % idx))
                self.AmountDrop[i].setFixedSize(QSize(amtcbwidth, cbheight))
                self.connect(self.AmountDrop[i],SIGNAL("activated(int)"),
                             self.AmountsChanged)
                self.Name.append(getattr(self, 'Name_%d' % idx))
                self.switchOnType['player'].extend([
                    self.AmountDrop[i], self.Name[i], ])
            else:
                self.switchOnType['drop'].extend([
                    self.GemLabel[i], self.Type[i], self.Effect[i], ])

            if i < 4:
                self.Quality.append(getattr(self, 'Quality_%d' % idx))
                self.Quality[i].insertItems(0, list(QualityValues))
                self.Quality[i].setFixedSize(QSize(amtcbwidth, cbheight))
                self.connect(self.Quality[i],SIGNAL("activated(int)"),
                             self.AmountsChanged)
                self.Points.append(getattr(self, 'Points_%d' % idx))
                self.Cost.append(getattr(self, 'Cost_%d' % idx))
                self.switchOnType['player'].extend([
                    self.Quality[i], self.Points[i], self.Cost[i], ])

            self.GroupItemFrame.layout().setRowMinimumHeight(i + 3, 
                max(cbheight, edheight))

        for tabname in PieceTabList:
            self.PieceTab.addTab(0, qApp.translate("B_SC",tabname,None))
        for tabname in JewelTabList:
            self.PieceTab.addTab(1, qApp.translate("B_SC",tabname,None))
        self.GroupItemFrame.stackUnder(self.PieceTab)
        l = self.ScWinFrame.layout().itemAt(self.ScWinFrame.layout().count() - 1)
        l.layout().itemAt(1).changeSize(1, -self.PieceTab.baseOverlap(),
                                        QSizePolicy.Minimum, QSizePolicy.Fixed)


    def initControls(self):
        self.GroupStats.mousePressEvent = self.ignoreMouseEvent
        self.GroupResists.mousePressEvent = self.ignoreMouseEvent
        self.GroupItemFrame.mousePressEvent = self.ignoreMouseEvent

        self.connect(self.GroupStats,SIGNAL("mousePressEvent(QMouseEvent*)"),
                     self.mousePressEvent)
        self.connect(self.GroupResists,SIGNAL("mousePressEvent(QMouseEvent*)"),
                     self.mousePressEvent)
        self.connect(self.GroupItemFrame,SIGNAL("mousePressEvent(QMouseEvent*)"),
                     self.mousePressEvent)

        self.connect(self.CharName,SIGNAL("textChanged(const QString&)"),
                     self.TemplateChanged)
        self.connect(self.Realm,SIGNAL("activated(int)"),
                     self.RealmChanged)
        self.connect(self.CharClass,SIGNAL("activated(int)"),
                     self.CharClassChanged)
        self.connect(self.CharRace,SIGNAL("activated(int)"),
                     self.RaceChanged)
        self.connect(self.CharLevel,SIGNAL("textChanged(const QString&)"),
                     self.TemplateChanged)

        self.connect(self.PieceTab,SIGNAL("currentChanged"),self.PieceTabChanged)
        self.connect(self.ItemLevel,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.ItemLevelButton,SIGNAL("clicked()"),self.ItemLevelShow)
        self.connect(self.QualDrop,SIGNAL("activated(int)"),
                     self.ItemChanged)
        self.connect(self.QualEdit,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.Bonus_Edit,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.AFDPS_Edit,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.Speed_Edit,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.Equipped,SIGNAL("stateChanged(int)"),self.ItemChanged)
        self.connect(self.ItemNameCombo,SIGNAL("activated(int)"),
                     self.ItemNameSelected)
        self.connect(self.ItemNameCombo,SIGNAL("textChanged(const QString&)"),
                     self.ItemNameEdited)
        self.connect(self.SkillsList,SIGNAL("activated(const QModelIndex&)"),
                     self.SkillClicked)

    def initMenu(self):
        self.rf_menu = QMenu('&Recent Files')
        self.connect(self.rf_menu, SIGNAL("triggered(QAction*)"), self.loadRecentFile)
        
        self.filemenu = QMenu('&File', self)
        self.filemenu.addAction('&New', self.newFile, QKeySequence(Qt.CTRL+Qt.Key_N))
        self.filemenu.addAction('&Open...', self.openFile, QKeySequence(Qt.CTRL+Qt.Key_O))
        self.filemenu.addAction('&Save', self.saveFile, QKeySequence(Qt.CTRL+Qt.Key_S))
        self.filemenu.addAction('Save &As...', self.saveAsFile)
        self.filemenu.addSeparator()
        self.filemenu.addAction('&Load Item...', self.loadItem,
                                QKeySequence(Qt.CTRL+Qt.SHIFT+Qt.Key_L))
        self.filemenu.addAction('Sa&ve Item...', self.saveItem,
                                QKeySequence(Qt.CTRL+Qt.SHIFT+Qt.Key_S))
        self.filemenu.addAction('Item Database Path...', self.chooseItemPath)
        self.filemenu.addSeparator()
        self.filemenu.addAction('Export &Quickbars...', self.openCraftBars)
        self.filemenu.addAction('Export &UI XML (Beta)...', self.generateUIXML)
        self.filemenu.addSeparator()
        self.filemenu.addMenu(self.rf_menu)
        self.filemenu.addSeparator()
        self.filemenu.addAction('E&xit', self.close, QKeySequence(Qt.CTRL+Qt.Key_X))
        self.menuBar().addMenu(self.filemenu)

        self.swapjewelmenu = QMenu('Jewel Slots', self)
        for piece in range(0,len(JewelTabList)):
            act = QAction(JewelTabList[piece], self)
            act.setData(QVariant(piece + len(PieceTabList)))
            self.swapjewelmenu.addAction(act)
        self.swappiecemenu = QMenu('Body Slots', self)
        for piece in range(0,len(PieceTabList)):
            act = QAction(PieceTabList[piece], self)
            act.setData(QVariant(piece))
            self.swappiecemenu.addAction(act)
        self.swapgemsmenu = QMenu('S&wap Gems with',self)
        self.connect(self.swapgemsmenu, SIGNAL("triggered(QAction*)"), self.swapWith)
        self.connect(self.swappiecemenu, SIGNAL("triggered(QAction*)"), self.swapWith)
        self.connect(self.swapjewelmenu, SIGNAL("triggered(QAction*)"), self.swapWith)

        self.movejewelmenu = QMenu('Jewel Slots', self)
        for piece in range(0,len(JewelTabList)):
            act = QAction(JewelTabList[piece], self)
            act.setData(QVariant(piece + len(PieceTabList)))
            self.movejewelmenu.addAction(act)
        self.movepiecemenu = QMenu('Body Slots', self)
        for piece in range(0,len(PieceTabList)):
            act = QAction(PieceTabList[piece], self)
            act.setData(QVariant(piece))
            self.movepiecemenu.addAction(act)
        self.moveitemmenu = QMenu('&Move Item to',self)
        self.connect(self.moveitemmenu, SIGNAL("triggered(QAction*)"), self.moveTo)
        self.connect(self.movepiecemenu, SIGNAL("triggered(QAction*)"), self.moveTo)
        self.connect(self.movejewelmenu, SIGNAL("triggered(QAction*)"), self.moveTo)

        self.newitemmenu = QMenu('&New Item', self)
        act = QAction('Drop Item', self)
        act.setData(QVariant('Drop Item'))
        self.newitemmenu.addAction(act)
        self.newitemmenu.addSeparator()
        for type in ('Normal Item', 'Caster Staff', 'Legendary Staff',
                     'Enhanced Bow', 'Legendary Bow',
                     'Legendary Weapon', 'Enhanced Armor'):
            act = QAction(type, self)
            act.setData(QVariant(type))
            self.newitemmenu.addAction(act)
        self.connect(self.newitemmenu, SIGNAL("triggered(QAction*)"), 
                     self.newItemType)

        self.chooseitemmenu = QMenu('Item &Type', self)
        for type in ('Normal Item', 'Caster Staff', 'Legendary Staff',
                     'Enhanced Bow', 'Legendary Bow',
                     'Legendary Weapon', 'Enhanced Armor'):
            act = QAction(type, self)
            act.setData(QVariant(type))
            self.chooseitemmenu.addAction(act)
        self.connect(self.chooseitemmenu, SIGNAL("triggered(QAction*)"), 
                     self.chooseItemType)

        self.editmenu = QMenu('&Edit', self)
        self.chooseitemmenuid = self.editmenu.addMenu(self.chooseitemmenu)
        self.swapgemsmenuid = self.editmenu.addMenu(self.swapgemsmenu)
        self.editmenu.addSeparator()
        self.editmenu.addMenu(self.newitemmenu)
        self.editmenu.addMenu(self.moveitemmenu)
        self.editmenu.addAction('Delete Item', self.deleteCurrentItem)
        self.editmenu.addAction('Clear Item', self.clearCurrentItem)
        self.editmenu.addSeparator()
        self.editmenu.addAction('&Options...', self.openOptions,
                                QKeySequence(Qt.ALT+Qt.Key_O))
        self.menuBar().addMenu(self.editmenu)

        self.viewmenu = QMenu('&View', self)
        self.craftingmenuid = self.viewmenu.addAction('&Gem Crafting', 
                                  self.openCraftWindow,
                                  QKeySequence(Qt.ALT+Qt.Key_G))
        self.viewmenu.addSeparator()
        self.viewmenu.addAction('&Materials', self.openMaterialsReport,
                                QKeySequence(Qt.ALT+Qt.Key_M))
        self.viewmenu.addAction('&Configuration', self.openConfigReport,
                                QKeySequence(Qt.ALT+Qt.Key_C))
        self.viewmenu.addAction('Choose Format...', self.chooseReportFile)
        self.viewmenu.addSeparator()
        self.showcapmenuid = self.viewmenu.addAction('&Distance to Cap', self.showCap,
                                                     QKeySequence(Qt.ALT+Qt.Key_D))
        self.showcapmenuid.setCheckable(True)
        self.showcapmenuid.setChecked(self.capDistance)
        self.menuBar().addMenu(self.viewmenu)

        self.errorsmenu = QMenu('Errors', self)
        self.errorsmenuid = self.menuBar().addMenu(self.errorsmenu)
        self.connect(self.errorsmenu, SIGNAL('triggered(QAction*)'), 
                     self.changePieceTab)
        self.errorsmenuid.setEnabled(False)
        self.helpmenu = QMenu('&Help', self)
        self.helpmenu.addAction('&About', self.aboutBox)
        self.menuBar().addMenu(self.helpmenu)

    def fix_taborder(self, line):
        if line > 0:
            prev = self.Requirement[line - 1]
        else: 
            prev = self.Equipped
        for i in range(line, 12):
            # Create the (sometimes used) edit boxes
            self.setTabOrder(prev,self.Type[i])
            self.setTabOrder(self.Type[i],self.AmountEdit[i])
            if i < 6:
                self.setTabOrder(self.AmountEdit[i],self.AmountDrop[i])
                self.setTabOrder(self.AmountDrop[i],self.Effect[i])
                if i < 4:
                    self.setTabOrder(self.Effect[i],self.Quality[i])
                    self.setTabOrder(self.Quality[i],self.Requirement[i])
                else:
                    self.setTabOrder(self.Effect[i],self.Requirement[i])
            else:
                self.setTabOrder(self.AmountEdit[i],self.Effect[i])
                self.setTabOrder(self.Effect[i],self.Requirement[i])
            prev = self.Requirement[i]
        self.setTabOrder(prev,self.SkillsList)

    def showFixWidgets(self):
        for i in range(0,6):
            self.GemLabel[i].show()
            self.Type[i].show()
            self.Effect[i].show()

    def showDropWidgets(self, item):
        if not self.isVisible(): return
        self.GroupItemFrame.hide()
        self.showFixWidgets()
        for w in self.switchOnType['player']:
            w.hide()
        for w in self.switchOnType['drop']:
            w.show()
        for i in range(0,4):
            self.GemLabel[i].setEnabled(1)
            self.GemLabel[i].setText('Slot &%d:' % (i + 1))
        #self.GroupItemFrame.updateGeometry()
        self.craftingmenuid.setEnabled(False)
        self.chooseitemmenuid.setEnabled(False)
        self.swapgemsmenuid.setEnabled(False)
        self.GroupItemFrame.show()

    def showPlayerWidgets(self, item):
        self.GroupItemFrame.hide()
        self.showFixWidgets()
        for w in self.switchOnType['drop']:
            w.hide()
        for w in self.switchOnType['player']:
            w.show()
        for i in range(0,item.slotCount()):
            self.GemLabel[i].setEnabled(1)
            if item.slot(i).slotType() == 'player':
                self.GemLabel[i].setText('Gem &%d:' % (i + 1))
            else:
                self.GemLabel[i].setText('Slot &%d:' % (i + 1))
                if i < 4:
                    self.Quality[i].hide()
                    self.Points[i].hide()
                    self.Cost[i].hide()
                self.Requirement[i].show()
            if item.slot(i).slotType() == 'unused':
                if item.slot(i).type() == 'Unused':
                    self.GemLabel[i].hide()
                    self.Type[i].hide()
                    self.AmountDrop[i].hide()
                    self.Effect[i].hide()
                    self.Requirement[i].hide()

        #self.GroupItemFrame.updateGeometry()
        #self.craftingmenuid.setEnabled(True)
        self.testCraftingMenu()
        self.chooseitemmenuid.setEnabled(True)
        self.swapgemsmenuid.setEnabled(True)
        self.GroupItemFrame.show()

    def testCraftingMenu(self):
        item = self.itemattrlist[self.currentTabLabel]
        enableCrafting = False
        for slot in item.slots():
            if slot.crafted():
                enableCrafting = True
        self.craftingmenuid.setEnabled(enableCrafting)

    def closeEvent(self, e):
        OW = Options.Options(self)
        OW.save()
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 
                                      "This template has been changed.\n"
                                      "Do you want to save these changes?", 
                                      QMessageBox.Yes, QMessageBox.No, QMessageBox.Cancel)
            if ret == QMessageBox.Cancel:
                e.ignore()
                return
            if ret == QMessageBox.Yes:
                self.saveFile()
                if self.modified: 
                    e.ignore()
                    return
        e.accept()


    def initialize(self, moretodo):
        self.nocalc = 1
        self.noteText = ''
        self.craftMultiplier = 1
        self.filename = None
        self.newcount = self.newcount + 1
        filetitle = unicode("Template" + str(self.newcount))
        self.setWindowTitle(filetitle + " - Kort's Spellcrafting Calculator")

        self.PieceTab.setCurrentIndex(0, 0)
        self.currentTab = self.PieceTab
        self.currentTabLabel = string.strip(str(self.PieceTab.tabText(0, 0)))

        self.Equipped.setChecked(1)

        self.itemattrlist = { }
        self.itemnumbering = 1
        for tab in PieceTabList:
            self.itemattrlist[tab] = Item(realm=self.realm,state='player',loc=tab)
            self.itemattrlist[tab].next = Item(realm=self.realm,state='drop',loc=tab)
            self.itemattrlist[tab].ItemName = "Crafted Item" \
                                            + str(self.itemnumbering)
            self.itemattrlist[tab].next.ItemName = "Drop Item" \
                                                 + str(self.itemnumbering)
            self.itemnumbering += 1
        for tab in JewelTabList:
            self.itemattrlist[tab] = Item(realm=self.realm,state='drop',loc=tab)
            self.itemattrlist[tab].ItemName = "Drop Item" \
                                            + str(self.itemnumbering)
            self.itemnumbering += 1

        self.CharName.setText('')
        self.Realm.setCurrentIndex(Realms.index(self.realm))
        self.RealmChanged(self.Realm.currentIndex())
        self.CharLevel.setText('50')
        self.restoreItem(self.itemattrlist[self.currentTabLabel])
        self.modified = 0
        self.nocalc = moretodo
        if self.nocalc: return
        self.calculate()

    def asXML(self):
        document = Document()
        rootnode = document.createElement('SCTemplate')
        document.appendChild(rootnode)
        childnode = document.createElement('Name')
        childnode.appendChild(document.createTextNode(str(self.CharName.text())))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Realm')
        childnode.appendChild(document.createTextNode(self.realm))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Class')
        childnode.appendChild(document.createTextNode(self.charclass))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Race')
        childnode.appendChild(document.createTextNode(unicode(self.CharRace.currentText())))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Level')
        childnode.appendChild(document.createTextNode(unicode(self.CharLevel.text())))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Notes')
        childnode.appendChild(document.createTextNode(str(self.noteText)))
        rootnode.appendChild(childnode)

        for key, item in self.itemattrlist.iteritems():
            # use firstChild here because item.asXML() constructs a Document()
            while item is not None:
                childnode = item.asXML()
                if childnode is not None:
                    rootnode.appendChild(childnode.firstChild)
                item = item.next
        return document

    def PieceTabChanged(self, row, col):
        self.currentTabLabel = string.strip(str(self.PieceTab.tabText(row, col)))
        if self.currentTabLabel in JewelTabList:
            swapactionlist = self.swapjewelmenu.actions()
            moveactionlist = self.swapjewelmenu.actions()
            swapsubmenu = self.swappiecemenu
            movesubmenu = self.movepiecemenu
        else:
            swapactionlist = self.swappiecemenu.actions()
            moveactionlist = self.movepiecemenu.actions()
            swapsubmenu = self.swapjewelmenu
            movesubmenu = self.movejewelmenu
        self.swapgemsmenu.clear()
        self.moveitemmenu.clear()
        self.swapgemsmenu.addMenu(swapsubmenu)
        self.moveitemmenu.addMenu(movesubmenu)
        for act in swapactionlist:
            if str(act.text()) == self.currentTabLabel: continue
            self.swapgemsmenu.addAction(act)
        for act in moveactionlist:
            if str(act.text()) == self.currentTabLabel: continue
            self.moveitemmenu.addAction(act)
        if self.nocalc:
            return
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

        self.testCraftingMenu()

    def changePieceTab(self,a0):
        mask = a0.data().toInt()[0]
        row = (mask >> 8) & 0xff
        col = mask & 0xff
        self.PieceTab.setCurrentIndex(row, col)

    def FixupItemLevel(self):
        if str(self.ItemLevel.text()) == '' \
                or re.compile('\D').search(str(self.ItemLevel.text())):
            itemimbue = 0
        else:
            itemlevel = int(str(self.ItemLevel.text()))
            if itemlevel > 51: itemlevel = 51
            if itemlevel < 1: itemlevel = 1
            self.ItemLevel.setText('%d' % itemlevel)

    def restoreItem(self, item):
        if item is None: return
        wasnocalc = self.nocalc
        self.nocalc = 1
        itemtype = item.ActiveState
        if itemtype == 'player':
            self.showPlayerWidgets(item)
        else:
            self.showDropWidgets(item)
        self.ItemNameCombo.clear()

        altitem = item
        while altitem is not None:
            self.ItemNameCombo.addItem(altitem.ItemName)
            altitem = altitem.next
        self.ItemNameCombo.setCurrentIndex(0)
        #self.ItemNameCombo.setEditText(item.ItemName)

        self.ItemLevel.setText(item.Level)
        location = item.Location
        self.Equipped.setChecked(int(item.Equipped))
        for slot in range(0, item.slotCount()):
            typecombo = self.Type[slot]
            typecombo.clear()
            if itemtype == 'player':
                if item.slot(slot).slotType() == 'player':
                    typelist = list(TypeList)
                else:
                    typelist = list(CraftedTypeList)
            else:
                typelist = list(DropTypeList)
            gemtype = str(item.slot(slot).type())
            if not gemtype in typelist:
                typelist.append(gemtype)
            typecombo.insertItems(0, typelist)
            typecombo.setCurrentIndex(typelist.index(gemtype))
            self.TypeChanged(typelist.index(gemtype), slot)
            gemeffect = str(item.slot(slot).effect())
            effect = self.Effect[slot].findText(gemeffect)
            if len(gemeffect) and effect < 0:
                if itemtype == 'player':
                    self.Effect[slot].addItem(gemeffect)
                    self.Effect[slot].setCurrentIndex(self.Effect[slot].count() - 1)
                    self.EffectChanged(effect, slot)
                else:
                    if not self.Effect[slot].isEditable():
                        self.Effect[slot].setEditable(True)
                    self.Effect[slot].setEditText(gemeffect)
            else:
                self.Effect[slot].setCurrentIndex(effect)
                self.EffectChanged(effect, slot)
            if itemtype == 'drop':
                self.AmountEdit[slot].setText(item.slot(slot).amount())
            else:
                gemamount = item.slot(slot).amount()
                amount = self.AmountDrop[slot].findText(gemamount)
                if len(gemamount) and gemamount != "0" and amount < 0:
                    self.AmountDrop[slot].addItem(gemamount)
                    self.AmountDrop[slot].setCurrentIndex(self.AmountDrop[slot].count() - 1)
                else:
                    self.AmountDrop[slot].setCurrentIndex(amount)
            if itemtype == 'player' and item.slot(slot).slotType() == 'player':
                quacombo = self.Quality[slot]
                gemqua = item.slot(slot).qua()
                if gemqua in QualityValues:
                    if quacombo.count() > 0:
                        quacombo.setCurrentIndex(QualityValues.index(gemqua))
            else:
                self.Requirement[slot].setText(item.slot(slot).requirement())
        self.AFDPS_Edit.setText(item.AFDPS)
        self.Speed_Edit.setText(item.Speed)
        self.Bonus_Edit.setText(item.Bonus)
        if itemtype == 'drop':
            self.QualEdit.setText(item.ItemQuality)
            #self.ItemNameCombo.setText(item.ItemName)
        else:
            if item.ItemQuality in QualityValues:
                self.QualDrop.setCurrentIndex(
                    QualityValues.index(item.ItemQuality))
        self.nocalc = wasnocalc
        if self.nocalc: return
        self.calculate()

    def insertSkill(self,amt,bonus,group):
        model = self.SkillsList.model()
        model.insertRows(model.rowCount(), 1)
        wid = 3
        if amt > -10 and amt < 10: wid += 1
        bonus = "%*d %s" % (wid, amt, bonus)
        index = model.index(model.rowCount()-1, 0, QModelIndex())
        model.setData(index, QVariant(bonus), Qt.DisplayRole)
        model.setData(index, QVariant(group), Qt.UserRole)

    def calculate(self):
        if self.nocalc:
            return
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
        totalprice = 0
        for key, item in self.itemattrlist.iteritems():
            utility = 0.0
            itemtype = item.ActiveState
            itemcost = 0
            itemprice = 0
            gemeffects = []
            for i in range(0, item.slotCount()):
                slot = item.slot(i)
                utility += slot.gemUtility()
                gemtype = slot.type()
                effect = slot.effect()
                amount = int('0'+re.sub('[^\d]', '', slot.amount()))
                if i < 4 and itemtype == 'player':
                    cost = slot.gemCost()
                    itemcost += cost
                    if key == self.currentTabLabel:
                        self.Cost[i].setText(SC.formatCost(cost))
                    if cost > 0:
                        itemprice += int(self.pricingInfo.get('PPGem', 0) * 10000)
                        if self.pricingInfo.get('HourInclude', 0):
                            itemprice += int(self.pricingInfo.get('Hour', 0) * 10000 \
                                           * int(slot.time()) / 60.0)
                        if self.pricingInfo.get('TierInclude', 0):
                            gemlvl = str(slot.gemLevel())
                            tierp = self.pricingInfo.get('Tier', {})
                            itemprice += int(float(tierp.get(gemlvl, 0)) * 10000)
                        if self.pricingInfo.get('QualInclude', 0):
                            gemqual = slot.qua()
                            qualp = self.pricingInfo.get('Qual', {})
                            itemprice += int(cost * float(qualp.get(gemqual, 0)) / 100.0)
                    if gemtype != 'Unused':
                        if [gemtype, effect] in gemeffects:
                            error_act = QAction('Two of same type of gem on %s' % key, self)
                            if item.Location in JewelTabList:
                                row = 1
                                col = JewelTabList.index(item.Location)
                            else:
                                row = 0
                                col = PieceTabList.index(item.Location)
                            error_act.setData(QVariant((row << 8) | col))
                            self.errorsmenu.addAction(error_act)
                            errorcount = errorcount + 1
                        gemeffects.append([gemtype, effect])
                if not item.Equipped == '1':
                    continue
                if gemtype == 'Skill':
                    if effect[0:4] == 'All ':
                        effects = AllBonusList[self.realm][self.charclass][effect]
                    else:
                        if self.hideNonClassSkills and \
                                not AllBonusList[self.realm][self.charclass] \
                                                ['Skills Hash'].has_key(effect):
                            effects = tuple()
                        else:
                            effects = (effect,)
                    for effect in effects:
                        if not skillTotals.has_key(effect):
                            skillTotals[effect] = amount
                        else:
                            skillTotals[effect] += amount
                elif gemtype == 'Focus':
                    if effect[0:4] == 'All ':
                        effects = AllBonusList[self.realm][self.charclass][effect]
                    elif self.hideNonClassSkills:
                        if self.hideNonClassSkills and \
                                not AllBonusList[self.realm][self.charclass] \
                                                ['Skills Hash'].has_key(effect):
                            effects = tuple()
                    else:
                        effects = (effect,)
                    for effect in effects:
                        skillTotals[effect + ' Focus'] = amount
                elif gemtype == 'Power':
                    self.totals[gemtype] += amount
                elif gemtype == 'Hits':
                    self.totals[gemtype] += amount
                elif gemtype == 'Resist':
                    self.totals[effect] += amount
                elif gemtype == 'Stat':
                    if effect == 'Acuity':
                        for e in AllBonusList[self.realm][self.charclass][effect]:
                            self.totals[e] += amount
                    else:
                        self.totals[effect] += amount
                elif gemtype == 'Other Bonus' or gemtype == 'PvE Bonus':
                    if not otherTotals.has_key(effect):
                        otherTotals[effect] = amount
                    else:
                        otherTotals[effect] += amount
                elif gemtype == 'Cap Increase':
                    if effect == 'Acuity':
                        effects = AllBonusList[self.realm][self.charclass][effect]
                    else:
                        effects = (effect,)
                    for effect in effects:
                        self.capTotals[effect] += amount
            totalutility += utility
            itemimbue = self.getItemImbue(item)
            imbuepts = self.calcImbue(item, key == self.currentTabLabel)
            if self.pricingInfo.get('PPInclude', 0):
                itemprice += int(self.pricingInfo.get('PPImbue', 0) * 10000 * imbuepts)
                itemprice += int(self.pricingInfo.get('PPOC', 0) * 10000 \
                               * max(0, int(imbuepts - self.getItemImbue(item))))
                if itemcost > 0:
                    itemprice += int(self.pricingInfo.get('PPLevel', 0) * 10000 \
                                   * int(item.Level))
            if itemcost > 0:
                itemprice += int(self.pricingInfo.get('PPItem', 0) * 10000)
            itemprice += int(itemcost * self.pricingInfo.get('General', 0) / 100.0)
            if self.pricingInfo.get('CostInPrice', 1):
                itemprice += itemcost
            totalcost += itemcost
            totalprice += itemprice
            if itemtype == 'player':
                if (imbuepts - itemimbue) >= 6:
                    error_act = QAction('Impossible Overcharge on %s' % key, self)
                    if item.Location in JewelTabList:
                        row = 1
                        col = JewelTabList.index(item.Location)
                    else:
                        row = 0
                        col = PieceTabList.index(item.Location)
                    error_act.setData(QVariant((row << 8) | col))
                    self.errorsmenu.addAction(error_act)
                    errorcount = errorcount + 1
                elif imbuepts > (itemimbue+0.5):
                    success = -OCStartPercentages[int(imbuepts-itemimbue)]
                    for slot in item.slots():
                        if not slot.crafted(): continue
                        success += GemQualOCModifiers[slot.qua()]
                    success += ItemQualOCModifiers[str(self.QualDrop.currentText())]
                    skillbonus = (int(self.crafterSkill / 50) - 10) * 5
                    if skillbonus > 50: skillbonus = 50
                    success += skillbonus
            if key == self.currentTabLabel:
                self.ItemUtility.setText('%3.1f' % utility)
                if item.ActiveState == 'player':
                    self.ItemImbue.setText('%3.1f' % imbuepts)
                    self.ItemImbueTotal.setText(' / ' + unicode(itemimbue))
                    self.ItemCost.setText(SC.formatCost(itemcost))
                    self.ItemPrice.setText(SC.formatCost(itemprice))
                    for i in range(0, item.slotCount()):
                        slot = item.slot(i)
                        self.Name[i].setText(slot.gemName(self.realm))
                        if slot.crafted() and slot.done() == "1":
                            self.GemLabel[i].setEnabled(0)
                        else:
                            self.GemLabel[i].setEnabled(1)
                    if (imbuepts - itemimbue) >= 6:
                        self.ItemOvercharge.setText('Impossible!')
                    elif imbuepts > (itemimbue+0.5):
                        if success < 0:
                            self.ItemOvercharge.setText('BOOM! (%d%%)' % success)
                        else:
                            self.ItemOvercharge.setText('%d%%' % success)
                    else:
                        self.ItemOvercharge.setText('None')
        for (key, val) in self.totals.iteritems():
            if not self.capDistance:
                if self.includeRacials:
                    if GemTables['All']['Resist'].has_key(key):
                        rr = str(self.StatBonus[key].text())
                        if rr != '-':
                            val += int(rr[1:-1])
                if self.capTotals.has_key(key):
                  if self.capTotals[key] > 0:
                    self.StatCap[key].setText('('+str(self.capTotals[key])+')')
                  else:
                    self.StatCap[key].setText('-')
                self.StatValue[key].setText(unicode(val))
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
                    self.StatCap[key].setText('('+unicode(int(capcap))+')')
                else:
                    capmod = 0
                self.StatValue[key].setText(unicode(int(basecap + capmod) - val))
        self.SkillsList.model().removeRows(0, self.SkillsList.model().rowCount())
        for skill, amount in skillTotals.iteritems():
            if not self.capDistance:
                self.insertSkill(amount, skill, "Skill")
            else:
                if skill[-6:] == " Focus":
                    capcalc = HighCapBonusList['Focus']
                else:
                    capcalc = HighCapBonusList['Skill']
                thiscap = int(charlevel * capcalc[0]) + capcalc[1]
                self.insertSkill(thiscap - amount, skill, "Skill")
        for bonus, amount in otherTotals.iteritems():
            if not self.capDistance:
                self.insertSkill(amount, bonus, "Bonus")
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
                self.insertSkill(cap + capmod - amount, bonus, "Bonus")
        totalprice += self.pricingInfo.get('PPOrder', 0) * 10000
        self.TotalCost.setText(SC.formatCost(totalcost))
        self.TotalPrice.setText(SC.formatCost(totalprice))
        self.TotalUtility.setText('%3.1f' % totalutility)
        self.errorsmenuid.setEnabled(errorcount > 0)

    def getItemImbue(self, item):
        try: itemlevel = int(item.Level)
        except: itemlevel = 0
        if itemlevel < 1 or itemlevel > 51:
            itemlevel = 1
            item.Level = '1'
        if (item.Level == item.AFDPS) \
                and (itemlevel % 2 == 1) and (itemlevel > 1) and (itemlevel != 51):
            itemlevel = itemlevel - 1
        try: itemqual = int(item.ItemQuality) - 94
        except: itemqual = -1
        if itemqual < 0 or itemqual >= len(ImbuePts[itemlevel - 1]):
            itemqual = 0
            item.ItemQuality = '94'
        itemimbue = ImbuePts[itemlevel - 1][itemqual]
        return itemimbue

    def calcImbue(self, item, display):
        itemstate = item.ActiveState
        if itemstate == 'drop': return 0
        mvals = []
        for slot in item.slots():
            mval = slot.gemImbue()
            mvals.append(mval)
        if len(mvals) < 4:
            mvals.extend([0,0,0,0])
        maximbue = max(mvals)
        if display:
            for j in range(0, 4):
                if j != mvals.index(maximbue):
                    self.Points[j].setText('%3.1f' % (mvals[j] / 2.0))
                else:
                    self.Points[j].setText('%3.1f' % mvals[j])
        totalimbue = ((maximbue + sum(mvals)) / 2.0)
        return totalimbue
        
    def getMultiplier(self, type):
        return ImbueMultipliers[type]

    def TemplateChanged(self,a0):
        if self.nocalc: return
        self.modified = 1
        self.calculate()

    def RaceChanged(self, a0):
        race = str(self.CharRace.currentText())
        for rt in GemLists['All']['Resist']:
            if Races['All'][race]['Resists'].has_key(rt):
              if self.includeRacials:
                self.StatBonus[rt].setText('('+str(Races['All'][race]['Resists'][rt])+')')
              else:
                self.StatBonus[rt].setText('+'+str(Races['All'][race]['Resists'][rt]))
            else:
                self.StatBonus[rt].setText('-')
        if self.nocalc: return
        self.modified = 1
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

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
        self.CharRace.insertItems(0, list(racelist))
        if race in racelist:
            self.CharRace.setCurrentIndex(racelist.index(race))
        self.RaceChanged(self.CharRace.currentIndex())

    def RealmChanged(self,a0):
        self.realm = str(self.Realm.currentText())
        self.CharClass.clear()
        self.CharClass.insertItems(0, list(ClassList[self.realm]))
        if self.charclass in ClassList[self.realm]:
            self.CharClass.setCurrentIndex(ClassList[self.realm].index(self.charclass))
        self.CharClassChanged(self.CharClass.currentIndex())

    def ItemLevelShow(self):
        level = self.ItemLevelWindow.exec_()
        if level != -1:
            self.ItemLevel.setText(str(level))
            self.AFDPS_Edit.setText(str(self.ItemLevelWindow.afdps))

    def ItemChanged(self,a0):
        if self.nocalc: return
        self.modified = 1
        item = self.itemattrlist[self.currentTabLabel]
        self.FixupItemLevel()
        item.Level = unicode(self.ItemLevel.text())
        item.AFDPS = unicode(self.AFDPS_Edit.text())
        item.Speed = unicode(self.Speed_Edit.text())
        item.Bonus = unicode(self.Bonus_Edit.text())
        if self.Equipped.isChecked():
            item.Equipped = '1'
        else:
            item.Equipped = '0'
        if item.ActiveState == 'player':
            item.ItemQuality = unicode(self.QualDrop.currentText())
        else:
            #item.ItemNameCombo = unicode(self.ItemName.text())
            item.ItemQuality = unicode(self.QualEdit.text())
        self.calculate()

    def ItemNameSelected(self,a0):
        if self.nocalc: return
        if isinstance(a0,int):
            if a0 == 0: return
            item = self.itemattrlist[self.currentTabLabel]
            wasequipped = item.Equipped
            item.Equipped = '0'
            prev = item
            for a1 in range(0, a0 - 1):
                prev = prev.next
            item = prev.next
            prev.next = prev.next.next
            item.next = self.itemattrlist[self.currentTabLabel]
            self.itemattrlist[self.currentTabLabel] = item
            item.Equipped = wasequipped
            self.restoreItem(item)

    def ItemNameEdited(self,a0):
        if self.nocalc: return
        if self.ItemNameCombo.currentIndex() == -1:
            # strange interactions with focusOut...
            self.ItemNameCombo.setCurrentIndex(0)
        if self.ItemNameCombo.findText(a0) > 0: return
        item = self.itemattrlist[self.currentTabLabel]
        item.ItemName = unicode(self.ItemNameCombo.lineEdit().text())
        self.ItemNameCombo.setItemText(0,item.ItemName)
        self.modified = 1

    def senderSlot(self):
        index = self.sender().objectName()[-2:]
        if index[0] == '_': index = index[1:]
        return int(index) - 1

    def AmountsChanged(self, amount, slot = -1):
        if self.nocalc: return
        if slot < 0:
            slot = self.senderSlot()      
        #sys.stdout.write("Changes to slot %d %s\n" % (slot, str(self.sender().objectName())))
        item = self.itemattrlist[self.currentTabLabel]
        if item.ActiveState == 'player':
            item.slot(slot).setAmount(self.AmountDrop[slot].currentText())
        else:
            item.slot(slot).setAmount(self.AmountEdit[slot].text())
        if item.slot(slot).slotType() == 'player':
            item.slot(slot).setQua(self.Quality[slot].currentText())
        else:
            item.slot(slot).setRequirement(self.Requirement[slot].text())
        self.modified = 1
        self.calculate()

    def EffectChanged(self, value, slot = -1):
        if slot < 0:
            slot = self.senderSlot()        
        item = self.itemattrlist[self.currentTabLabel]
        if isinstance(value,int):
            efftext = str(self.Effect[slot].currentText())
        else:
            efftext = str(self.Effect[slot].lineEdit().text())
        #sys.stdout.write("Changes to slot %d Value %d Effect Item %s\n" % (slot, value, efftext))
        if not self.nocalc:
            item.slot(slot).setEffect(efftext)
            self.modified = 1
        typetext = str(item.slot(slot).type())
        effcombo = self.Effect[slot]
        unique = ((len(efftext) > 3 and efftext[-3:] == "...") \
               or not isinstance(value,int))
        if effcombo.isEditable() and not unique:
            refocus = self.Effect[slot].hasFocus()
            effcombo.setEditable(False)
            self.fix_taborder(slot)
        elif unique and not effcombo.isEditable():
            refocus = self.Effect[slot].hasFocus()
            effcombo.setEditable(True)
            self.fix_taborder(slot)
            if refocus:
                effcombo.lineEdit().selectAll()
        else:
            refocus = False
        if refocus:
            flip = self.Effect[slot].setFocus()
        if item.ActiveState == 'player':
            amount = self.AmountDrop[slot]
        else:
            amount = self.AmountEdit[slot]
        if typetext == 'Unused':
            amount.clear()
            if item.slot(slot).slotType() == 'player':
                self.Quality[slot].setCurrentIndex(0)
        elif item.ActiveState == 'player':
            amtindex = amount.currentIndex()
            amount.clear()
            if item.slot(slot).slotType() == 'player':
                valueslist = ValuesLists
            else:
                valueslist = CraftedValuesLists
            if valueslist.has_key(typetext):
                valueslist = valueslist[typetext]
                if isinstance(valueslist, dict):
                    if valueslist.has_key(efftext):
                        valueslist = valueslist[efftext]
                    else:
                        valueslist = tuple()
                elif efftext[0:5] == "All M":
                    valueslist = valueslist[:1]
                if len(valueslist) > 0:
                    amount.insertItems(0, list(valueslist))
                if amtindex < 0:
                    amtindex = 0
                if amtindex < len(valueslist):
                    amount.setCurrentIndex(amtindex)
            if item.slot(slot).slotType() == 'player':
                self.Quality[slot].setCurrentIndex(len(QualityValues)-2)
        # Cascade the changes
        self.AmountsChanged(0, slot)

    def TypeChanged(self, Value, slot = -1):
        if slot < 0:
            slot = self.senderSlot()
        item = self.itemattrlist[self.currentTabLabel]
        typetext = str(self.Type[slot].currentText())
        if not self.nocalc:
            item.slot(slot).setType(typetext)
            self.modified = 1
        effcombo = self.Effect[slot]
        if effcombo.isEditable():
            effcombo.setEditable(False)
            self.fix_taborder(slot)
        effcombo.clear()
        if item.ActiveState == 'player':
            if item.slot(slot).slotType() == 'player':
                effectlist = self.effectlists
            else:
                effectlist = self.itemeffectlists
        else:
            effectlist = self.dropeffectlists
        if effectlist.has_key(typetext):
            effectlist = effectlist[typetext]
        else:
            effectlist = list()
        if len(effectlist) > 0:
            effcombo.insertItems(0, list(effectlist))
        # Here we go... cascade
        effcombo.setCurrentIndex(0)
        self.EffectChanged(0, slot)
        self.testCraftingMenu()
    
    def clearCurrentItem(self):
        item = Item(realm=self.realm,loc=self.currentTabLabel,
                    state=self.itemattrlist[self.currentTabLabel].ActiveState)
        if item.ActiveState == 'drop':
            item.ItemName = "Drop Item" + str(self.itemnumbering)
        else:
            item.ItemName = "Crafted Item" + str(self.itemnumbering)
        self.itemattrlist[self.currentTabLabel] = item
        self.itemnumbering += 1
        if self.nocalc: return
        self.modified = 1
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def deleteCurrentItem(self):
        if self.itemattrlist[self.currentTabLabel].next is None:
            self.clearCurrentItem()
            return
        item = self.itemattrlist[self.currentTabLabel]
        self.itemattrlist[self.currentTabLabel] = item.next
        item.next = None
        if self.nocalc: return
        self.modified = 1
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def chooseItemPath(self):
        itemdir = QFileDialog.getExistingDirectory(self, 'Select Item Database Path', self.ItemPath)
        if itemdir:
            self.ItemPath = os.path.abspath(unicode(itemdir))
            ret = QMessageBox.question(self, 'Create Database Directories?', 
                                      "Create realm and item slot directories" +\
                                      " underneath %s ?" % itemdir, 
                                      QMessageBox.Yes, QMessageBox.No)
            if ret == QMessageBox.Yes:
                realms = list(Realms)
                realms.append("All")
                for realm in realms:
                    itempath = os.path.join(self.ItemPath, realm)
                    if not os.path.exists(itempath):
                        os.makedirs(itempath)
                    for ext in FileExt.values():
                        if ext == '*':
                            continue
                        if not isinstance(ext, types.StringType):
                            ext = ext[0]
                        itempath = os.path.join(self.ItemPath, realm, ext)
                        if not os.path.exists(itempath):
                            os.makedirs(itempath)

    def saveItem(self):
        itemname = string.replace(unicode(self.ItemNameCombo.currentText()), ' ', '_')
        if itemname == '':
            QMessageBox.critical(self, 'Error!', 
                'Cannot save item - You must specify a name!', 'OK')
            return
        item = self.itemattrlist[self.currentTabLabel]

        ext = FileExt[self.currentTabLabel]
        extstr = ''
        if not isinstance(ext, types.StringType):
            for e in ext:
                extstr += '*%s.xml ' % e
            ext = ext[0]
        else:
            extstr = '*%s.xml' % ext
        extstr = "Items (%s);;All Files (*.*)" % extstr.rstrip()
        itemname = itemname + '_' + ext + '.xml'
        itemdir = self.ItemPath
        recentdir = []
        if os.path.exists(os.path.join(itemdir, self.realm, ext)):
            itemdir = os.path.join(self.ItemPath, self.realm, ext)
            if self.coop:
                for realm in Realms:
                    if realm != self.realm:
                        recentdir.append(os.path.join(self.ItemPath, realm, ext))
            recentdir.append(os.path.join(self.ItemPath, "All", ext))
        filename = os.path.join(itemdir, itemname)
        filename = QFileDialog.getSaveFileName(self, "Save Item", filename, 
                                               "Templates (*.xml);;All Files (*.*)")
        filename = unicode(filename)
        if filename != '':
            item.save(filename)
            # QMessageBox.information(None, 'Success!',
            #         '%s successfully saved!' % itemname, 'OK')

    def loadItem(self):
        ext = FileExt[self.currentTabLabel]
        extstr = ''
        if not isinstance(ext, types.StringType):
            for e in ext:
                extstr += '*%s.xml *.%s ' % (e, e)
            ext = ext[0]
        else:
            extstr = '*%s.xml *.%s' % (ext, ext)
        extstr = "Items (%s);;All Files (*.*)" % extstr.rstrip()
        itemdir = self.ItemPath
        recentdir = []
        if os.path.exists(os.path.join(itemdir, self.realm, ext)):
            itemdir = os.path.join(self.ItemPath, self.realm, ext)
            if self.coop:
                for realm in Realms:
                    if realm != self.realm:
                        recentdir.append(os.path.join(self.ItemPath, realm, ext))
            recentdir.append(os.path.join(self.ItemPath, "All", ext))
        Qfd = ItemList.ItemListDialog(self, "Load Item", itemdir, extstr, 
                                      self.realm, self.charclass)
        Qfd.setHistory(recentdir)
        if Qfd.exec_():
            if Qfd.selectedFiles().count() > 0:
                filename = unicode(Qfd.selectedFiles()[0])
                item = Item(realm=self.realm,state='drop',loc=self.currentTabLabel)
                if item.load(filename,str(self.itemnumbering)) == -1: return
                if string.lower(item.Realm) != string.lower(self.realm)\
                    and string.lower(item.Realm) != 'all'\
                    and not self.coop:
                    QMessageBox.critical(None, 'Error!', 'You are trying to load an '
                                                       + 'item for another realm!', 'OK')
                    return
                self.itemnumbering += 1
                item.Location = self.currentTabLabel
                item.Equipped = self.itemattrlist[self.currentTabLabel].Equipped
                self.itemattrlist[self.currentTabLabel].Equipped = '0'
                item.next = self.itemattrlist[self.currentTabLabel]
                self.itemattrlist[self.currentTabLabel] = item
                self.restoreItem(item)
                self.modified = 1

    def newFile(self):
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 
                                      "This template has been changed.\n"
                                      "Do you want to save these changes?", 
                                      QMessageBox.Yes, QMessageBox.No, QMessageBox.Cancel)
            if ret == QMessageBox.Cancel: return
            if ret == QMessageBox.Yes:
                self.saveFile()
                if self.modified: return
        self.initialize(0)

    def saveFile(self):
        if self.filename is None:
            self.saveAsFile()
        else:
            try:
                f = open(self.filename, 'w')
                f.write(XMLHelper.writexml(self.asXML(), UnicodeStringIO(), '', '\t', '\n'))
                f.close()
                self.modified = 0
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + self.filename, 'OK')

    def saveAsFile(self):
        filename = self.filename
        if filename is None:
            filename = os.path.join(self.TemplatePath, str(self.CharName.text()) + "_template.xml")
        filename = unicode(filename)
        filename = QFileDialog.getSaveFileName(self, "Save Template", filename, 
                                               "Templates (*.xml);;All Files (*.*)")
        filename = unicode(filename)
        if filename != '':
            if filename[-4:] != '.xml':
                filename += '.xml'
            try:
                f = open(filename, 'w')
                f.write(XMLHelper.writexml(self.asXML(), UnicodeStringIO(), '', '\t', '\n'))
                f.close()
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + filename, 'OK')
                return
            self.modified = 0
            self.filename = os.path.abspath(filename)
            self.updateRecentFiles(self.filename)
            self.TemplatePath = os.path.dirname(self.filename)
            filetitle = os.path.basename(self.filename)
            self.setWindowTitle(filetitle + " - Kort's Spellcrafting Calculator")
            
    def openFile(self, *args):
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 
                                      "This template has been changed.\n"
                                      "Do you want to save these changes?", 
                                      QMessageBox.Yes, QMessageBox.No, QMessageBox.Cancel)
            if ret == QMessageBox.Cancel: return
            if ret == QMessageBox.Yes:
                self.saveFile()
                if self.modified: return
        if len(args) == 0:
            filename = QFileDialog.getOpenFileName(self, "Open Template", self.TemplatePath, 
                                                   "Templates (*.xml *.scc);;All Files (*.*)")
        else:
            filename = args[0]
        filename = unicode(filename)
        if filename is not None and filename != '':
            f = None
            try:
                f = open(filename, 'r')
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
                    'Error loading template file ' + unicode(filename), 'OK')
                if f is not None: f.close()
                return
            self.filename = os.path.abspath(filename)
            self.updateRecentFiles(self.filename)
            self.TemplatePath = os.path.dirname(self.filename)
            filetitle = os.path.basename(self.filename)
            self.setWindowTitle(filetitle + " - Kort's Spellcrafting Calculator")

    def updateRecentFiles(self, fn):
        if fn is not None:
            while fn in self.recentFiles:
                self.recentFiles.remove(fn)
            self.recentFiles.insert(0, fn)
        if len(self.recentFiles) > 5:
            del self.recentFiles[5:]
        self.rf_menu.clear()
        for count in range(0, len(self.recentFiles)):
            act = QAction('&%d %s' % (count + 1, self.recentFiles[count]), self)
            act.setData(QVariant(count))
            self.rf_menu.addAction(act)

    def loadFromXML(self, template):
        self.initialize(1)
        racename = ''
        classname = ''
        self.itemnumbering = 1
        itemdefault = self.itemattrlist.copy()
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
            elif child.tagName == 'Level':
                self.CharLevel.setText(XMLHelper.getText(child.childNodes))
            elif child.tagName == 'Notes':
                self.noteText = XMLHelper.getText(child.childNodes)
            elif child.tagName == 'SCItem':
                newItem = Item(realm=self.realm)
                newItem.loadFromXML(child,str(self.itemnumbering))
                self.itemnumbering += 1
                if self.itemattrlist[newItem.Location] == itemdefault[newItem.Location]:
                    self.itemattrlist[newItem.Location] = newItem
                elif newItem.Equipped == '1':
                    self.itemattrlist[newItem.Location].Equipped = '0'
                    item = newItem
                    while item.next is not None:
                        item = item.next
                    item.next = self.itemattrlist[newItem.Location]
                    self.itemattrlist[newItem.Location] = newItem
                else:
                    item = self.itemattrlist[newItem.Location] 
                    while item.next is not None:
                        item = item.next
                    item.next = newItem
            elif child.tagName == 'Coop':
                self.coop = eval(XMLHelper.getText(child.childNodes), 
                                 globals(), globals())
        self.Realm.setCurrentIndex(Realms.index(self.realm))
        self.RealmChanged(self.Realm.currentIndex())
        if AllBonusList[self.realm].has_key(self.charclass):
            self.CharClass.setCurrentIndex(ClassList[self.realm].index(self.charclass))
            self.CharClassChanged(self.CharClass.currentIndex())
        if racename in AllBonusList[self.realm][self.charclass]['Races']:
            self.CharRace.setCurrentIndex(AllBonusList[self.realm][self.charclass] \
                                                      ['Races'].index(racename))
            self.RaceChanged('')
        self.restoreItem(self.itemattrlist[self.currentTabLabel])
        self.modified = 0
        self.nocalc = 0
        self.calculate()
        
    def loadFromLela(self, scclines):
        self.initialize(1)
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
                self.Realm.setCurrentIndex(Realms.index(self.realm))
                self.RealmChanged(self.realm)
                if AllBonusList[self.realm].has_key(self.charclass):
                   self.CharClass.setCurrentIndex(ClassList[self.realm].index(self.charclass))
                   self.CharClassChanged(self.CharClass.currentIndex())
        for itemnum in range(0, 19):
            item = Item(realm=self.realm,loc=TabList[itemnum])
            item.loadLelaItemFromSCC(itemnum, scclines, self.realm)
            self.itemattrlist[item.Location] = item
        self.restoreItem(self.itemattrlist[self.currentTabLabel])
        self.modified = 0
        self.nocalc = 0
        self.calculate()
        
    def openOptions(self):
        self.nocalc = 1
        res = Options.Options(self).exec_()
        if res == 1:
             self.showcapmenuid.setChecked(self.capDistance)
             self.RealmChanged(self.Realm.currentIndex())
             self.restoreItem(self.itemattrlist[self.currentTabLabel])
             self.modified = 1
        self.nocalc = 0
        self.calculate()

    def openCraftWindow(self):
        CW = CraftWindow.CraftWindow(self, '', 1)
        CW.loadItem(self.itemattrlist[self.currentTabLabel])
        CW.ExpMultiplier.setValue(self.craftMultiplier)
        CW.exec_()
        self.craftMultiplier = int(CW.ExpMultiplier.value())
        self.restoreItem(self.itemattrlist[self.currentTabLabel])
        self.modified = 1
    
    def openMaterialsReport(self):
        RW = ReportWindow.ReportWindow(self, '', 1)
        RW.materialsReport(self.itemattrlist)
        RW.exec_()

    def openConfigReport(self):
        RW = ReportWindow.ReportWindow(self, '', 1)
        RW.parseConfigReport(self.reportFile, self.itemattrlist)
        RW.exec_()

    def chooseReportFile(self):
        filename = QFileDialog.getOpenFileName(self, "Choose Report Format", "reports", 
                                               "Reports (*.xml *.rpt);;All Files (*.*)")
        if filename is not None and str(filename) != '':
            self.reportFile = str(filename)

    def aboutBox(self):
        splash = AboutScreen(parent=self,modal=True)
        splash.exec_()

    def openCraftBars(self):
        CB = CraftBar.CraftBar(self, '', 1)
        CB.exec_()

    def DelveItemsDialog(self, find, findtype = None):
        locs = []
        finddesc = findtype
        if findtype is not None:
            if (find == 'AF' or find == '% Power Pool'):
                findtype = None
            else:
                findtype = findtype[-5:]
        for key, item in self.itemattrlist.iteritems():
            activestate = item.ActiveState
            for slot in range(0, item.slotCount()):
                slottype = str(item.slot(slot).type())
                if slottype == 'Unused': continue
                effect = item.slot(slot).effect()
                if findtype is not None:
                    if slottype[-5:] != findtype: continue
                elif effect != 'AF' and effect != '% Power Pool':
                    if slottype == 'Resist': continue
                    if slottype[-5:] == 'Bonus': continue
                if effect != find:
                    if find == 'Power' or find == '% Power Pool':
                       if effect != 'Power' and effect != '% Power Pool':
                           continue
                    elif effect == 'Acuity':
                       if not find in AllBonusList[self.realm][self.charclass][effect]:
                           continue
                    elif (slottype == 'Skill' or slottype == 'Focus') \
                            and effect[0:4] == 'All ' \
                            and effect in AllBonusList[self.realm][self.charclass].keys():
                        if not find in AllBonusList[self.realm][self.charclass][effect]:
                            continue
                    else:
                        continue
                amount = item.slot(slot).amount()
                if slottype == 'Focus':
                    amount += ' Levels Focus'
                if effect != find: 
                    amount += ' ' + effect
                if slottype == 'Cap Increase':
                    amount += ' Cap'
                locs.append([key, amount])
        DW = DisplayWindow.DisplayWindow(self)
        if findtype:
            DW.setWindowTitle('Slots With %s %s' % (find, finddesc))
        else:
            DW.setWindowTitle('Slots With %s' % find)
        DW.loadLocations(locs)
        DW.exec_()

    def gemClicked(self, item, slot):
        RW = ReportWindow.ReportWindow(self, '', True)
        RW.setWindowTitle('Materials')
        RW.materialsReport({item: self.itemattrlist[item]}, slot)
        RW.exec_()

    def mousePressEvent(self, e):
        if e is None: return
        child = self.childAt(e.pos())
        if child is None: return
        if not isinstance(child, QLabel): return
        if str(child.text()) == '': return
        shortname = str(child.objectName())
        nameidx = 1
        while nameidx < len(shortname):
            if shortname[nameidx] < 'a' or shortname[nameidx] > 'z':
                shorttype = shortname[nameidx:]
                shortname = shortname[0:nameidx]
            nameidx += 1
        if shortname in ['Gem', 'Points', 'Cost', 'Name']:
            slotid = child.objectName()[-2:]
            if str(slotid[0:1]) == '_':
                slotid = slotid[1:]
            item = self.itemattrlist[self.currentTabLabel]
            slot = int(slotid)
            if item.slot(slot).slotType() == 'player':
                self.gemClicked(self.currentTabLabel, slot)
            return
        if shortname in ['', 'Label', 'Total', 'Item']: return
        if child.parent().objectName() == 'GroupResists':
           self.DelveItemsDialog(shortname, 'Resist')
        else:
           self.DelveItemsDialog(shortname)

    def SkillClicked(self,index):
        effect = str(index.data(Qt.DisplayRole).toString())
        bonus = str(index.data(Qt.UserRole).toString())
        amount, effect = string.split(effect.lstrip(), ' ', 1)
        self.DelveItemsDialog(effect, bonus)

    def showCap(self):
        self.capDistance = not self.capDistance
        self.showcapmenuid.setChecked(self.capDistance)
        self.calculate()

    def swapWith(self, action):
        cur = self.itemattrlist[self.currentTabLabel]
        if cur.ActiveState != 'player': return
        piece = str(action.text())
        part = self.itemattrlist[piece]
        if cur == part: return
        while part.ActiveState != 'player':
            ## could offer a message here if we fail
            if part.next is None: return
            part = part.next
        for i in range(0,min(cur.slotCount(),part.slotCount())):
            if cur.slot(i).slotType() != 'player' \
                    or part.slot(i).slotType()  != 'player':
                continue
            itemslot = cur.itemslots[i]
            cur.itemslots[i] = part.itemslots[i]
            part.itemslots[i] = itemslot
        self.modified = 1
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def moveTo(self, action):
        cur = self.itemattrlist[self.currentTabLabel]
        if cur.ActiveState != 'player': return
        piece = str(action.text())
        part = self.itemattrlist[piece]
        if cur == part: return
        if cur.next is None:
            item = Item(realm=self.realm,loc=self.currentTabLabel,
                        state=cur.ActiveState)
            if cur.ActiveState == 'drop':
                item.ItemName = "Drop Item" + str(self.itemnumbering)
            else:
                item.ItemName = "Crafted Item" + str(self.itemnumbering)
            self.itemnumbering += 1
            self.itemattrlist[self.currentTabLabel] = item
        else:
            self.itemattrlist[self.currentTabLabel] = cur.next
        cur.next = part
        cur.Location = piece
        self.itemattrlist[piece] = cur
        self.currentTabLabel = piece
        if piece in JewelTabList:
            row = 1
            col = JewelTabList.index(piece)
        else:
            row = 0
            col = PieceTabList.index(piece)
        self.modified = 1
        self.PieceTab.setCurrentIndex(row, col)

    def chooseItemType(self, action):
        newtype = str(action.data().toString())
        item = self.itemattrlist[self.currentTabLabel]
        if newtype == 'Normal Item' or newtype == 'Enhanced Bow':
            item.slot(4).setSlotType('effect')
            if item.slot(5).type()[-6:] == "Effect":
                item.slot(4).setAll(item.slot(5).type(), item.slot(5).amount(), 
                             item.slot(5).effect(), item.slot(5).requirement())
            item.slot(5).setType('Unused')
            item.slot(5).setSlotType('unused')
        else:
            item.slot(5).setSlotType('effect')
            if item.slot(4).type()[-6:] == 'Effect':
                item.slot(5).setAll(item.slot(4).type(), item.slot(4).amount(), 
                             item.slot(4).effect(), item.slot(4).requirement())
            item.slot(4).setSlotType('crafted')

        if newtype == 'Caster Staff' or newtype == 'Legendary Staff':
            for fixslot in item.slots():
                 if fixslot.type() == 'Focus':
                     fixslot.setType('Unused')

        if newtype == 'Normal Item':
            item.slot(3).setSlotType('player')
        elif newtype == 'Caster Staff':
            item.slot(3).setSlotType('player')
            item.slot(4).setAll('Focus', '50', 'All Spell Lines')
        elif newtype == 'Legendary Staff':
            item.slot(3).setSlotType('crafted')
            item.slot(3).setAll('Focus', '50', 'All Spell Lines')
            item.slot(4).setAll('Other Bonus', '2', 'Magic Damage', 
                                requirement="vs All Monsters")
            item.slot(5).setAll('Charged Effect', '60', 'Dmg w/Resist Debuff', 
                                requirement="Level 50")
        elif newtype == 'Enhanced Bow':
            item.slot(3).setSlotType('player')
            item.slot(4).setAll('Offensive Effect', '20', 'Direct Damage')
        elif newtype == 'Legendary Bow':
            item.slot(3).setSlotType('crafted')
            item.slot(3).setAll('Other Bonus', '2', 'Archery Damage', 
                                requirement="vs All Monsters")
            item.slot(4).setAll('Other Bonus', '10', 'AF')
            item.slot(5).setAll('Offensive Effect', '25', 'Dmg w/Resist Debuff', 
                                requirement="Level 50")
        elif newtype == 'Legendary Weapon':
            item.slot(3).setSlotType('crafted')
            item.slot(3).setAll('Other Bonus', '2', 'Melee Damage', 
                                requirement="vs All Monsters")
            item.slot(4).setAll('Other Bonus', '10', 'AF')
            item.slot(5).setAll('Offensive Effect', '60', 'Dmg w/Resist Debuff', 
                                requirement="Level 50")
        elif newtype == 'Enhanced Armor':
            item.slot(3).setSlotType('player')

        # Recover from previously legendary items
        if item.slot(3).slotType() == 'player' and \
                not item.slot(3).crafted():
            item.slot(3).setType('Unused')
        self.restoreItem(item)

    def newItemType(self, action):
        newtype = str(action.data().toString())
        if newtype == 'Drop Item':
            item = Item(realm=self.realm,loc=self.currentTabLabel,state='drop')
            item.ItemName = "Drop Item" + str(self.itemnumbering)
        else:
            item = Item(realm=self.realm,loc=self.currentTabLabel,state='player')
            item.ItemName = "Crafted Item" + str(self.itemnumbering)
        self.itemnumbering += 1
        item.next = self.itemattrlist[self.currentTabLabel]
        self.itemattrlist[self.currentTabLabel] = item
        if newtype == 'Drop Item' or newtype == 'Normal Item':
            self.restoreItem(item)
        else:
            self.chooseItemType(action)

    def loadRecentFile(self, action):
        index = action.data().toInt()[0]
        self.openFile(self.recentFiles[index], True)

    def generateUIXML(self):
        UIXML.uixml(self)
   
    def ignoreMouseEvent(self, e):
        e.ignore()

    def resizeEvent(self, e):
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            self.sizegrip.move(self.width() - 15, self.height() - 15)

if __name__ == '__main__':
    app = QApplication([])
    scw = ScWindow()

