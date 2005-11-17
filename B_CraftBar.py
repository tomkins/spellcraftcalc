# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CraftBar.ui'
#
# Created: Wed Nov 16 21:38:32 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.15
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_CraftBar(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("B_CraftBar")



        self.TextLabel1 = QLabel(self,"TextLabel1")
        self.TextLabel1.setGeometry(QRect(22,17,103,16))

        self.PathSelectButton = QPushButton(self,"PathSelectButton")
        self.PathSelectButton.setGeometry(QRect(425,13,28,26))

        self.TextLabel2 = QLabel(self,"TextLabel2")
        self.TextLabel2.setGeometry(QRect(174,39,191,16))

        self.DaocPath = QLineEdit(self,"DaocPath")
        self.DaocPath.setGeometry(QRect(129,14,295,22))

        self.GroupBox20 = QGroupBox(self,"GroupBox20")
        self.GroupBox20.setGeometry(QRect(10,57,217,243))

        self.TextLabel4 = QLabel(self.GroupBox20,"TextLabel4")
        self.TextLabel4.setGeometry(QRect(38,20,134,16))

        self.CharList = QListView(self.GroupBox20,"CharList")
        self.CharList.addColumn(self.__tr("Char Name"))
        self.CharList.addColumn(self.__tr("Server"))
        self.CharList.setGeometry(QRect(5,44,205,193))

        self.TextLabel14 = QLabel(self,"TextLabel14")
        self.TextLabel14.setGeometry(QRect(39,304,154,41))
        self.TextLabel14.setAlignment(QLabel.AlignTop | QLabel.AlignLeft)

        self.GroupBox21 = QGroupBox(self,"GroupBox21")
        self.GroupBox21.setGeometry(QRect(229,274,261,143))

        self.TextLabel9 = QLabel(self.GroupBox21,"TextLabel9")
        self.TextLabel9.setGeometry(QRect(5,6,250,134))
        self.TextLabel9.setAlignment(QLabel.AlignTop | QLabel.AlignLeft)

        self.GroupBox19 = QGroupBox(self,"GroupBox19")
        self.GroupBox19.setGeometry(QRect(254,57,213,189))

        self.TextLabel1_2 = QLabel(self.GroupBox19,"TextLabel1_2")
        self.TextLabel1_2.setGeometry(QRect(69,9,73,16))

        self.HotbarNum = QSpinBox(self.GroupBox19,"HotbarNum")
        self.HotbarNum.setGeometry(QRect(145,103,54,21))
        self.HotbarNum.setMaxValue(30)
        self.HotbarNum.setMinValue(1)

        self.TextLabel10 = QLabel(self.GroupBox19,"TextLabel10")
        self.TextLabel10.setGeometry(QRect(12,152,59,13))

        self.NumGems = QLabel(self.GroupBox19,"NumGems")
        self.NumGems.setGeometry(QRect(164,168,28,16))

        self.EndPos = QLabel(self.GroupBox19,"EndPos")
        self.EndPos.setGeometry(QRect(139,150,26,16))
        self.EndPos.setAlignment(QLabel.AlignVCenter | QLabel.AlignLeft)

        self.EndBar = QLabel(self.GroupBox19,"EndBar")
        self.EndBar.setGeometry(QRect(73,150,22,16))

        self.TextLabel15 = QLabel(self.GroupBox19,"TextLabel15")
        self.TextLabel15.setGeometry(QRect(11,168,152,16))
        self.TextLabel15.setAlignment(QLabel.AlignVCenter | QLabel.AlignLeft)

        self.TextLabel8 = QLabel(self.GroupBox19,"TextLabel8")
        self.TextLabel8.setGeometry(QRect(5,129,132,16))
        self.TextLabel8.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel7 = QLabel(self.GroupBox19,"TextLabel7")
        self.TextLabel7.setGeometry(QRect(40,105,97,16))
        self.TextLabel7.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.HotbarPos = QSpinBox(self.GroupBox19,"HotbarPos")
        self.HotbarPos.setGeometry(QRect(145,127,54,21))
        self.HotbarPos.setMaxValue(10)
        self.HotbarPos.setMinValue(1)

        self.TextLabel11 = QLabel(self.GroupBox19,"TextLabel11")
        self.TextLabel11.setGeometry(QRect(94,150,44,16))

        self.ArmsSelect = QCheckBox(self.GroupBox19,"ArmsSelect")
        self.ArmsSelect.setGeometry(QRect(9,47,47,17))

        self.HeadSelect = QCheckBox(self.GroupBox19,"HeadSelect")
        self.HeadSelect.setGeometry(QRect(9,66,50,17))

        self.LegsSelect = QCheckBox(self.GroupBox19,"LegsSelect")
        self.LegsSelect.setGeometry(QRect(68,28,49,17))

        self.HandsSelect = QCheckBox(self.GroupBox19,"HandsSelect")
        self.HandsSelect.setGeometry(QRect(68,47,54,17))

        self.FeetSelect = QCheckBox(self.GroupBox19,"FeetSelect")
        self.FeetSelect.setGeometry(QRect(68,66,45,17))

        self.RangedSelect = QCheckBox(self.GroupBox19,"RangedSelect")
        self.RangedSelect.setGeometry(QRect(68,85,64,17))

        self.RHSelect = QCheckBox(self.GroupBox19,"RHSelect")
        self.RHSelect.setGeometry(QRect(124,28,78,17))

        self.LHSelect = QCheckBox(self.GroupBox19,"LHSelect")
        self.LHSelect.setGeometry(QRect(124,47,84,17))

        self.THSelect = QCheckBox(self.GroupBox19,"THSelect")
        self.THSelect.setGeometry(QRect(124,66,71,17))

        self.ChestSelect = QCheckBox(self.GroupBox19,"ChestSelect")
        self.ChestSelect.setGeometry(QRect(9,28,50,17))

        self.LoadGemsButton = QPushButton(self,"LoadGemsButton")
        self.LoadGemsButton.setGeometry(QRect(311,246,99,26))

        self.PushButton19 = QPushButton(self,"PushButton19")
        self.PushButton19.setGeometry(QRect(198,422,99,26))

        self.languageChange()

        self.resize(QSize(490,451).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.PathSelectButton,SIGNAL("clicked()"),self.openFileDialog)
        self.connect(self.PushButton19,SIGNAL("clicked()"),self.accept)
        self.connect(self.LoadGemsButton,SIGNAL("clicked()"),self.loadGems)
        self.connect(self.DaocPath,SIGNAL("textChanged(const QString&)"),self.findPath)
        self.connect(self.HotbarNum,SIGNAL("valueChanged(int)"),self.hotbarNumChanged)
        self.connect(self.HotbarPos,SIGNAL("valueChanged(int)"),self.hotbarPosChanged)
        self.connect(self.ChestSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.ArmsSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.HeadSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.LegsSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.HandsSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.FeetSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.RangedSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.RHSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.LHSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.THSelect,SIGNAL("clicked()"),self.PieceBoxChanged)


    def languageChange(self):
        self.setCaption(self.__tr("Craft Bar Setup"))
        self.TextLabel1.setText(self.__tr("Path to DAoC Folder:"))
        self.PathSelectButton.setText(self.__tr("..."))
        self.TextLabel2.setText(self.__tr("(i.e. C:\\Mythic\\[Atlantis, Camelot, Isles])"))
        self.GroupBox20.setTitle(self.__tr("Character"))
        self.TextLabel4.setText(self.__tr("Select Character to Modify:"))
        self.CharList.header().setLabel(0,self.__tr("Char Name"))
        self.CharList.header().setLabel(1,self.__tr("Server"))
        self.TextLabel14.setText(self.__tr("You must be logged out of \n"
"the selected character for \n"
"the changes to be made"))
        self.GroupBox21.setTitle(QString.null)
        self.TextLabel9.setText(self.__tr("This dialog lets you automatically set up hotbars for \n"
"crafting gems. It takes all \"non-finished\" gems and \n"
"places them in order on your hotbars starting at the \n"
"bar and position you specify. It will place all the gems \n"
"consecutively, so make sure you do not have \n"
"anything on your bars in that range. If you do not \n"
"leave enough space, it will error w/o changing your \n"
"bars. A backup copy of your character will be saved \n"
"in [charname]_bak-[server].ini in your DAoC folder.\n"
"Removing the _bak will restore your settings."))
        self.GroupBox19.setTitle(self.__tr("Hotbar"))
        self.TextLabel1_2.setText(self.__tr("Gems to Load:"))
        self.TextLabel10.setText(self.__tr("Ending Bar:"))
        self.NumGems.setText(self.__tr("0"))
        self.EndPos.setText(self.__tr("0"))
        self.EndBar.setText(self.__tr("0"))
        self.TextLabel15.setText(self.__tr("Total Number of Gems to Load:"))
        self.TextLabel8.setText(self.__tr("Hotbar Position to Start At:"))
        self.TextLabel7.setText(self.__tr("Hotbar # to Start At:"))
        self.TextLabel11.setText(self.__tr("Position:"))
        self.ArmsSelect.setText(self.__tr("Arms"))
        self.HeadSelect.setText(self.__tr("Head"))
        self.LegsSelect.setText(self.__tr("Legs"))
        self.HandsSelect.setText(self.__tr("Hands"))
        self.FeetSelect.setText(self.__tr("Feet"))
        self.RangedSelect.setText(self.__tr("Ranged"))
        self.RHSelect.setText(self.__tr("Right Hand"))
        self.LHSelect.setText(self.__tr("Left Hand"))
        self.THSelect.setText(self.__tr("2 Handed"))
        self.ChestSelect.setText(self.__tr("Chest"))
        self.LoadGemsButton.setText(self.__tr("Load Gems"))
        self.PushButton19.setText(self.__tr("Close"))


    def findPath(self,a0):
        print "B_CraftBar.findPath(const QString&): Not implemented yet"

    def hotbarNumChanged(self,a0):
        print "B_CraftBar.hotbarNumChanged(int): Not implemented yet"

    def hotbarPosChanged(self,a0):
        print "B_CraftBar.hotbarPosChanged(int): Not implemented yet"

    def loadGems(self):
        print "B_CraftBar.loadGems(): Not implemented yet"

    def PieceBoxChanged(self):
        print "B_CraftBar.PieceBoxChanged(): Not implemented yet"

    def openFileDialog(self):
        print "B_CraftBar.openFileDialog(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("B_CraftBar",s,c)
