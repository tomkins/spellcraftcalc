# Form implementation generated from reading ui file 'CraftBar.ui'
#
# Created: Sun Apr 4 17:55:23 2004
#      by: The Python User Interface Compiler (pyuic) 3.8
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_CraftBar(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if name == None:
            self.setName('B_CraftBar')

        self.resize(490,451)
        self.setCaption(self.tr("Craft Bar Setup"))

        self.TextLabel1 = QLabel(self,'TextLabel1')
        self.TextLabel1.setGeometry(QRect(22,17,103,16))
        self.TextLabel1.setText(self.tr("Path to DAoC Folder:"))

        self.PathSelectButton = QPushButton(self,'PathSelectButton')
        self.PathSelectButton.setGeometry(QRect(425,13,28,26))
        self.PathSelectButton.setText(self.tr("..."))

        self.TextLabel2 = QLabel(self,'TextLabel2')
        self.TextLabel2.setGeometry(QRect(174,39,191,16))
        self.TextLabel2.setText(self.tr("(i.e. C:\\Mythic\\[Atlantis, Camelot, Isles])"))

        self.DaocPath = QLineEdit(self,'DaocPath')
        self.DaocPath.setGeometry(QRect(129,14,295,22))

        self.GroupBox20 = QGroupBox(self,'GroupBox20')
        self.GroupBox20.setGeometry(QRect(10,57,217,243))
        self.GroupBox20.setTitle(self.tr("Character"))

        self.TextLabel4 = QLabel(self.GroupBox20,'TextLabel4')
        self.TextLabel4.setGeometry(QRect(38,20,134,16))
        self.TextLabel4.setText(self.tr("Select Character to Modify:"))

        self.CharList = QListView(self.GroupBox20,'CharList')
        self.CharList.addColumn(self.tr("Char Name"))
        self.CharList.addColumn(self.tr("Server"))
        self.CharList.setGeometry(QRect(5,44,205,193))

        self.TextLabel14 = QLabel(self,'TextLabel14')
        self.TextLabel14.setGeometry(QRect(39,304,154,41))
        TextLabel14_font = QFont(self.TextLabel14.font())
        TextLabel14_font.setPointSize(9)
        TextLabel14_font.setBold(1)
        self.TextLabel14.setFont(TextLabel14_font)
        self.TextLabel14.setText(self.tr("You must be logged out of \n"
"the selected character for \n"
"the changes to be made"))
        self.TextLabel14.setAlignment(QLabel.AlignTop | QLabel.AlignLeft)

        self.GroupBox21 = QGroupBox(self,'GroupBox21')
        self.GroupBox21.setGeometry(QRect(229,274,261,143))
        self.GroupBox21.setTitle(self.tr(""))

        self.TextLabel9 = QLabel(self.GroupBox21,'TextLabel9')
        self.TextLabel9.setGeometry(QRect(5,6,250,134))
        self.TextLabel9.setText(self.tr("This dialog lets you automatically set up hotbars for \n"
"crafting gems. It takes all \"non-finished\" gems and \n"
"places them in order on your hotbars starting at the \n"
"bar and position you specify. It will place all the gems \n"
"consecutively, so make sure you do not have \n"
"anything on your bars in that range. If you do not \n"
"leave enough space, it will error w/o changing your \n"
"bars. A backup copy of your character will be saved \n"
"in [charname]_bak-[server].ini in your DAoC folder.\n"
"Removing the _bak will restore your settings."))
        self.TextLabel9.setAlignment(QLabel.AlignTop | QLabel.AlignLeft)

        self.GroupBox19 = QGroupBox(self,'GroupBox19')
        self.GroupBox19.setGeometry(QRect(254,57,213,189))
        self.GroupBox19.setTitle(self.tr("Hotbar"))

        self.TextLabel1_2 = QLabel(self.GroupBox19,'TextLabel1_2')
        self.TextLabel1_2.setGeometry(QRect(69,9,73,16))
        self.TextLabel1_2.setText(self.tr("Gems to Load:"))

        self.HotbarNum = QSpinBox(self.GroupBox19,'HotbarNum')
        self.HotbarNum.setGeometry(QRect(145,103,54,21))
        self.HotbarNum.setMaxValue(10)
        self.HotbarNum.setMinValue(1)

        self.TextLabel10 = QLabel(self.GroupBox19,'TextLabel10')
        self.TextLabel10.setGeometry(QRect(12,152,59,13))
        self.TextLabel10.setText(self.tr("Ending Bar:"))

        self.NumGems = QLabel(self.GroupBox19,'NumGems')
        self.NumGems.setGeometry(QRect(164,168,28,16))
        self.NumGems.setText(self.tr("0"))

        self.EndPos = QLabel(self.GroupBox19,'EndPos')
        self.EndPos.setGeometry(QRect(139,150,26,16))
        self.EndPos.setText(self.tr("0"))
        self.EndPos.setAlignment(QLabel.AlignVCenter | QLabel.AlignLeft)

        self.EndBar = QLabel(self.GroupBox19,'EndBar')
        self.EndBar.setGeometry(QRect(73,150,22,16))
        self.EndBar.setText(self.tr("0"))

        self.TextLabel15 = QLabel(self.GroupBox19,'TextLabel15')
        self.TextLabel15.setGeometry(QRect(11,168,152,16))
        self.TextLabel15.setText(self.tr("Total Number of Gems to Load:"))
        self.TextLabel15.setAlignment(QLabel.AlignVCenter | QLabel.AlignLeft)

        self.TextLabel8 = QLabel(self.GroupBox19,'TextLabel8')
        self.TextLabel8.setGeometry(QRect(5,129,132,16))
        self.TextLabel8.setText(self.tr("Hotbar Position to Start At:"))
        self.TextLabel8.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel7 = QLabel(self.GroupBox19,'TextLabel7')
        self.TextLabel7.setGeometry(QRect(40,105,97,16))
        self.TextLabel7.setText(self.tr("Hotbar # to Start At:"))
        self.TextLabel7.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.HotbarPos = QSpinBox(self.GroupBox19,'HotbarPos')
        self.HotbarPos.setGeometry(QRect(145,127,54,21))
        self.HotbarPos.setMaxValue(10)
        self.HotbarPos.setMinValue(1)

        self.TextLabel11 = QLabel(self.GroupBox19,'TextLabel11')
        self.TextLabel11.setGeometry(QRect(94,150,44,16))
        self.TextLabel11.setText(self.tr("Position:"))

        self.ArmsSelect = QCheckBox(self.GroupBox19,'ArmsSelect')
        self.ArmsSelect.setGeometry(QRect(9,47,47,17))
        self.ArmsSelect.setText(self.tr("Arms"))

        self.HeadSelect = QCheckBox(self.GroupBox19,'HeadSelect')
        self.HeadSelect.setGeometry(QRect(9,66,50,17))
        self.HeadSelect.setText(self.tr("Head"))

        self.LegsSelect = QCheckBox(self.GroupBox19,'LegsSelect')
        self.LegsSelect.setGeometry(QRect(68,28,49,17))
        self.LegsSelect.setText(self.tr("Legs"))

        self.HandsSelect = QCheckBox(self.GroupBox19,'HandsSelect')
        self.HandsSelect.setGeometry(QRect(68,47,54,17))
        self.HandsSelect.setText(self.tr("Hands"))

        self.FeetSelect = QCheckBox(self.GroupBox19,'FeetSelect')
        self.FeetSelect.setGeometry(QRect(68,66,45,17))
        self.FeetSelect.setText(self.tr("Feet"))

        self.RangedSelect = QCheckBox(self.GroupBox19,'RangedSelect')
        self.RangedSelect.setGeometry(QRect(68,85,64,17))
        self.RangedSelect.setText(self.tr("Ranged"))

        self.RHSelect = QCheckBox(self.GroupBox19,'RHSelect')
        self.RHSelect.setGeometry(QRect(124,28,78,17))
        self.RHSelect.setText(self.tr("Right Hand"))

        self.LHSelect = QCheckBox(self.GroupBox19,'LHSelect')
        self.LHSelect.setGeometry(QRect(124,47,84,17))
        self.LHSelect.setText(self.tr("Left Hand"))

        self.THSelect = QCheckBox(self.GroupBox19,'THSelect')
        self.THSelect.setGeometry(QRect(124,66,71,17))
        self.THSelect.setText(self.tr("2 Handed"))

        self.ChestSelect = QCheckBox(self.GroupBox19,'ChestSelect')
        self.ChestSelect.setGeometry(QRect(9,28,50,17))
        self.ChestSelect.setText(self.tr("Chest"))

        self.LoadGemsButton = QPushButton(self,'LoadGemsButton')
        self.LoadGemsButton.setGeometry(QRect(311,246,99,26))
        self.LoadGemsButton.setText(self.tr("Load Gems"))

        self.PushButton19 = QPushButton(self,'PushButton19')
        self.PushButton19.setGeometry(QRect(198,422,99,26))
        self.PushButton19.setText(self.tr("Close"))

        self.connect(self.PathSelectButton,SIGNAL('clicked()'),self.openFileDialog)
        self.connect(self.PushButton19,SIGNAL('clicked()'),self,SLOT('accept()'))
        self.connect(self.LoadGemsButton,SIGNAL('clicked()'),self.loadGems)
        self.connect(self.DaocPath,SIGNAL('textChanged(const QString&)'),self.findPath)
        self.connect(self.HotbarNum,SIGNAL('valueChanged(int)'),self.hotbarNumChanged)
        self.connect(self.HotbarPos,SIGNAL('valueChanged(int)'),self.hotbarPosChanged)
        self.connect(self.ChestSelect,SIGNAL('clicked()'),self.PieceBoxChanged)
        self.connect(self.ArmsSelect,SIGNAL('clicked()'),self.PieceBoxChanged)
        self.connect(self.HeadSelect,SIGNAL('clicked()'),self.PieceBoxChanged)
        self.connect(self.LegsSelect,SIGNAL('clicked()'),self.PieceBoxChanged)
        self.connect(self.HandsSelect,SIGNAL('clicked()'),self.PieceBoxChanged)
        self.connect(self.FeetSelect,SIGNAL('clicked()'),self.PieceBoxChanged)
        self.connect(self.RangedSelect,SIGNAL('clicked()'),self.PieceBoxChanged)
        self.connect(self.RHSelect,SIGNAL('clicked()'),self.PieceBoxChanged)
        self.connect(self.LHSelect,SIGNAL('clicked()'),self.PieceBoxChanged)
        self.connect(self.THSelect,SIGNAL('clicked()'),self.PieceBoxChanged)

    def event(self,ev):
        ret = QDialog.event(self,ev)

        if ev.type() == QEvent.ApplicationFontChange:
            TextLabel14_font = QFont(self.TextLabel14.font())
            TextLabel14_font.setPointSize(9)
            TextLabel14_font.setBold(1)
            self.TextLabel14.setFont(TextLabel14_font)

        return ret

    def findPath(self,a0):
        print 'B_CraftBar.findPath(const QString&): not implemented yet'

    def hotbarNumChanged(self,a0):
        print 'B_CraftBar.hotbarNumChanged(int): not implemented yet'

    def hotbarPosChanged(self,a0):
        print 'B_CraftBar.hotbarPosChanged(int): not implemented yet'

    def loadGems(self):
        print 'B_CraftBar.loadGems(): not implemented yet'

    def PieceBoxChanged(self):
        print 'B_CraftBar.PieceBoxChanged(): not implemented yet'

    def openFileDialog(self):
        print 'B_CraftBar.openFileDialog(): not implemented yet'
