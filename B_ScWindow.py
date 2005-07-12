# Form implementation generated from reading ui file 'ScWindow.ui'
#
# Created: Sat Mar 12 23:31:30 2005
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

        self.resize(782,521)
        f = QFont(self.font())
        f.setFamily('Arial')
        f.setPointSize(8)
        self.setFont(f)
        self.setCaption(self.tr("Spellcrafting Calculator"))

        self.GroupBox9 = QGroupBox(self,'GroupBox9')
        self.GroupBox9.setGeometry(QRect(613,3,165,111))
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

        self.ButtonGroup2 = QButtonGroup(self,'ButtonGroup2')
        self.ButtonGroup2.setGeometry(QRect(613,114,165,51))
        self.ButtonGroup2.setTitle(self.tr("Display"))

        self.TotalBonus = QRadioButton(self.ButtonGroup2,'TotalBonus')
        self.TotalBonus.setGeometry(QRect(11,15,85,17))
        self.TotalBonus.setText(self.tr("Total Bonus"))
        self.TotalBonus.setChecked(1)

        self.CapDistance = QRadioButton(self.ButtonGroup2,'CapDistance')
        self.CapDistance.setGeometry(QRect(11,32,109,17))
        self.CapDistance.setText(self.tr("Distance To Cap"))

        self.GroupBox1 = QGroupBox(self,'GroupBox1')
        self.GroupBox1.setGeometry(QRect(5,3,85,182))
        self.GroupBox1.setTitle(self.tr("Stats"))

        self.StrengthLabel = QLabel(self.GroupBox1,'StrengthLabel')
        self.StrengthLabel.setGeometry(QRect(6,16,28,16))
        self.StrengthLabel.setText(self.tr("STR:"))

        self.Strength = QLabel(self.GroupBox1,'Strength')
        self.Strength.setGeometry(QRect(35,16,20,16))
        self.Strength.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Strength.setText(self.tr("0"))

        self.StrengthCap = QLabel(self.GroupBox1,'StrengthCap')
        self.StrengthCap.setGeometry(QRect(57,16,20,16))
        self.StrengthCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.StrengthCap.setText(self.tr("-"))

        self.ConstitutionLabel = QLabel(self.GroupBox1,'ConstitutionLabel')
        self.ConstitutionLabel.setGeometry(QRect(6,32,28,16))
        self.ConstitutionLabel.setText(self.tr("CON:"))

        self.Constitution = QLabel(self.GroupBox1,'Constitution')
        self.Constitution.setGeometry(QRect(35,32,20,16))
        self.Constitution.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Constitution.setText(self.tr("0"))

        self.ConstitutionCap = QLabel(self.GroupBox1,'ConstitutionCap')
        self.ConstitutionCap.setGeometry(QRect(57,32,20,16))
        self.ConstitutionCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.ConstitutionCap.setText(self.tr("-"))

        self.DexterityLabel = QLabel(self.GroupBox1,'DexterityLabel')
        self.DexterityLabel.setGeometry(QRect(6,48,28,16))
        self.DexterityLabel.setText(self.tr("DEX:"))

        self.Dexterity = QLabel(self.GroupBox1,'Dexterity')
        self.Dexterity.setGeometry(QRect(35,48,20,16))
        self.Dexterity.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Dexterity.setText(self.tr("0"))

        self.DexterityCap = QLabel(self.GroupBox1,'DexterityCap')
        self.DexterityCap.setGeometry(QRect(57,48,20,16))
        self.DexterityCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.DexterityCap.setText(self.tr("-"))

        self.QuicknessLabel = QLabel(self.GroupBox1,'QuicknessLabel')
        self.QuicknessLabel.setGeometry(QRect(6,64,28,16))
        self.QuicknessLabel.setText(self.tr("QUI:"))

        self.Quickness = QLabel(self.GroupBox1,'Quickness')
        self.Quickness.setGeometry(QRect(35,64,20,16))
        self.Quickness.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Quickness.setText(self.tr("0"))

        self.QuicknessCap = QLabel(self.GroupBox1,'QuicknessCap')
        self.QuicknessCap.setGeometry(QRect(57,64,20,16))
        self.QuicknessCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.QuicknessCap.setText(self.tr("-"))

        self.IntelligenceLabel = QLabel(self.GroupBox1,'IntelligenceLabel')
        self.IntelligenceLabel.setGeometry(QRect(6,80,28,16))
        self.IntelligenceLabel.setText(self.tr("INT:"))

        self.Intelligence = QLabel(self.GroupBox1,'Intelligence')
        self.Intelligence.setGeometry(QRect(35,80,20,16))
        self.Intelligence.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Intelligence.setText(self.tr("0"))

        self.IntelligenceCap = QLabel(self.GroupBox1,'IntelligenceCap')
        self.IntelligenceCap.setGeometry(QRect(57,80,20,16))
        self.IntelligenceCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.IntelligenceCap.setText(self.tr("-"))

        self.PietyLabel = QLabel(self.GroupBox1,'PietyLabel')
        self.PietyLabel.setGeometry(QRect(6,96,28,16))
        self.PietyLabel.setText(self.tr("PIE:"))

        self.Piety = QLabel(self.GroupBox1,'Piety')
        self.Piety.setGeometry(QRect(35,96,20,16))
        self.Piety.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Piety.setText(self.tr("0"))

        self.PietyCap = QLabel(self.GroupBox1,'PietyCap')
        self.PietyCap.setGeometry(QRect(57,96,20,16))
        self.PietyCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.PietyCap.setText(self.tr("-"))

        self.CharismaLabel = QLabel(self.GroupBox1,'CharismaLabel')
        self.CharismaLabel.setGeometry(QRect(6,112,28,16))
        self.CharismaLabel.setText(self.tr("CHA:"))

        self.Charisma = QLabel(self.GroupBox1,'Charisma')
        self.Charisma.setGeometry(QRect(35,112,20,16))
        self.Charisma.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Charisma.setText(self.tr("0"))

        self.CharismaCap = QLabel(self.GroupBox1,'CharismaCap')
        self.CharismaCap.setGeometry(QRect(57,112,20,16))
        self.CharismaCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.CharismaCap.setText(self.tr("-"))

        self.EmpathyLabel = QLabel(self.GroupBox1,'EmpathyLabel')
        self.EmpathyLabel.setGeometry(QRect(6,128,28,16))
        self.EmpathyLabel.setText(self.tr("EMP:"))

        self.Empathy = QLabel(self.GroupBox1,'Empathy')
        self.Empathy.setGeometry(QRect(35,128,20,16))
        self.Empathy.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Empathy.setText(self.tr("0"))

        self.EmpathyCap = QLabel(self.GroupBox1,'EmpathyCap')
        self.EmpathyCap.setGeometry(QRect(57,128,20,16))
        self.EmpathyCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.EmpathyCap.setText(self.tr("-"))

        self.PowerLabel = QLabel(self.GroupBox1,'PowerLabel')
        self.PowerLabel.setGeometry(QRect(6,144,28,16))
        self.PowerLabel.setText(self.tr("Pow:"))

        self.Power = QLabel(self.GroupBox1,'Power')
        self.Power.setGeometry(QRect(35,144,20,16))
        self.Power.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Power.setText(self.tr("0"))

        self.PowerCap = QLabel(self.GroupBox1,'PowerCap')
        self.PowerCap.setGeometry(QRect(57,144,20,16))
        self.PowerCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.PowerCap.setText(self.tr("-"))

        self.HitsLabel = QLabel(self.GroupBox1,'HitsLabel')
        self.HitsLabel.setGeometry(QRect(6,160,20,16))
        self.HitsLabel.setText(self.tr("Hits:"))

        self.Hits = QLabel(self.GroupBox1,'Hits')
        self.Hits.setGeometry(QRect(27,160,20,16))
        self.Hits.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Hits.setText(self.tr("0"))

        self.HitsCap = QLabel(self.GroupBox1,'HitsCap')
        self.HitsCap.setGeometry(QRect(49,160,28,16))
        self.HitsCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.HitsCap.setText(self.tr("-"))

        self.GroupBox5 = QGroupBox(self,'GroupBox5')
        self.GroupBox5.setGeometry(QRect(182,137,135,48))
        self.GroupBox5.setTitle(self.tr("Totals"))

        self.TotalCostLabel = QLabel(self.GroupBox5,'TotalCostLabel')
        self.TotalCostLabel.setGeometry(QRect(6,13,29,16))
        self.TotalCostLabel.setText(self.tr("Cost:"))

        self.TotalCost = QLabel(self.GroupBox5,'TotalCost')
        self.TotalCost.setGeometry(QRect(45,14,86,16))
        self.TotalCost.setText(self.tr("0"))

        self.TotalPriceLabel = QLabel(self.GroupBox5,'TotalPriceLabel')
        self.TotalPriceLabel.setGeometry(QRect(6,29,37,16))
        self.TotalPriceLabel.setText(self.tr("Price:"))

        self.TotalPrice = QLabel(self.GroupBox5,'TotalPrice')
        self.TotalPrice.setGeometry(QRect(45,29,85,16))
        self.TotalPrice.setText(self.tr("0"))

        self.GroupBox4 = QGroupBox(self,'GroupBox4')
        self.GroupBox4.setGeometry(QRect(182,3,135,136))
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
        self.GroupBox2.setGeometry(QRect(91,3,90,182))
        self.GroupBox2.setTitle(self.tr("Resists"))

        self.BodyLabel = QLabel(self.GroupBox2,'BodyLabel')
        self.BodyLabel.setGeometry(QRect(6,16,36,16))
        self.BodyLabel.setText(self.tr("Body:"))

        self.Body = QLabel(self.GroupBox2,'Body')
        self.Body.setGeometry(QRect(44,16,17,16))
        self.Body.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Body.setText(self.tr("0"))

        self.BodyRR = QLabel(self.GroupBox2,'BodyRR')
        self.BodyRR.setGeometry(QRect(67,16,17,16))
        self.BodyRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.BodyRR.setText(self.tr("-"))

        self.ColdLabel = QLabel(self.GroupBox2,'ColdLabel')
        self.ColdLabel.setGeometry(QRect(6,34,36,16))
        self.ColdLabel.setText(self.tr("Cold:"))

        self.Cold = QLabel(self.GroupBox2,'Cold')
        self.Cold.setGeometry(QRect(44,34,17,16))
        self.Cold.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Cold.setText(self.tr("0"))

        self.ColdRR = QLabel(self.GroupBox2,'ColdRR')
        self.ColdRR.setGeometry(QRect(67,34,17,16))
        self.ColdRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.ColdRR.setText(self.tr("-"))

        self.HeatLabel = QLabel(self.GroupBox2,'HeatLabel')
        self.HeatLabel.setGeometry(QRect(6,52,36,16))
        self.HeatLabel.setText(self.tr("Heat:"))

        self.Heat = QLabel(self.GroupBox2,'Heat')
        self.Heat.setGeometry(QRect(44,52,17,16))
        self.Heat.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Heat.setText(self.tr("0"))

        self.HeatRR = QLabel(self.GroupBox2,'HeatRR')
        self.HeatRR.setGeometry(QRect(67,52,17,16))
        self.HeatRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.HeatRR.setText(self.tr("-"))

        self.EnergyLabel = QLabel(self.GroupBox2,'EnergyLabel')
        self.EnergyLabel.setGeometry(QRect(6,70,36,16))
        self.EnergyLabel.setText(self.tr("Energy:"))

        self.Energy = QLabel(self.GroupBox2,'Energy')
        self.Energy.setGeometry(QRect(44,70,17,16))
        self.Energy.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Energy.setText(self.tr("0"))

        self.EnergyRR = QLabel(self.GroupBox2,'EnergyRR')
        self.EnergyRR.setGeometry(QRect(67,70,17,16))
        self.EnergyRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.EnergyRR.setText(self.tr("-"))

        self.MatterLabel = QLabel(self.GroupBox2,'MatterLabel')
        self.MatterLabel.setGeometry(QRect(6,88,36,16))
        self.MatterLabel.setText(self.tr("Matter:"))

        self.Matter = QLabel(self.GroupBox2,'Matter')
        self.Matter.setGeometry(QRect(44,88,17,16))
        self.Matter.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Matter.setText(self.tr("0"))

        self.MatterRR = QLabel(self.GroupBox2,'MatterRR')
        self.MatterRR.setGeometry(QRect(67,88,17,16))
        self.MatterRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.MatterRR.setText(self.tr("-"))

        self.SpiritLabel = QLabel(self.GroupBox2,'SpiritLabel')
        self.SpiritLabel.setGeometry(QRect(6,106,36,16))
        self.SpiritLabel.setText(self.tr("Spirit:"))

        self.Spirit = QLabel(self.GroupBox2,'Spirit')
        self.Spirit.setGeometry(QRect(44,106,17,16))
        self.Spirit.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Spirit.setText(self.tr("0"))

        self.SpiritRR = QLabel(self.GroupBox2,'SpiritRR')
        self.SpiritRR.setGeometry(QRect(67,106,17,16))
        self.SpiritRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.SpiritRR.setText(self.tr("-"))

        self.CrushLabel = QLabel(self.GroupBox2,'CrushLabel')
        self.CrushLabel.setGeometry(QRect(6,124,36,16))
        self.CrushLabel.setText(self.tr("Crush:"))

        self.Crush = QLabel(self.GroupBox2,'Crush')
        self.Crush.setGeometry(QRect(44,124,17,16))
        self.Crush.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Crush.setText(self.tr("0"))

        self.CrushRR = QLabel(self.GroupBox2,'CrushRR')
        self.CrushRR.setGeometry(QRect(67,124,17,16))
        self.CrushRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.CrushRR.setText(self.tr("-"))

        self.ThrustLabel = QLabel(self.GroupBox2,'ThrustLabel')
        self.ThrustLabel.setGeometry(QRect(6,142,36,16))
        self.ThrustLabel.setText(self.tr("Thrust:"))

        self.Thrust = QLabel(self.GroupBox2,'Thrust')
        self.Thrust.setGeometry(QRect(44,142,17,16))
        self.Thrust.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Thrust.setText(self.tr("0"))

        self.ThrustRR = QLabel(self.GroupBox2,'ThrustRR')
        self.ThrustRR.setGeometry(QRect(67,142,17,16))
        self.ThrustRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.ThrustRR.setText(self.tr("-"))

        self.SlashLabel = QLabel(self.GroupBox2,'SlashLabel')
        self.SlashLabel.setGeometry(QRect(6,160,36,16))
        self.SlashLabel.setText(self.tr("Slash:"))

        self.Slash = QLabel(self.GroupBox2,'Slash')
        self.Slash.setGeometry(QRect(44,160,17,16))
        self.Slash.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.Slash.setText(self.tr("0"))

        self.SlashRR = QLabel(self.GroupBox2,'SlashRR')
        self.SlashRR.setGeometry(QRect(67,160,17,16))
        self.SlashRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)
        self.SlashRR.setText(self.tr("-"))

        self.GroupSkillsList = QGroupBox(self,'GroupSkillsList')
        self.GroupSkillsList.setGeometry(QRect(318,3,129,136))
        self.GroupSkillsList.setTitle(self.tr("Skills"))

        self.SkillsList = QListBox(self.GroupSkillsList,'SkillsList')
        self.SkillsList.setGeometry(QRect(8,15,115,116))

        self.GroupOtherBonusList = QGroupBox(self,'GroupOtherBonusList')
        self.GroupOtherBonusList.setGeometry(QRect(449,3,163,136))
        self.GroupOtherBonusList.setTitle(self.tr("Other Bonuses"))

        self.OtherBonusList = QListBox(self.GroupOtherBonusList,'OtherBonusList')
        self.OtherBonusList.setGeometry(QRect(3,15,154,116))

        self.FileNameLabel = QLabel(self,'FileNameLabel')
        self.FileNameLabel.setGeometry(QRect(325,142,285,14))
        self.FileNameLabel.setText(self.tr(""))

        self.OcErrorString = QLabel(self,'OcErrorString')
        self.OcErrorString.setGeometry(QRect(325,157,285,14))
        self.OcErrorString.setText(self.tr(""))

        self.DupErrorString = QLabel(self,'DupErrorString')
        self.DupErrorString.setGeometry(QRect(325,173,285,14))
        self.DupErrorString.setText(self.tr(""))

        self.TypeTab = QTabWidget(self,'TypeTab')
        self.TypeTab.setGeometry(QRect(2,190,776,313))

        self.Armor = QWidget(self.TypeTab,'Armor')

        self.PieceTab = QTabWidget(self.Armor,'PieceTab')
        self.PieceTab.setGeometry(QRect(1,0,777,294))

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

        self.JewelTab = QTabWidget(self.Jewelry,'JewelTab')
        self.JewelTab.setGeometry(QRect(1,0,777,294))

        self.Neck = QWidget(self.JewelTab,'Neck')

        self.ItemLevelLabel = QLabel(self.Neck,'ItemLevelLabel')
        self.ItemLevelLabel.setGeometry(QRect(7,2,59,22))
        self.ItemLevelLabel.setText(self.tr("Item Level:"))

        self.ItemLevel = QLineEdit(self.Neck,'ItemLevel')
        self.ItemLevel.setGeometry(QRect(63,2,35,22))

        self.ItemLevelButton = QPushButton(self.Neck,'ItemLevelButton')
        self.ItemLevelButton.setGeometry(QRect(98,4,18,18))
        self.ItemLevelButton.setText(self.tr("..."))

        self.ItemQualityLabel = QLabel(self.Neck,'ItemQualityLabel')
        self.ItemQualityLabel.setGeometry(QRect(136,2,50,22))
        self.ItemQualityLabel.setText(self.tr("Quality:"))

        self.QualEdit = QLineEdit(self.Neck,'QualEdit')
        self.QualEdit.setGeometry(QRect(177,2,51,22))

        self.QualDrop = SearchingCombo(0,self.Neck,'QualDrop')
        self.QualDrop.insertItem(self.tr("94"))
        self.QualDrop.insertItem(self.tr("95"))
        self.QualDrop.insertItem(self.tr("96"))
        self.QualDrop.insertItem(self.tr("97"))
        self.QualDrop.insertItem(self.tr("98"))
        self.QualDrop.insertItem(self.tr("99"))
        self.QualDrop.insertItem(self.tr("100"))
        self.QualDrop.setGeometry(QRect(177,2,52,22))

        self.Bonus_Label = QLabel(self.Neck,'Bonus_Label')
        self.Bonus_Label.setGeometry(QRect(244,2,40,22))
        self.Bonus_Label.setText(self.tr("Bonus:"))

        self.Bonus_Edit = QLineEdit(self.Neck,'Bonus_Edit')
        self.Bonus_Edit.setGeometry(QRect(284,2,35,22))

        self.AFDPS_Label = QLabel(self.Neck,'AFDPS_Label')
        self.AFDPS_Label.setGeometry(QRect(330,2,55,22))
        self.AFDPS_Label.setText(self.tr("AF/DPS:"))

        self.AFDPS_Edit = QLineEdit(self.Neck,'AFDPS_Edit')
        self.AFDPS_Edit.setGeometry(QRect(375,2,35,22))

        self.Speed_Label = QLabel(self.Neck,'Speed_Label')
        self.Speed_Label.setGeometry(QRect(420,2,40,22))
        self.Speed_Label.setText(self.tr("Speed:"))

        self.Speed_Edit = QLineEdit(self.Neck,'Speed_Edit')
        self.Speed_Edit.setGeometry(QRect(460,2,35,22))

        self.Utility_Label = QLabel(self.Neck,'Utility_Label')
        self.Utility_Label.setGeometry(QRect(507,2,35,16))
        self.Utility_Label.setText(self.tr("Utility:"))

        self.Utility = QLabel(self.Neck,'Utility')
        self.Utility.setGeometry(QRect(545,2,28,16))
        self.Utility.setText(self.tr("0.0"))

        self.TotalUtility = QLabel(self.Neck,'TotalUtility')
        self.TotalUtility.setGeometry(QRect(545,17,73,14))
        self.TotalUtility.setText(self.tr("0.0"))

        self.Total_Label = QLabel(self.Neck,'Total_Label')
        self.Total_Label.setGeometry(QRect(507,17,34,14))
        self.Total_Label.setText(self.tr("Total:"))

        self.Equipped = QCheckBox(self.Neck,'Equipped')
        self.Equipped.setGeometry(QRect(579,2,71,22))
        self.Equipped.setText(self.tr("Equipped"))

        self.Type_Label = QLabel(self.Neck,'Type_Label')
        self.Type_Label.setGeometry(QRect(50,33,119,14))
        self.Type_Label.setText(self.tr("Type"))

        self.Amount_Label = QLabel(self.Neck,'Amount_Label')
        self.Amount_Label.setGeometry(QRect(181,33,44,14))
        self.Amount_Label.setText(self.tr("Amount"))

        self.Effect_Label = QLabel(self.Neck,'Effect_Label')
        self.Effect_Label.setGeometry(QRect(237,33,142,14))
        self.Effect_Label.setText(self.tr("Effect"))

        self.Quality_Label = QLabel(self.Neck,'Quality_Label')
        self.Quality_Label.setGeometry(QRect(391,33,44,14))
        self.Quality_Label.setText(self.tr("Quality"))

        self.Points_Label = QLabel(self.Neck,'Points_Label')
        self.Points_Label.setGeometry(QRect(443,33,35,14))
        self.Points_Label.setText(self.tr("Points"))
        self.Points_Label.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_Label = QLabel(self.Neck,'Cost_Label')
        self.Cost_Label.setGeometry(QRect(482,33,70,14))
        self.Cost_Label.setText(self.tr("Cost"))
        self.Cost_Label.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_Label = QLabel(self.Neck,'Name_Label')
        self.Name_Label.setGeometry(QRect(562,33,200,14))
        self.Name_Label.setText(self.tr("Name"))

        self.Gem_Label_1 = QLabel(self.Neck,'Gem_Label_1')
        self.Gem_Label_1.setGeometry(QRect(7,48,34,22))
        self.Gem_Label_1.setText(self.tr("Gem 1:"))

        self.Type_1 = SearchingCombo(0,self.Neck,'Type_1')
        self.Type_1.insertItem(self.tr("Unused"))
        self.Type_1.insertItem(self.tr("Stat"))
        self.Type_1.insertItem(self.tr("Resist"))
        self.Type_1.insertItem(self.tr("Hits"))
        self.Type_1.insertItem(self.tr("Power"))
        self.Type_1.insertItem(self.tr("Focus"))
        self.Type_1.insertItem(self.tr("Skill"))
        self.Type_1.setGeometry(QRect(46,48,127,22))

        self.Amount_Edit_1 = QLineEdit(self.Neck,'Amount_Edit_1')
        self.Amount_Edit_1.setGeometry(QRect(177,48,51,22))

        self.Amount_Drop_1 = SearchingCombo(0,self.Neck,'Amount_Drop_1')
        self.Amount_Drop_1.setGeometry(QRect(177,48,52,22))

        self.Effect_1 = SearchingCombo(0,self.Neck,'Effect_1')
        self.Effect_1.setGeometry(QRect(233,48,150,22))

        self.Quality_1 = SearchingCombo(0,self.Neck,'Quality_1')
        self.Quality_1.setGeometry(QRect(387,48,52,22))

        self.Points_1 = QLabel(self.Neck,'Points_1')
        self.Points_1.setGeometry(QRect(443,48,35,22))
        self.Points_1.setText(self.tr("0.0"))
        self.Points_1.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_1 = QLabel(self.Neck,'Cost_1')
        self.Cost_1.setGeometry(QRect(482,48,70,22))
        self.Cost_1.setText(self.tr("0c"))
        self.Cost_1.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_1 = QLabel(self.Neck,'Name_1')
        self.Name_1.setGeometry(QRect(562,48,200,22))
        self.Name_1.setText(self.tr(""))

        self.Gem_Label_2 = QLabel(self.Neck,'Gem_Label_2')
        self.Gem_Label_2.setGeometry(QRect(7,69,34,22))
        self.Gem_Label_2.setText(self.tr("Gem 2:"))

        self.Amount_Edit_2 = QLineEdit(self.Neck,'Amount_Edit_2')
        self.Amount_Edit_2.setGeometry(QRect(177,69,51,22))

        self.Amount_Drop_2 = SearchingCombo(0,self.Neck,'Amount_Drop_2')
        self.Amount_Drop_2.setGeometry(QRect(177,69,52,22))

        self.Type_2 = SearchingCombo(0,self.Neck,'Type_2')
        self.Type_2.insertItem(self.tr("Unused"))
        self.Type_2.insertItem(self.tr("Stat"))
        self.Type_2.insertItem(self.tr("Resist"))
        self.Type_2.insertItem(self.tr("Hits"))
        self.Type_2.insertItem(self.tr("Power"))
        self.Type_2.insertItem(self.tr("Focus"))
        self.Type_2.insertItem(self.tr("Skill"))
        self.Type_2.setGeometry(QRect(46,69,127,22))

        self.Effect_2 = SearchingCombo(0,self.Neck,'Effect_2')
        self.Effect_2.setGeometry(QRect(233,69,150,22))

        self.Quality_2 = SearchingCombo(0,self.Neck,'Quality_2')
        self.Quality_2.setGeometry(QRect(387,69,52,22))

        self.Points_2 = QLabel(self.Neck,'Points_2')
        self.Points_2.setGeometry(QRect(443,69,35,22))
        self.Points_2.setText(self.tr("0.0"))
        self.Points_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_2 = QLabel(self.Neck,'Cost_2')
        self.Cost_2.setGeometry(QRect(482,69,70,22))
        self.Cost_2.setText(self.tr("0c"))
        self.Cost_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_2 = QLabel(self.Neck,'Name_2')
        self.Name_2.setGeometry(QRect(562,69,200,22))
        self.Name_2.setText(self.tr(""))

        self.Gem_Label_3 = QLabel(self.Neck,'Gem_Label_3')
        self.Gem_Label_3.setGeometry(QRect(7,90,34,22))
        self.Gem_Label_3.setText(self.tr("Gem 3:"))

        self.Type_3 = SearchingCombo(0,self.Neck,'Type_3')
        self.Type_3.insertItem(self.tr("Unused"))
        self.Type_3.insertItem(self.tr("Stat"))
        self.Type_3.insertItem(self.tr("Resist"))
        self.Type_3.insertItem(self.tr("Hits"))
        self.Type_3.insertItem(self.tr("Power"))
        self.Type_3.insertItem(self.tr("Focus"))
        self.Type_3.insertItem(self.tr("Skill"))
        self.Type_3.setGeometry(QRect(46,90,127,22))

        self.Amount_Edit_3 = QLineEdit(self.Neck,'Amount_Edit_3')
        self.Amount_Edit_3.setGeometry(QRect(177,90,51,22))

        self.Amount_Drop_3 = SearchingCombo(0,self.Neck,'Amount_Drop_3')
        self.Amount_Drop_3.setGeometry(QRect(177,90,52,22))

        self.Effect_3 = SearchingCombo(0,self.Neck,'Effect_3')
        self.Effect_3.setGeometry(QRect(233,90,150,22))

        self.Quality_3 = SearchingCombo(0,self.Neck,'Quality_3')
        self.Quality_3.setGeometry(QRect(387,90,52,22))

        self.Points_3 = QLabel(self.Neck,'Points_3')
        self.Points_3.setGeometry(QRect(443,90,35,22))
        self.Points_3.setText(self.tr("0.0"))
        self.Points_3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_3 = QLabel(self.Neck,'Cost_3')
        self.Cost_3.setGeometry(QRect(482,90,70,22))
        self.Cost_3.setText(self.tr("0c"))
        self.Cost_3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_3 = QLabel(self.Neck,'Name_3')
        self.Name_3.setGeometry(QRect(562,90,200,22))
        self.Name_3.setText(self.tr(""))

        self.Gem_Label_4 = QLabel(self.Neck,'Gem_Label_4')
        self.Gem_Label_4.setGeometry(QRect(7,111,34,22))
        self.Gem_Label_4.setText(self.tr("Gem 4:"))

        self.Type_4 = SearchingCombo(0,self.Neck,'Type_4')
        self.Type_4.insertItem(self.tr("Unused"))
        self.Type_4.insertItem(self.tr("Stat"))
        self.Type_4.insertItem(self.tr("Resist"))
        self.Type_4.insertItem(self.tr("Hits"))
        self.Type_4.insertItem(self.tr("Power"))
        self.Type_4.insertItem(self.tr("Focus"))
        self.Type_4.insertItem(self.tr("Skill"))
        self.Type_4.setGeometry(QRect(46,111,127,22))

        self.Amount_Edit_4 = QLineEdit(self.Neck,'Amount_Edit_4')
        self.Amount_Edit_4.setGeometry(QRect(177,111,51,22))

        self.Amount_Drop_4 = SearchingCombo(0,self.Neck,'Amount_Drop_4')
        self.Amount_Drop_4.setGeometry(QRect(177,111,52,22))

        self.Effect_4 = SearchingCombo(0,self.Neck,'Effect_4')
        self.Effect_4.setGeometry(QRect(233,111,150,22))

        self.Quality_4 = SearchingCombo(0,self.Neck,'Quality_4')
        self.Quality_4.setGeometry(QRect(387,111,52,22))

        self.Points_4 = QLabel(self.Neck,'Points_4')
        self.Points_4.setGeometry(QRect(443,111,35,22))
        self.Points_4.setText(self.tr("0.0"))
        self.Points_4.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_4 = QLabel(self.Neck,'Cost_4')
        self.Cost_4.setGeometry(QRect(482,111,70,22))
        self.Cost_4.setText(self.tr("0c"))
        self.Cost_4.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_4 = QLabel(self.Neck,'Name_4')
        self.Name_4.setGeometry(QRect(562,111,200,22))
        self.Name_4.setText(self.tr(""))

        self.Gem_Label_5 = QLabel(self.Neck,'Gem_Label_5')
        self.Gem_Label_5.setGeometry(QRect(7,132,34,22))
        self.Gem_Label_5.setText(self.tr("Gem 5:"))

        self.Type_5 = SearchingCombo(0,self.Neck,'Type_5')
        self.Type_5.insertItem(self.tr("Unused"))
        self.Type_5.insertItem(self.tr("Stat"))
        self.Type_5.insertItem(self.tr("Resist"))
        self.Type_5.insertItem(self.tr("Hits"))
        self.Type_5.insertItem(self.tr("Power"))
        self.Type_5.insertItem(self.tr("Focus"))
        self.Type_5.insertItem(self.tr("Skill"))
        self.Type_5.setGeometry(QRect(46,132,127,22))

        self.Amount_Edit_5 = QLineEdit(self.Neck,'Amount_Edit_5')
        self.Amount_Edit_5.setGeometry(QRect(177,132,51,22))

        self.Effect_5 = SearchingCombo(0,self.Neck,'Effect_5')
        self.Effect_5.setGeometry(QRect(233,132,150,22))

        self.Gem_Label_6 = QLabel(self.Neck,'Gem_Label_6')
        self.Gem_Label_6.setGeometry(QRect(7,153,34,22))
        self.Gem_Label_6.setText(self.tr("Gem 6:"))

        self.Type_6 = SearchingCombo(0,self.Neck,'Type_6')
        self.Type_6.insertItem(self.tr("Unused"))
        self.Type_6.insertItem(self.tr("Stat"))
        self.Type_6.insertItem(self.tr("Resist"))
        self.Type_6.insertItem(self.tr("Hits"))
        self.Type_6.insertItem(self.tr("Power"))
        self.Type_6.insertItem(self.tr("Focus"))
        self.Type_6.insertItem(self.tr("Skill"))
        self.Type_6.setGeometry(QRect(46,153,127,22))

        self.Amount_Edit_6 = QLineEdit(self.Neck,'Amount_Edit_6')
        self.Amount_Edit_6.setGeometry(QRect(177,153,51,22))

        self.Effect_6 = SearchingCombo(0,self.Neck,'Effect_6')
        self.Effect_6.setGeometry(QRect(233,153,150,22))

        self.Gem_Label_7 = QLabel(self.Neck,'Gem_Label_7')
        self.Gem_Label_7.setGeometry(QRect(7,174,34,22))
        self.Gem_Label_7.setText(self.tr("Gem 7:"))

        self.Type_7 = SearchingCombo(0,self.Neck,'Type_7')
        self.Type_7.insertItem(self.tr("Unused"))
        self.Type_7.insertItem(self.tr("Stat"))
        self.Type_7.insertItem(self.tr("Resist"))
        self.Type_7.insertItem(self.tr("Hits"))
        self.Type_7.insertItem(self.tr("Power"))
        self.Type_7.insertItem(self.tr("Focus"))
        self.Type_7.insertItem(self.tr("Skill"))
        self.Type_7.setGeometry(QRect(46,174,127,22))

        self.Amount_Edit_7 = QLineEdit(self.Neck,'Amount_Edit_7')
        self.Amount_Edit_7.setGeometry(QRect(177,174,51,22))

        self.Effect_7 = SearchingCombo(0,self.Neck,'Effect_7')
        self.Effect_7.setGeometry(QRect(233,174,150,22))

        self.Gem_Label_8 = QLabel(self.Neck,'Gem_Label_8')
        self.Gem_Label_8.setGeometry(QRect(7,195,34,22))
        self.Gem_Label_8.setText(self.tr("Gem 8:"))

        self.Type_8 = SearchingCombo(0,self.Neck,'Type_8')
        self.Type_8.insertItem(self.tr("Unused"))
        self.Type_8.insertItem(self.tr("Stat"))
        self.Type_8.insertItem(self.tr("Resist"))
        self.Type_8.insertItem(self.tr("Hits"))
        self.Type_8.insertItem(self.tr("Power"))
        self.Type_8.insertItem(self.tr("Focus"))
        self.Type_8.insertItem(self.tr("Skill"))
        self.Type_8.setGeometry(QRect(46,195,127,22))

        self.Amount_Edit_8 = QLineEdit(self.Neck,'Amount_Edit_8')
        self.Amount_Edit_8.setGeometry(QRect(177,195,51,22))

        self.Effect_8 = SearchingCombo(0,self.Neck,'Effect_8')
        self.Effect_8.setGeometry(QRect(233,195,150,22))

        self.Gem_Label_9 = QLabel(self.Neck,'Gem_Label_9')
        self.Gem_Label_9.setGeometry(QRect(7,216,34,22))
        self.Gem_Label_9.setText(self.tr("Gem 9:"))

        self.Type_9 = SearchingCombo(0,self.Neck,'Type_9')
        self.Type_9.insertItem(self.tr("Unused"))
        self.Type_9.insertItem(self.tr("Stat"))
        self.Type_9.insertItem(self.tr("Resist"))
        self.Type_9.insertItem(self.tr("Hits"))
        self.Type_9.insertItem(self.tr("Power"))
        self.Type_9.insertItem(self.tr("Focus"))
        self.Type_9.insertItem(self.tr("Skill"))
        self.Type_9.setGeometry(QRect(46,216,127,22))

        self.Amount_Edit_9 = QLineEdit(self.Neck,'Amount_Edit_9')
        self.Amount_Edit_9.setGeometry(QRect(177,216,51,22))

        self.Effect_9 = SearchingCombo(0,self.Neck,'Effect_9')
        self.Effect_9.setGeometry(QRect(233,216,150,22))

        self.Gem_Label_10 = QLabel(self.Neck,'Gem_Label_10')
        self.Gem_Label_10.setGeometry(QRect(7,237,41,22))
        self.Gem_Label_10.setText(self.tr("Gem10:"))

        self.Type_10 = SearchingCombo(0,self.Neck,'Type_10')
        self.Type_10.insertItem(self.tr("Unused"))
        self.Type_10.insertItem(self.tr("Stat"))
        self.Type_10.insertItem(self.tr("Resist"))
        self.Type_10.insertItem(self.tr("Hits"))
        self.Type_10.insertItem(self.tr("Power"))
        self.Type_10.insertItem(self.tr("Focus"))
        self.Type_10.insertItem(self.tr("Skill"))
        self.Type_10.setGeometry(QRect(46,237,127,22))

        self.Amount_Edit_10 = QLineEdit(self.Neck,'Amount_Edit_10')
        self.Amount_Edit_10.setGeometry(QRect(177,237,51,22))

        self.Effect_10 = SearchingCombo(0,self.Neck,'Effect_10')
        self.Effect_10.setGeometry(QRect(233,237,150,22))

        self.Imbue_Label = QLabel(self.Neck,'Imbue_Label')
        self.Imbue_Label.setGeometry(QRect(380,160,76,14))
        self.Imbue_Label.setText(self.tr("Imbue Points:"))

        self.Imbue = QLabel(self.Neck,'Imbue')
        self.Imbue.setGeometry(QRect(443,160,35,14))
        self.Imbue.setText(self.tr("0.0"))
        self.Imbue.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Slash_Label = QLabel(self.Neck,'Slash_Label')
        self.Slash_Label.setGeometry(QRect(487,160,8,14))
        self.Slash_Label.setText(self.tr("/"))

        self.Total_Imbue = QLabel(self.Neck,'Total_Imbue')
        self.Total_Imbue.setGeometry(QRect(498,160,29,14))
        self.Total_Imbue.setText(self.tr("0.0"))

        self.Overcharge_Label = QLabel(self.Neck,'Overcharge_Label')
        self.Overcharge_Label.setGeometry(QRect(380,178,59,14))
        self.Overcharge_Label.setText(self.tr("Overcharge:"))

        self.Overcharge = QLabel(self.Neck,'Overcharge')
        self.Overcharge.setGeometry(QRect(443,178,90,14))
        self.Overcharge.setText(self.tr("None"))
        self.Overcharge.setAlignment(QLabel.AlignVCenter | QLabel.AlignCenter)

        self.ItemCost_Label = QLabel(self.Neck,'ItemCost_Label')
        self.ItemCost_Label.setGeometry(QRect(380,196,50,14))
        self.ItemCost_Label.setText(self.tr("Item Cost:"))

        self.ItemCost = QLabel(self.Neck,'ItemCost')
        self.ItemCost.setGeometry(QRect(482,196,70,14))
        self.ItemCost.setText(self.tr(""))
        self.ItemCost.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ButtonGroup1 = QButtonGroup(self.Neck,'ButtonGroup1')
        self.ButtonGroup1.setEnabled(1)
        self.ButtonGroup1.setGeometry(QRect(607,30,146,19))
        self.ButtonGroup1.setLineWidth(0)
        self.ButtonGroup1.setTitle(self.tr(""))

        self.Drop = QRadioButton(self.ButtonGroup1,'Drop')
        self.Drop.setGeometry(QRect(100,2,52,17))
        self.Drop.setText(self.tr("Drop"))
        self.Drop.setChecked(1)

        self.PlayerMade = QRadioButton(self.ButtonGroup1,'PlayerMade')
        self.PlayerMade.setGeometry(QRect(10,2,85,17))
        self.PlayerMade.setText(self.tr("Player Made"))

        self.ClearItem = QPushButton(self.Neck,'ClearItem')
        self.ClearItem.setGeometry(QRect(683,209,79,26))
        self.ClearItem.setText(self.tr("Clear Item"))

        self.LoadItem = QPushButton(self.Neck,'LoadItem')
        self.LoadItem.setGeometry(QRect(683,157,79,26))
        self.LoadItem.setText(self.tr("Load Item"))

        self.SaveItem = QPushButton(self.Neck,'SaveItem')
        self.SaveItem.setGeometry(QRect(596,157,79,26))
        self.SaveItem.setText(self.tr("Save Item"))

        self.ItemName_Label = QLabel(self.Neck,'ItemName_Label')
        self.ItemName_Label.setEnabled(1)
        self.ItemName_Label.setGeometry(QRect(498,43,59,16))
        self.ItemName_Label.setText(self.tr("Item Name:"))

        self.ItemName = QLineEdit(self.Neck,'ItemName')
        self.ItemName.setGeometry(QRect(494,61,160,22))

        self.CraftButton = QPushButton(self.Neck,'CraftButton')
        self.CraftButton.setGeometry(QRect(662,2,69,26))
        self.CraftButton.setText(self.tr("Craft..."))
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
        self.connect(self.ClearItem,SIGNAL('clicked()'),self.ClearCurrentItem)
        self.connect(self.Equipped,SIGNAL('clicked()'),self.EquippedClicked)
        self.connect(self.TotalBonus,SIGNAL('clicked()'),self.TotalBonusSet)
        self.connect(self.CapDistance,SIGNAL('clicked()'),self.DistanceCapSet)
        self.connect(self.ItemLevelButton,SIGNAL('clicked()'),self.ItemLevelShow)
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
        self.connect(self.SkillsList,SIGNAL('clicked(QListBoxItem*)'),self.SkillClicked)
        self.connect(self.CharClass,SIGNAL('activated(const QString&)'),self.CharClassChanged)
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
        self.connect(self.CharRace,SIGNAL('activated(const QString&)'),self.RaceChanged)

        self.setTabOrder(self.CharName,self.CharClass)
        self.setTabOrder(self.CharClass,self.CharLevel)
        self.setTabOrder(self.CharLevel,self.CharRace)
        self.setTabOrder(self.CharRace,self.TotalBonus)
        self.setTabOrder(self.TotalBonus,self.CapDistance)
        self.setTabOrder(self.CapDistance,self.TypeTab)
        self.setTabOrder(self.TypeTab,self.PieceTab)
        self.setTabOrder(self.PieceTab,self.JewelTab)
        self.setTabOrder(self.JewelTab,self.ItemLevel)
        self.setTabOrder(self.ItemLevel,self.ItemLevelButton)
        self.setTabOrder(self.ItemLevelButton,self.QualEdit)
        self.setTabOrder(self.QualEdit,self.QualDrop)
        self.setTabOrder(self.QualDrop,self.Bonus_Edit)
        self.setTabOrder(self.Bonus_Edit,self.AFDPS_Edit)
        self.setTabOrder(self.AFDPS_Edit,self.Speed_Edit)
        self.setTabOrder(self.Speed_Edit,self.Equipped)
        self.setTabOrder(self.Equipped,self.CraftButton)
        self.setTabOrder(self.CraftButton,self.Drop)
        self.setTabOrder(self.Drop,self.PlayerMade)
        self.setTabOrder(self.PlayerMade,self.Type_1)
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
        self.setTabOrder(self.Effect_5,self.Type_6)
        self.setTabOrder(self.Type_6,self.Amount_Edit_6)
        self.setTabOrder(self.Amount_Edit_6,self.Effect_6)
        self.setTabOrder(self.Effect_6,self.Type_7)
        self.setTabOrder(self.Type_7,self.Amount_Edit_7)
        self.setTabOrder(self.Amount_Edit_7,self.Effect_7)
        self.setTabOrder(self.Effect_7,self.Type_8)
        self.setTabOrder(self.Type_8,self.Amount_Edit_8)
        self.setTabOrder(self.Amount_Edit_8,self.Effect_8)
        self.setTabOrder(self.Effect_8,self.Type_9)
        self.setTabOrder(self.Type_9,self.Amount_Edit_9)
        self.setTabOrder(self.Amount_Edit_9,self.Effect_9)
        self.setTabOrder(self.Effect_9,self.Type_10)
        self.setTabOrder(self.Type_10,self.Amount_Edit_10)
        self.setTabOrder(self.Amount_Edit_10,self.Effect_10)
        self.setTabOrder(self.Effect_10,self.ItemName)
        self.setTabOrder(self.ItemName,self.SaveItem)
        self.setTabOrder(self.SaveItem,self.LoadItem)
        self.setTabOrder(self.LoadItem,self.ClearItem)

    def AmountChanged(self,a0):
        print 'B_SC.AmountChanged(const QString&): not implemented yet'

    def CharClassChanged(self,a0):
        print 'B_SC.CharClassChanged(const QString&): not implemented yet'

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

    def OpenCraftWindow(self):
        print 'B_SC.OpenCraftWindow(): not implemented yet'

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

    def recalculate(self,a0):
        print 'B_SC.recalculate(const QString&): not implemented yet'

    def saveFile(self):
        print 'B_SC.saveFile(): not implemented yet'
