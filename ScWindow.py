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
import MultiTabBar
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
        self.itemeffectlists = DropLists['All'].copy()

        self.fixedtaborder = False

        QMainWindow.__init__(self,None,Qt.Window)
        self.setAttribute(Qt.WA_DeleteOnClose)
        Ui_B_SC.setupUi(self,self)

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
        self.initLayout()
        self.initMenu()
        self.initControls()
        self.updateGeometry()
        OW = Options.Options(self)
        OW.load()
        self.pricingInfo = OW.getPriceInfo()
        self.updateRecentFiles(None)
        self.initialize(0)

    def initLayout(self):
        testfont = QFontMetrics(qApp.font())

        self.switchOnType = {'drop' : [], 'player' : [] }
        self.switchOnType['drop'] = [ 
            self.QualEdit, self.ItemName, self.LabelRequirement,
        ]
        self.switchOnType['player'] = [
            self.LabelGemQuality, self.LabelGemPoints, self.LabelGemCost,
            self.ItemImbueLabel, self.ItemImbue, self.ItemImbueTotal,
            self.ItemOverchargeLabel, self.ItemOvercharge, 
            self.ItemCostLabel, self.ItemCost, self.QualDrop,
            self.ItemPriceLabel, self.ItemPrice,
        ]

        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            height = max(self.CharName.sizeHint().height(),
                         self.Realm.sizeHint().height())
        else:
            height = min(self.CharName.minimumSizeHint().height(),
                         self.Realm.minimumSizeHint().height())


        self.StatLabel = {}
        self.StatValue = {}
        self.StatCap = {}
        self.StatBonus = {}

        self.statlayout = QtGui.QGridLayout(self.GroupStats)
        self.statlayout.setMargin(3)
        self.statlayout.setSpacing(0)
        row = 0
        for stat in (GemLists['All']['Stat'] + ('Power', 'Hits',)):
            self.StatLabel[stat] = getattr(self, stat + 'Label')
            self.StatValue[stat] = getattr(self, stat)
            self.StatCap[stat] = getattr(self, stat + 'Cap')
            self.statlayout.addWidget(self.StatLabel[stat],row,0,1,1)
            self.statlayout.addWidget(self.StatValue[stat],row,1,1,1)
            self.statlayout.addWidget(self.StatCap[stat],row,2,1,1)
            row += 1
        width = testfont.size(Qt.TextSingleLine, "400").width()
        self.statlayout.setColumnMinimumWidth(1,width)
        width = testfont.size(Qt.TextSingleLine, " (400)").width()
        self.statlayout.setColumnMinimumWidth(2,width)

        self.resistlayout = QtGui.QGridLayout(self.GroupResists)
        self.resistlayout.setMargin(3)
        self.resistlayout.setSpacing(1)
        row = 0
        for stat in (GemLists['All']['Resist']):
            self.StatLabel[stat] = getattr(self, stat + 'Label')
            self.StatValue[stat] = getattr(self, stat)
            self.StatBonus[stat] = getattr(self, stat + 'RR')
            self.resistlayout.addWidget(self.StatLabel[stat],row,0,1,1)
            self.resistlayout.addWidget(self.StatValue[stat],row,1,1,1)
            self.resistlayout.addWidget(self.StatBonus[stat],row,2,1,1)
            row += 1
        width = testfont.size(Qt.TextSingleLine, "26").width()
        self.resistlayout.setColumnMinimumWidth(1,width)
        width = testfont.size(Qt.TextSingleLine, " (5)").width()
        self.resistlayout.setColumnMinimumWidth(2,width)

        self.skilllayout = QtGui.QGridLayout(self.GroupSkillsList)
        self.skilllayout.setMargin(3)
        self.skilllayout.setSpacing(0)
        self.skilllayout.addWidget(self.SkillsList,0,0)
        self.skilllayout.setColumnStretch(0, 1)

        self.otherlayout = QtGui.QGridLayout(self.GroupOtherBonusList)
        self.otherlayout.setMargin(3)
        self.otherlayout.setSpacing(0)
        self.otherlayout.addWidget(self.OtherBonusList,0,0)
        self.otherlayout.setColumnStretch(0, 1)

        self.charlayout = QtGui.QGridLayout(self.GroupCharInfo)
        self.charlayout.setMargin(3)
        self.charlayout.setSpacing(0)
        row = 0
        for stat in ('CharName', 'Realm', 'CharClass', 'CharRace', 
                     'CharLevel', ):
            self.charlayout.addWidget(getattr(self, 'Label' + stat),row,0,1,1)
            ctl = getattr(self, stat)
            ctl.setFixedSize(QSize(ctl.width(), height))
            self.charlayout.addWidget(ctl,row,1,1,2)
            row += 1
        for stat in ('TotalCost', 'TotalPrice', ):
            self.charlayout.addWidget(getattr(self, 'Label' + stat),row,0,1,1)
            self.charlayout.addWidget(getattr(self, stat),row,1,1,2)
            row += 1
        self.charlayout.addWidget(self.LabelTotalUtility,row,0,1,2)
        self.charlayout.addWidget(self.TotalUtility,row,2,1,1)

        self.statusBar().hide()
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            self.sizegrip = QSizeGrip(self)

        self.CharLevel.setValidator(QIntValidator(0, 99, self))
        self.ItemLevel.setValidator(QIntValidator(0, 99, self))
        self.QualEdit.setValidator(QIntValidator(0, 100, self))
        self.Bonus_Edit.setValidator(QIntValidator(0, 99, self))

        self.Realm.insertItems(0, list(Realms))
        self.QualDrop.insertItems(0, list(QualityValues))

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

        editAmountValidator = QIntValidator(-999, +999, self)

        layout = True
        hspacer = QSpacerItem(5,0,QSizePolicy.Fixed,QSizePolicy.Minimum)
        vspacer = QSpacerItem(0,4,QSizePolicy.Minimum,QSizePolicy.Fixed)

        self.itemgrouplayout = QtGui.QHBoxLayout(self.DropCraftButtonFrame)
        self.itemgrouplayout.setMargin(0)
        self.itemgrouplayout.setSpacing(0)
        self.itemgrouplayout.addWidget(self.PlayerMade)
        self.itemgrouplayout.addWidget(self.Drop)

        self.itemcontrollayout = QtGui.QHBoxLayout()
        self.itemcontrollayout.setMargin(0)
        self.itemcontrollayout.setSpacing(0)
        col = 0
        for obj in (self.ItemLevelLabel, self.ItemLevel, self.ItemLevelButton, 
                    self.ItemQualityLabel, self.QualDrop, self.QualEdit, 
                    self.ItemBonusLabel, self.Bonus_Edit, self.ItemAFDPSLabel, 
                    self.AFDPS_Edit, self.ItemSpeedLabel, self.Speed_Edit, 
                    self.Equipped):
            if str(obj.objectName())[-5:] != 'Label':
                obj.setFixedSize(QSize(obj.width(), height))
            self.itemcontrollayout.addWidget(obj)
            col += 1
            if col == 3 or (col > 6 and str(obj.objectName())[-5:] != 'Label'):
                self.itemcontrollayout.addStretch(1)
                col += 1
        self.itemcontrollayout.addWidget(self.DropCraftButtonFrame)

        self.itemlayout = QtGui.QGridLayout(self.GroupItemFrame)
        self.itemlayout.setMargin(3)
        self.itemlayout.setSpacing(0)
        row = 0
        self.itemlayout.addItem(QSpacerItem(1, self.PieceTab.baseOverlap(),
                                    QSizePolicy.Minimum, QSizePolicy.Fixed),
                                row,0,1,10)
        row += 1
        self.itemlayout.addLayout(self.itemcontrollayout,row,0,1,10)
        row += 1

        col = 1
        for obj in (self.LabelGemType, self.LabelGemAmount, self.LabelGemEffect,
                    self.LabelGemQuality, self.LabelGemPoints, self.LabelGemCost,):
            self.itemlayout.addWidget(obj,row,col,1,1)
            col += 1
        self.itemlayout.addItem(QSpacerItem(hspacer),row,7,1,1)
        self.itemlayout.addWidget(self.LabelRequirement,row,4,1,3)
        self.itemlayout.addWidget(self.LabelItemName,row,8,1,2)
        #self.itemlayout.setColumnStretch(3, 1)
        self.itemlayout.setColumnStretch(8, 1)

        width = testfont.size(Qt.TextSingleLine, " Slot 10:").width()
        self.itemlayout.setColumnMinimumWidth(0,width)
        width = testfont.size(Qt.TextSingleLine, " Points").width()
        self.itemlayout.setColumnMinimumWidth(5,width)
        width = testfont.size(Qt.TextSingleLine, " 999g 00s 00c").width()
        self.itemlayout.setColumnMinimumWidth(6,width)

        row += 1
        self.ItemName.setFixedSize(QSize(self.ItemName.width(), height))
        self.itemlayout.addWidget(self.ItemName,row,8,1,2)
        for i in range(0, 12):
            idx = i + 1
            self.GemLabel.append(getattr(self, 'Gem_Label_%d' % idx))
            self.Type.append(getattr(self, 'Type_%d' % idx))
            self.connect(self.Type[i],SIGNAL("activated(int)"),
                         self.TypeChanged)
            self.Effect.append(getattr(self, 'Effect_%d' % idx))
            self.Effect[i].setInsertPolicy(QComboBox.NoInsert)
            self.connect(self.Effect[i],SIGNAL("activated(int)"),
                         self.EffectChanged)
            self.connect(self.Effect[i],SIGNAL("editTextChanged(const QString&)"),
                         self.EffectChanged)
            self.AmountEdit.append(getattr(self, 'Amount_Edit_%d' % idx))
            self.switchOnType['drop'].append(self.AmountEdit[i])
            self.AmountEdit[i].setValidator(editAmountValidator)
            self.connect(self.AmountEdit[i],SIGNAL("textChanged(const QString&)"),
                         self.AmountsChanged)
            self.Requirement.append(getattr(self, 'Requirement_%d' % idx))
            self.connect(self.Requirement[i],SIGNAL("textChanged(const QString&)"),
                         self.AmountsChanged)
            self.itemlayout.addWidget(self.GemLabel[i],row,0,1,1)
            self.Type[i].setFixedSize(QSize(self.Type[i].getMinimumWidth(list(DropTypeList)), height))
            self.itemlayout.addWidget(self.Type[i],row,1,1,1)
            self.AmountEdit[i].setFixedSize(QSize(self.AmountEdit[i].width(), height))
            self.itemlayout.addWidget(self.AmountEdit[i],row,2,1,1)

            l = reduce(lambda x, y: x+y, [ list(x) for x in GemLists['All'].values() ])
            self.Effect[i].setFixedSize(QSize(self.Effect[i].getMinimumWidth(l), height))
            self.itemlayout.addWidget(self.Effect[i],row,3,1,1)
            self.Requirement[i].setFixedSize(QSize(self.Requirement[i].width(), height))
            self.itemlayout.addWidget(self.Requirement[i],row,4,1,3)
            self.switchOnType['drop'].append(self.AmountEdit[i])
            if i < 6:
                self.AmountDrop.append(getattr(self, 'Amount_Drop_%d' % idx))
                self.AmountDrop[i].setFixedSize(QSize(self.AmountDrop[i].getMinimumWidth(['100']), height))
                self.itemlayout.addWidget(self.AmountDrop[i],row,2,1,1)
                self.Name.append(getattr(self, 'Name_%d' % idx))
                self.itemlayout.addWidget(self.Name[i],row,8,1,2)
                self.connect(self.AmountDrop[i],SIGNAL("activated(int)"),
                             self.AmountsChanged)
                self.switchOnType['player'].extend([
                    self.AmountDrop[i], self.Name[i], ])
            else:
                self.switchOnType['drop'].extend([
                    self.GemLabel[i], self.Type[i], self.Effect[i], self.Requirement[i], ])
            if i < 4:
                self.Quality.append(getattr(self, 'Quality_%d' % idx))
                self.Quality[i].insertItems(0, list(QualityValues))
                self.connect(self.Quality[i],SIGNAL("activated(int)"),
                             self.AmountsChanged)
                self.Points.append(getattr(self, 'Points_%d' % idx))
                self.Cost.append(getattr(self, 'Cost_%d' % idx))
                self.Quality[i].setFixedSize(QSize(self.Quality[i].getMinimumWidth(), height))
                #self.Quality[i].setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)
                #self.Quality[i].setMinimumContentsLength(3)
                #self.Quality[i].setFixedSize(QSize(self.Quality[i].sizeHint().width(), height))
                self.itemlayout.addWidget(self.Quality[i],row,4,1,1)
                self.itemlayout.addWidget(self.Points[i],row,5,1,1)
                self.itemlayout.addWidget(self.Cost[i],row,6,1,1)
                self.switchOnType['player'].extend([
                    self.Quality[i], self.Points[i], self.Cost[i], ])
                self.switchOnType['drop'].append(self.Requirement[i])
            self.itemlayout.setRowMinimumHeight(row, height)
            row += 1

        self.itemlayout.addWidget(self.ItemImbueLabel,row-5,3,1,2)
        self.itemlayout.addWidget(self.ItemImbue,row-5,5,1,1)
        self.itemlayout.addWidget(self.ItemImbueTotal,row-5,6,1,1)
        self.itemlayout.addWidget(self.ItemOverchargeLabel,row-4,3,1,2)
        self.itemlayout.addWidget(self.ItemOvercharge,row-4,5,1,2)
        self.itemlayout.addWidget(self.ItemCostLabel,row-3,3,1,2)
        self.itemlayout.addWidget(self.ItemCost,row-3,5,1,2)
        self.itemlayout.addWidget(self.ItemPriceLabel,row-2,3,1,2)
        self.itemlayout.addWidget(self.ItemPrice,row-2,5,1,2)
        self.itemlayout.addWidget(self.ItemUtilityLabel,row-2,8,1,1)
        self.itemlayout.addWidget(self.ItemUtility,row-2,9,1,1)
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            self.itemlayout.addWidget(self.sizegrip,row-1,9,1,1)

        self.PieceTab.setFocusPolicy(Qt.StrongFocus)
        for tabname in PieceTabList:
            self.PieceTab.addTab(0, qApp.translate("B_SC",tabname,None))
        for tabname in JewelTabList:
            self.PieceTab.addTab(1, qApp.translate("B_SC",tabname,None))
        self.GroupItemFrame.stackUnder(self.PieceTab)

        self.tabslayout = QVBoxLayout()
        #self.GroupItemFrame.setContentsMargins(left, top, right, bottom)
        self.tabslayout.addWidget(self.PieceTab)
        self.tabslayout.addItem(QSpacerItem(1, -self.PieceTab.baseOverlap(),
                                            QSizePolicy.Minimum, QSizePolicy.Fixed))
        self.tabslayout.addWidget(self.GroupItemFrame)
 
        self.mainlayout = QGridLayout(self.ScWinFrame)
        self.mainlayout.setMargin(3)
        self.mainlayout.setSpacing(0)
        self.mainlayout.addWidget(self.GroupStats,0,0,1,1)
        self.mainlayout.addItem(QSpacerItem(hspacer),0,1,1,1)
        self.mainlayout.addWidget(self.GroupResists,0,2,1,1)
        self.mainlayout.addItem(QSpacerItem(hspacer),0,3,1,1)
        self.mainlayout.addWidget(self.GroupSkillsList,0,4,1,1)
        self.mainlayout.addItem(QSpacerItem(hspacer),0,5,1,1)
        self.mainlayout.addWidget(self.GroupOtherBonusList,0,6,1,1)
        self.mainlayout.addItem(QSpacerItem(hspacer),0,7,1,1)
        self.mainlayout.addWidget(self.GroupCharInfo,0,8,1,1)
        self.mainlayout.addItem(QSpacerItem(vspacer),1,0,1,9)
        self.mainlayout.addLayout(self.tabslayout,2,0,1,9)

        self.mainlayout.setRowStretch(0, 0)
        self.mainlayout.setRowStretch(2, 1)
        self.mainlayout.setColumnStretch(4, 1)
        self.mainlayout.setColumnStretch(6, 1)

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
        self.connect(self.ItemName,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.Bonus_Edit,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.AFDPS_Edit,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.Speed_Edit,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.Equipped,SIGNAL("stateChanged(int)"),self.ItemChanged)
        self.connect(self.PlayerMade,SIGNAL("toggled(bool)"),self.PlayerToggled)
        self.connect(self.Drop,SIGNAL("toggled(bool)"),self.DropToggled)
        self.connect(self.SkillsList,SIGNAL("itemActivated(QListWidgetItem*)"),
                     self.SkillClicked)
        self.connect(self.OtherBonusList,SIGNAL("itemActivated(QListWidgetItem*)"),
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
        self.filemenu.addAction('&Save Item...', self.saveItem,
                                QKeySequence(Qt.CTRL+Qt.SHIFT+Qt.Key_S))
        self.filemenu.addSeparator()
        self.filemenu.addAction('Export &Quickbars...', self.openCraftBars)
        self.filemenu.addAction('Export &UI XML (Beta)...', self.generateUIXML)
        self.filemenu.addSeparator()
        self.filemenu.addMenu(self.rf_menu)
        self.filemenu.addSeparator()
        self.filemenu.addAction('E&xit', self.close, QKeySequence(Qt.CTRL+Qt.Key_X))
        self.menuBar().addMenu(self.filemenu)

        self.swapGems = QMenu('S&wap Gems With', self)
        for piece in range(0,len(PieceTabList)):
            act = QAction(PieceTabList[piece], self)
            act.setData(QVariant(piece))
            self.swapGems.addAction(act)
        self.connect(self.swapGems, SIGNAL("triggered(QAction*)"), self.swapWith)

        self.editmenu = QMenu('&Edit', self)
        self.editmenu.addAction('&Clear Item', self.clearCurrentItem)
        self.editmenu.addMenu(self.swapGems)
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
            prev = self.ItemName
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
        self.setTabOrder(self.SkillsList,self.OtherBonusList)

    def showDropWidgets(self):
        if not self.isVisible(): return
        self.GroupItemFrame.hide()
        for w in self.switchOnType['player']:
            w.hide()
        for w in self.switchOnType['drop']:
            w.show()
        for i in range(0,4):
            self.GemLabel[i].setEnabled(1)
            self.GemLabel[i].setText('Slot %d:' % (i + 1))
        self.craftingmenuid.setEnabled(False)
        self.GroupItemFrame.show()

    def showPlayerWidgets(self):
        self.GroupItemFrame.hide()
        for w in self.switchOnType['player']:
            w.show()
        for w in self.switchOnType['drop']:
            w.hide()
        for i in range(0,4):
            self.GemLabel[i].setEnabled(1)
            self.GemLabel[i].setText('Gem %d:' % (i + 1))
        self.craftingmenuid.setEnabled(True)
        self.GroupItemFrame.show()

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
        self.craftMultiplier = 6
        self.filename = None
        self.newcount = self.newcount + 1
        filetitle = unicode("Template" + str(self.newcount))
        self.setWindowTitle(filetitle + " - Kort's Spellcrafting Calculator")

        self.PieceTab.setCurrentIndex(0, 0)
        self.currentTab = self.PieceTab
        self.currentTabLabel = string.strip(str(self.PieceTab.tabText(0, 0)))

        self.Equipped.setChecked(1)

        self.itemattrlist = { }
        for tab in TabList:
            self.itemattrlist[tab] = Item(realm=self.realm,loc=tab)
        self.ItemLevel.setText('51')
        self.CharLevel.setText('50')

        self.RealmChanged(self.realm)
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
        childnode = document.createElement('Class')
        childnode.appendChild(document.createTextNode(self.charclass))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Race')
        childnode.appendChild(document.createTextNode(unicode(self.CharRace.currentText())))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Level')
        childnode.appendChild(document.createTextNode(unicode(self.CharLevel.text())))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Realm')
        childnode.appendChild(document.createTextNode(self.realm))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Notes')
        childnode.appendChild(document.createTextNode(str(self.noteText)))
        rootnode.appendChild(childnode)

        for key, item in self.itemattrlist.iteritems():
            # use firstChild here because item.asXML() constructs a Document()
            childnode = item.asXML()
            if childnode is not None:
                rootnode.appendChild(childnode.firstChild)
        return document

    def PieceTabChanged(self, row, col):
        if self.nocalc:
            return
        self.currentTabLabel = string.strip(str(self.PieceTab.tabText(row, col)))
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

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
            self.PlayerMade.setChecked(1)
            self.showPlayerWidgets()
            typelist = list(TypeList)
        else:
            self.Drop.setChecked(1)
            self.showDropWidgets()
            typelist = list(DropTypeList)
        self.ItemLevel.setText(item.Level)
        location = item.Location
        self.Equipped.setChecked(int(item.Equipped))
        for slot in range(0, item.slotCount()):
            typecombo = self.Type[slot]
            typecombo.clear()
            if itemtype == 'player' and \
                    not item.slot(slot).slotType() == 'player':
                typelist = list(EffectTypeList)
            gemtype = str(item.slot(slot).type())
            if not gemtype in typelist:
                typelist.append(gemtype)
            typecombo.insertItems(0, list(typelist))
            typecombo.setCurrentIndex(typelist.index(gemtype))
            self.TypeChanged(typelist.index(gemtype), slot)
            gemeffect = str(item.slot(slot).effect())
            effect = self.Effect[slot].findText(gemeffect)
            if len(gemeffect) and effect < 0:
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
                if ValuesLists.has_key(gemtype):
                    if isinstance(ValuesLists[gemtype], tuple):
                        amountlist = ValuesLists[gemtype]
                    else:
                        if ValuesLists[gemtype].has_key(gemeffect):
                            amountlist = ValuesLists[gemtype][gemeffect]
                if gemamount in amountlist:
                    self.AmountDrop[slot].setCurrentIndex(amountlist.index(gemamount))
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
            self.ItemName.setText(item.ItemName)
        else:
            if item.ItemQuality in QualityValues:
                self.QualDrop.setCurrentIndex(
                    QualityValues.index(item.ItemQuality))
        self.nocalc = wasnocalc
        if self.nocalc: return
        self.calculate()

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
                if self.PlayerMade.isChecked():
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
        self.SkillsList.clear()
        for skill, amount in skillTotals.iteritems():
            if not self.capDistance:
                self.SkillsList.addItem('%d %s' % (amount, skill))
            else:
                if skill[-6:] == " Focus":
                    capcalc = HighCapBonusList['Focus']
                else:
                    capcalc = HighCapBonusList['Skill']
                thiscap = int(charlevel * capcalc[0]) + capcalc[1]
                self.SkillsList.addItem('%d %s' % (thiscap - amount, skill))
        self.OtherBonusList.clear()
        for bonus, amount in otherTotals.iteritems():
            if not self.capDistance:
                self.OtherBonusList.addItem('%d %s' % (amount, bonus))
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
                self.OtherBonusList.addItem('%d %s' % (cap + capmod - amount, bonus))        
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
        maximbue = max(mvals)
        if display:
            for j in range(0, 4):
                if j != mvals.index(maximbue):
                    self.Points[j].setText('%3.1f' % (mvals[j] / 2.0))
                else:
                    self.Points[j].setText('%3.1f' % mvals[j])
        mvals.remove(maximbue)
        totalimbue = ((maximbue * 2 + sum(mvals)) / 2.0)
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
        if self.PlayerMade.isChecked():
            state = 'player'
            item.ItemQuality = unicode(self.QualDrop.currentText())
        else:
            state = 'drop'
            item.ItemName = unicode(self.ItemName.text())
            item.ItemQuality = unicode(self.QualEdit.text())
        self.calculate()

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
        if self.PlayerMade.isChecked():
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
        if self.PlayerMade.isChecked():
            amount = self.AmountDrop[slot]
        else:
            amount = self.AmountEdit[slot]
        if typetext == 'Unused':
            amount.clear()
            if item.slot(slot).slotType() == 'player' and self.PlayerMade.isChecked():
                self.Quality[slot].setCurrentIndex(0)
        elif self.PlayerMade.isChecked():
            amtindex = amount.currentIndex()
            amount.clear()
            if ValuesLists.has_key(typetext):
                valueslist = ValuesLists[typetext]
                if isinstance(valueslist, dict):
                    if valueslist.has_key(efftext):
                        valueslist = valueslist[efftext]
                    else:
                        valueslist = tuple()
                elif efftext[0:5] == "All M":
                    valueslist = ("1",)
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
        if not self.PlayerMade.isChecked():
            effectlist = self.dropeffectlists
        elif item.slot(slot).slotType() == 'player':
            effectlist = self.effectlists
        else:
            # XXX Grow this for crafted enhanced armor/weap/lw's
            effectlist = self.itemeffectlists
        if effectlist.has_key(typetext):
            effectlist = effectlist[typetext]
        else:
            effectlist = list()
        if len(effectlist) > 0:
            effcombo.insertItems(0, list(effectlist))
        # Here we go... cascade
        effcombo.setCurrentIndex(0)
        self.EffectChanged(0, slot)
    
    def DropToggled(self,a0):
        if self.nocalc or not a0: return
        item = self.itemattrlist[self.currentTabLabel]
        item.ActiveState = 'drop'
        self.modified = 1
        self.restoreItem(item)

    def PlayerToggled(self, a0):
        if self.nocalc or not a0: return
        item = self.itemattrlist[self.currentTabLabel]
        item.ActiveState = 'player'
        self.modified = 1
        self.restoreItem(item)

    def clearCurrentItem(self):
        self.itemattrlist[self.currentTabLabel] = Item(realm=self.realm,loc=self.currentTabLabel)
        if self.nocalc: return
        self.modified = 1
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def saveItem(self):
        itemname = unicode(self.ItemName.text())
        if itemname == '':
            QMessageBox.critical(None, 'Error!', 
                'Cannot save item - You must specifify a name!', 'OK')
            return
        item = self.itemattrlist[self.currentTabLabel]
        ext = FileExt[self.currentTabLabel]
        if not isinstance(ext, types.StringType):
            ext = ext[0]
        itemdir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 
                               'items', self.realm, ext)
        if not os.path.exists(itemdir):
            os.makedirs(itemdir)
        filename = os.path.join(itemdir, string.replace(itemname, ' ', '_') + '_' \
            + ext \
            + '.xml')
        item.save(filename)
        QMessageBox.information(None, 'Success!',
                '%s successfully saved!' % itemname, 'OK')
        
    def loadItem(self):
        ext = FileExt[self.currentTabLabel]
        extstr = ''
        if not isinstance(ext, types.StringType):
            for e in ext:
                extstr += '*%s.xml *.%s ' % (e, e)
            ext = ext[0]
        else:
            extstr = '*%s.xml *.%s' % (ext, ext)
        extstr = "Items (%s)" % extstr
        itemdir = os.path.join(self.ItemPath, self.realm, ext)
        Qfd = ItemList.ItemListDialog(self, "Load Item", itemdir, extstr, 
                                      self.realm, self.charclass)
        if Qfd.exec_():
            if Qfd.selectedFiles().count() > 0:
                filename = unicode(Qfd.selectedFiles()[0])
                item = Item(self.currentTabLabel)
                item.Realm = self.realm
                if item.load(filename) == -1 : return
                if string.lower(item.Realm) != string.lower(self.realm)\
                    and string.lower(item.Realm) != 'all'\
                    and not self.coop:
                    QMessageBox.critical(None, 'Error!', 'You are trying to load an '
                                                       + 'item for another realm!', 'OK')
                    return
                item.Location = self.currentTabLabel
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
                                               "Templates (*.xml)")
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
                                                   "Templates (*.xml *.scc)")
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
        self.clearCurrentItem()
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
                self.itemattrlist[newItem.Location] = newItem
            elif child.tagName == 'Coop':
                self.coop = eval(XMLHelper.getText(child.childNodes), 
                                 globals(), globals())
        self.Realm.setCurrentIndex(Realms.index(self.realm))
        self.RealmChanged(self.realm)
        if AllBonusList[self.realm].has_key(self.charclass):
            self.CharClass.setCurrentIndex(ClassList[self.realm].index(self.charclass))
            self.CharClassChanged('')
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
        self.clearCurrentItem()
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
                   self.CharClassChanged('')
        for itemnum in range(0, 19):
            item = Item(TabList[itemnum])
            #item.Location = TabList[itemnum]
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
             self.CharClassChanged('')
             self.modified = 1
        self.nocalc = 0
        self.calculate()

    def openCraftWindow(self):
        CW = CraftWindow.CraftWindow(self, '', 1)
        CW.loadItem(self.itemattrlist.get(self.currentTabLabel))
        CW.ExpMultiplier.setValue(self.craftMultiplier)
        CW.exec_()
        self.craftMultiplier = int(CW.ExpMultiplier.value())
        self.calculate()
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
                                               "Reports (*.xml *.rpt)")
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
        for key, item in self.itemattrlist.iteritems():
            activestate = item.ActiveState
            for slot in range(0, item.slotCount()):
                itemtype = str(item.slot(slot).type())
                if itemtype == 'Unused': continue
                if (findtype and itemtype != findtype) or \
                   (not findtype and itemtype in ('Resist',)): continue
                effect = item.slot(slot).effect()
                if effect != find: 
                    if find == 'Power' or find == '% Power Pool':
                       if effect != 'Power' and effect != '% Power Pool':
                           continue
                    elif effect == 'Acuity':
                       if not find in AllBonusList[self.realm][self.charclass][effect]:
                           continue
                    elif (type == 'Skill' or itemtype == 'Focus') and effect[0:4] == 'All ' \
                            and effect in AllBonusList[self.realm][self.charclass].keys():
                        if not find in AllBonusList[self.realm][self.charclass][effect]:
                            continue
                    else:
                        continue
                amount = item.slot(slot).amount()
                if type == 'Focus':
                    amount += ' Levels Focus'
                if effect != find: 
                    amount += ' ' + effect
                if itemtype == 'Cap Increase':
                    amount += ' Cap'
                locs.append([key, amount])
        DW = DisplayWindow.DisplayWindow(self)
        if findtype:
            DW.setWindowTitle('Slots With %s %s' % (find, findtype))
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
            if self.PlayerMade.isChecked():
                self.gemClicked(self.currentTabLabel, int(slotid))
            return
        if shortname in ['', 'Label', 'Total', 'Item']: return
        if child.parent().objectName() == 'GroupResists':
           self.DelveItemsDialog(shortname, 'Resist')
        else:
           self.DelveItemsDialog(shortname)

    def SkillClicked(self,a0):
        if a0 is None: return
        if not ' ' in str(a0.text()): return
        amount, effect = string.split(str(a0.text()), ' ', 1)
        self.DelveItemsDialog(effect)

    def showCap(self):
        self.capDistance = not self.capDistance
        self.showcapmenuid.setChecked(self.capDistance)
        self.calculate()

    def swapWith(self, action):
        piece = action.data().toInt()[0]
        part = TabList[piece]
        cur = self.itemattrlist.get(self.currentTabLabel, Item(self.currentTabLabel))
        swap = self.itemattrlist.get(part, Item(part))
        self.itemattrlist[part] = cur
        self.itemattrlist[self.currentTabLabel] = swap
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def loadRecentFile(self, action):
        index = action.data().toInt()[0]
        self.openFile(self.recentFiles[index], True)

    def generateUIXML(self):
        UIXML.uixml(self)
   
    def ignoreMouseEvent(self, e):
        e.ignore()

if __name__ == '__main__':
    app = QApplication([])
    scw = ScWindow()

