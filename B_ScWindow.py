# Form implementation generated from reading ui file 'ScWindow.ui'
#
# Created: Sun Apr 4 17:55:21 2004
#      by: The Python User Interface Compiler (pyuic) 3.8
#
# WARNING! All changes made in this file will be lost!


from qt import *
from SearchingCombo import *


class B_SC(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)

        if name == None:
            self.setName('B_SC')

        self.resize(751,517)
        f = QFont(self.font())
        f.setFamily('Arial')
        self.setFont(f)
        self.setCaption(self.tr("Spellcrafting Calculator"))

        self.GroupBox6 = QGroupBox(self,'GroupBox6')
        self.GroupBox6.setGeometry(QRect(310,21,121,145))
        self.GroupBox6.setTitle(self.tr("Skills"))

        self.SkillsList = QListBox(self.GroupBox6,'SkillsList')
        self.SkillsList.setGeometry(QRect(8,15,106,123))

        self.GroupBox6_2 = QGroupBox(self,'GroupBox6_2')
        self.GroupBox6_2.setGeometry(QRect(435,21,173,145))
        self.GroupBox6_2.setTitle(self.tr("Other Bonuses"))

        self.OtherBonusList = QListBox(self.GroupBox6_2,'OtherBonusList')
        self.OtherBonusList.setGeometry(QRect(3,15,164,123))

        self.GroupBox7 = QGroupBox(self,'GroupBox7')
        self.GroupBox7.setGeometry(QRect(310,165,215,44))
        self.GroupBox7.setTitle(self.tr("Reports"))

        self.ConfigButton = QPushButton(self.GroupBox7,'ConfigButton')
        self.ConfigButton.setGeometry(QRect(7,14,99,26))
        self.ConfigButton.setText(self.tr("Config Report"))

        self.MatsButton = QPushButton(self.GroupBox7,'MatsButton')
        self.MatsButton.setGeometry(QRect(111,14,99,26))
        self.MatsButton.setText(self.tr("Mats List"))

        self.FileNameLabel = QLabel(self,'FileNameLabel')
        self.FileNameLabel.setGeometry(QRect(10,208,159,16))
        self.FileNameLabel.setText(self.tr(""))

        self.TextLabel3 = QLabel(self,'TextLabel3')
        self.TextLabel3.setGeometry(QRect(10,194,53,14))
        TextLabel3_font = QFont(self.TextLabel3.font())
        TextLabel3_font.setBold(1)
        self.TextLabel3.setFont(TextLabel3_font)
        self.TextLabel3.setText(self.tr("Version:"))

        self.Version = QLabel(self,'Version')
        self.Version.setGeometry(QRect(61,194,56,14))
        Version_font = QFont(self.Version.font())
        Version_font.setBold(1)
        self.Version.setFont(Version_font)
        self.Version.setText(self.tr("0.1"))

        self.TypeTab = QTabWidget(self,'TypeTab')
        self.TypeTab.setGeometry(QRect(0,224,788,377))

        self.Armor = QWidget(self.TypeTab,'Armor')

        self.PieceTab = QTabWidget(self.Armor,'PieceTab')
        self.PieceTab.setGeometry(QRect(3,9,868,343))

        self.Chest = QWidget(self.PieceTab,'Chest')
        self.PieceTab.insertTab(self.Chest,self.tr("Chest"))

        self.Arms = QWidget(self.PieceTab,'Arms')
        self.PieceTab.insertTab(self.Arms,self.tr("Arms"))

        self.Head = QWidget(self.PieceTab,'Head')
        self.PieceTab.insertTab(self.Head,self.tr("Head"))

        self.Legs = QWidget(self.PieceTab,'Legs')
        self.PieceTab.insertTab(self.Legs,self.tr("Legs"))

        self.Hands = QWidget(self.PieceTab,'Hands')
        self.PieceTab.insertTab(self.Hands,self.tr("Hands"))

        self.Feet = QWidget(self.PieceTab,'Feet')
        self.PieceTab.insertTab(self.Feet,self.tr("Feet"))

        self.Right_Hand = QWidget(self.PieceTab,'Right_Hand')
        self.PieceTab.insertTab(self.Right_Hand,self.tr("Right Hand"))

        self.Left_Hand = QWidget(self.PieceTab,'Left_Hand')
        self.PieceTab.insertTab(self.Left_Hand,self.tr("Left Hand"))

        self.Two_Handed = QWidget(self.PieceTab,'Two_Handed')
        self.PieceTab.insertTab(self.Two_Handed,self.tr("2 Handed"))

        self.Ranged = QWidget(self.PieceTab,'Ranged')
        self.PieceTab.insertTab(self.Ranged,self.tr("Ranged"))

        self.Spare = QWidget(self.PieceTab,'Spare')
        self.PieceTab.insertTab(self.Spare,self.tr("Spare"))
        self.TypeTab.insertTab(self.Armor,self.tr("Armor/Weapons"))

        self.Jewelry = QWidget(self.TypeTab,'Jewelry')

        self.TextLabel4_2 = QLabel(self.Jewelry,'TextLabel4_2')
        self.TextLabel4_2.setGeometry(QRect(287,-21,259,17))
        self.TextLabel4_2.setText(self.tr("TextLabel4"))

        self.JewelTab = QTabWidget(self.Jewelry,'JewelTab')
        self.JewelTab.setGeometry(QRect(3,9,838,341))

        self.Neck = QWidget(self.JewelTab,'Neck')

        self.Imbue = QLabel(self.Neck,'Imbue')
        self.Imbue.setGeometry(QRect(352,3,34,16))
        self.Imbue.setText(self.tr("0.0"))
        self.Imbue.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Imbue_Label = QLabel(self.Neck,'Imbue_Label')
        self.Imbue_Label.setGeometry(QRect(430,3,76,16))
        self.Imbue_Label.setText(self.tr("Imbue Points"))

        self.Slash_Label = QLabel(self.Neck,'Slash_Label')
        self.Slash_Label.setGeometry(QRect(388,3,8,16))
        self.Slash_Label.setText(self.tr("/"))
        self.Slash_Label.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Utility = QLabel(self.Neck,'Utility')
        self.Utility.setGeometry(QRect(545,3,28,16))
        self.Utility.setText(self.tr("0.0"))

        self.Utility_Label = QLabel(self.Neck,'Utility_Label')
        self.Utility_Label.setGeometry(QRect(507,3,37,16))
        self.Utility_Label.setText(self.tr("Utility:"))

        self.Total_Imbue = QLabel(self.Neck,'Total_Imbue')
        self.Total_Imbue.setGeometry(QRect(401,3,29,16))
        self.Total_Imbue.setText(self.tr("0.0"))

        self.Equipped = QCheckBox(self.Neck,'Equipped')
        self.Equipped.setGeometry(QRect(579,2,71,17))
        self.Equipped.setText(self.tr("Equipped"))

        self.TotalUtility = QLabel(self.Neck,'TotalUtility')
        self.TotalUtility.setGeometry(QRect(545,20,73,16))
        self.TotalUtility.setText(self.tr("0.0"))

        self.Total_Label = QLabel(self.Neck,'Total_Label')
        self.Total_Label.setGeometry(QRect(507,20,34,16))
        self.Total_Label.setText(self.tr("Total:"))

        self.Overcharge_Label = QLabel(self.Neck,'Overcharge_Label')
        self.Overcharge_Label.setGeometry(QRect(363,20,59,16))
        self.Overcharge_Label.setText(self.tr("Overcharge:"))

        self.Overcharge = QLabel(self.Neck,'Overcharge')
        self.Overcharge.setGeometry(QRect(428,20,79,16))
        self.Overcharge.setText(self.tr("None"))

        self.TextLabel23 = QLabel(self.Neck,'TextLabel23')
        self.TextLabel23.setGeometry(QRect(11,2,59,22))
        self.TextLabel23.setText(self.tr("Item Quality:"))

        self.ItemLevel = QLineEdit(self.Neck,'ItemLevel')
        self.ItemLevel.setGeometry(QRect(205,3,93,22))

        self.TextLabel39 = QLabel(self.Neck,'TextLabel39')
        self.TextLabel39.setGeometry(QRect(146,7,59,13))
        self.TextLabel39.setText(self.tr("Item Level:"))

        self.PushButton11 = QPushButton(self.Neck,'PushButton11')
        self.PushButton11.setGeometry(QRect(303,3,24,23))
        self.PushButton11.setText(self.tr("..."))

        self.QualEdit = QLineEdit(self.Neck,'QualEdit')
        self.QualEdit.setGeometry(QRect(76,2,35,22))

        self.Gem_Label_1 = QLabel(self.Neck,'Gem_Label_1')
        self.Gem_Label_1.setGeometry(QRect(7,61,34,22))
        self.Gem_Label_1.setText(self.tr("Gem 1:"))

        self.Type_1 = SearchingCombo(0,self.Neck,'Type_1')
        self.Type_1.insertItem(self.tr("Unused"))
        self.Type_1.insertItem(self.tr("Stat"))
        self.Type_1.insertItem(self.tr("Resist"))
        self.Type_1.insertItem(self.tr("Hits"))
        self.Type_1.insertItem(self.tr("Power"))
        self.Type_1.insertItem(self.tr("Focus"))
        self.Type_1.insertItem(self.tr("Skill"))
        self.Type_1.setGeometry(QRect(46,61,127,22))

        self.CraftButton = QPushButton(self.Neck,'CraftButton')
        self.CraftButton.setGeometry(QRect(662,2,69,26))
        self.CraftButton.setText(self.tr("Craft..."))

        self.Effect_1 = SearchingCombo(0,self.Neck,'Effect_1')
        self.Effect_1.setGeometry(QRect(256,61,150,22))

        self.Cost_Label = QLabel(self.Neck,'Cost_Label')
        self.Cost_Label.setGeometry(QRect(559,40,29,16))
        self.Cost_Label.setText(self.tr("Cost:"))

        self.Name_Label = QLabel(self.Neck,'Name_Label')
        self.Name_Label.setGeometry(QRect(619,40,34,16))
        self.Name_Label.setText(self.tr("Name:"))

        self.Points_Label = QLabel(self.Neck,'Points_Label')
        self.Points_Label.setGeometry(QRect(498,40,35,16))
        self.Points_Label.setText(self.tr("Points:"))

        self.Quality_3 = SearchingCombo(0,self.Neck,'Quality_3')
        self.Quality_3.setGeometry(QRect(411,110,81,22))

        self.Gem_Label_3 = QLabel(self.Neck,'Gem_Label_3')
        self.Gem_Label_3.setGeometry(QRect(7,110,34,23))
        self.Gem_Label_3.setText(self.tr("Gem 3:"))

        self.Type_3 = SearchingCombo(0,self.Neck,'Type_3')
        self.Type_3.insertItem(self.tr("Unused"))
        self.Type_3.insertItem(self.tr("Stat"))
        self.Type_3.insertItem(self.tr("Resist"))
        self.Type_3.insertItem(self.tr("Hits"))
        self.Type_3.insertItem(self.tr("Power"))
        self.Type_3.insertItem(self.tr("Focus"))
        self.Type_3.insertItem(self.tr("Skill"))
        self.Type_3.setGeometry(QRect(46,110,127,22))

        self.Effect_3 = SearchingCombo(0,self.Neck,'Effect_3')
        self.Effect_3.setGeometry(QRect(256,110,150,22))

        self.Effect_4 = SearchingCombo(0,self.Neck,'Effect_4')
        self.Effect_4.setGeometry(QRect(256,134,150,22))

        self.Amount_Drop_4 = SearchingCombo(0,self.Neck,'Amount_Drop_4')
        self.Amount_Drop_4.setGeometry(QRect(177,134,74,22))

        self.Type_4 = SearchingCombo(0,self.Neck,'Type_4')
        self.Type_4.insertItem(self.tr("Unused"))
        self.Type_4.insertItem(self.tr("Stat"))
        self.Type_4.insertItem(self.tr("Resist"))
        self.Type_4.insertItem(self.tr("Hits"))
        self.Type_4.insertItem(self.tr("Power"))
        self.Type_4.insertItem(self.tr("Focus"))
        self.Type_4.insertItem(self.tr("Skill"))
        self.Type_4.setGeometry(QRect(46,134,127,22))

        self.Quality_4 = SearchingCombo(0,self.Neck,'Quality_4')
        self.Quality_4.setGeometry(QRect(411,134,81,22))

        self.Gem_Label_2 = QLabel(self.Neck,'Gem_Label_2')
        self.Gem_Label_2.setGeometry(QRect(7,85,34,22))
        self.Gem_Label_2.setText(self.tr("Gem 2:"))

        self.Type_2 = SearchingCombo(0,self.Neck,'Type_2')
        self.Type_2.insertItem(self.tr("Unused"))
        self.Type_2.insertItem(self.tr("Stat"))
        self.Type_2.insertItem(self.tr("Resist"))
        self.Type_2.insertItem(self.tr("Hits"))
        self.Type_2.insertItem(self.tr("Power"))
        self.Type_2.insertItem(self.tr("Focus"))
        self.Type_2.insertItem(self.tr("Skill"))
        self.Type_2.setGeometry(QRect(46,86,127,22))

        self.Quality_2 = SearchingCombo(0,self.Neck,'Quality_2')
        self.Quality_2.setGeometry(QRect(411,86,81,22))

        self.Speed_Edit = QLineEdit(self.Neck,'Speed_Edit')
        self.Speed_Edit.setGeometry(QRect(540,110,36,22))

        self.AFDPS_Edit = QLineEdit(self.Neck,'AFDPS_Edit')
        self.AFDPS_Edit.setGeometry(QRect(540,86,36,22))

        self.Bonus_Edit = QLineEdit(self.Neck,'Bonus_Edit')
        self.Bonus_Edit.setGeometry(QRect(540,133,36,22))

        self.Amount_Drop_2 = SearchingCombo(0,self.Neck,'Amount_Drop_2')
        self.Amount_Drop_2.setGeometry(QRect(177,86,74,22))

        self.Effect_2 = SearchingCombo(0,self.Neck,'Effect_2')
        self.Effect_2.setGeometry(QRect(256,86,150,22))

        self.Amount_Drop_3 = SearchingCombo(0,self.Neck,'Amount_Drop_3')
        self.Amount_Drop_3.setGeometry(QRect(177,110,74,22))

        self.Points_4 = QLabel(self.Neck,'Points_4')
        self.Points_4.setGeometry(QRect(498,137,20,16))
        self.Points_4.setText(self.tr("0.0"))

        self.Points_2 = QLabel(self.Neck,'Points_2')
        self.Points_2.setGeometry(QRect(498,89,23,16))
        self.Points_2.setText(self.tr("0.0"))

        self.Points_1 = QLabel(self.Neck,'Points_1')
        self.Points_1.setGeometry(QRect(498,64,24,16))
        self.Points_1.setText(self.tr("0.0"))

        self.Points_3 = QLabel(self.Neck,'Points_3')
        self.Points_3.setGeometry(QRect(498,113,22,16))
        self.Points_3.setText(self.tr("0.0"))

        self.Speed_Label = QLabel(self.Neck,'Speed_Label')
        self.Speed_Label.setGeometry(QRect(494,110,39,22))
        self.Speed_Label.setText(self.tr("Speed:"))

        self.Bonus_Label = QLabel(self.Neck,'Bonus_Label')
        self.Bonus_Label.setGeometry(QRect(494,135,41,22))
        self.Bonus_Label.setText(self.tr("Bonus:"))

        self.AFDPS_Label = QLabel(self.Neck,'AFDPS_Label')
        self.AFDPS_Label.setGeometry(QRect(494,87,47,22))
        self.AFDPS_Label.setText(self.tr("AF/DPS:"))

        self.Amount_Drop_1 = SearchingCombo(0,self.Neck,'Amount_Drop_1')
        self.Amount_Drop_1.setGeometry(QRect(177,61,74,22))

        self.Amount_Edit_4 = QLineEdit(self.Neck,'Amount_Edit_4')
        self.Amount_Edit_4.setGeometry(QRect(176,134,74,22))

        self.Amount_Edit_3 = QLineEdit(self.Neck,'Amount_Edit_3')
        self.Amount_Edit_3.setGeometry(QRect(176,110,74,22))

        self.Amount_Edit_2 = QLineEdit(self.Neck,'Amount_Edit_2')
        self.Amount_Edit_2.setGeometry(QRect(176,86,74,22))

        self.Amount_Edit_1 = QLineEdit(self.Neck,'Amount_Edit_1')
        self.Amount_Edit_1.setGeometry(QRect(176,61,74,22))

        self.QualDrop = SearchingCombo(0,self.Neck,'QualDrop')
        self.QualDrop.insertItem(self.tr("94"))
        self.QualDrop.insertItem(self.tr("95"))
        self.QualDrop.insertItem(self.tr("96"))
        self.QualDrop.insertItem(self.tr("97"))
        self.QualDrop.insertItem(self.tr("98"))
        self.QualDrop.insertItem(self.tr("99"))
        self.QualDrop.insertItem(self.tr("100"))
        self.QualDrop.setGeometry(QRect(76,2,52,22))

        self.TextLabel31_5_2 = QLabel(self.Neck,'TextLabel31_5_2')
        self.TextLabel31_5_2.setGeometry(QRect(48,44,81,16))
        self.TextLabel31_5_2.setText(self.tr("Type:"))

        self.TextLabel32_5_2 = QLabel(self.Neck,'TextLabel32_5_2')
        self.TextLabel32_5_2.setGeometry(QRect(190,43,65,16))
        self.TextLabel32_5_2.setText(self.tr("Amount:"))

        self.TextLabel33_5_2 = QLabel(self.Neck,'TextLabel33_5_2')
        self.TextLabel33_5_2.setGeometry(QRect(269,43,81,16))
        self.TextLabel33_5_2.setText(self.tr("Effect:"))

        self.Effect_7 = SearchingCombo(0,self.Neck,'Effect_7')
        self.Effect_7.setGeometry(QRect(256,212,150,22))

        self.Gem_Label_5 = QLabel(self.Neck,'Gem_Label_5')
        self.Gem_Label_5.setGeometry(QRect(7,157,34,22))
        self.Gem_Label_5.setText(self.tr("Gem 5:"))

        self.Gem_Label_4 = QLabel(self.Neck,'Gem_Label_4')
        self.Gem_Label_4.setGeometry(QRect(7,134,34,22))
        self.Gem_Label_4.setText(self.tr("Gem 4:"))

        self.Type_5 = SearchingCombo(0,self.Neck,'Type_5')
        self.Type_5.insertItem(self.tr("Unused"))
        self.Type_5.insertItem(self.tr("Stat"))
        self.Type_5.insertItem(self.tr("Resist"))
        self.Type_5.insertItem(self.tr("Hits"))
        self.Type_5.insertItem(self.tr("Power"))
        self.Type_5.insertItem(self.tr("Focus"))
        self.Type_5.insertItem(self.tr("Skill"))
        self.Type_5.setGeometry(QRect(46,157,127,22))

        self.Amount_Edit_5 = QLineEdit(self.Neck,'Amount_Edit_5')
        self.Amount_Edit_5.setGeometry(QRect(176,157,74,22))

        self.Effect_5 = SearchingCombo(0,self.Neck,'Effect_5')
        self.Effect_5.setGeometry(QRect(256,157,150,22))

        self.Quality_5 = SearchingCombo(0,self.Neck,'Quality_5')
        self.Quality_5.setGeometry(QRect(411,157,81,22))

        self.Amount_Edit_7 = QLineEdit(self.Neck,'Amount_Edit_7')
        self.Amount_Edit_7.setGeometry(QRect(176,212,74,22))

        self.Type_6 = SearchingCombo(0,self.Neck,'Type_6')
        self.Type_6.insertItem(self.tr("Unused"))
        self.Type_6.insertItem(self.tr("Stat"))
        self.Type_6.insertItem(self.tr("Resist"))
        self.Type_6.insertItem(self.tr("Hits"))
        self.Type_6.insertItem(self.tr("Power"))
        self.Type_6.insertItem(self.tr("Focus"))
        self.Type_6.insertItem(self.tr("Skill"))
        self.Type_6.setGeometry(QRect(46,181,127,22))

        self.Amount_Edit_6 = QLineEdit(self.Neck,'Amount_Edit_6')
        self.Amount_Edit_6.setGeometry(QRect(176,181,74,22))

        self.Effect_6 = SearchingCombo(0,self.Neck,'Effect_6')
        self.Effect_6.setGeometry(QRect(256,181,150,22))

        self.Quality_6 = SearchingCombo(0,self.Neck,'Quality_6')
        self.Quality_6.setGeometry(QRect(411,181,81,22))

        self.Gem_Label_6 = QLabel(self.Neck,'Gem_Label_6')
        self.Gem_Label_6.setGeometry(QRect(7,181,34,22))
        self.Gem_Label_6.setText(self.tr("Gem 6:"))

        self.Type_7 = SearchingCombo(0,self.Neck,'Type_7')
        self.Type_7.insertItem(self.tr("Unused"))
        self.Type_7.insertItem(self.tr("Stat"))
        self.Type_7.insertItem(self.tr("Resist"))
        self.Type_7.insertItem(self.tr("Hits"))
        self.Type_7.insertItem(self.tr("Power"))
        self.Type_7.insertItem(self.tr("Focus"))
        self.Type_7.insertItem(self.tr("Skill"))
        self.Type_7.setGeometry(QRect(46,212,127,22))

        self.Gem_Label_7 = QLabel(self.Neck,'Gem_Label_7')
        self.Gem_Label_7.setGeometry(QRect(7,212,34,22))
        self.Gem_Label_7.setText(self.tr("Gem 7:"))

        self.Gem_Label_8 = QLabel(self.Neck,'Gem_Label_8')
        self.Gem_Label_8.setGeometry(QRect(7,236,34,22))
        self.Gem_Label_8.setText(self.tr("Gem 8:"))

        self.Type_8 = SearchingCombo(0,self.Neck,'Type_8')
        self.Type_8.insertItem(self.tr("Unused"))
        self.Type_8.insertItem(self.tr("Stat"))
        self.Type_8.insertItem(self.tr("Resist"))
        self.Type_8.insertItem(self.tr("Hits"))
        self.Type_8.insertItem(self.tr("Power"))
        self.Type_8.insertItem(self.tr("Focus"))
        self.Type_8.insertItem(self.tr("Skill"))
        self.Type_8.setGeometry(QRect(46,236,127,22))

        self.Quality_8 = SearchingCombo(0,self.Neck,'Quality_8')
        self.Quality_8.setGeometry(QRect(411,236,81,22))

        self.Amount_Edit_8 = QLineEdit(self.Neck,'Amount_Edit_8')
        self.Amount_Edit_8.setGeometry(QRect(176,236,74,22))

        self.Effect_8 = SearchingCombo(0,self.Neck,'Effect_8')
        self.Effect_8.setGeometry(QRect(256,236,150,22))

        self.Type_9 = SearchingCombo(0,self.Neck,'Type_9')
        self.Type_9.insertItem(self.tr("Unused"))
        self.Type_9.insertItem(self.tr("Stat"))
        self.Type_9.insertItem(self.tr("Resist"))
        self.Type_9.insertItem(self.tr("Hits"))
        self.Type_9.insertItem(self.tr("Power"))
        self.Type_9.insertItem(self.tr("Focus"))
        self.Type_9.insertItem(self.tr("Skill"))
        self.Type_9.setGeometry(QRect(46,260,127,22))

        self.Amount_Edit_9 = QLineEdit(self.Neck,'Amount_Edit_9')
        self.Amount_Edit_9.setGeometry(QRect(176,260,74,22))

        self.Effect_9 = SearchingCombo(0,self.Neck,'Effect_9')
        self.Effect_9.setGeometry(QRect(256,260,150,22))

        self.Quality_9 = SearchingCombo(0,self.Neck,'Quality_9')
        self.Quality_9.setGeometry(QRect(411,260,81,22))

        self.Gem_Label_9 = QLabel(self.Neck,'Gem_Label_9')
        self.Gem_Label_9.setGeometry(QRect(7,260,34,22))
        self.Gem_Label_9.setText(self.tr("Gem 9:"))

        self.Gem_Label_10 = QLabel(self.Neck,'Gem_Label_10')
        self.Gem_Label_10.setGeometry(QRect(0,285,41,22))
        self.Gem_Label_10.setText(self.tr("Gem 10:"))
        self.Gem_Label_10.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Type_10 = SearchingCombo(0,self.Neck,'Type_10')
        self.Type_10.insertItem(self.tr("Unused"))
        self.Type_10.insertItem(self.tr("Stat"))
        self.Type_10.insertItem(self.tr("Resist"))
        self.Type_10.insertItem(self.tr("Hits"))
        self.Type_10.insertItem(self.tr("Power"))
        self.Type_10.insertItem(self.tr("Focus"))
        self.Type_10.insertItem(self.tr("Skill"))
        self.Type_10.setGeometry(QRect(46,285,127,22))

        self.Amount_Edit_10 = QLineEdit(self.Neck,'Amount_Edit_10')
        self.Amount_Edit_10.setGeometry(QRect(176,285,74,22))

        self.Effect_10 = SearchingCombo(0,self.Neck,'Effect_10')
        self.Effect_10.setGeometry(QRect(256,285,150,22))

        self.Quality_10 = SearchingCombo(0,self.Neck,'Quality_10')
        self.Quality_10.setGeometry(QRect(411,285,81,22))

        self.Quality_7 = SearchingCombo(0,self.Neck,'Quality_7')
        self.Quality_7.setGeometry(QRect(411,212,81,22))

        self.ButtonGroup1 = QButtonGroup(self.Neck,'ButtonGroup1')
        self.ButtonGroup1.setEnabled(1)
        self.ButtonGroup1.setGeometry(QRect(607,33,146,19))
        self.ButtonGroup1.setLineWidth(0)
        self.ButtonGroup1.setTitle(self.tr(""))

        self.Drop = QRadioButton(self.ButtonGroup1,'Drop')
        self.Drop.setGeometry(QRect(100,2,52,17))
        self.Drop.setText(self.tr("Drop"))
        self.Drop.setChecked(1)

        self.PlayerMade = QRadioButton(self.ButtonGroup1,'PlayerMade')
        self.PlayerMade.setGeometry(QRect(10,2,85,17))
        self.PlayerMade.setText(self.tr("Player Made"))

        self.ItemCost_Label = QLabel(self.Neck,'ItemCost_Label')
        self.ItemCost_Label.setGeometry(QRect(503,183,50,16))
        self.ItemCost_Label.setText(self.tr("Item Cost:"))

        self.ItemCost = QLabel(self.Neck,'ItemCost')
        self.ItemCost.setGeometry(QRect(554,183,92,16))
        self.ItemCost.setText(self.tr(""))
        self.ItemCost.setAlignment(QLabel.AlignVCenter | QLabel.AlignLeft)

        self.ClearItem = QPushButton(self.Neck,'ClearItem')
        self.ClearItem.setGeometry(QRect(683,209,79,26))
        self.ClearItem.setText(self.tr("Clear Item"))

        self.LoadItem = QPushButton(self.Neck,'LoadItem')
        self.LoadItem.setGeometry(QRect(683,157,79,26))
        self.LoadItem.setText(self.tr("Load Item"))

        self.SaveItem = QPushButton(self.Neck,'SaveItem')
        self.SaveItem.setGeometry(QRect(596,157,79,26))
        self.SaveItem.setText(self.tr("Save Item"))

        self.MoreSlots = QPushButton(self.Neck,'MoreSlots')
        self.MoreSlots.setGeometry(QRect(499,208,107,27))
        self.MoreSlots.setText(self.tr("View More Slots...."))

        self.TextLabel34_5_2 = QLabel(self.Neck,'TextLabel34_5_2')
        self.TextLabel34_5_2.setGeometry(QRect(426,43,41,16))
        self.TextLabel34_5_2.setText(self.tr("Quality:"))

        self.ItemName_Label = QLabel(self.Neck,'ItemName_Label')
        self.ItemName_Label.setEnabled(1)
        self.ItemName_Label.setGeometry(QRect(498,43,59,16))
        self.ItemName_Label.setText(self.tr("Item Name:"))

        self.Cost_2 = QLabel(self.Neck,'Cost_2')
        self.Cost_2.setGeometry(QRect(531,89,64,16))
        self.Cost_2.setText(self.tr("0c"))
        self.Cost_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_2 = QLabel(self.Neck,'Name_2')
        self.Name_2.setGeometry(QRect(603,89,169,16))
        self.Name_2.setText(self.tr(""))

        self.Cost_3 = QLabel(self.Neck,'Cost_3')
        self.Cost_3.setGeometry(QRect(526,113,69,16))
        self.Cost_3.setText(self.tr("0c"))
        self.Cost_3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_3 = QLabel(self.Neck,'Name_3')
        self.Name_3.setGeometry(QRect(602,113,173,16))
        self.Name_3.setText(self.tr(""))

        self.Cost_4 = QLabel(self.Neck,'Cost_4')
        self.Cost_4.setGeometry(QRect(520,137,75,16))
        self.Cost_4.setText(self.tr("0c"))
        self.Cost_4.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_4 = QLabel(self.Neck,'Name_4')
        self.Name_4.setGeometry(QRect(602,137,169,16))
        self.Name_4.setText(self.tr(""))

        self.Cost_1 = QLabel(self.Neck,'Cost_1')
        self.Cost_1.setGeometry(QRect(519,64,76,16))
        self.Cost_1.setText(self.tr("0c"))
        self.Cost_1.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_1 = QLabel(self.Neck,'Name_1')
        self.Name_1.setGeometry(QRect(602,64,169,16))
        self.Name_1.setText(self.tr(""))

        self.Quality_1 = SearchingCombo(0,self.Neck,'Quality_1')
        self.Quality_1.setGeometry(QRect(411,61,81,22))

        self.ItemName = QLineEdit(self.Neck,'ItemName')
        self.ItemName.setGeometry(QRect(494,61,160,22))
        self.JewelTab.insertTab(self.Neck,self.tr("Neck"))

        self.Cloak = QWidget(self.JewelTab,'Cloak')
        self.JewelTab.insertTab(self.Cloak,self.tr("Cloak"))

        self.Jewel = QWidget(self.JewelTab,'Jewel')
        self.JewelTab.insertTab(self.Jewel,self.tr("Jewel"))

        self.Belt = QWidget(self.JewelTab,'Belt')
        self.JewelTab.insertTab(self.Belt,self.tr("Belt"))

        self.LeftRing = QWidget(self.JewelTab,'LeftRing')
        self.JewelTab.insertTab(self.LeftRing,self.tr("Left Ring"))

        self.RightRing = QWidget(self.JewelTab,'RightRing')
        self.JewelTab.insertTab(self.RightRing,self.tr("Right Ring"))

        self.LeftWrist = QWidget(self.JewelTab,'LeftWrist')
        self.JewelTab.insertTab(self.LeftWrist,self.tr("Left Wrist"))

        self.RightWrist = QWidget(self.JewelTab,'RightWrist')
        self.JewelTab.insertTab(self.RightWrist,self.tr("Right Wrist"))
        self.TypeTab.insertTab(self.Jewelry,self.tr("Jewelry"))

        self.ButtonGroup2 = QButtonGroup(self,'ButtonGroup2')
        self.ButtonGroup2.setGeometry(QRect(612,21,166,51))
        self.ButtonGroup2.setTitle(self.tr("Display"))

        self.TotalBonus = QRadioButton(self.ButtonGroup2,'TotalBonus')
        self.TotalBonus.setGeometry(QRect(11,15,85,17))
        self.TotalBonus.setText(self.tr("Total Bonus"))
        self.TotalBonus.setChecked(1)

        self.CapDistance = QRadioButton(self.ButtonGroup2,'CapDistance')
        self.CapDistance.setGeometry(QRect(11,32,109,17))
        self.CapDistance.setText(self.tr("Distance To Cap"))

        self.DupErrorString = QLabel(self,'DupErrorString')
        self.DupErrorString.setGeometry(QRect(530,184,285,17))
        self.DupErrorString.setText(self.tr(""))

        self.GroupBox9 = QGroupBox(self,'GroupBox9')
        self.GroupBox9.setGeometry(QRect(613,72,167,111))
        self.GroupBox9.setTitle(self.tr("Char Info"))

        self.TextLabel1_2 = QLabel(self.GroupBox9,'TextLabel1_2')
        self.TextLabel1_2.setGeometry(QRect(6,16,37,16))
        self.TextLabel1_2.setText(self.tr("Name:"))

        self.TextLabel2_2 = QLabel(self.GroupBox9,'TextLabel2_2')
        self.TextLabel2_2.setGeometry(QRect(6,40,33,16))
        self.TextLabel2_2.setText(self.tr("Class:"))

        self.TextLabel3_2 = QLabel(self.GroupBox9,'TextLabel3_2')
        self.TextLabel3_2.setGeometry(QRect(6,65,38,16))
        self.TextLabel3_2.setText(self.tr("Level:"))

        self.TextLabel3_2_2 = QLabel(self.GroupBox9,'TextLabel3_2_2')
        self.TextLabel3_2_2.setGeometry(QRect(6,88,38,16))
        self.TextLabel3_2_2.setText(self.tr("Race:"))

        self.CharClass = SearchingCombo(0,self.GroupBox9,'CharClass')
        self.CharClass.setGeometry(QRect(46,38,114,22))

        self.CharName = QLineEdit(self.GroupBox9,'CharName')
        self.CharName.setGeometry(QRect(46,14,114,22))

        self.CharLevel = QLineEdit(self.GroupBox9,'CharLevel')
        self.CharLevel.setGeometry(QRect(46,61,37,22))

        self.CharRace = SearchingCombo(0,self.GroupBox9,'CharRace')
        self.CharRace.setGeometry(QRect(46,84,114,22))

        self.GroupBox1 = QGroupBox(self,'GroupBox1')
        self.GroupBox1.setGeometry(QRect(5,21,75,172))
        self.GroupBox1.setTitle(self.tr("Stats"))

        self.Str = QLabel(self.GroupBox1,'Str')
        self.Str.setGeometry(QRect(42,16,28,18))
        self.Str.setText(self.tr("0"))

        self.StrLabel = QLabel(self.GroupBox1,'StrLabel')
        self.StrLabel.setGeometry(QRect(11,16,27,18))
        self.StrLabel.setText(self.tr("STR:"))

        self.EmpLabel = QLabel(self.GroupBox1,'EmpLabel')
        self.EmpLabel.setGeometry(QRect(11,146,24,18))
        self.EmpLabel.setText(self.tr("EMP:"))

        self.Emp = QLabel(self.GroupBox1,'Emp')
        self.Emp.setGeometry(QRect(42,146,28,18))
        self.Emp.setText(self.tr("0"))

        self.Con = QLabel(self.GroupBox1,'Con')
        self.Con.setGeometry(QRect(42,34,28,19))
        self.Con.setText(self.tr("0"))

        self.ConLabel = QLabel(self.GroupBox1,'ConLabel')
        self.ConLabel.setGeometry(QRect(10,34,25,19))
        self.ConLabel.setText(self.tr("CON:"))

        self.DexLabel = QLabel(self.GroupBox1,'DexLabel')
        self.DexLabel.setGeometry(QRect(11,52,26,18))
        self.DexLabel.setText(self.tr("DEX:"))

        self.Dex = QLabel(self.GroupBox1,'Dex')
        self.Dex.setGeometry(QRect(42,52,28,18))
        self.Dex.setText(self.tr("0"))

        self.Qui = QLabel(self.GroupBox1,'Qui')
        self.Qui.setGeometry(QRect(42,71,28,18))
        self.Qui.setText(self.tr("0"))

        self.QuiLabel = QLabel(self.GroupBox1,'QuiLabel')
        self.QuiLabel.setGeometry(QRect(11,71,24,18))
        self.QuiLabel.setText(self.tr("QUI:"))

        self.IntLabel = QLabel(self.GroupBox1,'IntLabel')
        self.IntLabel.setGeometry(QRect(11,90,22,18))
        self.IntLabel.setText(self.tr("INT:"))

        self.PieLabel = QLabel(self.GroupBox1,'PieLabel')
        self.PieLabel.setGeometry(QRect(11,109,20,19))
        self.PieLabel.setText(self.tr("PIE:"))

        self.Pie = QLabel(self.GroupBox1,'Pie')
        self.Pie.setGeometry(QRect(42,109,28,19))
        self.Pie.setText(self.tr("0"))

        self.Cha = QLabel(self.GroupBox1,'Cha')
        self.Cha.setGeometry(QRect(42,128,28,18))
        self.Cha.setText(self.tr("0"))

        self.ChaLabel = QLabel(self.GroupBox1,'ChaLabel')
        self.ChaLabel.setGeometry(QRect(11,128,26,18))
        self.ChaLabel.setText(self.tr("CHA:"))

        self.Int = QLabel(self.GroupBox1,'Int')
        self.Int.setGeometry(QRect(42,90,28,18))
        self.Int.setText(self.tr("0"))

        self.GroupBox5 = QGroupBox(self,'GroupBox5')
        self.GroupBox5.setGeometry(QRect(174,176,135,48))
        self.GroupBox5.setTitle(self.tr("Totals"))

        self.TextLabel20 = QLabel(self.GroupBox5,'TextLabel20')
        self.TextLabel20.setGeometry(QRect(6,13,29,16))
        self.TextLabel20.setText(self.tr("Cost:"))

        self.TextLabel21 = QLabel(self.GroupBox5,'TextLabel21')
        self.TextLabel21.setGeometry(QRect(6,29,37,16))
        self.TextLabel21.setText(self.tr("Price:"))

        self.TotalPrice = QLabel(self.GroupBox5,'TotalPrice')
        self.TotalPrice.setGeometry(QRect(45,29,85,16))
        self.TotalPrice.setText(self.tr("0"))

        self.TotalCost = QLabel(self.GroupBox5,'TotalCost')
        self.TotalCost.setGeometry(QRect(45,14,86,16))
        self.TotalCost.setText(self.tr("0"))

        self.GroupBox3 = QGroupBox(self,'GroupBox3')
        self.GroupBox3.setGeometry(QRect(174,21,134,60))
        self.GroupBox3.setTitle(self.tr("Hits && Power"))

        self.PowerLabel = QLabel(self.GroupBox3,'PowerLabel')
        self.PowerLabel.setGeometry(QRect(9,35,37,16))
        self.PowerLabel.setSizePolicy(QSizePolicy(3,3,self.PowerLabel.sizePolicy().hasHeightForWidth()))
        self.PowerLabel.setText(self.tr("Power:"))

        self.Hits = QLabel(self.GroupBox3,'Hits')
        self.Hits.setGeometry(QRect(47,16,32,16))
        self.Hits.setText(self.tr("0"))

        self.Power = QLabel(self.GroupBox3,'Power')
        self.Power.setGeometry(QRect(47,35,28,16))
        self.Power.setText(self.tr("0"))

        self.HitsLabel = QLabel(self.GroupBox3,'HitsLabel')
        self.HitsLabel.setGeometry(QRect(9,16,37,16))
        self.HitsLabel.setText(self.tr("Hits:"))

        self.GroupBox4 = QGroupBox(self,'GroupBox4')
        self.GroupBox4.setGeometry(QRect(174,81,135,97))
        self.GroupBox4.setTitle(self.tr("Focus"))

        self.Focus_1 = QLabel(self.GroupBox4,'Focus_1')
        self.Focus_1.setGeometry(QRect(7,18,122,16))
        self.Focus_1.setText(self.tr(""))

        self.Focus_2 = QLabel(self.GroupBox4,'Focus_2')
        self.Focus_2.setGeometry(QRect(7,36,122,16))
        self.Focus_2.setText(self.tr(""))

        self.Focus_3 = QLabel(self.GroupBox4,'Focus_3')
        self.Focus_3.setGeometry(QRect(7,55,122,16))
        self.Focus_3.setText(self.tr(""))

        self.Focus_4 = QLabel(self.GroupBox4,'Focus_4')
        self.Focus_4.setGeometry(QRect(7,75,122,16))
        self.Focus_4.setText(self.tr(""))

        self.GroupBox2 = QGroupBox(self,'GroupBox2')
        self.GroupBox2.setGeometry(QRect(83,21,90,172))
        self.GroupBox2.setTitle(self.tr("Resists"))

        self.BodyLabel = QLabel(self.GroupBox2,'BodyLabel')
        self.BodyLabel.setGeometry(QRect(6,16,36,17))
        self.BodyLabel.setText(self.tr("Body:"))

        self.EnergyLabel = QLabel(self.GroupBox2,'EnergyLabel')
        self.EnergyLabel.setGeometry(QRect(6,64,36,17))
        self.EnergyLabel.setText(self.tr("Energy:"))

        self.SlashLabel = QLabel(self.GroupBox2,'SlashLabel')
        self.SlashLabel.setGeometry(QRect(6,151,36,17))
        self.SlashLabel.setText(self.tr("Slash:"))

        self.ThrustLabel = QLabel(self.GroupBox2,'ThrustLabel')
        self.ThrustLabel.setGeometry(QRect(6,134,36,16))
        self.ThrustLabel.setText(self.tr("Thrust:"))

        self.CrushLabel = QLabel(self.GroupBox2,'CrushLabel')
        self.CrushLabel.setGeometry(QRect(6,117,36,17))
        self.CrushLabel.setText(self.tr("Crush:"))

        self.SpiritLabel = QLabel(self.GroupBox2,'SpiritLabel')
        self.SpiritLabel.setGeometry(QRect(6,99,36,17))
        self.SpiritLabel.setText(self.tr("Spirit:"))

        self.Spirit = QLabel(self.GroupBox2,'Spirit')
        self.Spirit.setGeometry(QRect(48,99,17,17))
        self.Spirit.setText(self.tr("0"))

        self.Crush = QLabel(self.GroupBox2,'Crush')
        self.Crush.setGeometry(QRect(48,117,17,17))
        self.Crush.setText(self.tr("0"))

        self.Thrust = QLabel(self.GroupBox2,'Thrust')
        self.Thrust.setGeometry(QRect(48,134,17,16))
        self.Thrust.setText(self.tr("0"))

        self.Slash = QLabel(self.GroupBox2,'Slash')
        self.Slash.setGeometry(QRect(48,151,17,17))
        self.Slash.setText(self.tr("0"))

        self.HeatLabel = QLabel(self.GroupBox2,'HeatLabel')
        self.HeatLabel.setGeometry(QRect(6,48,36,17))
        self.HeatLabel.setText(self.tr("Heat:"))

        self.Heat = QLabel(self.GroupBox2,'Heat')
        self.Heat.setGeometry(QRect(48,48,17,17))
        self.Heat.setText(self.tr("0"))

        self.Energy = QLabel(self.GroupBox2,'Energy')
        self.Energy.setGeometry(QRect(48,64,17,17))
        self.Energy.setText(self.tr("0"))

        self.MatterLabel = QLabel(self.GroupBox2,'MatterLabel')
        self.MatterLabel.setGeometry(QRect(6,81,36,16))
        self.MatterLabel.setText(self.tr("Matter:"))

        self.Matter = QLabel(self.GroupBox2,'Matter')
        self.Matter.setGeometry(QRect(48,81,17,16))
        self.Matter.setText(self.tr("0"))

        self.Body = QLabel(self.GroupBox2,'Body')
        self.Body.setGeometry(QRect(48,16,17,17))
        self.Body.setSizePolicy(QSizePolicy(1,1,self.Body.sizePolicy().hasHeightForWidth()))
        self.Body.setText(self.tr("0"))

        self.ColdLabel = QLabel(self.GroupBox2,'ColdLabel')
        self.ColdLabel.setGeometry(QRect(6,32,36,16))
        self.ColdLabel.setText(self.tr("Cold:"))

        self.Cold = QLabel(self.GroupBox2,'Cold')
        self.Cold.setGeometry(QRect(48,32,17,16))
        self.Cold.setText(self.tr("0"))

        self.BodyRR = QLabel(self.GroupBox2,'BodyRR')
        self.BodyRR.setGeometry(QRect(67,16,17,16))
        self.BodyRR.setText(self.tr("-"))

        self.ColdRR = QLabel(self.GroupBox2,'ColdRR')
        self.ColdRR.setGeometry(QRect(67,32,17,16))
        self.ColdRR.setText(self.tr("-"))

        self.HeatRR = QLabel(self.GroupBox2,'HeatRR')
        self.HeatRR.setGeometry(QRect(67,48,17,16))
        self.HeatRR.setText(self.tr("-"))

        self.EnergyRR = QLabel(self.GroupBox2,'EnergyRR')
        self.EnergyRR.setGeometry(QRect(67,64,17,16))
        self.EnergyRR.setText(self.tr("-"))

        self.MatterRR = QLabel(self.GroupBox2,'MatterRR')
        self.MatterRR.setGeometry(QRect(67,81,17,16))
        self.MatterRR.setText(self.tr("-"))

        self.SpiritRR = QLabel(self.GroupBox2,'SpiritRR')
        self.SpiritRR.setGeometry(QRect(67,99,17,16))
        self.SpiritRR.setText(self.tr("-"))

        self.CrushRR = QLabel(self.GroupBox2,'CrushRR')
        self.CrushRR.setGeometry(QRect(67,117,17,16))
        self.CrushRR.setText(self.tr("-"))

        self.ThrustRR = QLabel(self.GroupBox2,'ThrustRR')
        self.ThrustRR.setGeometry(QRect(67,134,17,16))
        self.ThrustRR.setText(self.tr("-"))

        self.SlashRR = QLabel(self.GroupBox2,'SlashRR')
        self.SlashRR.setGeometry(QRect(67,151,17,16))
        self.SlashRR.setText(self.tr("-"))

        self.OcErrorString = QLabel(self,'OcErrorString')
        self.OcErrorString.setGeometry(QRect(530,205,285,16))
        self.OcErrorString.setText(self.tr(""))

        self.connect(self.JewelTab,SIGNAL('currentChanged(QWidget*)'),self.JewelTabChanged)
        self.connect(self.PlayerMade,SIGNAL('toggled(bool)'),self.PlayerToggled)
        self.connect(self.Drop,SIGNAL('toggled(bool)'),self.DropToggled)
        self.connect(self.PieceTab,SIGNAL('currentChanged(QWidget*)'),self.PieceTabChanged)
        self.connect(self.TypeTab,SIGNAL('currentChanged(QWidget*)'),self.TypeTabChanged)
        self.connect(self.Type_1,SIGNAL('activated(const QString&)'),self.Type_1_Changed)
        self.connect(self.Type_2,SIGNAL('activated(const QString&)'),self.Type_2_Changed)
        self.connect(self.Type_3,SIGNAL('activated(const QString&)'),self.Type_3_Changed)
        self.connect(self.Type_4,SIGNAL('activated(const QString&)'),self.Type_4_Changed)
        self.connect(self.Type_5,SIGNAL('activated(const QString&)'),self.Type_5_Changed)
        self.connect(self.Type_6,SIGNAL('activated(const QString&)'),self.Type_6_Changed)
        self.connect(self.Amount_Drop_1,SIGNAL('activated(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Drop_2,SIGNAL('activated(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Drop_3,SIGNAL('activated(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Drop_4,SIGNAL('activated(const QString&)'),self.AmountChanged)
        self.connect(self.Effect_1,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Effect_2,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Effect_3,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Effect_4,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Effect_5,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Effect_6,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.QualDrop,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.ItemLevel,SIGNAL('textChanged(const QString&)'),self.recalculate)
        self.connect(self.Quality_1,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Quality_2,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Quality_3,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Quality_4,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Quality_5,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Quality_6,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.ClearItem,SIGNAL('clicked()'),self.ClearCurrentItem)
        self.connect(self.Equipped,SIGNAL('clicked()'),self.EquippedClicked)
        self.connect(self.TotalBonus,SIGNAL('clicked()'),self.TotalBonusSet)
        self.connect(self.CapDistance,SIGNAL('clicked()'),self.DistanceCapSet)
        self.connect(self.PushButton11,SIGNAL('clicked()'),self.ItemLevelShow)
        self.connect(self.Amount_Edit_5,SIGNAL('textChanged(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Edit_6,SIGNAL('textChanged(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Edit_1,SIGNAL('textChanged(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Edit_2,SIGNAL('textChanged(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Edit_3,SIGNAL('textChanged(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Edit_4,SIGNAL('textChanged(const QString&)'),self.AmountChanged)
        self.connect(self.LoadItem,SIGNAL('clicked()'),self.Load_Item)
        self.connect(self.SaveItem,SIGNAL('clicked()'),self.Save_Item)
        self.connect(self.CharLevel,SIGNAL('textChanged(const QString&)'),self.recalculate)
        self.connect(self.CraftButton,SIGNAL('clicked()'),self.OpenCraftWindow)
        self.connect(self.MatsButton,SIGNAL('clicked()'),self.OpenMaterialsReport)
        self.connect(self.ConfigButton,SIGNAL('clicked()'),self.OpenConfigReport)
        self.connect(self.SkillsList,SIGNAL('clicked(QListBoxItem*)'),self.SkillClicked)
        self.connect(self.CharClass,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.AFDPS_Edit,SIGNAL('textChanged(const QString&)'),self.recalculate)
        self.connect(self.Speed_Edit,SIGNAL('textChanged(const QString&)'),self.recalculate)
        self.connect(self.Bonus_Edit,SIGNAL('textChanged(const QString&)'),self.recalculate)
        self.connect(self.ItemName,SIGNAL('textChanged(const QString&)'),self.recalculate)
        self.connect(self.Type_7,SIGNAL('activated(const QString&)'),self.Type_7_Changed)
        self.connect(self.Type_8,SIGNAL('activated(const QString&)'),self.Type_8_Changed)
        self.connect(self.Type_9,SIGNAL('activated(const QString&)'),self.Type_9_Changed)
        self.connect(self.Type_10,SIGNAL('activated(const QString&)'),self.Type_10_Changed)
        self.connect(self.Amount_Edit_7,SIGNAL('textChanged(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Edit_8,SIGNAL('textChanged(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Edit_9,SIGNAL('textChanged(const QString&)'),self.AmountChanged)
        self.connect(self.Amount_Edit_10,SIGNAL('textChanged(const QString&)'),self.AmountChanged)
        self.connect(self.Effect_7,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Effect_8,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Effect_9,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.Effect_10,SIGNAL('activated(const QString&)'),self.recalculate)
        self.connect(self.MoreSlots,SIGNAL('clicked()'),self.openMoreSlots)
        self.connect(self.CharRace,SIGNAL('activated(const QString&)'),self.RaceChanged)

        self.setTabOrder(self.QualEdit,self.QualDrop)
        self.setTabOrder(self.QualDrop,self.ItemLevel)
        self.setTabOrder(self.ItemLevel,self.PushButton11)
        self.setTabOrder(self.PushButton11,self.Equipped)
        self.setTabOrder(self.Equipped,self.CraftButton)
        self.setTabOrder(self.CraftButton,self.Type_1)
        self.setTabOrder(self.Type_1,self.Amount_Edit_1)
        self.setTabOrder(self.Amount_Edit_1,self.Amount_Drop_1)
        self.setTabOrder(self.Amount_Drop_1,self.Effect_1)
        self.setTabOrder(self.Effect_1,self.Quality_1)
        self.setTabOrder(self.Quality_1,self.Type_2)
        self.setTabOrder(self.Type_2,self.Amount_Edit_2)
        self.setTabOrder(self.Amount_Edit_2,self.Amount_Drop_2)
        self.setTabOrder(self.Amount_Drop_2,self.Effect_2)
        self.setTabOrder(self.Effect_2,self.Quality_2)
        self.setTabOrder(self.Quality_2,self.Type_3)
        self.setTabOrder(self.Type_3,self.Amount_Edit_3)
        self.setTabOrder(self.Amount_Edit_3,self.Amount_Drop_3)
        self.setTabOrder(self.Amount_Drop_3,self.Effect_3)
        self.setTabOrder(self.Effect_3,self.Quality_3)
        self.setTabOrder(self.Quality_3,self.Type_4)
        self.setTabOrder(self.Type_4,self.Amount_Edit_4)
        self.setTabOrder(self.Amount_Edit_4,self.Amount_Drop_4)
        self.setTabOrder(self.Amount_Drop_4,self.Effect_4)
        self.setTabOrder(self.Effect_4,self.Quality_4)
        self.setTabOrder(self.Quality_4,self.Type_5)
        self.setTabOrder(self.Type_5,self.Amount_Edit_5)
        self.setTabOrder(self.Amount_Edit_5,self.Effect_5)
        self.setTabOrder(self.Effect_5,self.Quality_5)
        self.setTabOrder(self.Quality_5,self.Type_6)
        self.setTabOrder(self.Type_6,self.Amount_Edit_6)
        self.setTabOrder(self.Amount_Edit_6,self.Effect_6)
        self.setTabOrder(self.Effect_6,self.Quality_6)
        self.setTabOrder(self.Quality_6,self.Drop)
        self.setTabOrder(self.Drop,self.LoadItem)
        self.setTabOrder(self.LoadItem,self.SaveItem)
        self.setTabOrder(self.SaveItem,self.ClearItem)
        self.setTabOrder(self.ClearItem,self.ItemName)
        self.setTabOrder(self.ItemName,self.AFDPS_Edit)
        self.setTabOrder(self.AFDPS_Edit,self.Speed_Edit)
        self.setTabOrder(self.Speed_Edit,self.Bonus_Edit)
        self.setTabOrder(self.Bonus_Edit,self.SkillsList)
        self.setTabOrder(self.SkillsList,self.OtherBonusList)
        self.setTabOrder(self.OtherBonusList,self.ConfigButton)
        self.setTabOrder(self.ConfigButton,self.MatsButton)
        self.setTabOrder(self.MatsButton,self.TotalBonus)
        self.setTabOrder(self.TotalBonus,self.CharName)
        self.setTabOrder(self.CharName,self.CharClass)
        self.setTabOrder(self.CharClass,self.CharLevel)
        self.setTabOrder(self.CharLevel,self.TypeTab)
        self.setTabOrder(self.TypeTab,self.PieceTab)
        self.setTabOrder(self.PieceTab,self.JewelTab)

    def event(self,ev):
        ret = QMainWindow.event(self,ev)

        if ev.type() == QEvent.ApplicationFontChange:
            TextLabel3_font = QFont(self.TextLabel3.font())
            TextLabel3_font.setBold(1)
            self.TextLabel3.setFont(TextLabel3_font)
            Version_font = QFont(self.Version.font())
            Version_font.setBold(1)
            self.Version.setFont(Version_font)

        return ret

    def AmountChanged(self,a0):
        print 'B_SC.AmountChanged(const QString&): not implemented yet'

    def ClearCurrentItem(self):
        print 'B_SC.ClearCurrentItem(): not implemented yet'

    def DistanceCapSet(self):
        print 'B_SC.DistanceCapSet(): not implemented yet'

    def DropToggled(self,a0):
        print 'B_SC.DropToggled(bool): not implemented yet'

    def EquippedClicked(self):
        print 'B_SC.EquippedClicked(): not implemented yet'

    def ItemLevelChanged(self,a0):
        print 'B_SC.ItemLevelChanged(const QString&): not implemented yet'

    def ItemLevelShow(self):
        print 'B_SC.ItemLevelShow(): not implemented yet'

    def JewelTabChanged(self,a0):
        print 'B_SC.JewelTabChanged(QWidget*): not implemented yet'

    def Load_Item(self):
        print 'B_SC.Load_Item(): not implemented yet'

    def OpenConfigReport(self):
        print 'B_SC.OpenConfigReport(): not implemented yet'

    def OpenCraftWindow(self):
        print 'B_SC.OpenCraftWindow(): not implemented yet'

    def OpenMaterialsReport(self):
        print 'B_SC.OpenMaterialsReport(): not implemented yet'

    def PieceTabChanged(self,a0):
        print 'B_SC.PieceTabChanged(QWidget*): not implemented yet'

    def PlayerToggled(self,a0):
        print 'B_SC.PlayerToggled(bool): not implemented yet'

    def QualityChanged(self,a0):
        print 'B_SC.QualityChanged(const QString&): not implemented yet'

    def Save_Item(self):
        print 'B_SC.Save_Item(): not implemented yet'

    def SkillClicked(self,a0):
        print 'B_SC.SkillClicked(QListBoxItem*): not implemented yet'

    def TotalBonusSet(self):
        print 'B_SC.TotalBonusSet(): not implemented yet'

    def TypeTabChanged(self,a0):
        print 'B_SC.TypeTabChanged(QWidget*): not implemented yet'

    def Type_10_Changed(self,a0):
        print 'B_SC.Type_10_Changed(const QString&): not implemented yet'

    def Type_1_Changed(self,a0):
        print 'B_SC.Type_1_Changed(const QString&): not implemented yet'

    def Type_2_Changed(self,a0):
        print 'B_SC.Type_2_Changed(const QString&): not implemented yet'

    def Type_3_Changed(self,a0):
        print 'B_SC.Type_3_Changed(const QString&): not implemented yet'

    def Type_4_Changed(self,a0):
        print 'B_SC.Type_4_Changed(const QString&): not implemented yet'

    def Type_5_Changed(self,a0):
        print 'B_SC.Type_5_Changed(const QString&): not implemented yet'

    def Type_6_Changed(self,a0):
        print 'B_SC.Type_6_Changed(const QString&): not implemented yet'

    def Type_7_Changed(self,a0):
        print 'B_SC.Type_7_Changed(const QString&): not implemented yet'

    def Type_8_Changed(self,a0):
        print 'B_SC.Type_8_Changed(const QString&): not implemented yet'

    def Type_9_Changed(self,a0):
        print 'B_SC.Type_9_Changed(const QString&): not implemented yet'

    def newFile(self):
        print 'B_SC.newFile(): not implemented yet'

    def RaceChanged(self,a0):
        print 'B_SC.RaceChanged(const QString&): not implemented yet'

    def openMoreSlots(self):
        print 'B_SC.openMoreSlots(): not implemented yet'

    def recalculate(self,a0):
        print 'B_SC.recalculate(const QString&): not implemented yet'

    def saveFile(self):
        print 'B_SC.saveFile(): not implemented yet'
