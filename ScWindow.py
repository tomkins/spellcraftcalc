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
        self.nocalc = 1
        self.save = 0
        self.totals = { }
        self.capTotals = { }
        self.recentFiles = []
        self.effectlists = GemLists['All'].copy()
        self.dropeffectlists = DropLists['All'].copy()

        self.reportFile = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                                       'reports', 'Default_Config_Report.xml')
        self.coop = False

        self.fixedtaborder = False

        QMainWindow.__init__(self,None,Qt.Window)
        # |Qt.WindowSystemMenuHint|Qt.WindowTitleHint|Qt.WindowMinimizeButtonHint
        self.setAttribute(Qt.WA_DeleteOnClose)
        Ui_B_SC.setupUi(self,self)

        self.switchOnType = {'drop' : [], 'player' : [] }
        self.switchOnType['drop'] = [ 
            self.QualEdit, self.SaveItem, self.ItemName,
        ]
        self.switchOnType['player'] = [
            self.QualDrop, self.CraftButton, 
            self.LabelGemQuality, self.LabelGemPoints, self.LabelGemCost,
            self.ItemImbueLabel, self.ItemImbue, self.ItemImbueTotal,
            self.ItemOverchargeLabel, self.ItemOvercharge,
            self.ItemCostLabel, self.ItemCost,
            ## self.ItemPriceLabel, self.ItemPrice, XXX not calculated yet
        ]

        testfont = QFontMetrics(qApp.font())

        self.EffectWidths = [self.Effect_1.width(), self.Effect_10.width()]

        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            height = max(self.CharName.sizeHint().height(),
                         self.Realm.sizeHint().height())
        else:
            height = min(self.CharName.minimumSizeHint().height(),
                         self.Realm.minimumSizeHint().height())

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        for ctl in (self.GroupItemFrame.children() + [self.CharLevel]):
            if ((ctl.metaObject().className() == "QLineEdit" or 
                 ctl.metaObject().className() == "QComboBox") and 
                ctl.objectName() != "ItemName"):
                size = ctl.size()
                size.setHeight(height)
                ctl.setSizePolicy(QSizePolicy(sizePolicy))
                ctl.setMaximumSize(size)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        for ctl in (self.GroupCharInfo.children() + [self.ItemName]):
            if ((ctl.metaObject().className() == "QLineEdit" or 
                 ctl.metaObject().className() == "QComboBox") and 
                ctl.objectName() != "CharLevel"):
                size.setHeight(height)
                ctl.setSizePolicy(QSizePolicy(sizePolicy))
                ctl.setMaximumHeight(height)

        self.statlayout = QtGui.QGridLayout(self.GroupStats)
        self.statlayout.setMargin(3)
        self.statlayout.setSpacing(0)
        row = 0
        for stat in (GemLists['All']['Stat'] + ('Power', 'Hits',)):
            self.statlayout.addWidget(getattr(self, stat + 'Label'),row,0,1,1)
            self.statlayout.addWidget(getattr(self, stat + ''),row,1,1,1)
            self.statlayout.addWidget(getattr(self, stat + 'Cap'),row,2,1,1)
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
            self.resistlayout.addWidget(getattr(self, stat + 'Label'),row,0,1,1)
            self.resistlayout.addWidget(getattr(self, stat + ''),row,1,1,1)
            self.resistlayout.addWidget(getattr(self, stat + 'RR'),row,2,1,1)
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
        for stat in ('CharName', 'Realm', 'CharClass', 'CharRace', ):
            self.charlayout.addWidget(getattr(self, 'Label' + stat),row,0,1,1)
            self.charlayout.addWidget(getattr(self, stat),row,1,1,2)
            row += 1
        self.charlayout.addWidget(self.LabelCharLevel,row,0,1,1)
        self.charlayout.addWidget(self.CharLevel,row,1,1,1)
        row += 1
        for stat in ('TotalCost', 'TotalPrice',):
            self.charlayout.addWidget(getattr(self, stat + 'Label'),row,0,1,1)
            self.charlayout.addWidget(getattr(self, stat),row,1,1,2)
            row += 1
        self.charlayout.addWidget(self.ItemTotalUtilityLabel,row,0,1,2)
        self.charlayout.addWidget(self.ItemTotalUtility,row,2,1,1)

        self.setWindowTitle("Kort's Spellcrafting Calulator")
        self.fixtabs = True

        self.statusBar().hide()
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            self.sizegrip = QSizeGrip(self)

        self.CharLevel.setValidator(QIntValidator(0, 99, self))
        self.ItemLevel.setValidator(QIntValidator(0, 99, self))
        self.QualEdit.setValidator(QIntValidator(0, 100, self))
        self.Bonus_Edit.setValidator(QIntValidator(0, 99, self))

        # This doesn't matter for tinctures, keep hidden
        self.Quality_5.hide()
        self.Points_5.hide()
        self.Cost_5.hide()
        self.Quality_6.hide()
        self.Points_6.hide()
        self.Cost_6.hide()

        ## XXX not calculated yet - we must hide :)
        self.ItemPriceLabel.hide()
        self.ItemPrice.hide()

        self.PieceTab.setFocusPolicy(Qt.StrongFocus)
        for tabname in PieceTabList:
            self.PieceTab.addTab(0, qApp.translate("B_SC",tabname,None))
        for tabname in JewelTabList:
            self.PieceTab.addTab(1, qApp.translate("B_SC",tabname,None))

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
        self.Name = []

        editAmountValidator = QIntValidator(-999, +999, self)

        layout = True
        hspacer = QSpacerItem(5,0,QSizePolicy.Fixed,QSizePolicy.Minimum)
        vspacer = QSpacerItem(0,3,QSizePolicy.Minimum,QSizePolicy.Fixed)

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
            self.itemcontrollayout.addWidget(obj)
            col += 1
            if col == 3 or (col > 6 and str(obj.objectName())[-5:] != 'Label'):
                self.itemcontrollayout.addStretch(1)
                col += 1
        self.itemcontrollayout.addWidget(self.DropCraftButtonFrame)

        self.itemlayout = QtGui.QGridLayout(self.GroupItemFrame)
        self.itemlayout.setMargin(2)
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
        self.itemlayout.addWidget(self.LabelItemName,row,8,1,2)
        #self.itemlayout.setColumnStretch(3, 1)
        self.itemlayout.setColumnStretch(8, 1)

        width = max(testfont.size(Qt.TextSingleLine, " Gem 10:").width(),
                    testfont.size(Qt.TextSingleLine, " Slot 10:").width())
        self.itemlayout.setColumnMinimumWidth(0,width)
        width = testfont.size(Qt.TextSingleLine, " Points").width()
        self.itemlayout.setColumnMinimumWidth(5,width)
        width = testfont.size(Qt.TextSingleLine, "  999g 00s 00c").width()
        self.itemlayout.setColumnMinimumWidth(6,width)

        row += 1
        self.itemlayout.addWidget(self.ItemName,row,8,1,2)
        for i in range(0, 10):
            idx = i + 1
            self.GemLabel.append(getattr(self, 'Gem_Label_%d' % idx))
            self.Type.append(getattr(self, 'Type_%d' % idx))
            self.connect(self.Type[i],SIGNAL("activated(const QString&)"),
                         self.TypeChanged)
            self.Effect.append(getattr(self, 'Effect_%d' % idx))
# XXX       self.Effect[i].setInsertionPolicy(QComboBox.BeforeCurrent)
            self.connect(self.Effect[i],SIGNAL("activated(const QString&)"),
                         self.EffectChanged)
            self.AmountEdit.append(getattr(self, 'Amount_Edit_%d' % idx))
            self.switchOnType['drop'].append(self.AmountEdit[i])
            self.AmountEdit[i].setValidator(editAmountValidator)
            self.connect(self.AmountEdit[i],SIGNAL("textChanged(const QString&)"),
                         self.AmountChanged)
            self.itemlayout.addWidget(self.GemLabel[i],row,0,1,1)
            self.itemlayout.addWidget(self.Type[i],row,1,1,1)
            self.itemlayout.addWidget(self.AmountEdit[i],row,2,1,1)
            self.itemlayout.addWidget(self.Effect[i],row,3,1,1)
            if i < 6:
                self.AmountDrop.append(getattr(self, 'Amount_Drop_%d' % idx))
                self.connect(self.AmountDrop[i],SIGNAL("activated(const QString&)"),
                             self.AmountChanged)
                self.Quality.append(getattr(self, 'Quality_%d' % idx))
                self.Quality[i].insertItems(0, list(QualityValues))
                self.connect(self.Quality[i],SIGNAL("activated(const QString&)"),
                             self.QualityChanged)
                self.Points.append(getattr(self, 'Points_%d' % idx))
                self.Cost.append(getattr(self, 'Cost_%d' % idx))
                self.Name.append(getattr(self, 'Name_%d' % idx))
                self.itemlayout.addWidget(self.AmountDrop[i],row,2,1,1)
                self.itemlayout.addWidget(self.Quality[i],row,4,1,1)
                self.itemlayout.addWidget(self.Points[i],row,5,1,1)
                self.itemlayout.addWidget(self.Cost[i],row,6,1,1)
                self.itemlayout.addWidget(self.Name[i],row,8,1,2)
                self.switchOnType['player'].extend([
                    self.AmountDrop[i], self.Name[i]])
                if i < 4:
                    self.switchOnType['player'].extend([
                        self.Quality[i], self.Points[i], self.Cost[i]])
            else:
                self.switchOnType['drop'].extend([
                    self.GemLabel[i], self.Type[i], self.Effect[i]])

            self.itemlayout.setRowMinimumHeight(row, height)
            row += 1

        self.itembuttonlayout = QtGui.QGridLayout()
        self.itembuttonlayout.setMargin(0)
        self.itembuttonlayout.setSpacing(3)
        self.itembuttonlayout.addWidget(self.ItemUtilityLabel,0,0,1,1)
        self.itembuttonlayout.addWidget(self.ItemUtility,0,1,1,1)
        self.itembuttonlayout.addWidget(self.LoadItem,1,0,1,2)
        self.itembuttonlayout.addWidget(self.CraftButton,2,0,1,2)
        self.itembuttonlayout.addWidget(self.SaveItem,2,0,1,2)
        self.itembuttonlayout.addWidget(self.ClearItem,3,0,1,2)
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            self.itembuttonlayout.addWidget(self.sizegrip,4,2,1,1)
        self.itemlayout.addLayout(self.itembuttonlayout,row-5,9,5,1)

        self.itemlayout.addWidget(self.ItemImbueLabel,row-4,3,1,2)
        self.itemlayout.addWidget(self.ItemImbue,row-4,5,1,1)
        self.itemlayout.addWidget(self.ItemImbueTotal,row-4,6,1,1)
        self.itemlayout.addWidget(self.ItemOverchargeLabel,row-3,3,1,2)
        self.itemlayout.addWidget(self.ItemOvercharge,row-3,5,1,2)
        self.itemlayout.addWidget(self.ItemCostLabel,row-2,3,1,2)
        self.itemlayout.addWidget(self.ItemCost,row-2,6,1,1)
        self.itemlayout.addWidget(self.ItemPriceLabel,row-1,3,1,2)
        self.itemlayout.addWidget(self.ItemPrice,row-1,6,1,1)

        self.tabslayout = QVBoxLayout()
        self.GroupItemFrame.stackUnder(self.PieceTab)
        #(left, top, right, bottom) = self.GroupItemFrame.getContentsMargins()
        #top -= self.PieceTab.baseOverlap()
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

        self.mainlayout.setColumnStretch(4, 1)
        self.mainlayout.setColumnStretch(6, 1)

        self.updateGeometry()

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
        self.connect(self.Realm,SIGNAL("activated(const QString&)"),
                     self.RealmChanged)
        self.connect(self.CharClass,SIGNAL("activated(const QString&)"),
                     self.CharClassChanged)
        self.connect(self.CharRace,SIGNAL("activated(const QString&)"),
                     self.RaceChanged)
        self.connect(self.CharLevel,SIGNAL("textChanged(const QString&)"),
                     self.TemplateChanged)

        self.connect(self.PieceTab,SIGNAL("currentChanged"),self.PieceTabChanged)
        self.connect(self.ItemLevel,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.ItemLevelButton,SIGNAL("clicked()"),self.ItemLevelShow)
        self.connect(self.QualDrop,SIGNAL("activated(const QString&)"),
                     self.ItemChanged)
        self.connect(self.ItemName,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.Bonus_Edit,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.AFDPS_Edit,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.Speed_Edit,SIGNAL("textChanged(const QString&)"),
                     self.ItemChanged)
        self.connect(self.PlayerMade,SIGNAL("toggled(bool)"),self.PlayerToggled)
        self.connect(self.Drop,SIGNAL("toggled(bool)"),self.DropToggled)
        self.connect(self.Equipped,SIGNAL("clicked()"),self.EquippedClicked)
        self.connect(self.LoadItem,SIGNAL("clicked()"),self.Load_Item)
        self.connect(self.SaveItem,SIGNAL("clicked()"),self.Save_Item)
        self.connect(self.CraftButton,SIGNAL("clicked()"),self.OpenCraftWindow)
        self.connect(self.ClearItem,SIGNAL("clicked()"),self.ClearCurrentItem)
        self.connect(self.SkillsList,SIGNAL("itemActivated(QListWidgetItem*)"),
                     self.SkillClicked)
        self.connect(self.OtherBonusList,SIGNAL("itemActivated(QListWidgetItem*)"),
                     self.SkillClicked)

        self.startup = 1
        self.pricingInfo = {}

        self.ItemLevelWindow = ItemLevel.ItemLevel(self.window(), '', 1)
        self.DaocPath = ''
        self.realm = 'Albion'
        self.charclass = 'Armsman'
        self.crafterSkill = 1000
        self.showDoneInMatsList = 0
        self.noteText = ''
        self.capDistance = False
        self.includeRacials = False
        self.hideNonClassSkills = False
        OW = Options.Options(self)
        OW.load()

        self.rf_menu = QMenu('&Recent Files')
        self.connect(self.rf_menu, SIGNAL("triggered(QAction*)"), self.loadRecentFile)
        
        self.filemenu = QMenu('&File', self)
        self.filemenu.addAction('&New', self.newFile, QKeySequence(Qt.CTRL+Qt.Key_N))
        self.filemenu.addAction('&Open...', self.openFile, QKeySequence(Qt.CTRL+Qt.Key_O))
        self.filemenu.addAction('&Save', self.saveFile, QKeySequence(Qt.CTRL+Qt.Key_S))
        self.filemenu.addAction('Save &As...', self.saveAsFile)
        self.filemenu.addSeparator()
        self.filemenu.addAction('Export &Quickbars...', self.openCraftBars)
        self.filemenu.addAction('Export &UI XML (Beta)...', self.generateUIXML)
        self.filemenu.addSeparator()
        self.filemenu.addMenu(self.rf_menu)
        self.filemenu.addSeparator()
        self.filemenu.addAction('E&xit', self.close, QKeySequence(Qt.CTRL+Qt.Key_X))
        self.menuBar().addMenu(self.filemenu)

        self.updateRecentFiles(None)

        self.swapGems = QMenu('S&wap Gems With...', self)
        for piece in range(0,len(PieceTabList)):
            act = QAction(PieceTabList[piece], self)
            act.setData(QVariant(piece))
            self.swapGems.addAction(act)
        self.connect(self.swapGems, SIGNAL("triggered(QAction*)"), self.swapWith)

        self.editmenu = QMenu('&Edit', self)
        self.editmenu.addMenu(self.swapGems)
        self.editmenu.addSeparator()
        self.editmenu.addAction('&Options...', self.openOptions)
        self.menuBar().addMenu(self.editmenu)

        self.viewmenu = QMenu('&View', self)
        self.showcapmenuid = self.viewmenu.addAction('Distance to &Cap', self.showCap)
        self.showcapmenuid.setCheckable(True)
        self.showcapmenuid.setChecked(self.capDistance)
        self.viewmenu.addSeparator()
        self.viewmenu.addAction('Conf. Report', self.openConfigReport,
                                QKeySequence(Qt.CTRL+Qt.Key_C))
        self.viewmenu.addAction('Choose Format...', self.chooseReportFile)
        self.viewmenu.addSeparator()
        self.viewmenu.addAction('&Materials', self.openMaterialsReport,
                                QKeySequence(Qt.CTRL+Qt.Key_M))
        self.menuBar().addMenu(self.viewmenu)

        self.errorsmenu = QMenu('Errors', self)
        self.errorsmenu.addSeparator()
        self.errorsmenuid = self.menuBar().addMenu(self.errorsmenu)
        self.errorsmenuid.setEnabled(False)

        self.helpmenu = QMenu('&Help', self)
        self.helpmenu.addAction('&About', self.aboutBox)
        self.menuBar().addMenu(self.helpmenu)

        self.pricingInfo = OW.getPriceInfo()
        self.initialize()

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

    def showWideEffects(self, wide):
        width = self.EffectWidths[wide]
        for num in range(0, 5):
            self.Effect[num].setMaximumWidth(width)
        self.itemlayout.setColumnMinimumWidth(3,width)
        
    def showDropWidgets(self):
        self.GroupItemFrame.hide()
        for w in self.switchOnType['player']:
            w.hide()
        for w in self.switchOnType['drop']:
            w.show()
        self.showWideEffects(1)
        for i in range(0,5):
            self.GemLabel[i].setEnabled(1)
            self.GemLabel[i].setText('Slot %d:' % (i + 1))
        self.GroupItemFrame.show()

    def showPlayerWidgets(self):
        self.GroupItemFrame.hide()
        for w in self.switchOnType['player']:
            w.show()
        for w in self.switchOnType['drop']:
            w.hide()
        self.showWideEffects(0)
        for i in range(0,5):
            self.GemLabel[i].setEnabled(1)
            self.GemLabel[i].setText('Gem %d:' % (i + 1))
        self.GemLabel[4].setText('Proc:')
        self.GroupItemFrame.show()

    def closeEvent(self, e):
        OW = Options.Options(self)
        OW.save()
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?',
                                      'Some changes may not have been saved. '
                                    + 'Are you sure you want to quit?', 'Yes', 'No')
            if ret == 0:
                e.accept()
            else:
                e.ignore()
        else: 
            e.accept()


    def initialize(self):

# Options passed over from the options box
        self.noteText = ''
        self.craftMultiplier = 6
        self.save = 0
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
        self.save = 1
        self.nocalc = 0
        self.calculate()

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

        for key, item in self.itemattrlist.iteritems():
            # use firstChild here because item.asXML() constructs a Document()
            rootnode.appendChild(item.asXML().firstChild)
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
            item.loadAttr('ItemQuality', unicode(self.QualDrop.currentText()))
        else:
            state = 'drop'
            item.loadAttr('ItemName', unicode(self.ItemName.text())) 
            item.loadAttr('ItemQuality', unicode(self.QualEdit.text()))
        item.loadAttr('AFDPS', unicode(self.AFDPS_Edit.text()))
        item.loadAttr('Speed', unicode(self.Speed_Edit.text())) 
        item.loadAttr('Bonus', unicode(self.Bonus_Edit.text()))
        item.loadAttr('ActiveState', state)
        for slot in range(0, item.slotCount()):
            item.slot(slot).setType(self.Type[slot].currentText())
            item.slot(slot).setEffect(self.Effect[slot].currentText())
            if state == 'drop':
                item.slot(slot).setAmount(self.AmountEdit[slot].text())
            else:
                item.slot(slot).setAmount(self.AmountDrop[slot].currentText())
                item.slot(slot).setQua(self.Quality[slot].currentText())
        self.itemattrlist[self.currentTabLabel] = item

    def restoreItem(self, item):
        if item is None: return
        wascalc = self.nocalc
        self.nocalc = 1
        wassave = self.save
        self.save = 0
        itemtype = item.getAttr('ActiveState')
        if itemtype == 'player':
            self.PlayerMade.setChecked(1)
            self.showPlayerWidgets()
            typelist = list(TypeList)
        else:
            self.Drop.setChecked(1)
            self.showDropWidgets()
            typelist = list(DropTypeList)
        self.ItemLevel.setText(item.getAttr('Level'))
        location = item.getAttr('Location')
        self.Equipped.setChecked(int(item.getAttr('Equipped')))
        for slot in range(0, item.slotCount()):
            typecombo = self.Type[slot]
            typecombo.clear()
            if slot == 4 and itemtype == 'player':
                typelist = list(EffectTypeList)
            gemtype = str(item.slot(slot).type())
            if not gemtype in typelist:
                typelist.append(gemtype)
            typecombo.insertItems(0, list(typelist))
            typecombo.setCurrentIndex(typelist.index(gemtype))
            self.UpdateCombo(0, slot)
            if gemtype == 'Unused':
                continue
            gemeffect = str(item.slot(slot).effect())
            effect = self.Effect[slot].findText(gemeffect)
            if len(gemeffect) and effect < 0:
                if not self.Effect[slot].isEditable():
                    self.Effect[slot].setEditable(True)
                self.Effect[slot].setEditText(gemeffect)
            else:
                self.Effect[slot].setCurrentIndex(effect)
            self.UpdateCombo(1, slot)
            if itemtype == 'drop':
                am = item.slot(slot).amount()
                amedit = self.AmountEdit[slot]
                amedit.setText(am)
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
                quacombo = self.Quality[slot]
                gemqua = item.slot(slot).qua()
                if gemqua in QualityValues:
                    if quacombo.count() > 0:
                        quacombo.setCurrentIndex(QualityValues.index(gemqua))
        self.AFDPS_Edit.setText(item.getAttr('AFDPS'))
        self.Speed_Edit.setText(item.getAttr('Speed'))
        self.Bonus_Edit.setText(item.getAttr('Bonus'))
        if itemtype == 'drop':
            self.QualEdit.setText(item.getAttr('ItemQuality'))
            self.ItemName.setText(item.getAttr('ItemName'))
        else:
            if item.getAttr('ItemQuality') in QualityValues:
                self.QualDrop.setCurrentIndex(
                    QualityValues.index(item.getAttr('ItemQuality')))
        self.nocalc = wascalc
        self.save = wassave
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
        for key, item in self.itemattrlist.iteritems():
            utility = 0.0
            itemtype = item.getAttr('ActiveState')
            itemcost = 0
            gemeffects = []
            for i in range(0, item.slotCount()):
                gemtype = item.slot(i).type()
                if str(item.slot(i).amount()) == '':
                    amount = 0
                else:
                    amount = re.sub('[^\d]', '', item.slot(i).amount())
                    if amount == '': amount = '0'
                    amount = int(amount)
                effect = item.slot(i).effect()
                if effect != '' and [gemtype, effect] in gemeffects:
                    error_act = QAction('Two of same type of gem on %s' % key, self)
                    if item.Location in JewelTabList:
                        row = 1
                        col = JewelTabList.index(item.Location)
                    else:
                        row = 0
                        col = PieceTabList.index(item.Location)
                    error_act.setData(QVariant((row << 8) | col))
                    self.errorsmenu.addAction(error_act)
                    self.connect(self.errorsmenu, SIGNAL('triggered(QAction*)'), 
                                 self.changePieceTab)
                    errorcount = errorcount + 1
                gemeffects.append([gemtype, effect])
                if itemtype == 'player':
                    if key == self.currentTabLabel:
                        self.Cost[i].setText('')
                    cost = item.slot(i).gemCost()
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
                                if not AllBonusList[self.realm][self.charclass] \
                                                   ['Skills Hash'].has_key(effect):
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
                    error_act = QAction('Impossible Overcharge on %s' % key, self)
                    if item.Location in JewelTabList:
                        row = 1
                        col = JewelTabList.index(item.Location)
                    else:
                        row = 0
                        col = PieceTabList.index(item.Location)
                    error_act.setData(QVariant((row << 8) | col))
                    #error_act.setData(QVariant(errorcount))
                    self.errorsmenu.addAction(error_act)
                    self.connect(self.errorsmenu, SIGNAL('triggered(QAction*)'), 
                                 self.changePieceTab)
                    errorcount = errorcount + 1
                elif imbue > (itemimbue+0.5):
                    success = -OCStartPercentages[int(imbue-itemimbue)]
                    for slot in item.slots():
                        if item.slot(i).slotType != 'crafted': continue
                        if slot.type() == 'Unused': continue
                        success += GemQualOCModifiers[slot.qua()]
                    success += ItemQualOCModifiers[str(self.QualDrop.currentText())]
                    skillbonus = (int(self.crafterSkill / 50) - 10) * 5
                    if skillbonus > 50: skillbonus = 50
                    success += skillbonus
            if key == self.currentTabLabel:
                self.ItemUtility.setText('%3.1f' % utility)
                if self.PlayerMade.isChecked():
                    self.ItemImbue.setText('%3.1f' % imbue)
                    self.ItemImbueTotal.setText(' / ' + unicode(itemimbue))
                    self.ItemCost.setText(SC.formatCost(itemcost))
                    for i in range(0, item.slotCount()):
                        if item.slot(i).slotType != 'crafted': continue
                        n = self.Name[i]
                        n.setText(item.slot(i).gemName())
                        if item.slot(i).done() == "1":
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
        for (key, val) in self.totals.iteritems():
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
        self.TotalPrice.setText(SC.formatCost(self.computePrice()))
        self.errorsmenuid.setEnabled(errorcount > 0)

        self.nocalc = 0

    def computePrice(self):
        price = 0
        cost = 0
        for key, item in self.itemattrlist.iteritems():
            itemcost = 0
            itemtype = item.getAttr('ActiveState')
            if itemtype == 'drop': continue
            for slot in item.slots():
                gemcost = slot.gemCost()
                gemlvl = slot.gemLevel()
                cost += gemcost
                itemcost += gemcost
                if gemcost > 0:
                    price += self.pricingInfo.get('PPGem', 0) * 10000
                    if self.pricingInfo.get('HourInclude', 0):
                        price += self.pricingInfo.get('Hour', 0) * 10000 \
                               * int(slot.time()) / 60.0
                    if self.pricingInfo.get('TierInclude', 0):
                        tierp = self.pricingInfo.get('Tier', {})
                        price += float(tierp.get(str(gemlvl), 0)) * 10000
                    if self.pricingInfo.get('QualInclude', 0):
                        gemqual = slot.qua()
                        qualp = self.pricingInfo.get('Qual', {})
                        price += (gemcost * float(qualp.get(gemqual, 0)) / 100.0)
            if self.pricingInfo.get('PPInclude', 0):
                imbuepts = self.calcImbue(item, 0)
                price += self.pricingInfo.get('PPImbue', 0) * 10000 * imbuepts
                price += self.pricingInfo.get('PPOC', 0) * 10000 \
                       * max(0, int(imbuepts - self.getItemImbue(item)))
                if itemcost > 0:
                    price += self.pricingInfo.get('PPLevel', 0) * 10000 \
                           * int(item.getAttr('Level'))
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
        itemstate = item.getAttr('ActiveState')
        if itemstate == 'drop': return 0
        mvals = []
        for slot in item.slots():
            mval = slot.gemImbue()
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

    def TemplateChanged(self,a0):
        if self.save:
            self.modified = 1
        self.calculate()

    def UpdateCombo(self, type, num):
        typecombo = self.Type[num]
        typetext = str(typecombo.currentText())
        effcombo = self.Effect[num]
        efftext = str(effcombo.currentText())
        itemslot = self.itemattrlist[self.currentTabLabel].slot(num)
        if itemslot.slotType() == 'crafted':
            amount = self.AmountDrop[num]
        else:
            amount = self.AmountEdit[num]
        if typetext == 'Unused':
            if type == 0:
                effcombo.clear()
                if effcombo.isEditable():
                    effcombo.setEditable(False)
                    self.fix_taborder(num)
                amount.clear()
                if self.PlayerMade.isChecked():
                    self.Quality[num].setCurrentIndex(0)
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
                    effcombo.insertItems(0, list(effectlist))
                    effcombo.setCurrentIndex(0)
            if type == 1:
                unique = (not efftext in effectlist) \
                      or (len(efftext) > 3 and efftext[-3:] == "...")
                if effcombo.isEditable() and not unique:
                    refocus = self.Effect[num].hasFocus()
                    effcombo.setEditable(False)
                    effcombo.setCurrentIndex(effectlist.index(efftext))
                    self.fix_taborder(num)
                elif unique and not effcombo.isEditable():
                    refocus = self.Effect[num].hasFocus()
                    effcombo.setEditable(True)
                    effcombo.setEditText(efftext)
                    self.fix_taborder(num)
                else:
                    refocus = False
                if refocus:
                    flip = self.Effect[num].setFocus()
            if self.PlayerMade.isChecked():
                amtindex = amount.currentIndex()
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
                        amount.insertItems(0, list(valueslist))
                    if amtindex < 0:
                        amtindex = 0
                    if amtindex < len(valueslist):
                        amount.setCurrentIndex(amtindex)
                if type == 0:
                    self.Quality[num].setCurrentIndex(len(QualityValues)-2)

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
        if self.save:
            self.modified = 1
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
        self.CharRace.insertItems(0, list(racelist))
        if race in racelist:
          self.CharRace.setCurrentIndex(racelist.index(race))
        self.RaceChanged('')

    def RealmChanged(self,a0):
        self.realm = str(self.Realm.currentText())
        self.CharClass.clear()
        self.CharClass.insertItems(0, list(ClassList[self.realm]))
        if self.charclass in ClassList[self.realm]:
          self.CharClass.setCurrentIndex(ClassList[self.realm].index(self.charclass))
        self.CharClassChanged('')
    
    def ItemChanged(self,a0):
        if self.save:
            self.modified = 1
            item = self.itemattrlist[self.currentTabLabel]
            self.storeItem(item)
        self.calculate()

    def TypeChanged(self, Value):
        index = self.focusWidget().objectName()[-2:]
        if index[0] == '_': index = index[1:]
        wascalc = self.nocalc
        self.nocalc = 1
        self.UpdateCombo(0, int(index) - 1)
        self.nocalc = wascalc
        if self.save:
            self.modified = 1
            self.storeItem(self.itemattrlist[self.currentTabLabel])
        self.calculate()

    def EffectChanged(self, value):
        index = str(self.focusWidget().objectName())[-2:]
        if index[0] == '_': index = index[1:]
        wascalc = self.nocalc
        self.nocalc = 1
        self.UpdateCombo(1, int(index) - 1)
        self.nocalc = wascalc
        if self.save:
            self.modified = 1
            self.storeItem(self.itemattrlist[self.currentTabLabel])
        self.calculate()

    def AmountChanged(self,a0):
        if self.save:
            self.modified = 1
        self.storeItem(self.itemattrlist[self.currentTabLabel])
        self.calculate()

    def QualityChanged(self,a0):
        if self.save:
            self.modified = 1
        self.storeItem(self.itemattrlist[self.currentTabLabel])
        self.calculate()

    def EquippedClicked(self):
        if self.save:
            self.modified = 1
            self.storeItem(self.itemattrlist[self.currentTabLabel])
        self.calculate()
    
    def DropToggled(self,a0):
        if self.nocalc:
            return
        if not a0: 
            return
        item = self.itemattrlist[self.currentTabLabel]
        item.loadAttr('ActiveState','drop')
        self.showDropWidgets()
        self.restoreItem(item)

    def PlayerToggled(self, a0):
        if self.nocalc:
            return
        if not a0: 
            return
        item = self.itemattrlist[self.currentTabLabel]
        item.loadAttr('ActiveState','player')
        self.showPlayerWidgets()
        self.restoreItem(item)

    def ClearCurrentItem(self):
        self.modified = 1
        self.itemattrlist[self.currentTabLabel] = Item(realm=self.realm,loc=self.currentTabLabel)
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def Save_Item(self):
        itemname = unicode(self.ItemName.text())
        if itemname == '':
            QMessageBox.critical(None, 'Error!', 
                'Cannot save item - You must specifify a name!', 'OK')
            return
        item = self.itemattrlist[self.currentTabLabel]
        self.storeItem(item)
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
        
    def Load_Item(self):
        ext = FileExt[self.currentTabLabel]
        extstr = ''
        if not isinstance(ext, types.StringType):
            for e in ext:
                extstr += '*%s.xml *.%s ' % (e, e)
            ext = ext[0]
        else:
            extstr = '*%s.xml *.%s' % (ext, ext)
        extstr = "Items (%s)" % extstr
        itemdir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 
                               'items', self.realm, ext)
        Qfd = ItemList.ItemListDialog(self, "Load Item", itemdir, extstr, 
                                      self.realm, self.charclass)
        if Qfd.exec_():
            if Qfd.selectedFiles().count() > 0:
                filename = unicode(Qfd.selectedFiles()[0])
                item = Item(self.currentTabLabel)
                item.loadAttr('Realm', self.realm)
                if item.load(filename) == -1 : return
                if string.lower(item.getAttr('Realm')) != string.lower(self.realm)\
                    and string.lower(item.getAttr('Realm')) != 'all'\
                    and not self.coop:
                    QMessageBox.critical(None, 'Error!', 'You are trying to load an '
                                                       + 'item for another realm!', 'OK')
                    return
                item.loadAttr('Location', self.currentTabLabel)
                self.itemattrlist[self.currentTabLabel] = item
                self.restoreItem(item)
                self.modified = 1

    def ItemLevelShow(self):
        level = self.ItemLevelWindow.exec_()
        if level != -1:
            self.ItemLevel.setText(str(level))
            self.AFDPS_Edit.setText(str(self.ItemLevelWindow.afdps))

    def newFile(self):
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 
                                      'Some changes may not have been saved. Are you '
                                    + 'sure you want to discard these changes?', 'Yes', 'No')
            if ret == 1:
                return
        wascalc = self.nocalc
        self.nocalc = 1
        self.initialize()

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
        filename = self.filename
        if filename is None:
            templatedir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), "templates")
            filename = os.path.join(templatedir, str(self.CharName.text()) + "_template.xml")
        filename = unicode(filename)
        while filename != '':
            filename = QFileDialog.getSaveFileName(self, "Save Template", filename, 
                                                   "Templates (*.xml)")
            filename = unicode(filename)
            if filename != '' and os.path.exists(filename):
                ret = QMessageBox.warning(self, "Overwrite?", "Do you want to overwrite the "
                                                            + "selected file?", "Yes", "No")
                if ret != 1:
                    continue
            break
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
            self.setWindowTitle(filetitle + " - Kort's Spellcrafting Calculator")
            

    def openFile(self, *args):
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 
                                      'Some changes may not have been saved. Are you sure '
                                    + 'you want to discard these changes?', 'Yes', 'No')
            if ret == 1:
                return
        if len(args) == 0:
            templatedir = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 
                                       'templates')
            filename = QFileDialog.getOpenFileName(self, "Open Template", templatedir, 
                                                   "Templates (*.xml *.scc)")
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
        self.Realm.setCurrentIndex(Realms.index(self.realm))
        self.RealmChanged(self.realm)
        if AllBonusList[self.realm].has_key(self.charclass):
            self.CharClass.setCurrentIndex(ClassList[self.realm].index(self.charclass))
            self.CharClassChanged('')
        if racename in AllBonusList[self.realm][self.charclass]['Races']:
            self.CharRace.setCurrentIndex(AllBonusList[self.realm][self.charclass] \
                                                      ['Races'].index(racename))
            self.RaceChanged('')
        self.nocalc = wascalc
        self.restoreItem(self.itemattrlist[self.currentTabLabel])
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
                self.Realm.setCurrentIndex(Realms.index(self.realm))
                self.RealmChanged(self.realm)
                if AllBonusList[self.realm].has_key(self.charclass):
                   self.CharClass.setCurrentIndex(ClassList[self.realm].index(self.charclass))
                   self.CharClassChanged('')

        for itemnum in range(0, 19):
            item = Item(TabList[itemnum])
            #item.loadAttr('Location', TabList[itemnum])
            item.loadLelaItemFromSCC(itemnum, scclines, self.realm)
            self.itemattrlist[item.getAttr('Location')] = item
        self.nocalc = wascalc
        self.restoreItem(self.itemattrlist[self.currentTabLabel])
        
    def openOptions(self):
        self.modified = 1
        self.nocalc = 1
        res = Options.Options(self).exec_()
        if res == 1:
             self.CharClassChanged('')
        self.nocalc = 0
        self.calculate()

    def OpenCraftWindow(self):
        self.storeItem(self.itemattrlist[self.currentTabLabel])
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
        CB = CraftBar.CraftBar(self.DaocPath, self, '', 1)
        CB.exec_()
        self.DaocPath = str(CB.DaocPath.text())

    def DelveItemsDialog(self, find, findtype = None):
        locs = []
        for key, item in self.itemattrlist.iteritems():
            activestate = item.getAttr('ActiveState')
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
