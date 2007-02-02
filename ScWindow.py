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
from ScOptions import ScOptions
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
import binascii

UserEventIDRestoreItem = QEvent.Type(QEvent.User + 1)
UserEventIDUpdateTypeList = QEvent.Type(QEvent.User + 2)

class UpdateTypeListEvent(QEvent):
    def __init__(self, slot):
        QEvent.__init__(self, UserEventIDUpdateTypeList)
        self.slot = slot

class RestoreItemEvent(QEvent):
    def __init__(self, item):
        QEvent.__init__(self, UserEventIDRestoreItem)
        self.item = item

def plainXMLTag(strval):
    i = 0
    while i < len(strval):
        if not (strval[i].isalpha() or (i > 0 and strval[i].isdigit())):
            strval = strval[:i] + strval[i+1:]
        else:
            i += 1
    return strval

class AboutScreen(QDialog):
    def __init__(self,parent = None,name = "About",modal = True,
                 fl = Qt.SplashScreen):
        QDialog.__init__(self,parent,fl)
        self.setModal(modal)
        self.setObjectName(name)
        pixmap = QPixmap(":/images/Spellcraft.png")
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
        ScOptions()
        ScOptions.instance().load()

        self.splashFile = None
        self.newcount = 0
        self.startup = 1
        self.nocalc = 1
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
        self.charclass = 'Armsman'

        self.ItemLevelWindow = ItemLevel.ItemLevel(self.window(), '', 1)
        self.loadOptions()
        self.initMenu()
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
            self.LabelGemMakes, self.LabelGemPoints,
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

        for stat in (DropLists['All']['Stat'] + ('PowerPool', 'AF',)):
            self.StatLabel[stat] = getattr(self, stat + 'Label')
            self.StatValue[stat] = getattr(self, stat)
            self.StatCap[stat] = getattr(self, stat + 'Cap')
        width = testfont.size(Qt.TextSingleLine, "CON: ").width()
        self.GroupStats.layout().setColumnMinimumWidth(0,width)
        width = testfont.size(Qt.TextSingleLine, "400").width()
        self.GroupStats.layout().setColumnMinimumWidth(1,width)
        width = testfont.size(Qt.TextSingleLine, " (400)").width()
        self.GroupStats.layout().setColumnMinimumWidth(2,width)

        for stat in (DropLists['All']['Resist']):
            self.StatLabel[stat] = getattr(self, stat + 'Label')
            self.StatValue[stat] = getattr(self, stat)
            self.StatBonus[stat] = getattr(self, stat + 'Cap')
        width = testfont.size(Qt.TextSingleLine, "Energy: ").width()
        self.GroupResists.layout().setColumnMinimumWidth(0,width)
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
        self.CharName.setFixedSize(QSize(cbwidth, edheight))
        self.Realm.setFixedSize(QSize(cbwidth, cbheight))
        self.CharClass.setFixedSize(QSize(cbwidth, cbheight))
        self.CharRace.setFixedSize(QSize(cbwidth, cbheight))
        self.CharLevel.setFixedSize(QSize(amtedwidth, edheight))
        self.OutfitName.setFixedSize(QSize(cbwidth, cbheight))

        self.Realm.insertItems(0, list(Realms))
        self.OutfitName.setCompleter(None)

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
        self.Makes = []
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
        self.ItemNameCombo.setCompleter(None)

        width = testfont.size(Qt.TextSingleLine, " Slot 10:").width()
        self.GroupItemFrame.layout().setColumnMinimumWidth(0,width)
        width = testfont.size(Qt.TextSingleLine, " Points").width()
        self.GroupItemFrame.layout().setColumnMinimumWidth(5,width)
        reqwidth = width
        width = testfont.size(Qt.TextSingleLine, "  999g 00s 00c").width()
        self.GroupItemFrame.layout().setColumnMinimumWidth(6,width)
        reqwidth += width + amtcbwidth
        self.GroupItemFrame.layout().setColumnStretch(8, 1)

        typewidth = self.Type_1.getMinimumWidth(list(DropTypeList))
        l = reduce(lambda x, y: x+y, [ list(x) \
                                       for x in GemLists['All'].values() ])
        effectwidth = self.Effect_1.getMinimumWidth(l)

        # XXX FIX ME - I want to have a decimal!  But Double validator isn't working
        editAmountValidator = QIntValidator(-999, +999, self)

        for i in range(0, 12):
            idx = i + 1

            self.GemLabel.append(getattr(self, 'Gem_Label_%d' % idx))
            self.Type.append(getattr(self, 'Type_%d' % idx))
            self.Type[i].setFixedSize(QSize(typewidth, cbheight))
            self.connect(self.Type[i],SIGNAL("activated(int)"),
                         self.typeChanged)
            self.GemLabel[i].setBuddy(self.Type[i])

            self.AmountEdit.append(getattr(self, 'Amount_Edit_%d' % idx))
            self.AmountEdit[i].setFixedSize(QSize(amtcbwidth, edheight))
            self.AmountEdit[i].setValidator(editAmountValidator)
            self.switchOnType['drop'].append(self.AmountEdit[i])
            self.connect(self.AmountEdit[i],SIGNAL("editingFinished()"),
                         self.amountsChanged)
            #self.connect(self.AmountEdit[i],SIGNAL("textChanged(const QString&)"),
            #             self.amountsChanged)

            self.Effect.append(getattr(self, 'Effect_%d' % idx))
            self.Effect[i].setFixedSize(QSize(effectwidth, cbheight))
            self.Effect[i].setInsertPolicy(QComboBox.NoInsert)
            self.connect(self.Effect[i],SIGNAL("activated(int)"),
                         self.effectChanged)
            self.connect(self.Effect[i],SIGNAL("editTextChanged(const QString&)"),
                         self.effectChanged)

            self.Requirement.append(getattr(self, 'Requirement_%d' % idx))
            self.Requirement[i].setFixedSize(QSize(reqwidth, edheight))
            self.switchOnType['drop'].append(self.Requirement[i])
            self.connect(self.Requirement[i],SIGNAL("editingFinished()"),
                         self.amountsChanged)
            #self.connect(self.Requirement[i],SIGNAL("textChanged(const QString&)"),
            #            self.amountsChanged)

            if i < 6:
                self.AmountDrop.append(getattr(self, 'Amount_Drop_%d' % idx))
                self.AmountDrop[i].setFixedSize(QSize(amtcbwidth, cbheight))
                self.connect(self.AmountDrop[i],SIGNAL("activated(int)"),
                             self.amountsChanged)
                self.Name.append(getattr(self, 'Name_%d' % idx))
                self.switchOnType['player'].extend([
                    self.AmountDrop[i], self.Name[i], ])
            else:
                self.switchOnType['drop'].extend([
                    self.GemLabel[i], self.Type[i], self.Effect[i], ])

            if i < 4:
                self.Makes.append(getattr(self, 'Makes_%d' % idx))
                self.Makes[i].setFixedSize(QSize(amtcbwidth, cbheight))
                self.connect(self.Makes[i],SIGNAL("valueChanged(int)"),
                             self.amountsChanged)
                # Hide '0' values
                self.Makes[i].setSpecialValueText(" ")
                self.Points.append(getattr(self, 'Points_%d' % idx))
                self.Cost.append(getattr(self, 'Cost_%d' % idx))
                self.switchOnType['player'].extend([
                    self.Makes[i], self.Points[i], self.Cost[i], ])

            self.GroupItemFrame.layout().setRowMinimumHeight(i + 3, 
                max(cbheight, edheight))

        for tabname in PieceTabList:
            self.PieceTab.addTab(0, qApp.translate("B_SC",tabname,None))
        for tabname in JewelTabList:
            self.PieceTab.addTab(1, qApp.translate("B_SC",tabname,None))
        self.GroupItemFrame.stackUnder(self.PieceTab)
        l = self.ScWinFrame.layout().itemAt(self.ScWinFrame.layout().count()-1)
        l.layout().itemAt(1).changeSize(1, -self.PieceTab.baseOverlap(),
                                        QSizePolicy.Minimum, QSizePolicy.Fixed)


    def initControls(self):
        # Send these home to the parent form (this QMainWindow), they are dumb QFrames:
        self.GroupStats.mousePressEvent = self.ignoreMouseEvent
        self.GroupResists.mousePressEvent = self.ignoreMouseEvent
        self.GroupItemFrame.mousePressEvent = self.ignoreMouseEvent

        self.connect(self.GroupStats,SIGNAL("mousePressEvent(QMouseEvent*)"),
                     self.mousePressEvent)
        self.connect(self.GroupResists,SIGNAL("mousePressEvent(QMouseEvent*)"),
                     self.mousePressEvent)
        self.connect(self.GroupItemFrame,
                     SIGNAL("mousePressEvent(QMouseEvent*)"),
                     self.mousePressEvent)

        #self.connect(self.CharName,SIGNAL("editingFinished()"),
        #             self.templateChanged)
        self.connect(self.CharName,SIGNAL("textChanged(const QString&)"),
                     self.templateChanged)
        self.connect(self.Realm,SIGNAL("activated(int)"),
                     self.realmChanged)
        self.connect(self.CharClass,SIGNAL("activated(int)"),
                     self.charClassChanged)
        self.connect(self.CharRace,SIGNAL("activated(int)"),
                     self.raceChanged)
        #self.connect(self.CharLevel,SIGNAL("editingFinished()"),
        #             self.templateChanged)
        self.connect(self.CharLevel,SIGNAL("textChanged(const QString&)"),
                     self.templateChanged)
        self.connect(self.OutfitName,SIGNAL("activated(int)"), 
                     self.outfitNameSelected)
        #self.connect(self.OutfitName.lineEdit(),SIGNAL("editingFinished()"),
        #             self.outfitNameEdited)
        self.connect(self.OutfitName,SIGNAL("editTextChanged(const QString&)"),
                     self.outfitNameEdited)


        self.connect(self.PieceTab,SIGNAL("currentChanged"),
                     self.pieceTabChanged)
        #self.connect(self.ItemLevel,SIGNAL("editingFinished()"),
        #             self.itemChanged)
        self.connect(self.ItemLevel,SIGNAL("textChanged(const QString&)"),
                     self.itemChanged)
        self.connect(self.ItemLevelButton,SIGNAL("clicked()"),
                     self.itemLevelShow)
        self.connect(self.QualDrop,SIGNAL("activated(int)"),
                     self.itemChanged)
        #self.connect(self.ItemLevel,SIGNAL("editingFinished()"),
        #             self.itemChanged)
        self.connect(self.QualEdit,SIGNAL("textChanged(const QString&)"),
                     self.itemChanged)
        #self.connect(self.Bonus_Edit,SIGNAL("editingFinished()"),
        #             self.itemChanged)
        self.connect(self.Bonus_Edit,SIGNAL("textChanged(const QString&)"),
                     self.itemChanged)
        #self.connect(self.AFDPS_Edit,SIGNAL("editingFinished()"),
        #             self.itemChanged)
        self.connect(self.AFDPS_Edit,SIGNAL("textChanged(const QString&)"),
                     self.itemChanged)
        #self.connect(self.Speed_Edit,SIGNAL("editingFinished()"),
        #             self.itemChanged)
        self.connect(self.Speed_Edit,SIGNAL("textChanged(const QString&)"),
                     self.itemChanged)
        self.connect(self.Equipped,SIGNAL("stateChanged(int)"),
                     self.itemChanged)
        self.connect(self.ItemNameCombo,SIGNAL("activated(int)"),
                     self.itemNameSelected)
        #self.connect(self.ItemNameCombo.lineEdit(),SIGNAL("editingFinished()"),
        #             self.itemNameEdited)
        self.connect(self.ItemNameCombo,SIGNAL("editTextChanged(const QString&)"),
                    self.itemNameEdited)
        self.connect(self.SkillsList,SIGNAL("activated(const QModelIndex&)"),
                     self.skillClicked)

    def getIcon(self, namebase):
        thisicon = QIcon()
        for size in (16, 24, 32,):
             thisicon.addFile(':/images/normal/' + namebase + str(size) + '.png',
                              QSize(size, size), QIcon.Normal, QIcon.Off)
             thisicon.addFile(':/images/disabled/' + namebase + str(size) + '.png',
                              QSize(size, size), QIcon.Disabled, QIcon.Off)
             thisicon.addFile(':/images/hot/' + namebase + str(size) + '.png',
                              QSize(size, size), QIcon.Active, QIcon.Off)
        return thisicon

    def initMenu(self):
        self.toolbar = QToolBar("Crafting Toolbar")
        self.toolbar.setObjectName("CraftingToolbar")

        self.rf_menu = QMenu('&Recent Files')
        self.connect(self.rf_menu, SIGNAL("triggered(QAction*)"),
                     self.loadRecentFile)
        
        self.filemenu = QMenu('&File', self)
        self.filemenu.addAction('&New', self.newFile,
                                QKeySequence(Qt.CTRL+Qt.Key_N))
        self.toolbar.addAction(self.getIcon('New'), 'New', self.newFile)
        self.filemenu.addAction('&Open...', self.openFile,
                                QKeySequence(Qt.CTRL+Qt.Key_O))
        self.toolbar.addAction(self.getIcon('Open'), 'Open', self.openFile)
        self.filemenu.addAction('&Save', self.saveFile,
                                QKeySequence(Qt.CTRL+Qt.Key_S))
        self.toolbar.addAction(self.getIcon('Save'), 'Save', self.saveFile)
        self.filemenu.addAction('Save &As...', self.saveAsFile)
        self.toolbar.addAction(self.getIcon('SaveAs'), 'Save As',
                               self.saveAsFile)

        self.filemenu.addSeparator()
        self.toolbar.addSeparator()

        self.filemenu.addAction('&Load Item...', self.loadItem,
                                QKeySequence(Qt.CTRL+Qt.SHIFT+Qt.Key_L))
        self.toolbar.addAction(self.getIcon('LoadItem'), 'Load Item', 
                               self.loadItem)
        self.filemenu.addAction('Sa&ve Item...', self.saveItem,
                                QKeySequence(Qt.CTRL+Qt.SHIFT+Qt.Key_S))
        self.toolbar.addAction(self.getIcon('SaveItem'), 'Save Item', 
                               self.saveItem)
        self.filemenu.addAction('Item Database Path...', self.chooseItemPath)

        self.filemenu.addSeparator()
        self.toolbar.addSeparator()

        self.filemenu.addAction('Export &Quickbars...', self.openCraftBars)
        self.toolbar.addAction(self.getIcon('ExportGems'), 'Quickbars', 
                               self.openCraftBars)
        self.filemenu.addAction('Export SCTemplate XML...', self.exportAsFile)
        self.filemenu.addAction('Export &UI Window...', self.generateUIXML)
        self.filemenu.addAction('Choose UI Format...', self.chooseXMLUIFile)

        self.filemenu.addSeparator()

        self.filemenu.addMenu(self.rf_menu)
        self.filemenu.addSeparator()
        self.filemenu.addAction('E&xit', self.close,
                                QKeySequence(Qt.CTRL+Qt.Key_X))
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

        # DON"T SWAP TWICE!!!!!!
        #self.connect(self.swapgemsmenu, SIGNAL("triggered(QAction*)"),
        #             self.swapWith)
        self.connect(self.swappiecemenu, SIGNAL("triggered(QAction*)"),
                     self.swapWith)
        self.connect(self.swapjewelmenu, SIGNAL("triggered(QAction*)"),
                     self.swapWith)

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
        self.connect(self.moveitemmenu, SIGNAL("triggered(QAction*)"),
                     self.moveTo)
        self.connect(self.movepiecemenu, SIGNAL("triggered(QAction*)"),
                     self.moveTo)
        self.connect(self.movejewelmenu, SIGNAL("triggered(QAction*)"),
                     self.moveTo)

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
        self.editmenu.addSeparator()

        # FIXME
        self.editmenu.addAction('&New Outfit', self.newOutfit)
        self.deleteOutfitAction = self.editmenu.addAction('&Delete Current Outfit', self.deleteOutfit)

        self.menuBar().addMenu(self.editmenu)

        self.viewmenu = QMenu('&View', self)
        self.craftingmenuid = self.viewmenu.addAction('Craft &Gems',
                                  self.openCraftWindow,
                                  QKeySequence(Qt.ALT+Qt.Key_G))
        self.craftingtoolid = self.toolbar.addAction(self.getIcon('CraftGems'),
                                  'Craft Gems', self.openCraftWindow)

        self.viewmenu.addSeparator()

        self.viewmenu.addAction('&Materials Report', self.openMaterialsReport,
                                QKeySequence(Qt.ALT+Qt.Key_M))
        self.toolbar.addAction(self.getIcon('MatsReport'), 'Materials Report',
                               self.openMaterialsReport)
        self.viewmenu.addAction('&Configuration Report', self.openConfigReport,
                                QKeySequence(Qt.ALT+Qt.Key_C))
        self.toolbar.addAction(self.getIcon('ConfReport'), 'Configuration Report',
                               self.openConfigReport)
        self.viewmenu.addAction('Choose Config Template...',
                                self.chooseReportFile)

        self.viewmenu.addSeparator()

        self.viewtoolbarmenu = QMenu('&Toolbar', self)
        for (title, res) in (("Large", 32,), ("Normal", 24,),
                             ("Tiny", 16,),  ("Hide", 0,),):
            act = QAction(title, self)
            act.setData(QVariant(res))
            act.setCheckable(True)
            self.viewtoolbarmenu.addAction(act)
        self.viewtoolbarmenu.actions()[1].setChecked(True)
        self.connect(self.viewtoolbarmenu, SIGNAL("triggered(QAction*)"), 
                     self.viewToolbar)
        self.viewmenu.addMenu(self.viewtoolbarmenu)

        self.viewmenu.addSeparator()

        self.showcapmenuid = self.viewmenu.addAction('&Distance to Cap',
                                 self.showCap, QKeySequence(Qt.ALT+Qt.Key_D))
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

        self.addToolBar(self.toolbar)
        state = ScOptions.instance().getOption('WindowState', None)
        if state:
            self.restoreState(binascii.a2b_base64(state), 0)
            iconsz = ScOptions.instance().getOption('ToolbarSize', 16)
            if self.toolbar.isHidden():
                iconsz = 0
            for act in self.viewtoolbarmenu.actions():
                if act.data().toInt()[0] == iconsz:
                    act.setChecked(True)
                else:
                    act.setChecked(False)
            if iconsz != 0:
                self.setIconSize(QSize(iconsz, iconsz))

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
                    self.setTabOrder(self.Effect[i],self.Makes[i])
                    self.setTabOrder(self.Makes[i],self.Requirement[i])
                else:
                    self.setTabOrder(self.Effect[i],self.Requirement[i])
            else:
                self.setTabOrder(self.AmountEdit[i],self.Effect[i])
                self.setTabOrder(self.Effect[i],self.Requirement[i])
            prev = self.Requirement[i]
        self.setTabOrder(prev,self.SkillsList)

    def showFixWidgets(self):
        for i in range(0,6):
            self.GemLabel[i].setText('Slot &%d:' % (i + 1))
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
        #self.GroupItemFrame.updateGeometry()
        self.craftingmenuid.setEnabled(False)
        self.craftingtoolid.setEnabled(False)
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
            if item.slot(i).slotType() == 'player':
                self.GemLabel[i].setText('Gem &%d:' % (i + 1))
            else:
                if i < 4:
                    self.Makes[i].hide()
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
        self.craftingtoolid.setEnabled(enableCrafting)

    def closeEvent(self, e):
        self.saveOptions()
        ScOptions.instance().save()
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 
                                      "This template has been changed.\n"
                                      "Do you want to save these changes?", 
                                      QMessageBox.Yes, QMessageBox.No,
                                      QMessageBox.Cancel)
            if ret == QMessageBox.Cancel:
                e.ignore()
                return
            if ret == QMessageBox.Yes:
                self.saveFile()
                if self.modified: 
                    e.ignore()
                    return
        e.accept()

    def loadOptions(self):
        self.realm = ScOptions.instance().getOption('Realm', 'Albion')
        self.crafterSkill = ScOptions.instance().getOption('CrafterSkill', 1000)
        self.showDoneInMatsList = ScOptions.instance().getOption('DontShowDoneGems', False)
        self.includeRacials = ScOptions.instance().getOption('IncludeRRInRacials', False)
        self.capDistance = ScOptions.instance().getOption('DistanceToCap', False)
        self.hideNonClassSkills = ScOptions.instance().getOption('HideNonClassSkills', False)
        self.coop = ScOptions.instance().getOption('Coop', False)
        self.pricingInfo = ScOptions.instance().getOption('Pricing', {})
        self.recentFiles = ScOptions.instance().getOption('RecentFiles', [])
        self.ItemPath = ScOptions.instance().getOption('ItemPath',
            os.path.join(os.path.dirname(
                os.path.abspath(sys.argv[0])), "items"))
        self.TemplatePath = ScOptions.instance().getOption('TemplatePath',
            os.path.join(os.path.dirname(
                os.path.abspath(sys.argv[0])), "templates"))
        self.ReportPath = ScOptions.instance().getOption('ReportPath',
            os.path.join(os.path.dirname(
                os.path.abspath(sys.argv[0])), "reports"))
        self.ReportFile = ScOptions.instance().getOption('ConfigReportXSLT',
            os.path.join(self.ReportPath, 'DefaultConfigReport.xsl'))
        self.UiReportFile = ScOptions.instance().getOption('ConfigUiReportXSLT',
            os.path.join(self.ReportPath, 'DefaultUiXmlWindow.xsl'))

        x = ScOptions.instance().getOption('WindowX', self.pos().x())
        y = ScOptions.instance().getOption('WindowY', self.pos().y())
        w = ScOptions.instance().getOption('WindowW', self.width())
        h = ScOptions.instance().getOption('WindowH', self.height())

        screenW = QApplication.desktop().width()
        screenH = QApplication.desktop().height()
        if w < 100:
            w = 781
        if h < 100:
            w = 589

        if w > screenW:
            w = 781
        if h > screenH:
            h = 589

        if x < 20 or x > (screenW - 20):
            x = 20
        if y < 20 or y > (screenH - 20):
            y = 20

        self.resize(w, h)
        self.move(x, y)
        self.updateGeometry()

        if not self.pricingInfo.has_key('Tier') or\
                not isinstance(self.pricingInfo['Tier'], dict):
            self.pricingInfo['Tier'] = {}
            ScOptions.instance().setOption('Pricing', self.pricingInfo)

    def saveOptions(self):
        ScOptions.instance().setOption('Realm', self.realm)
        ScOptions.instance().setOption('RecentFiles', self.recentFiles)
        ScOptions.instance().setOption('ItemPath', self.ItemPath)
        ScOptions.instance().setOption('TemplatePath', self.TemplatePath)
        ScOptions.instance().setOption('ReportPath', self.ReportPath)
        ScOptions.instance().setOption('ConfigReportXSLT', self.ReportFile)
        ScOptions.instance().setOption('ConfigUiReportXSLT', self.UiReportFile)

        ScOptions.instance().setOption('WindowX', self.pos().x())
        ScOptions.instance().setOption('WindowY', self.pos().y())
        ScOptions.instance().setOption('WindowW', self.width())
        ScOptions.instance().setOption('WindowH', self.height())

        ScOptions.instance().setOption('WindowState', 
            binascii.b2a_base64(self.saveState(0))[:-1])
        ScOptions.instance().setOption('ToolbarSize',
            self.iconSize().width())

    def initialize(self, moretodo):
        self.nocalc = 1
        self.noteText = ''
        self.filename = None
        self.newcount = self.newcount + 1
        filetitle = unicode("Template" + str(self.newcount))
        self.setWindowTitle(filetitle + " - Kort's Spellcrafting Calculator")

        self.PieceTab.setCurrentIndex(0, 0)
        self.currentTab = self.PieceTab
        self.currentTabLabel = string.strip(str(self.PieceTab.tabText(0, 0)))

        self.outfitnumbering = 1
        self.currentOutfit = 0
        self.outfitlist = []
        self.OutfitName.clear()
        self.deleteOutfitAction.setEnabled(False)

        self.itemIndex = 0
        self.itemattrlist = { }
        self.itemnumbering = 1

        for tab in PieceTabList:
            item = Item('player', tab, self.realm, self.itemIndex)
            self.itemIndex += 1
            item.next = Item('drop', tab, self.realm, self.itemIndex)
            self.itemIndex += 1
            item.ItemName = "Crafted Item" + str(self.itemnumbering)
            item.next.ItemName = "Drop Item" + str(self.itemnumbering)
            self.itemnumbering += 1
            self.itemattrlist[tab] = item
        for tab in JewelTabList:
            item = Item('drop', tab, self.realm, self.itemIndex)
            self.itemIndex += 1
            item.ItemName = "Drop Item" + str(self.itemnumbering)
            self.itemnumbering += 1
            self.itemattrlist[tab] = item

        self.CharName.setText('')
        self.Realm.setCurrentIndex(Realms.index(self.realm))
        self.realmChanged(Realms.index(self.realm))
        self.CharLevel.setText('50')
        self.appendOutfit()
        self.restoreItem(self.itemattrlist[self.currentTabLabel])
        self.modified = 0
        self.nocalc = moretodo
        if self.nocalc: return
        self.calculate()

    def asXML(self, rich=False):
        document = Document()
        rootnode = document.createElement('SCTemplate')
        document.appendChild(rootnode)
        childnode = document.createElement('Name')
        childnode.appendChild(document.createTextNode(
                                       unicode(self.CharName.text())))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Realm')
        childnode.appendChild(document.createTextNode(self.realm))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Class')
        childnode.appendChild(document.createTextNode(self.charclass))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Race')
        childnode.appendChild(document.createTextNode(
                                       unicode(self.CharRace.currentText())))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Level')
        childnode.appendChild(document.createTextNode(
                                       unicode(self.CharLevel.text())))
        rootnode.appendChild(childnode)
        childnode = document.createElement('Notes')
        childnode.appendChild(document.createTextNode(unicode(self.noteText)))
        rootnode.appendChild(childnode)

        if rich:
            totalsdict = self.summarize()
            for key in (u'Cost', u'Price', u'Utility',):
                val = totalsdict[key]
                childnode = document.createElement(key)
                childnode.appendChild(document.createTextNode(unicode(val)))
                rootnode.appendChild(childnode)
            for key in (u'Stats', u'Resists', u'Skills', u'Focus', 
                        u'OtherBonuses', u'PvEBonuses'):
                if key == 'Stats':
                    types = DropLists['All']['Stat'] + ('% Power Pool', 'AF')
                elif key == 'Resists':
                    types = DropLists['All']['Resist']
                else:
                    types = totalsdict[key].keys()
                    types.sort()
                childnode = document.createElement(key)
                if key[-7:] == 'Bonuses':
                    childnode.setAttribute(u'text', key[:-7] + u' ' + key[-7:])
                for type in types:
                    tagname = unicode(plainXMLTag(type))
                    effectnode = document.createElement(tagname)
                    if tagname != type:
                        effectnode.setAttribute(u'text', unicode(type))
                    if key == 'Stats':
                        subs = (u'Bonus', u'TotalBonus', u'BaseCap', 
                                u'CapBonus', u'TotalCapBonus', 
                                u'BaseCapToCapBonus',) 
                    else:
                        subs = (u'Bonus', u'TotalBonus', u'BaseCap',)
                        if key == u'Resists' and \
                                totalsdict[key][type].has_key('RacialBonus'): 
                            subs = subs + ('RacialBonus',)
                    for subtype in subs:
                        tagname = unicode(plainXMLTag(subtype))
                        valnode = document.createElement(tagname)
                        if tagname != subtype:
                            effectnode.setAttribute(u'text', unicode(subtype))
                        val = unicode(totalsdict[key][type][subtype])
                        valnode.appendChild(document.createTextNode(val))
                        effectnode.appendChild(valnode)
                    childnode.appendChild(effectnode)
                rootnode.appendChild(childnode)

        for key in TabList:
            item = self.itemattrlist[key]
            # use firstChild here because item.asXML() constructs a Document()
            while item is not None:
                childnode = item.asXML(self.pricingInfo, self.crafterSkill,rich,True)
                if childnode is not None:
                    rootnode.appendChild(childnode.firstChild)
                item = item.next

        for idx in range(0, len(self.outfitlist)):
            outfit = self.outfitlist[idx]
            outfitnode = document.createElement('Outfit')
            outfitnode.setAttribute(u'Name', outfit[None])
            outfitnode.setAttribute(u'Active', unicode(int(idx == self.currentOutfit)))
            for piece, item in outfit.iteritems():
                if piece is None: continue
                piecenode = document.createElement('OutfitItem')
                piecenode.setAttribute('Location', piece)
                piecenode.setAttribute('Index', unicode(item[0]))
                piecenode.setAttribute('Equipped', unicode(item[1]))
                outfitnode.appendChild(piecenode)
            rootnode.appendChild(outfitnode)

        return document

    def pieceTabChanged(self, row, col):
        self.currentTabLabel = string.strip(str(self.PieceTab.tabText(row,col)))
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

    def fixupItemLevel(self):
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

        # Make sure the combo doesn't do anything stupid...
        self.ItemNameCombo.blockSignals(True)
        self.ItemNameCombo.clear()
        altitem = item
        while altitem is not None:
            self.ItemNameCombo.addItem(altitem.ItemName)
            altitem = altitem.next
        self.ItemNameCombo.setCurrentIndex(0)
        self.ItemNameCombo.setEditText(item.ItemName)
        self.ItemNameCombo.blockSignals(False)

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
            if self.hideNonClassSkills:
                if len(AllBonusList[self.realm][self.charclass]\
                        ['Focus Hash'].keys()) == 0 and \
                        location not in FocusTabList:
                    typelist.remove('Focus')
            if not gemtype in typelist:
                typelist.append(gemtype)

            typecombo.insertItems(0, typelist)
            typecombo.setCurrentIndex(typelist.index(gemtype))
            self.typeChanged(typelist.index(gemtype), slot)
            gemeffect = str(item.slot(slot).effect())
            effect = self.Effect[slot].findText(gemeffect)
            if len(gemeffect) and effect < 0:
                if itemtype == 'player':
                    self.Effect[slot].addItem(gemeffect)
                    self.Effect[slot].setCurrentIndex(
                                          self.Effect[slot].count() - 1)
                    self.effectChanged(effect, slot)
                else:
                    if not self.Effect[slot].isEditable():
                        self.Effect[slot].setEditable(True)
                    self.Effect[slot].setEditText(gemeffect)
            else:
                self.Effect[slot].setCurrentIndex(effect)
                self.effectChanged(effect, slot)
            if itemtype == 'drop':
                self.AmountEdit[slot].setText(item.slot(slot).amount())
            else:
                gemamount = item.slot(slot).amount()
                amount = self.AmountDrop[slot].findText(gemamount)
                if len(gemamount) and gemamount != "0" and amount < 0:
                    self.AmountDrop[slot].addItem(gemamount)
                    self.AmountDrop[slot].setCurrentIndex(
                                              self.AmountDrop[slot].count() - 1)
                else:
                    self.AmountDrop[slot].setCurrentIndex(amount)
            if itemtype == 'player' and item.slot(slot).slotType() == 'player':
                self.Makes[slot].setValue(int(item.slot(slot).makes()))
            else:
                self.Requirement[slot].setText(item.slot(slot).requirement())
        self.AFDPS_Edit.setText(item.AFDPS)
        self.Speed_Edit.setText(item.Speed)
        self.Bonus_Edit.setText(item.Bonus)
        if itemtype == 'drop':
            self.QualEdit.setText(item.ItemQuality)
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

    def summarize(self):
        charlevel = int(self.CharLevel.text())
        tot = {}
        tot['Cost'] = 0
        tot['Price'] = 0
        tot['Utility'] = 0.0
        tot['Stats'] = {}
        tot['Resists'] = {}
        tot['Skills'] = {}
        tot['Focus'] = {}
        tot['OtherBonuses'] = {}
        tot['PvEBonuses'] = {}
        for effect in DropLists['All']['Stat'] + ('AF', '% Power Pool'):
            tot['Stats'][effect] = {}
            tot['Stats'][effect]['TotalBonus'] = 0
            tot['Stats'][effect]['Bonus'] = 0
            tot['Stats'][effect]['TotalCapBonus'] = 0
            tot['Stats'][effect]['CapBonus'] = 0
            if HighCapBonusList.has_key(effect):
                capcalc = HighCapBonusList[effect]
                capcapcalc = HighCapBonusList[effect + ' Cap']
            else:
                capcalc = HighCapBonusList['Stat']
                capcapcalc = HighCapBonusList['Stat Cap']
            tot['Stats'][effect]['BaseCap'] \
                    = int(charlevel * capcalc[0]) + capcalc[1]
            tot['Stats'][effect]['BaseCapToCapBonus'] \
                    = int(charlevel * capcapcalc[0]) + capcapcalc[1]
        for effect in DropLists['All']['Resist']:
            tot['Resists'][effect] = {}
            tot['Resists'][effect]['TotalBonus'] = 0
            tot['Resists'][effect]['Bonus'] = 0
            race = str(self.CharRace.currentText())
            if Races['All'][race]['Resists'].has_key(effect):
                tot['Resists'][effect]['RacialBonus'] \
                        = Races['All'][race]['Resists'][effect]
            capcalc = HighCapBonusList['Resist']
            tot['Resists'][effect]['BaseCap'] \
                    = int(charlevel * capcalc[0]) + capcalc[1]
        for key, item in self.itemattrlist.iteritems():
            tot['Cost'] += item.cost()
            tot['Price'] += item.price(self.pricingInfo)
            if not item.Equipped == '1':
                continue
            tot['Utility'] += item.utility()
            for i in range(0, item.slotCount()):
                gemtype = item.slot(i).type()
                effect = item.slot(i).effect()
                amount = int('0'+re.sub('[^\d]', '', item.slot(i).amount()))
                if gemtype == 'Skill':
                    effects = [effect,]
                    if effect[0:4] == 'All ':
                        effects.extend(AllBonusList[self.realm] \
                                                   [self.charclass][effect])
                    for effect in effects:
                        if tot['Skills'].has_key(effect):
                            amts = tot['Skills'][effect]
                            amts['TotalBonus'] += amount
                        else:
                            tot['Skills'][effect] = {}
                            amts = tot['Skills'][effect]
                            amts['TotalBonus'] = amount
                            capcalc = HighCapBonusList['Skill']
                            amts['BaseCap'] = int(charlevel * capcalc[0]) \
                                            + capcalc[1]
                        amts['Bonus'] = min(amts['TotalBonus'], amts['BaseCap'])
                elif gemtype == 'Focus':
                    effects = [effect,]
                    if effect[0:4] == 'All ':
                        effects.extend(AllBonusList[self.realm] \
                                                   [self.charclass][effect])
                    for effect in effects:
                        if effect == '': continue
                        if tot['Focus'].has_key(effect):
                            amts = tot['Focus'][effect]
                        else:
                            tot['Focus'][effect] = {}
                            amts = tot['Focus'][effect]
                            capcalc = HighCapBonusList['Focus']
                            amts['BaseCap'] = int(charlevel * capcalc[0]) \
                                            + capcalc[1]
                        amts['TotalBonus'] = amount
                        amts['Bonus'] = min(amts['TotalBonus'], amts['BaseCap'])
                elif gemtype == 'Resist':
                    amts = tot['Resists'][effect]
                    amts['TotalBonus'] += amount
                    amts['Bonus'] = min(amts['TotalBonus'], amts['BaseCap'])
                elif gemtype == 'Stat':
                    effects = [effect,]
                    if effect == 'Acuity':
                        effects.extend(AllBonusList[self.realm] \
                                                   [self.charclass][effect])
                    for effect in effects:
                        amts = tot['Stats'][effect]
                        amts['TotalBonus'] += amount
                        amts['Bonus'] = min(amts['TotalBonus'],
                                            amts['BaseCap'] + amts['CapBonus'])
                elif gemtype == 'Cap Increase':
                    effects = [effect,]
                    # Power cap affects both Power and % Power Pool
                    if effect == 'Power':
                        effects.append('% Power Pool')
                    elif effect == 'Acuity':
                        effects.extend(AllBonusList[self.realm] \
                                                   [self.charclass][effect])
                    for effect in effects:
                        amts = tot['Stats'][effect]
                        amts['TotalCapBonus'] += amount
                        amts['CapBonus'] = min(amts['TotalCapBonus'],
                                               amts['BaseCapToCapBonus'])
                        amts['Bonus'] = min(amts['TotalBonus'],
                                            amts['BaseCap'] + amts['CapBonus'])
                elif gemtype == 'Other Bonus':
                    if effect in ('AF', '% Power Pool',):
                        amts = tot['Stats'][effect]
                        amts['TotalBonus'] += amount
                        amts['Bonus'] = min(amts['TotalBonus'],
                                            amts['BaseCap'] + amts['CapBonus'])
                    elif tot['OtherBonuses'].has_key(effect):
                        amts = tot['OtherBonuses'][effect]
                        amts['TotalBonus'] += amount
                        amts['Bonus'] = min(amts['TotalBonus'], amts['BaseCap'])
                    else:
                        tot['OtherBonuses'][effect] = {}
                        amts = tot['OtherBonuses'][effect]
                        if HighCapBonusList.has_key(effect):
                            capcalc = HighCapBonusList[effect]
                        else:
                            capcalc = HighCapBonusList[gemtype]
                        amts['BaseCap'] = int(charlevel * capcalc[0]) \
                                        + capcalc[1]
                        amts['TotalBonus'] = amount
                        amts['Bonus'] = min(amts['TotalBonus'], amts['BaseCap'])
                elif gemtype == 'PvE Bonus':
                    if tot['PvEBonuses'].has_key(effect):
                        amts = tot['PvEBonuses'][effect]
                        amts['TotalBonus'] += amount
                    else:
                        tot['PvEBonuses'][effect] = {}
                        amts = tot['PvEBonuses'][effect]
                        if HighCapBonusList.has_key(effect):
                            capcalc = HighCapBonusList[effect]
                        else:
                            capcalc = HighCapBonusList[gemtype]
                        amts['BaseCap'] = int(charlevel * capcalc[0]) \
                                        + capcalc[1]
                        amts['TotalBonus'] = amount
                    amts['Bonus'] = min(amts['TotalBonus'], amts['BaseCap'])
        tot['Price'] += self.pricingInfo.get('PPOrder', 0) * 10000
        return tot

    def showStat(self, stat, show):
        if self.StatLabel[stat].isHidden() != show:
            return
        self.StatLabel[stat].setVisible(show)
        self.StatValue[stat].setVisible(show)
        self.StatCap[stat].setVisible(show)

    def calculate(self):
        if self.nocalc:
            return
        errorcount = 0
        self.errorsmenu.clear()
        charleveltext = str(self.CharLevel.text())
        if charleveltext == '': 
            charlevel = 1
        else:
            charlevel = max(min(50, int(charleveltext)), 1)
        self.CharLevel.setText(str(charlevel))
        for key, item in self.itemattrlist.iteritems():
            if item.ActiveState != 'player': continue
            gemeffects = []
            for i in range(0, item.slotCount()):
                slot = item.slot(i)
                if slot.slotType() != 'player': continue
                gemtype = slot.type()
                if gemtype == 'Unused': continue
                effect = slot.effect()
                if [gemtype, effect] in gemeffects:
                    error_act = QAction('Two of same type of gem on %s' \
                                        % key, self)
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
        item = self.itemattrlist[self.currentTabLabel]
        self.ItemUtility.setText('%3.1f' % item.utility())
        if item.ActiveState == 'player':
            imbuevals = item.listGemImbue()
            imbuepts = sum(imbuevals)
            itemimbue = item.itemImbue()
            for i in range(0, item.slotCount()):
                slot = item.slot(i)
                if i < len(imbuevals):
                    self.Cost[i].setText(SC.formatCost(slot.gemCost(1)))
                    self.Points[i].setText('%3.1f' % imbuevals[i])
                if i < len(self.Name):
                    self.Name[i].setText(slot.gemName(self.realm))
            self.ItemImbue.setText('%3.1f' % imbuepts)
            self.ItemImbueTotal.setText(' / ' + unicode(itemimbue))
            self.ItemCost.setText(SC.formatCost(item.cost()))
            self.ItemPrice.setText(SC.formatCost(item.price(self.pricingInfo)))
            if imbuepts >= (itemimbue + 6.0):
                self.ItemOvercharge.setText('Impossible')
                error_act = QAction('Impossible overcharge on %s' % key, self)
                if item.Location in JewelTabList:
                    row = 1
                    col = JewelTabList.index(item.Location)
                else:
                    row = 0
                    col = PieceTabList.index(item.Location)
                error_act.setData(QVariant((row << 8) | col))
                self.errorsmenu.addAction(error_act)
                errorcount = errorcount + 1
            elif imbuepts < (itemimbue + 1.0):
                self.ItemOvercharge.setText('None')
            else:
                success = item.overchargeSuccess(self.crafterSkill)
                if success < 0:
                    self.ItemOvercharge.setText('BOOM! (%d%%)' % success)
                else:
                    self.ItemOvercharge.setText('%d%%' % success)
        tot = self.summarize()
        self.SkillsList.model().removeRows(0,self.SkillsList.model().rowCount())
        for key, amounts in tot['Resists'].iteritems():
            val = amounts['TotalBonus']
            if not self.capDistance:
                if self.includeRacials:
                    if amounts.has_key('RacialBonus'):
                        rr = amounts['RacialBonus']
                        val += rr
                self.StatValue[key].setText(unicode(val))
            else:
                basecap = amounts['BaseCap']
                self.StatValue[key].setText(unicode(basecap - val))
        for (key, datum) in tot['Stats'].iteritems():
            val = datum['TotalBonus']
            acuity = AllBonusList[self.realm][self.charclass]["Acuity"]
            if key == "% Power Pool":
                key = "PowerPool"
            elif key == "Acuity":
                 self.showStat(key, ((datum['TotalCapBonus'] > 0) \
                                  or (val > 0)) and (len(acuity) == 0))
            elif key in ("Charisma", "Empathy", "Intelligence", "Piety"):
                 self.showStat(key, (datum['TotalCapBonus'] > 0) \
                                 or (val > 0) or (key in acuity))
            if not self.capDistance:
                if datum['TotalCapBonus'] > 0:
                    self.StatCap[key].setText( \
                        '('+str(datum['TotalCapBonus'])+')')
                else:
                    self.StatCap[key].setText('-')
                self.StatValue[key].setText(unicode(val))
            else:
                basecap = datum['BaseCap']
                addcap = datum['BaseCapToCapBonus']
                if datum['TotalCapBonus'] > 0:
                    capmod = datum['TotalCapBonus']
                else:
                    capmod = 0
                capcap = addcap - capmod
                if capmod > addcap:  capmod = addcap
                self.StatCap[key].setText('('+unicode(int(capcap))+')')
                self.StatValue[key].setText(unicode(int(basecap + capmod) -val))
        for skillkey, suffix, lookup in (
                ('Skills', '', 'Skill'),
                ('Focus', ' Focus', 'Focus'),
                ('OtherBonuses', '', 'Bonus'),
                ('PvEBonuses', ' (PvE)', 'Bonus')):
            skills = tot[skillkey].keys()
            skills.sort()
            for skill in skills:
                amounts = tot[skillkey][skill]
                if self.capDistance:
                    amount = amounts['BaseCap'] - amounts['TotalBonus']
                else:
                    amount = amounts['TotalBonus']
                self.insertSkill(amount, skill + suffix, lookup)
        self.TotalCost.setText(SC.formatCost(tot['Cost']))
        self.TotalPrice.setText(SC.formatCost(tot['Price']))
        self.TotalUtility.setText('%3.1f' % tot['Utility'])
        self.errorsmenuid.setEnabled(errorcount > 0)
                
    def templateChanged(self,a0=None):
        if self.nocalc: return
        self.modified = 1
        self.calculate()

    def raceChanged(self, a0):
        race = str(self.CharRace.currentText())
        for rt in DropLists['All']['Resist']:
            if Races['All'][race]['Resists'].has_key(rt):
              if self.includeRacials:
                self.StatBonus[rt].setText('('+str(Races['All'][race] \
                                                        ['Resists'][rt])+')')
              else:
                self.StatBonus[rt].setText('+'+str(Races['All'][race] \
                                                        ['Resists'][rt]))
            else:
                self.StatBonus[rt].setText('-')
        if self.nocalc: return
        self.modified = 1
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def charClassChanged(self,a0):
        self.charclass = str(self.CharClass.currentText())
        showrealm = self.realm
        if self.coop:
            showrealm = 'All'
        self.dropeffectlists['Skill'] = DropLists[showrealm]['Skill']
        self.dropeffectlists['Focus'] = DropLists[showrealm]['Focus']
        if self.hideNonClassSkills:
            self.effectlists['Skill'] = AllBonusList['All'][self.charclass] \
                                                    ['All Skills']
            self.effectlists['Focus'] = AllBonusList['All'][self.charclass] \
                                                    ['All Focus']
        else:
            self.effectlists['Skill'] = GemLists[showrealm]['Skill']
            self.effectlists['Focus'] = GemLists[showrealm]['Focus']
        race = str(self.CharRace.currentText())
        self.CharRace.clear()
        racelist = AllBonusList[self.realm][self.charclass]['Races']
        self.CharRace.insertItems(0, list(racelist))
        if race not in racelist:
            race = racelist[0]
        self.CharRace.setCurrentIndex(racelist.index(race))
        self.raceChanged(racelist.index(race))
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def realmChanged(self,a0):
        self.realm = str(self.Realm.currentText())
        self.CharClass.clear()
        self.CharClass.insertItems(0, list(ClassList[self.realm]))
        if self.charclass not in ClassList[self.realm]:
            self.charclass = ClassList[self.realm][0]
        self.CharClass.setCurrentIndex(
                           ClassList[self.realm].index(self.charclass))
        self.charClassChanged(self.CharClass.currentIndex())

    def itemLevelShow(self):
        level = self.ItemLevelWindow.exec_()
        if level != -1:
            self.ItemLevel.setText(str(level))
            self.AFDPS_Edit.setText(str(self.ItemLevelWindow.afdps))

    def itemChanged(self,a0=None):
        if self.nocalc: return
        self.modified = 1
        item = self.itemattrlist[self.currentTabLabel]
        self.fixupItemLevel()
        item.Level = unicode(self.ItemLevel.text())
        item.AFDPS = unicode(self.AFDPS_Edit.text())
        item.Speed = unicode(self.Speed_Edit.text())
        item.Bonus = unicode(self.Bonus_Edit.text())
        if self.Equipped.isChecked():
            item.Equipped = '1'
        else:
            item.Equipped = '0'
        self.outfitlist[self.currentOutfit][self.currentTabLabel] \
                = ( item.TemplateIndex, item.Equipped, )

        if item.ActiveState == 'player':
            item.ItemQuality = unicode(self.QualDrop.currentText())
        else:
            item.ItemQuality = unicode(self.QualEdit.text())
        self.calculate()

    def itemNameSelected(self,a0):
        #sys.stdout.write("Selected Item %d\n" % a0)
        if self.nocalc: return
        if not isinstance(a0, int) or a0 < 1: return
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
        self.outfitlist[self.currentOutfit][self.currentTabLabel] \
                = ( item.TemplateIndex, item.Equipped, )
        # Block any additional signals here until AFTER we
        # execute restoreItem, so subsequent signals get the correct
        # currentIndex which short circuits this routine
        # (see a0 == 0 check above)
        self.ItemNameCombo.blockSignals(True)
        QApplication.postEvent(self, RestoreItemEvent(item))
        # self.restoreItem(item)

    def itemNameEdited(self,a0):
        #sys.stdout.write("Edited Item %d named %s\n" % (self.ItemNameCombo.currentIndex(), a0))
        if self.nocalc: return
        # Ignore side-effect signal textEditChanged() prior to activated()
        if self.ItemNameCombo.currentIndex() != 0: return
        # Don't update as we stumble upon a duplicate name, let them keep editing
        if self.ItemNameCombo.findText(a0) > -1: return
        item = self.itemattrlist[self.currentTabLabel]
        item.ItemName = unicode(self.ItemNameCombo.lineEdit().text())
        # blockSignals will not have the desired effect, save/restore the cursor as they insert
        cursorpos = self.ItemNameCombo.lineEdit().cursorPosition()
        self.ItemNameCombo.setItemText(0,item.ItemName)
        self.ItemNameCombo.lineEdit().setCursorPosition(cursorpos)
        self.modified = 1

    def senderSlot(self):
        index = self.sender().objectName()[-2:]
        if index[0] == '_': index = index[1:]
        return int(index) - 1

    def amountsChanged(self, amount = None, slot = -1):
        if self.nocalc: return
        if slot < 0:
            slot = self.senderSlot()      
        item = self.itemattrlist[self.currentTabLabel]
        if item.ActiveState == 'player':
            item.slot(slot).setAmount(self.AmountDrop[slot].currentText())
        else:
            item.slot(slot).setAmount(self.AmountEdit[slot].text())
        if item.slot(slot).slotType() == 'player':
            item.slot(slot).setMakes(str(self.Makes[slot].value()))
        else:
            item.slot(slot).setRequirement(self.Requirement[slot].text())
        self.modified = 1
        self.calculate()

    def effectChanged(self, value = None, slot = -1):
        if slot < 0:
            slot = self.senderSlot()        
        item = self.itemattrlist[self.currentTabLabel]
        if isinstance(value,int):
            efftext = str(self.Effect[slot].currentText())
        else:
            efftext = str(self.Effect[slot].lineEdit().text())
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
                self.Makes[slot].setValue(0)
                self.Makes[slot].setMaximum(0)
            else:
                self.Requirement[slot].setText("")
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
                    elif valueslist.has_key(None):
                        valueslist = valueslist[None]
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
                self.Makes[slot].setMaximum(99)
        # Cascade the changes
        self.amountsChanged(0, slot)

    def updateTypeList(self, slot):
        item = self.itemattrlist[self.currentTabLabel]
        itemtype = item.ActiveState
        location = item.Location
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
        if self.hideNonClassSkills:
            if len(AllBonusList[self.realm][self.charclass]\
                    ['Focus Hash'].keys()) == 0 and \
                    location not in FocusTabList:
                typelist.remove('Focus')
        if not gemtype in typelist:
            typelist.append(gemtype)

        typecombo.insertItems(0, typelist)
        typecombo.setCurrentIndex(typelist.index(gemtype))

    def typeChanged(self, Value = None, slot = -1):
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
        self.effectChanged(0, slot)
        self.testCraftingMenu()
    
        QApplication.postEvent(self, UpdateTypeListEvent(slot))
        
    def clearCurrentItem(self):
        self.itemattrlist[self.currentTabLabel].clear()
        #item = Item(realm=self.realm,loc=self.currentTabLabel,
        #            state=self.itemattrlist[self.currentTabLabel].ActiveState,
        #            idx=self.itemIndex)
        #if item.ActiveState == 'drop':
        #    item.ItemName = "Drop Item" + str(self.itemnumbering)
        #else:
        #    item.ItemName = "Crafted Item" + str(self.itemnumbering)
        #self.itemattrlist[self.currentTabLabel] = item
        #self.itemIndex += 1
        #self.itemnumbering += 1
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
        itemdir = QFileDialog.getExistingDirectory(self, 
                      'Select Item Database Path', self.ItemPath)
        if itemdir:
            self.ItemPath = os.path.abspath(unicode(itemdir))
            ret = QMessageBox.question(self, 'Create Database Directories?', 
                                       "Create realm and item slot directories"\
                                     + " underneath %s ?" % itemdir, 
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
        itemname = string.replace(unicode(self.ItemNameCombo.currentText()),
                                  ' ', '_')
        if itemname == '':
            QMessageBox.critical(self, 'Error!', 
                'Cannot save item - You must specify a name!', 'OK')
            return
        item = self.itemattrlist[self.currentTabLabel]

        item.Realm = self.realm

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
                        recentdir.append(os.path.join(self.ItemPath, realm,ext))
            recentdir.append(os.path.join(self.ItemPath, "All", ext))
        filename = os.path.join(itemdir, itemname)
        filename = QFileDialog.getSaveFileName(self, "Save Item", filename, 
                                   "Templates (*.xml);;All Files (*.*)")
        filename = unicode(filename)
        if filename != '':
            item.save(filename)

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
                        recentdir.append(os.path.join(self.ItemPath, realm,ext))
            recentdir.append(os.path.join(self.ItemPath, "All", ext))
        elif os.path.exists(os.path.join(itemdir, 'All', ext)):
            itemdir = os.path.join(self.ItemPath, 'All', ext)
        Qfd = ItemList.ItemListDialog(self, "Load Item", itemdir, extstr, 
                                      self.realm, self.charclass)
        Qfd.setHistory(recentdir)
        if Qfd.exec_():
            if Qfd.selectedFiles().count() > 0:
                filename = unicode(Qfd.selectedFiles()[0])
                item = Item('drop', self.currentTabLabel, self.realm,
                    self.itemIndex)
                if item.load(filename,str(self.itemnumbering)) == -1: return
                if string.lower(item.Realm) != string.lower(self.realm)\
                    and string.lower(item.Realm) != 'all'\
                    and not self.coop:
                    QMessageBox.critical(None, 'Error!',
                                         'You are trying to load an ' \
                                       + 'item for another realm!', 'OK')
                    return
                self.itemIndex += 1
                self.itemnumbering += 1
                if item.next:
                    item.next.TemplateIndex = self.itemIndex
                    self.itemIndex += 1
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
                                      QMessageBox.Yes, QMessageBox.No,
                                      QMessageBox.Cancel)
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
                f.write(XMLHelper.writexml(self.asXML(), UnicodeStringIO(),
                                           '', '\t', '\n'))
                f.close()
                self.modified = 0
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + self.filename, 'OK')

    def saveAsFile(self):
        filename = self.filename
        if filename is None:
            filename = os.path.join(self.TemplatePath,
                                    str(self.CharName.text()) + "_template.xml")
        filename = unicode(filename)
        filename = QFileDialog.getSaveFileName(self, "Save Template", filename, 
                                   "Templates (*.xml);;All Files (*.*)")
        filename = unicode(filename)
        if filename != '':
            if filename[-4:] != '.xml':
                filename += '.xml'
            try:
                f = open(filename, 'w')
                f.write(XMLHelper.writexml(self.asXML(), UnicodeStringIO(),
                                           '', '\t', '\n'))
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
            self.setWindowTitle(filetitle +" - Kort's Spellcrafting Calculator")
            
    def exportAsFile(self):
        filename = os.path.join(self.ReportPath, str(self.CharName.text()) \
                                               + "_report.xml")
        filename = unicode(filename)
        filename = QFileDialog.getSaveFileName(self, "Save SCTemplate XML", 
                       filename, "SCTemplates (*_report.xml);;All Files (*.*)")
        filename = unicode(filename)
        if filename != '':
            if filename[-4:] != '.xml':
                filename += '.xml'
            try:
                f = open(filename, 'w')
                f.write(XMLHelper.writexml(self.asXML(True), UnicodeStringIO(),
                        '', '\t', '\n'))
                f.close()
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + filename, 'OK')
                return
            self.ReportPath = os.path.dirname(os.path.abspath(filename))
            
    def openFile(self, *args):
        if self.modified:
            ret = QMessageBox.warning(self, 'Save Changes?', 
                                      "This template has been changed.\n"
                                      "Do you want to save these changes?", 
                                      QMessageBox.Yes, QMessageBox.No,
                                      QMessageBox.Cancel)
            if ret == QMessageBox.Cancel: return
            if ret == QMessageBox.Yes:
                self.saveFile()
                if self.modified: return
        if len(args) == 0:
            filename = QFileDialog.getOpenFileName(self, "Open Template",
                            self.TemplatePath, 
                            "Templates (*.xml);;All Files (*.*)")
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
            self.setWindowTitle(filetitle +" - Kort's Spellcrafting Calculator")

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
        self.OutfitName.clear()
        racename = ''
        classname = ''
        self.outfitlist = []
        self.outfitnumbering = 1
        self.currentOutfit = 0
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
                if newItem.TemplateIndex == -1:
                    newItem.TemplateIndex = self.itemIndex
                    self.itemIndex += 1
                else:
                    self.itemIndex = max(newItem.TemplateIndex + 1, self.itemIndex)
                if newItem.next:
                    if newItem.next.TemplateIndex == -1:
                        newItem.next.TemplateIndex = self.itemIndex
                        self.itemIndex += 1
                    else:
                        self.itemIndex = max(newItem.next.TemplateIndex + 1, self.itemIndex)

                self.itemnumbering += 1
                if self.itemattrlist[newItem.Location] \
                      == itemdefault[newItem.Location]:
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
            elif child.tagName == 'Outfit':
                if child.nodeType == Node.TEXT_NODE: continue
                self.outfitnumbering += 1
                outfitname = child.getAttribute('Name')
                active = child.getAttribute('Active')
                self.outfitlist.append( { None : outfitname } )
                if active == "1": self.currentOutfit = len(self.outfitlist) - 1
                for piecenode in child.childNodes:
                    if piecenode.nodeType == Node.TEXT_NODE: continue
                    piecename = piecenode.getAttribute('Location')
                    index = int(piecenode.getAttribute('Index'))
                    equipped = int(piecenode.getAttribute('Equipped'))
                    self.outfitlist[-1][piecename] = ( index, equipped, )

        self.Realm.setCurrentIndex(Realms.index(self.realm))
        self.realmChanged(Realms.index(self.realm))
        if AllBonusList[self.realm].has_key(self.charclass):
            self.CharClass.setCurrentIndex(
                               ClassList[self.realm].index(self.charclass))
            self.charClassChanged(ClassList[self.realm].index(self.charclass))
        if racename in AllBonusList[self.realm][self.charclass]['Races']:
            self.CharRace.setCurrentIndex(
                              AllBonusList[self.realm][self.charclass] \
                                                      ['Races'].index(racename))
            self.raceChanged('')

        if len(self.outfitlist) < 1:
            self.appendOutfit()
        else:
            self.OutfitName.blockSignals(True)
            for outfit in self.outfitlist:
                self.OutfitName.addItem(outfit[None])
            self.OutfitName.setCurrentIndex(self.currentOutfit)
            self.OutfitName.blockSignals(False)
            self.outfitNameSelected(self.currentOutfit)

        self.deleteOutfitAction.setEnabled(len(self.outfitlist) > 1)
        self.modified = 0
        self.nocalc = 0
        self.restoreItem(self.itemattrlist[self.currentTabLabel])
        
    def chooseXMLUIFile(self):
        filters = "UI XML Templates (*.xsl *.xslt);;All Files (*.*)"
        filename = QFileDialog.getOpenFileName(self, "Choose UI Window Format",
                       self.ReportPath, filters)
        filename = unicode(filename)
        if filename is not None and str(filename) != '':
            self.UiReportFile = os.path.abspath(filename)
            #if templates are in one path, do we really want to
            #assume the report files would be saved to the same?
            #
            #self.ReportPath = os.path.dirname(self.UiReportFile)

    def generateUIXML(self):
        UIXML.uixml(self, self.UiReportFile)
   
    def loadRecentFile(self, action):
        index = action.data().toInt()[0]
        self.openFile(self.recentFiles[index], True)

    def openOptions(self):
        self.nocalc = 1
        self.saveOptions()
        res = Options.Options(self).exec_()
        if res == 1:
            self.loadOptions()
            self.showcapmenuid.setChecked(self.capDistance)
            self.realmChanged(self.Realm.currentIndex())
            self.modified = 1
            self.nocalc = 0
            self.restoreItem(self.itemattrlist[self.currentTabLabel])
        else:
            self.nocalc = 0
            self.calculate()

    def openCraftWindow(self):
        CW = CraftWindow.CraftWindow(self, '', 1)
        CW.loadgems(list(self.itemattrlist[self.currentTabLabel].slots()))
        CW.exec_()
        self.restoreItem(self.itemattrlist[self.currentTabLabel])
        self.modified = 1

    def gemClicked(self, item, slot):
        #RW = ReportWindow.ReportWindow(self, '', True)
        #RW.setWindowTitle('Materials')
        #RW.materialsReport({item: self.itemattrlist[item]}, slot)
        #RW.exec_()
        CW = CraftWindow.CraftWindow(self, '', 1)
        CW.loadgems([self.itemattrlist[self.currentTabLabel].slot(slot - 1)],)
        CW.exec_()
        self.restoreItem(self.itemattrlist[self.currentTabLabel])
        self.modified = 1
    
    def openMaterialsReport(self):
        RW = ReportWindow.ReportWindow(self, '', 1)
        RW.materialsReport(self.itemattrlist)
        RW.exec_()

    def openConfigReport(self):
        RW = ReportWindow.ReportWindow(self, '', 1)
        RW.parseConfigReport(self.ReportFile, self.asXML(True))
        RW.exec_()

    def chooseReportFile(self):
        filters = "Report Templates (*.xsl *.xslt);;All Files (*.*)"
        filename = QFileDialog.getOpenFileName(self, "Choose Report Format",
                       self.ReportPath, filters)
        filename = unicode(filename)
        if filename is not None and str(filename) != '':
            self.ReportFile = os.path.abspath(filename)
            #if templates are in one path, would we really want to
            #assume the report files will be saved to the same?
            #
            #self.ReportPath = os.path.dirname(self.ReportFile)

    def openCraftBars(self):
        CB = CraftBar.CraftBar(self, '', 1)
        CB.exec_()

    def delveItemsDialog(self, find, findtype = None):
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
                       if not find in AllBonusList[self.realm] \
                                                  [self.charclass][effect]:
                           continue
                    elif (slottype == 'Skill' or slottype == 'Focus') \
                            and effect[0:4] == 'All ' \
                            and effect in AllBonusList[self.realm]\
                                                      [self.charclass].keys():
                        if not find in AllBonusList[self.realm] \
                                                   [self.charclass][effect]:
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

    def mousePressEvent(self, e):
        if e is None: return
        child = self.childAt(e.pos())
        if child is None: return
        if not isinstance(child, QLabel): return
        if str(child.text()) == '': return
        shortname = str(child.objectName())
        nameidx = 2
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
           self.delveItemsDialog(shortname, 'Resist')
        else:
           self.delveItemsDialog(shortname)

    def skillClicked(self,index):
        effect = str(index.data(Qt.DisplayRole).toString())
        bonus = str(index.data(Qt.UserRole).toString())
        if effect[-6:] == ' (PvE)' or effect[-6:] == ' Focus':
            effect = effect[:-6]
        amount, effect = string.split(effect.lstrip(), ' ', 1)
        self.delveItemsDialog(effect, bonus)

    def showCap(self):
        self.capDistance = not self.capDistance
        self.showcapmenuid.setChecked(self.capDistance)
        ScOptions.instance().setOption('DistanceToCap', self.capDistance)
        self.calculate()

    def swapWith(self, action):
        cur = self.itemattrlist[self.currentTabLabel]
        if cur.ActiveState != 'player': return
        piece = str(action.text())
        part = self.itemattrlist[piece]
        if cur == part: return
        prev = None
        while part.ActiveState != 'player':
            if part.next is None: 
                QMessageBox.critical(None, 'Error!', 'There is no crafted ' \
                    + piece + ' to swap gems with.  Create a new crafted ' \
                    + piece + ' and try again.', 'OK')
                return
            prev = part
            part = part.next
        if prev is not None:
            if self.itemattrlist[piece].Equipped == '1':
                self.itemattrlist[piece] = '0'
                part.Equipped = '1'
            prev.next = part.next
            part.next = self.itemattrlist[piece]
            self.itemattrlist[piece] = part
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
                item.slot(4).setType('Unused')
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
            item = Item('drop', self.currentTabLabel, self.realm, self.itemIndex)
            item.ItemName = "Drop Item" + str(self.itemnumbering)
        else:
            item = Item('player', self.currentTabLabel, self.realm, self.itemIndex)
            item.ItemName = "Crafted Item" + str(self.itemnumbering)
        self.itemIndex += 1
        self.itemnumbering += 1
        item.next = self.itemattrlist[self.currentTabLabel]
        self.itemattrlist[self.currentTabLabel] = item
        self.outfitlist[self.currentOutfit][self.currentTabLabel] \
                  = ( item.TemplateIndex, item.Equipped, )
        if newtype == 'Drop Item' or newtype == 'Normal Item':
            self.restoreItem(item)
        else:
            self.chooseItemType(action)

    def viewToolbar(self, action):
        view = action.data().toInt()[0]
        for act in self.viewtoolbarmenu.actions():
            if act.data().toInt()[0] == view:
                if not act.isChecked():
                    act.setChecked(True)
                    return
            else:
                if act.isChecked():
                    act.setChecked(False)
        if view == 0:
            self.toolbar.hide()
        else:
            self.setIconSize(QSize(view,view))
            self.toolbar.show()

    def appendOutfit(self):
        outfitname = 'Outfit%d' % self.outfitnumbering
        self.outfitnumbering += 1

        self.outfitlist.append( { None: outfitname } )
        idx = len(self.outfitlist) - 1

        self.currentOutfit = idx
        if idx != -1 and idx < len(self.outfitlist):
            for key, item in self.itemattrlist.iteritems():
                self.outfitlist[idx][key] = ( item.TemplateIndex, item.Equipped )
        self.OutfitName.blockSignals(True)
        self.OutfitName.addItem(outfitname)
        self.OutfitName.blockSignals(False)

    def newOutfit(self):
        f = QApplication.focusWidget()
        if f is not None: f.setFocus()
        self.appendOutfit()
        #sys.stdout.write("Created Outfit %d\n" % idx)
        self.OutfitName.setCurrentIndex(self.currentOutfit)
        if len(self.outfitlist) > 1:
            self.deleteOutfitAction.setEnabled(True)
        self.modified = 1

    def deleteOutfit(self):
        if self.currentOutfit < 0 or len(self.outfitlist) < 2: return
        #sys.stdout.write("Deleted Outfit %d\n" % self.currentOutfit)
        outfit = self.currentOutfit
        self.currentOutfit = 0
        del self.outfitlist[outfit]
        self.OutfitName.blockSignals(True)
        self.OutfitName.removeItem(outfit)
        self.OutfitName.setCurrentIndex(self.currentOutfit)
        self.OutfitName.blockSignals(False)
        self.modified = 1
        if len(self.outfitlist) < 2:
            self.deleteOutfitAction.setEnabled(False)
        self.outfitNameSelected(self.currentOutfit)

    def outfitNameSelected(self, idx):
        if not isinstance(idx, int): return
        if self.currentOutfit == idx: return
        #sys.stdout.write("Selected Outfit %d\n" % idx)
        self.currentOutfit = idx
        outfit = self.outfitlist[idx]
        for piece, indexes in outfit.iteritems():
            if piece is None: continue
            item = self.itemattrlist[piece]
            prev = None
            while item and item.TemplateIndex != indexes[0]:
                prev = item
                item = item.next
            if item: 
                if prev:
                    prev.next = prev.next.next
                    item.next = self.itemattrlist[piece]
                    self.itemattrlist[piece].Equipped = '0'
                    self.itemattrlist[piece] = item
                self.itemattrlist[piece].Equipped = indexes[1]
            else:
                self.outfitlist[idx][piece] = ( self.itemattrlist[piece].TemplateIndex, 
                                                self.itemattrlist[piece].Equipped, )
        if self.nocalc: return
        self.restoreItem(self.itemattrlist[self.currentTabLabel])

    def outfitNameEdited(self, a0=None):
        idx = self.currentOutfit
        # Ignore side-effect signal textEditChanged() prior to activated()
        if idx != self.OutfitName.currentIndex(): return
        # Don't update as we stumble upon a duplicate name, let them keep editing
        if self.OutfitName.findText(a0) > -1: return
        #sys.stdout.write("Edited Outfit %d named %s\n" % (idx, a0))
        outfitname = unicode(self.OutfitName.currentText())
        self.outfitlist[idx][None] = outfitname
        # blockSignals will not have the desired effect, save/restore the cursor as they insert
        cursorpos = self.OutfitName.lineEdit().cursorPosition()
        self.OutfitName.setItemText(idx, outfitname)
        self.OutfitName.lineEdit().setCursorPosition(cursorpos)
        self.modified = 1

    def aboutBox(self):
        splash = AboutScreen(parent=self,modal=True)
        splash.exec_()

    def ignoreMouseEvent(self, e):
        e.ignore()

    def resizeEvent(self, e):
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            self.sizegrip.move(self.width() - 15, self.height() - 15)

    def event(self, e):
        if e.type() == UserEventIDUpdateTypeList:
            self.updateTypeList(e.slot)
            return True
        elif e.type() == UserEventIDRestoreItem:
            #sys.stdout.write("Restoring Item\n")
            self.restoreItem(e.item)
            # Unblock any signals we may have blocked in itemNameSelected()
            self.ItemNameCombo.blockSignals(False)
            return True
        else:
            return QMainWindow.event(self, e)

if __name__ == '__main__':
    app = QApplication([])
    scw = ScWindow()

