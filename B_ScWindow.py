# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScWindow.ui'
#
# Created: Fri Nov 25 03:00:06 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.15
#
# WARNING! All changes made in this file will be lost!


from qt import *
#Import the Custom Widgets
from MultiTabBar import *
from SearchingCombo import *


class B_SC(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        if not name:
            self.setName("B_SC")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))

        self.GroupBox9 = QGroupBox(self.centralWidget(),"GroupBox9")
        self.GroupBox9.setGeometry(QRect(613,3,165,134))

        self.LabelCharName = QLabel(self.GroupBox9,"LabelCharName")
        self.LabelCharName.setGeometry(QRect(6,16,37,16))

        self.LabelRealm = QLabel(self.GroupBox9,"LabelRealm")
        self.LabelRealm.setGeometry(QRect(6,40,38,16))

        self.LabelCharClass = QLabel(self.GroupBox9,"LabelCharClass")
        self.LabelCharClass.setGeometry(QRect(6,65,38,16))

        self.LabelCharRace = QLabel(self.GroupBox9,"LabelCharRace")
        self.LabelCharRace.setGeometry(QRect(6,88,38,16))

        self.LabelCharLevel = QLabel(self.GroupBox9,"LabelCharLevel")
        self.LabelCharLevel.setGeometry(QRect(6,111,38,16))

        self.CharName = QLineEdit(self.GroupBox9,"CharName")
        self.CharName.setGeometry(QRect(46,14,114,22))
        self.CharName.setFrameShape(QLineEdit.LineEditPanel)
        self.CharName.setFrameShadow(QLineEdit.Sunken)

        self.Realm = SearchingCombo(self.GroupBox9,"Realm")
        self.Realm.setGeometry(QRect(46,38,114,22))

        self.CharClass = SearchingCombo(self.GroupBox9,"CharClass")
        self.CharClass.setGeometry(QRect(46,61,114,22))

        self.CharRace = SearchingCombo(self.GroupBox9,"CharRace")
        self.CharRace.setGeometry(QRect(46,84,114,22))

        self.CharLevel = QLineEdit(self.GroupBox9,"CharLevel")
        self.CharLevel.setGeometry(QRect(46,107,37,22))

        self.ButtonGroup2 = QButtonGroup(self.centralWidget(),"ButtonGroup2")
        self.ButtonGroup2.setGeometry(QRect(613,134,165,51))

        self.TotalBonus = QRadioButton(self.ButtonGroup2,"TotalBonus")
        self.TotalBonus.setGeometry(QRect(11,14,85,17))
        self.TotalBonus.setChecked(1)

        self.CapDistance = QRadioButton(self.ButtonGroup2,"CapDistance")
        self.CapDistance.setGeometry(QRect(11,30,109,17))

        self.GroupBox1 = QGroupBox(self.centralWidget(),"GroupBox1")
        self.GroupBox1.setGeometry(QRect(5,3,85,182))

        self.StrengthLabel = QLabel(self.GroupBox1,"StrengthLabel")
        self.StrengthLabel.setGeometry(QRect(6,16,28,16))

        self.Strength = QLabel(self.GroupBox1,"Strength")
        self.Strength.setGeometry(QRect(35,16,20,16))
        self.Strength.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.StrengthCap = QLabel(self.GroupBox1,"StrengthCap")
        self.StrengthCap.setGeometry(QRect(57,16,20,16))
        self.StrengthCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ConstitutionLabel = QLabel(self.GroupBox1,"ConstitutionLabel")
        self.ConstitutionLabel.setGeometry(QRect(6,32,28,16))

        self.Constitution = QLabel(self.GroupBox1,"Constitution")
        self.Constitution.setGeometry(QRect(35,32,20,16))
        self.Constitution.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ConstitutionCap = QLabel(self.GroupBox1,"ConstitutionCap")
        self.ConstitutionCap.setGeometry(QRect(57,32,20,16))
        self.ConstitutionCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.DexterityLabel = QLabel(self.GroupBox1,"DexterityLabel")
        self.DexterityLabel.setGeometry(QRect(6,48,28,16))

        self.Dexterity = QLabel(self.GroupBox1,"Dexterity")
        self.Dexterity.setGeometry(QRect(35,48,20,16))
        self.Dexterity.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.DexterityCap = QLabel(self.GroupBox1,"DexterityCap")
        self.DexterityCap.setGeometry(QRect(57,48,20,16))
        self.DexterityCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.QuicknessLabel = QLabel(self.GroupBox1,"QuicknessLabel")
        self.QuicknessLabel.setGeometry(QRect(6,64,28,16))

        self.Quickness = QLabel(self.GroupBox1,"Quickness")
        self.Quickness.setGeometry(QRect(35,64,20,16))
        self.Quickness.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.QuicknessCap = QLabel(self.GroupBox1,"QuicknessCap")
        self.QuicknessCap.setGeometry(QRect(57,64,20,16))
        self.QuicknessCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.IntelligenceLabel = QLabel(self.GroupBox1,"IntelligenceLabel")
        self.IntelligenceLabel.setGeometry(QRect(6,80,28,16))

        self.Intelligence = QLabel(self.GroupBox1,"Intelligence")
        self.Intelligence.setGeometry(QRect(35,80,20,16))
        self.Intelligence.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.IntelligenceCap = QLabel(self.GroupBox1,"IntelligenceCap")
        self.IntelligenceCap.setGeometry(QRect(57,80,20,16))
        self.IntelligenceCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.PietyLabel = QLabel(self.GroupBox1,"PietyLabel")
        self.PietyLabel.setGeometry(QRect(6,96,28,16))

        self.Piety = QLabel(self.GroupBox1,"Piety")
        self.Piety.setGeometry(QRect(35,96,20,16))
        self.Piety.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.PietyCap = QLabel(self.GroupBox1,"PietyCap")
        self.PietyCap.setGeometry(QRect(57,96,20,16))
        self.PietyCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.CharismaLabel = QLabel(self.GroupBox1,"CharismaLabel")
        self.CharismaLabel.setGeometry(QRect(6,112,28,16))

        self.Charisma = QLabel(self.GroupBox1,"Charisma")
        self.Charisma.setGeometry(QRect(35,112,20,16))
        self.Charisma.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.CharismaCap = QLabel(self.GroupBox1,"CharismaCap")
        self.CharismaCap.setGeometry(QRect(57,112,20,16))
        self.CharismaCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.EmpathyLabel = QLabel(self.GroupBox1,"EmpathyLabel")
        self.EmpathyLabel.setGeometry(QRect(6,128,28,16))

        self.Empathy = QLabel(self.GroupBox1,"Empathy")
        self.Empathy.setGeometry(QRect(35,128,20,16))
        self.Empathy.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.EmpathyCap = QLabel(self.GroupBox1,"EmpathyCap")
        self.EmpathyCap.setGeometry(QRect(57,128,20,16))
        self.EmpathyCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.PowerLabel = QLabel(self.GroupBox1,"PowerLabel")
        self.PowerLabel.setGeometry(QRect(6,144,28,16))

        self.Power = QLabel(self.GroupBox1,"Power")
        self.Power.setGeometry(QRect(35,144,20,16))
        self.Power.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.PowerCap = QLabel(self.GroupBox1,"PowerCap")
        self.PowerCap.setGeometry(QRect(57,144,20,16))
        self.PowerCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.HitsLabel = QLabel(self.GroupBox1,"HitsLabel")
        self.HitsLabel.setGeometry(QRect(6,160,20,16))

        self.Hits = QLabel(self.GroupBox1,"Hits")
        self.Hits.setGeometry(QRect(29,160,20,16))
        self.Hits.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.HitsCap = QLabel(self.GroupBox1,"HitsCap")
        self.HitsCap.setGeometry(QRect(49,160,28,16))
        self.HitsCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.GroupBox2 = QGroupBox(self.centralWidget(),"GroupBox2")
        self.GroupBox2.setGeometry(QRect(91,3,90,182))

        self.BodyLabel = QLabel(self.GroupBox2,"BodyLabel")
        self.BodyLabel.setGeometry(QRect(6,16,36,16))

        self.Body = QLabel(self.GroupBox2,"Body")
        self.Body.setGeometry(QRect(44,16,17,16))
        self.Body.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.BodyRR = QLabel(self.GroupBox2,"BodyRR")
        self.BodyRR.setGeometry(QRect(66,16,17,16))
        self.BodyRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ColdLabel = QLabel(self.GroupBox2,"ColdLabel")
        self.ColdLabel.setGeometry(QRect(6,34,36,16))

        self.Cold = QLabel(self.GroupBox2,"Cold")
        self.Cold.setGeometry(QRect(44,34,17,16))
        self.Cold.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ColdRR = QLabel(self.GroupBox2,"ColdRR")
        self.ColdRR.setGeometry(QRect(66,34,17,16))
        self.ColdRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.HeatLabel = QLabel(self.GroupBox2,"HeatLabel")
        self.HeatLabel.setGeometry(QRect(6,52,36,16))

        self.Heat = QLabel(self.GroupBox2,"Heat")
        self.Heat.setGeometry(QRect(44,52,17,16))
        self.Heat.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.HeatRR = QLabel(self.GroupBox2,"HeatRR")
        self.HeatRR.setGeometry(QRect(66,52,17,16))
        self.HeatRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.EnergyLabel = QLabel(self.GroupBox2,"EnergyLabel")
        self.EnergyLabel.setGeometry(QRect(6,70,36,16))

        self.Energy = QLabel(self.GroupBox2,"Energy")
        self.Energy.setGeometry(QRect(44,70,17,16))
        self.Energy.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.EnergyRR = QLabel(self.GroupBox2,"EnergyRR")
        self.EnergyRR.setGeometry(QRect(66,70,17,16))
        self.EnergyRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.MatterLabel = QLabel(self.GroupBox2,"MatterLabel")
        self.MatterLabel.setGeometry(QRect(6,88,36,16))

        self.Matter = QLabel(self.GroupBox2,"Matter")
        self.Matter.setGeometry(QRect(44,88,17,16))
        self.Matter.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.MatterRR = QLabel(self.GroupBox2,"MatterRR")
        self.MatterRR.setGeometry(QRect(66,88,17,16))
        self.MatterRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.SpiritLabel = QLabel(self.GroupBox2,"SpiritLabel")
        self.SpiritLabel.setGeometry(QRect(6,106,36,16))

        self.Spirit = QLabel(self.GroupBox2,"Spirit")
        self.Spirit.setGeometry(QRect(44,106,17,16))
        self.Spirit.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.SpiritRR = QLabel(self.GroupBox2,"SpiritRR")
        self.SpiritRR.setGeometry(QRect(66,106,17,16))
        self.SpiritRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.CrushLabel = QLabel(self.GroupBox2,"CrushLabel")
        self.CrushLabel.setGeometry(QRect(6,124,36,16))

        self.Crush = QLabel(self.GroupBox2,"Crush")
        self.Crush.setGeometry(QRect(44,124,17,16))
        self.Crush.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.CrushRR = QLabel(self.GroupBox2,"CrushRR")
        self.CrushRR.setGeometry(QRect(66,124,17,16))
        self.CrushRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ThrustLabel = QLabel(self.GroupBox2,"ThrustLabel")
        self.ThrustLabel.setGeometry(QRect(6,142,36,16))

        self.Thrust = QLabel(self.GroupBox2,"Thrust")
        self.Thrust.setGeometry(QRect(44,142,17,16))
        self.Thrust.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ThrustRR = QLabel(self.GroupBox2,"ThrustRR")
        self.ThrustRR.setGeometry(QRect(66,142,17,16))
        self.ThrustRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.SlashLabel = QLabel(self.GroupBox2,"SlashLabel")
        self.SlashLabel.setGeometry(QRect(6,160,36,16))

        self.Slash = QLabel(self.GroupBox2,"Slash")
        self.Slash.setGeometry(QRect(44,160,17,16))
        self.Slash.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.SlashRR = QLabel(self.GroupBox2,"SlashRR")
        self.SlashRR.setGeometry(QRect(66,160,17,16))
        self.SlashRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.GroupBox4 = QGroupBox(self.centralWidget(),"GroupBox4")
        self.GroupBox4.setGeometry(QRect(182,3,124,136))

        self.Focus_1 = QLabel(self.GroupBox4,"Focus_1")
        self.Focus_1.setGeometry(QRect(6,18,112,16))

        self.Focus_2 = QLabel(self.GroupBox4,"Focus_2")
        self.Focus_2.setGeometry(QRect(6,36,112,16))

        self.Focus_3 = QLabel(self.GroupBox4,"Focus_3")
        self.Focus_3.setGeometry(QRect(6,54,112,16))

        self.Focus_4 = QLabel(self.GroupBox4,"Focus_4")
        self.Focus_4.setGeometry(QRect(6,72,112,16))

        self.GroupBox5 = QGroupBox(self.centralWidget(),"GroupBox5")
        self.GroupBox5.setGeometry(QRect(182,134,124,51))

        self.TotalCostLabel = QLabel(self.GroupBox5,"TotalCostLabel")
        self.TotalCostLabel.setGeometry(QRect(6,13,30,16))

        self.TotalCost = QLabel(self.GroupBox5,"TotalCost")
        self.TotalCost.setGeometry(QRect(36,14,82,16))
        self.TotalCost.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TotalPriceLabel = QLabel(self.GroupBox5,"TotalPriceLabel")
        self.TotalPriceLabel.setGeometry(QRect(6,28,30,16))

        self.TotalPrice = QLabel(self.GroupBox5,"TotalPrice")
        self.TotalPrice.setGeometry(QRect(36,28,82,16))
        self.TotalPrice.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.GroupSkillsList = QGroupBox(self.centralWidget(),"GroupSkillsList")
        self.GroupSkillsList.setGeometry(QRect(307,3,140,136))

        self.SkillsList = QListBox(self.GroupSkillsList,"SkillsList")
        self.SkillsList.setGeometry(QRect(5,15,130,116))

        self.GroupOtherBonusList = QGroupBox(self.centralWidget(),"GroupOtherBonusList")
        self.GroupOtherBonusList.setGeometry(QRect(448,3,164,136))

        self.OtherBonusList = QListBox(self.GroupOtherBonusList,"OtherBonusList")
        self.OtherBonusList.setGeometry(QRect(5,15,154,116))

        self.LabelFileName = QLabel(self.centralWidget(),"LabelFileName")
        self.LabelFileName.setGeometry(QRect(315,142,285,14))

        self.LabelOcError = QLabel(self.centralWidget(),"LabelOcError")
        self.LabelOcError.setGeometry(QRect(315,157,285,14))

        self.LabelDupError = QLabel(self.centralWidget(),"LabelDupError")
        self.LabelDupError.setGeometry(QRect(315,173,285,14))

        self.frame3 = QGroupBox(self.centralWidget(),"frame3")
        self.frame3.setGeometry(QRect(3,235,776,265))
        self.frame3.setFrameShape(QGroupBox.StyledPanel)
        self.frame3.setFrameShadow(QGroupBox.Raised)

        self.ItemLevelLabel = QLabel(self.frame3,"ItemLevelLabel")
        self.ItemLevelLabel.setGeometry(QRect(7,5,59,22))

        self.ItemLevel = QLineEdit(self.frame3,"ItemLevel")
        self.ItemLevel.setGeometry(QRect(63,5,35,22))

        self.ItemLevelButton = QPushButton(self.frame3,"ItemLevelButton")
        self.ItemLevelButton.setGeometry(QRect(98,7,18,18))

        self.ItemQualityLabel = QLabel(self.frame3,"ItemQualityLabel")
        self.ItemQualityLabel.setGeometry(QRect(136,5,50,22))

        self.QualDrop = SearchingCombo(self.frame3,"QualDrop")
        self.QualDrop.setGeometry(QRect(177,5,52,22))

        self.QualEdit = QLineEdit(self.frame3,"QualEdit")
        self.QualEdit.setGeometry(QRect(177,5,51,22))

        self.ItemName = QLineEdit(self.frame3,"ItemName")
        self.ItemName.setGeometry(QRect(562,48,200,22))

        self.ItemBonusLabel = QLabel(self.frame3,"ItemBonusLabel")
        self.ItemBonusLabel.setGeometry(QRect(244,5,40,22))

        self.Bonus_Edit = QLineEdit(self.frame3,"Bonus_Edit")
        self.Bonus_Edit.setGeometry(QRect(284,5,35,22))

        self.ItemAFDPSLabel = QLabel(self.frame3,"ItemAFDPSLabel")
        self.ItemAFDPSLabel.setGeometry(QRect(330,5,55,22))

        self.AFDPS_Edit = QLineEdit(self.frame3,"AFDPS_Edit")
        self.AFDPS_Edit.setGeometry(QRect(375,5,35,22))

        self.ItemSpeedLabel = QLabel(self.frame3,"ItemSpeedLabel")
        self.ItemSpeedLabel.setGeometry(QRect(420,5,40,22))

        self.Speed_Edit = QLineEdit(self.frame3,"Speed_Edit")
        self.Speed_Edit.setGeometry(QRect(460,5,35,22))

        self.ItemUtilityLabel = QLabel(self.frame3,"ItemUtilityLabel")
        self.ItemUtilityLabel.setGeometry(QRect(507,3,35,14))

        self.ItemUtility = QLabel(self.frame3,"ItemUtility")
        self.ItemUtility.setGeometry(QRect(545,3,28,14))

        self.ItemTotalUtilityLabel = QLabel(self.frame3,"ItemTotalUtilityLabel")
        self.ItemTotalUtilityLabel.setGeometry(QRect(507,17,34,14))

        self.ItemTotalUtility = QLabel(self.frame3,"ItemTotalUtility")
        self.ItemTotalUtility.setGeometry(QRect(545,17,73,14))

        self.Equipped = QCheckBox(self.frame3,"Equipped")
        self.Equipped.setGeometry(QRect(579,7,71,22))

        self.CraftButton = QPushButton(self.frame3,"CraftButton")
        self.CraftButton.setGeometry(QRect(683,5,79,26))

        self.LabelGemType = QLabel(self.frame3,"LabelGemType")
        self.LabelGemType.setGeometry(QRect(50,33,119,14))

        self.LabelGemAmount = QLabel(self.frame3,"LabelGemAmount")
        self.LabelGemAmount.setGeometry(QRect(181,33,44,14))

        self.LabelGemEffect = QLabel(self.frame3,"LabelGemEffect")
        self.LabelGemEffect.setGeometry(QRect(237,33,142,14))

        self.LabelGemQuality = QLabel(self.frame3,"LabelGemQuality")
        self.LabelGemQuality.setGeometry(QRect(391,33,44,14))

        self.LabelGemPoints = QLabel(self.frame3,"LabelGemPoints")
        self.LabelGemPoints.setGeometry(QRect(443,33,35,14))
        self.LabelGemPoints.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.LabelGemCost = QLabel(self.frame3,"LabelGemCost")
        self.LabelGemCost.setGeometry(QRect(482,33,70,14))
        self.LabelGemCost.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ItemNameLabel = QLabel(self.frame3,"ItemNameLabel")
        self.ItemNameLabel.setGeometry(QRect(562,33,40,14))

        self.ButtonGroup1 = QButtonGroup(self.frame3,"ButtonGroup1")
        self.ButtonGroup1.setEnabled(1)
        self.ButtonGroup1.setGeometry(QRect(615,31,138,19))
        self.ButtonGroup1.setLineWidth(0)

        self.PlayerMade = QRadioButton(self.ButtonGroup1,"PlayerMade")
        self.PlayerMade.setGeometry(QRect(2,2,85,17))

        self.Drop = QRadioButton(self.ButtonGroup1,"Drop")
        self.Drop.setGeometry(QRect(92,2,52,17))
        self.Drop.setChecked(1)

        self.Gem_Label_1 = QLabel(self.frame3,"Gem_Label_1")
        self.Gem_Label_1.setGeometry(QRect(7,48,34,22))

        self.Type_1 = SearchingCombo(self.frame3,"Type_1")
        self.Type_1.setGeometry(QRect(46,48,127,22))

        self.Amount_Edit_1 = QLineEdit(self.frame3,"Amount_Edit_1")
        self.Amount_Edit_1.setGeometry(QRect(177,48,51,22))

        self.Amount_Drop_1 = SearchingCombo(self.frame3,"Amount_Drop_1")
        self.Amount_Drop_1.setGeometry(QRect(177,48,52,22))

        self.Effect_1 = SearchingCombo(self.frame3,"Effect_1")
        self.Effect_1.setGeometry(QRect(233,48,150,22))

        self.Quality_1 = SearchingCombo(self.frame3,"Quality_1")
        self.Quality_1.setGeometry(QRect(387,48,52,22))

        self.Points_1 = QLabel(self.frame3,"Points_1")
        self.Points_1.setGeometry(QRect(443,48,35,22))
        self.Points_1.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_1 = QLabel(self.frame3,"Cost_1")
        self.Cost_1.setGeometry(QRect(482,48,70,22))
        self.Cost_1.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_1 = QLabel(self.frame3,"Name_1")
        self.Name_1.setGeometry(QRect(562,48,200,22))

        self.Gem_Label_2 = QLabel(self.frame3,"Gem_Label_2")
        self.Gem_Label_2.setGeometry(QRect(7,69,34,22))

        self.Amount_Edit_2 = QLineEdit(self.frame3,"Amount_Edit_2")
        self.Amount_Edit_2.setGeometry(QRect(177,69,51,22))

        self.Amount_Drop_2 = SearchingCombo(self.frame3,"Amount_Drop_2")
        self.Amount_Drop_2.setGeometry(QRect(177,69,52,22))

        self.Type_2 = SearchingCombo(self.frame3,"Type_2")
        self.Type_2.setGeometry(QRect(46,69,127,22))

        self.Effect_2 = SearchingCombo(self.frame3,"Effect_2")
        self.Effect_2.setGeometry(QRect(233,69,150,22))

        self.Quality_2 = SearchingCombo(self.frame3,"Quality_2")
        self.Quality_2.setGeometry(QRect(387,69,52,22))

        self.Points_2 = QLabel(self.frame3,"Points_2")
        self.Points_2.setGeometry(QRect(443,69,35,22))
        self.Points_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_2 = QLabel(self.frame3,"Cost_2")
        self.Cost_2.setGeometry(QRect(482,69,70,22))
        self.Cost_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_2 = QLabel(self.frame3,"Name_2")
        self.Name_2.setGeometry(QRect(562,69,200,22))

        self.Gem_Label_3 = QLabel(self.frame3,"Gem_Label_3")
        self.Gem_Label_3.setGeometry(QRect(7,90,34,22))

        self.Type_3 = SearchingCombo(self.frame3,"Type_3")
        self.Type_3.setGeometry(QRect(46,90,127,22))

        self.Amount_Edit_3 = QLineEdit(self.frame3,"Amount_Edit_3")
        self.Amount_Edit_3.setGeometry(QRect(177,90,51,22))

        self.Amount_Drop_3 = SearchingCombo(self.frame3,"Amount_Drop_3")
        self.Amount_Drop_3.setGeometry(QRect(177,90,52,22))

        self.Effect_3 = SearchingCombo(self.frame3,"Effect_3")
        self.Effect_3.setGeometry(QRect(233,90,150,22))

        self.Quality_3 = SearchingCombo(self.frame3,"Quality_3")
        self.Quality_3.setGeometry(QRect(387,90,52,22))

        self.Points_3 = QLabel(self.frame3,"Points_3")
        self.Points_3.setGeometry(QRect(443,90,35,22))
        self.Points_3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_3 = QLabel(self.frame3,"Cost_3")
        self.Cost_3.setGeometry(QRect(482,90,70,22))
        self.Cost_3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_3 = QLabel(self.frame3,"Name_3")
        self.Name_3.setGeometry(QRect(562,90,200,22))

        self.Gem_Label_4 = QLabel(self.frame3,"Gem_Label_4")
        self.Gem_Label_4.setGeometry(QRect(7,111,34,22))

        self.Type_4 = SearchingCombo(self.frame3,"Type_4")
        self.Type_4.setGeometry(QRect(46,111,127,22))

        self.Amount_Edit_4 = QLineEdit(self.frame3,"Amount_Edit_4")
        self.Amount_Edit_4.setGeometry(QRect(177,111,51,22))

        self.Amount_Drop_4 = SearchingCombo(self.frame3,"Amount_Drop_4")
        self.Amount_Drop_4.setGeometry(QRect(177,111,52,22))

        self.Effect_4 = SearchingCombo(self.frame3,"Effect_4")
        self.Effect_4.setGeometry(QRect(233,111,150,22))

        self.Quality_4 = SearchingCombo(self.frame3,"Quality_4")
        self.Quality_4.setGeometry(QRect(387,111,52,22))

        self.Points_4 = QLabel(self.frame3,"Points_4")
        self.Points_4.setGeometry(QRect(443,111,35,22))
        self.Points_4.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_4 = QLabel(self.frame3,"Cost_4")
        self.Cost_4.setGeometry(QRect(482,111,70,22))
        self.Cost_4.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_4 = QLabel(self.frame3,"Name_4")
        self.Name_4.setGeometry(QRect(562,111,200,22))

        self.Gem_Label_5 = QLabel(self.frame3,"Gem_Label_5")
        self.Gem_Label_5.setGeometry(QRect(7,132,34,22))

        self.Type_5 = SearchingCombo(self.frame3,"Type_5")
        self.Type_5.setGeometry(QRect(46,132,127,22))

        self.Amount_Edit_5 = QLineEdit(self.frame3,"Amount_Edit_5")
        self.Amount_Edit_5.setGeometry(QRect(177,132,51,22))

        self.Effect_5 = SearchingCombo(self.frame3,"Effect_5")
        self.Effect_5.setGeometry(QRect(233,132,206,22))

        self.Gem_Label_6 = QLabel(self.frame3,"Gem_Label_6")
        self.Gem_Label_6.setGeometry(QRect(7,153,34,22))

        self.Type_6 = SearchingCombo(self.frame3,"Type_6")
        self.Type_6.setGeometry(QRect(46,153,127,22))

        self.Amount_Edit_6 = QLineEdit(self.frame3,"Amount_Edit_6")
        self.Amount_Edit_6.setGeometry(QRect(177,153,51,22))

        self.Effect_6 = SearchingCombo(self.frame3,"Effect_6")
        self.Effect_6.setGeometry(QRect(233,153,206,22))

        self.Gem_Label_7 = QLabel(self.frame3,"Gem_Label_7")
        self.Gem_Label_7.setGeometry(QRect(7,174,34,22))

        self.Type_7 = SearchingCombo(self.frame3,"Type_7")
        self.Type_7.setGeometry(QRect(46,174,127,22))

        self.Amount_Edit_7 = QLineEdit(self.frame3,"Amount_Edit_7")
        self.Amount_Edit_7.setGeometry(QRect(177,174,51,22))

        self.Effect_7 = SearchingCombo(self.frame3,"Effect_7")
        self.Effect_7.setGeometry(QRect(233,174,206,22))

        self.Gem_Label_8 = QLabel(self.frame3,"Gem_Label_8")
        self.Gem_Label_8.setGeometry(QRect(7,195,34,22))

        self.Type_8 = SearchingCombo(self.frame3,"Type_8")
        self.Type_8.setGeometry(QRect(46,195,127,22))

        self.Amount_Edit_8 = QLineEdit(self.frame3,"Amount_Edit_8")
        self.Amount_Edit_8.setGeometry(QRect(177,195,51,22))

        self.Effect_8 = SearchingCombo(self.frame3,"Effect_8")
        self.Effect_8.setGeometry(QRect(233,195,206,22))

        self.Gem_Label_9 = QLabel(self.frame3,"Gem_Label_9")
        self.Gem_Label_9.setGeometry(QRect(7,216,34,22))

        self.Type_9 = SearchingCombo(self.frame3,"Type_9")
        self.Type_9.setGeometry(QRect(46,216,127,22))

        self.Amount_Edit_9 = QLineEdit(self.frame3,"Amount_Edit_9")
        self.Amount_Edit_9.setGeometry(QRect(177,216,51,22))

        self.Effect_9 = SearchingCombo(self.frame3,"Effect_9")
        self.Effect_9.setGeometry(QRect(233,216,206,22))

        self.Gem_Label_10 = QLabel(self.frame3,"Gem_Label_10")
        self.Gem_Label_10.setGeometry(QRect(7,237,41,22))

        self.Type_10 = SearchingCombo(self.frame3,"Type_10")
        self.Type_10.setGeometry(QRect(46,237,127,22))

        self.Amount_Edit_10 = QLineEdit(self.frame3,"Amount_Edit_10")
        self.Amount_Edit_10.setGeometry(QRect(177,237,51,22))

        self.Effect_10 = SearchingCombo(self.frame3,"Effect_10")
        self.Effect_10.setGeometry(QRect(233,237,206,22))

        self.ItemImbueLabel = QLabel(self.frame3,"ItemImbueLabel")
        self.ItemImbueLabel.setGeometry(QRect(380,160,76,14))

        self.ItemImbue = QLabel(self.frame3,"ItemImbue")
        self.ItemImbue.setGeometry(QRect(443,160,35,14))
        self.ItemImbue.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ItemImbueSlashLabel = QLabel(self.frame3,"ItemImbueSlashLabel")
        self.ItemImbueSlashLabel.setGeometry(QRect(487,160,8,14))

        self.ItemImbueTotal = QLabel(self.frame3,"ItemImbueTotal")
        self.ItemImbueTotal.setGeometry(QRect(498,160,29,14))

        self.ItemOverchargeLabel = QLabel(self.frame3,"ItemOverchargeLabel")
        self.ItemOverchargeLabel.setGeometry(QRect(380,178,59,14))

        self.ItemOvercharge = QLabel(self.frame3,"ItemOvercharge")
        self.ItemOvercharge.setGeometry(QRect(443,178,90,14))
        self.ItemOvercharge.setAlignment(QLabel.AlignCenter)

        self.ItemCostLabel = QLabel(self.frame3,"ItemCostLabel")
        self.ItemCostLabel.setGeometry(QRect(380,196,50,14))

        self.ItemCost = QLabel(self.frame3,"ItemCost")
        self.ItemCost.setGeometry(QRect(482,196,70,14))
        self.ItemCost.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.LoadItem = QPushButton(self.frame3,"LoadItem")
        self.LoadItem.setGeometry(QRect(683,157,79,26))

        self.SaveItem = QPushButton(self.frame3,"SaveItem")
        self.SaveItem.setGeometry(QRect(683,189,79,26))

        self.ClearItem = QPushButton(self.frame3,"ClearItem")
        self.ClearItem.setGeometry(QRect(683,233,79,26))

        self.PieceTab = MultiTabBar(self.centralWidget(),"PieceTab")
        self.PieceTab.setGeometry(QRect(3,190,776,46))

        self.languageChange()

        self.resize(QSize(781,526).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.PieceTab,SIGNAL("selected(int)"),self.PieceTabChanged)
        self.connect(self.PlayerMade,SIGNAL("toggled(bool)"),self.PlayerToggled)
        self.connect(self.Drop,SIGNAL("toggled(bool)"),self.DropToggled)
        self.connect(self.Type_1,SIGNAL("activated(const QString&)"),self.Type_1_Changed)
        self.connect(self.Type_2,SIGNAL("activated(const QString&)"),self.Type_2_Changed)
        self.connect(self.Type_3,SIGNAL("activated(const QString&)"),self.Type_3_Changed)
        self.connect(self.Type_4,SIGNAL("activated(const QString&)"),self.Type_4_Changed)
        self.connect(self.Type_5,SIGNAL("activated(const QString&)"),self.Type_5_Changed)
        self.connect(self.Type_6,SIGNAL("activated(const QString&)"),self.Type_6_Changed)
        self.connect(self.Amount_Drop_1,SIGNAL("activated(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Drop_2,SIGNAL("activated(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Drop_3,SIGNAL("activated(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Drop_4,SIGNAL("activated(const QString&)"),self.AmountChanged)
        self.connect(self.Effect_1,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Effect_2,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Effect_3,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Effect_4,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Effect_5,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Effect_6,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.QualDrop,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.ItemLevel,SIGNAL("textChanged(const QString&)"),self.recalculate)
        self.connect(self.Quality_1,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Quality_2,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Quality_3,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Quality_4,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.ClearItem,SIGNAL("clicked()"),self.ClearCurrentItem)
        self.connect(self.Equipped,SIGNAL("clicked()"),self.EquippedClicked)
        self.connect(self.TotalBonus,SIGNAL("clicked()"),self.TotalBonusSet)
        self.connect(self.CapDistance,SIGNAL("clicked()"),self.DistanceCapSet)
        self.connect(self.ItemLevelButton,SIGNAL("clicked()"),self.ItemLevelShow)
        self.connect(self.Amount_Edit_5,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_6,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_1,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_2,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_3,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_4,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.LoadItem,SIGNAL("clicked()"),self.Load_Item)
        self.connect(self.SaveItem,SIGNAL("clicked()"),self.Save_Item)
        self.connect(self.CharLevel,SIGNAL("textChanged(const QString&)"),self.recalculate)
        self.connect(self.CraftButton,SIGNAL("clicked()"),self.OpenCraftWindow)
        self.connect(self.SkillsList,SIGNAL("clicked(QListBoxItem*)"),self.SkillClicked)
        self.connect(self.OtherBonusList,SIGNAL("clicked(QListBoxItem*)"),self.SkillClicked)
        self.connect(self.Realm,SIGNAL("activated(const QString&)"),self.RealmChanged)
        self.connect(self.CharClass,SIGNAL("activated(const QString&)"),self.CharClassChanged)
        self.connect(self.AFDPS_Edit,SIGNAL("textChanged(const QString&)"),self.recalculate)
        self.connect(self.Speed_Edit,SIGNAL("textChanged(const QString&)"),self.recalculate)
        self.connect(self.Bonus_Edit,SIGNAL("textChanged(const QString&)"),self.recalculate)
        self.connect(self.ItemName,SIGNAL("textChanged(const QString&)"),self.recalculate)
        self.connect(self.Type_7,SIGNAL("activated(const QString&)"),self.Type_7_Changed)
        self.connect(self.Type_8,SIGNAL("activated(const QString&)"),self.Type_8_Changed)
        self.connect(self.Type_9,SIGNAL("activated(const QString&)"),self.Type_9_Changed)
        self.connect(self.Type_10,SIGNAL("activated(const QString&)"),self.Type_10_Changed)
        self.connect(self.Amount_Edit_7,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_8,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_9,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_10,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Effect_7,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Effect_8,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Effect_9,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Effect_10,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.CharRace,SIGNAL("activated(const QString&)"),self.RaceChanged)

        self.setTabOrder(self.CharName,self.Realm)
        self.setTabOrder(self.Realm,self.CharClass)
        self.setTabOrder(self.CharClass,self.CharRace)
        self.setTabOrder(self.CharRace,self.CharLevel)
        self.setTabOrder(self.CharLevel,self.TotalBonus)
        self.setTabOrder(self.TotalBonus,self.CapDistance)
        self.setTabOrder(self.CapDistance,self.PieceTab)
        self.setTabOrder(self.PieceTab,self.ItemLevel)
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
        self.setTabOrder(self.ItemName,self.LoadItem)
        self.setTabOrder(self.LoadItem,self.SaveItem)
        self.setTabOrder(self.SaveItem,self.ClearItem)
        self.setTabOrder(self.ClearItem,self.SkillsList)
        self.setTabOrder(self.SkillsList,self.OtherBonusList)


    def languageChange(self):
        self.setCaption(self.__tr("Spellcrafting Calculator"))
        self.GroupBox9.setTitle(self.__tr("Char Info"))
        self.LabelCharName.setText(self.__tr("Name:"))
        self.LabelRealm.setText(self.__tr("Realm:"))
        self.LabelCharClass.setText(self.__tr("Class:"))
        self.LabelCharRace.setText(self.__tr("Race:"))
        self.LabelCharLevel.setText(self.__tr("Level:"))
        self.ButtonGroup2.setTitle(self.__tr("Display"))
        self.TotalBonus.setText(self.__tr("Total Bonus"))
        self.CapDistance.setText(self.__tr("Distance To Cap"))
        self.GroupBox1.setTitle(self.__tr("Stats"))
        self.StrengthLabel.setText(self.__tr("STR:"))
        self.Strength.setText(self.__tr("0"))
        self.StrengthCap.setText(self.__tr("-"))
        self.ConstitutionLabel.setText(self.__tr("CON:"))
        self.Constitution.setText(self.__tr("0"))
        self.ConstitutionCap.setText(self.__tr("-"))
        self.DexterityLabel.setText(self.__tr("DEX:"))
        self.Dexterity.setText(self.__tr("0"))
        self.DexterityCap.setText(self.__tr("-"))
        self.QuicknessLabel.setText(self.__tr("QUI:"))
        self.Quickness.setText(self.__tr("0"))
        self.QuicknessCap.setText(self.__tr("-"))
        self.IntelligenceLabel.setText(self.__tr("INT:"))
        self.Intelligence.setText(self.__tr("0"))
        self.IntelligenceCap.setText(self.__tr("-"))
        self.PietyLabel.setText(self.__tr("PIE:"))
        self.Piety.setText(self.__tr("0"))
        self.PietyCap.setText(self.__tr("-"))
        self.CharismaLabel.setText(self.__tr("CHA:"))
        self.Charisma.setText(self.__tr("0"))
        self.CharismaCap.setText(self.__tr("-"))
        self.EmpathyLabel.setText(self.__tr("EMP:"))
        self.Empathy.setText(self.__tr("0"))
        self.EmpathyCap.setText(self.__tr("-"))
        self.PowerLabel.setText(self.__tr("Pow:"))
        self.Power.setText(self.__tr("0"))
        self.PowerCap.setText(self.__tr("-"))
        self.HitsLabel.setText(self.__tr("Hits:"))
        self.Hits.setText(self.__tr("0"))
        self.HitsCap.setText(self.__tr("-"))
        self.GroupBox2.setTitle(self.__tr("Resists"))
        self.BodyLabel.setText(self.__tr("Body:"))
        self.Body.setText(self.__tr("0"))
        self.BodyRR.setText(self.__tr("-"))
        self.ColdLabel.setText(self.__tr("Cold:"))
        self.Cold.setText(self.__tr("0"))
        self.ColdRR.setText(self.__tr("-"))
        self.HeatLabel.setText(self.__tr("Heat:"))
        self.Heat.setText(self.__tr("0"))
        self.HeatRR.setText(self.__tr("-"))
        self.EnergyLabel.setText(self.__tr("Energy:"))
        self.Energy.setText(self.__tr("0"))
        self.EnergyRR.setText(self.__tr("-"))
        self.MatterLabel.setText(self.__tr("Matter:"))
        self.Matter.setText(self.__tr("0"))
        self.MatterRR.setText(self.__tr("-"))
        self.SpiritLabel.setText(self.__tr("Spirit:"))
        self.Spirit.setText(self.__tr("0"))
        self.SpiritRR.setText(self.__tr("-"))
        self.CrushLabel.setText(self.__tr("Crush:"))
        self.Crush.setText(self.__tr("0"))
        self.CrushRR.setText(self.__tr("-"))
        self.ThrustLabel.setText(self.__tr("Thrust:"))
        self.Thrust.setText(self.__tr("0"))
        self.ThrustRR.setText(self.__tr("-"))
        self.SlashLabel.setText(self.__tr("Slash:"))
        self.Slash.setText(self.__tr("0"))
        self.SlashRR.setText(self.__tr("-"))
        self.GroupBox4.setTitle(self.__tr("Focus"))
        self.Focus_1.setText(QString.null)
        self.Focus_2.setText(QString.null)
        self.Focus_3.setText(QString.null)
        self.Focus_4.setText(QString.null)
        self.GroupBox5.setTitle(self.__tr("Totals"))
        self.TotalCostLabel.setText(self.__tr("Cost:"))
        self.TotalCost.setText(self.__tr("0"))
        self.TotalPriceLabel.setText(self.__tr("Price:"))
        self.TotalPrice.setText(self.__tr("0"))
        self.GroupSkillsList.setTitle(self.__tr("Skills"))
        self.GroupOtherBonusList.setTitle(self.__tr("Other Bonuses"))
        self.LabelFileName.setText(QString.null)
        self.LabelOcError.setText(QString.null)
        self.LabelDupError.setText(QString.null)
        self.frame3.setTitle(QString.null)
        self.ItemLevelLabel.setText(self.__tr("Item Level:"))
        self.ItemLevelButton.setText(self.__tr("..."))
        self.ItemQualityLabel.setText(self.__tr("Quality:"))
        self.ItemBonusLabel.setText(self.__tr("Bonus:"))
        self.ItemAFDPSLabel.setText(self.__tr("AF/DPS:"))
        self.ItemSpeedLabel.setText(self.__tr("Speed:"))
        self.ItemUtilityLabel.setText(self.__tr("Utility:"))
        self.ItemUtility.setText(self.__tr("0.0"))
        self.ItemTotalUtilityLabel.setText(self.__tr("Total:"))
        self.ItemTotalUtility.setText(self.__tr("0.0"))
        self.Equipped.setText(self.__tr("Equipped"))
        self.CraftButton.setText(self.__tr("Craft..."))
        self.LabelGemType.setText(self.__tr("Type"))
        self.LabelGemAmount.setText(self.__tr("Amount"))
        self.LabelGemEffect.setText(self.__tr("Effect"))
        self.LabelGemQuality.setText(self.__tr("Quality"))
        self.LabelGemPoints.setText(self.__tr("Points"))
        self.LabelGemCost.setText(self.__tr("Cost"))
        self.ItemNameLabel.setText(self.__tr("Name"))
        self.ButtonGroup1.setTitle(QString.null)
        self.PlayerMade.setText(self.__tr("Player Made"))
        self.Drop.setText(self.__tr("Drop"))
        self.Gem_Label_1.setText(self.__tr("Gem 1:"))
        self.Points_1.setText(self.__tr("0.0"))
        self.Cost_1.setText(self.__tr("0c"))
        self.Name_1.setText(QString.null)
        self.Gem_Label_2.setText(self.__tr("Gem 2:"))
        self.Points_2.setText(self.__tr("0.0"))
        self.Cost_2.setText(self.__tr("0c"))
        self.Name_2.setText(QString.null)
        self.Gem_Label_3.setText(self.__tr("Gem 3:"))
        self.Points_3.setText(self.__tr("0.0"))
        self.Cost_3.setText(self.__tr("0c"))
        self.Name_3.setText(QString.null)
        self.Gem_Label_4.setText(self.__tr("Gem 4:"))
        self.Points_4.setText(self.__tr("0.0"))
        self.Cost_4.setText(self.__tr("0c"))
        self.Name_4.setText(QString.null)
        self.Gem_Label_5.setText(self.__tr("Gem 5:"))
        self.Gem_Label_6.setText(self.__tr("Gem 6:"))
        self.Gem_Label_7.setText(self.__tr("Gem 7:"))
        self.Gem_Label_8.setText(self.__tr("Gem 8:"))
        self.Gem_Label_9.setText(self.__tr("Gem 9:"))
        self.Gem_Label_10.setText(self.__tr("Gem10:"))
        self.ItemImbueLabel.setText(self.__tr("Imbue Points:"))
        self.ItemImbue.setText(self.__tr("0.0"))
        self.ItemImbueSlashLabel.setText(self.__tr("/"))
        self.ItemImbueTotal.setText(self.__tr("0.0"))
        self.ItemOverchargeLabel.setText(self.__tr("Overcharge:"))
        self.ItemOvercharge.setText(self.__tr("None"))
        self.ItemCostLabel.setText(self.__tr("Item Cost:"))
        self.ItemCost.setText(QString.null)
        self.LoadItem.setText(self.__tr("Load Item"))
        self.SaveItem.setText(self.__tr("Save Item"))
        self.ClearItem.setText(self.__tr("Clear Item"))


    def AmountChanged(self,a0):
        print "B_SC.AmountChanged(const QString&): Not implemented yet"

    def RealmChanged(self,a0):
        print "B_SC.RealmChanged(const QString&): Not implemented yet"

    def CharClassChanged(self,a0):
        print "B_SC.CharClassChanged(const QString&): Not implemented yet"

    def ClearCurrentItem(self):
        print "B_SC.ClearCurrentItem(): Not implemented yet"

    def DistanceCapSet(self):
        print "B_SC.DistanceCapSet(): Not implemented yet"

    def DropToggled(self,a0):
        print "B_SC.DropToggled(bool): Not implemented yet"

    def EquippedClicked(self):
        print "B_SC.EquippedClicked(): Not implemented yet"

    def ItemLevelChanged(self,a0):
        print "B_SC.ItemLevelChanged(const QString&): Not implemented yet"

    def ItemLevelShow(self):
        print "B_SC.ItemLevelShow(): Not implemented yet"

    def Load_Item(self):
        print "B_SC.Load_Item(): Not implemented yet"

    def OpenCraftWindow(self):
        print "B_SC.OpenCraftWindow(): Not implemented yet"

    def PieceTabChanged(self,a0):
        print "B_SC.PieceTabChanged(int): Not implemented yet"

    def PlayerToggled(self,a0):
        print "B_SC.PlayerToggled(bool): Not implemented yet"

    def QualityChanged(self,a0):
        print "B_SC.QualityChanged(const QString&): Not implemented yet"

    def Save_Item(self):
        print "B_SC.Save_Item(): Not implemented yet"

    def SkillClicked(self,a0):
        print "B_SC.SkillClicked(QListBoxItem*): Not implemented yet"

    def TotalBonusSet(self):
        print "B_SC.TotalBonusSet(): Not implemented yet"

    def Type_10_Changed(self,a0):
        print "B_SC.Type_10_Changed(const QString&): Not implemented yet"

    def Type_1_Changed(self,a0):
        print "B_SC.Type_1_Changed(const QString&): Not implemented yet"

    def Type_2_Changed(self,a0):
        print "B_SC.Type_2_Changed(const QString&): Not implemented yet"

    def Type_3_Changed(self,a0):
        print "B_SC.Type_3_Changed(const QString&): Not implemented yet"

    def Type_4_Changed(self,a0):
        print "B_SC.Type_4_Changed(const QString&): Not implemented yet"

    def Type_5_Changed(self,a0):
        print "B_SC.Type_5_Changed(const QString&): Not implemented yet"

    def Type_6_Changed(self,a0):
        print "B_SC.Type_6_Changed(const QString&): Not implemented yet"

    def Type_7_Changed(self,a0):
        print "B_SC.Type_7_Changed(const QString&): Not implemented yet"

    def Type_8_Changed(self,a0):
        print "B_SC.Type_8_Changed(const QString&): Not implemented yet"

    def Type_9_Changed(self,a0):
        print "B_SC.Type_9_Changed(const QString&): Not implemented yet"

    def newFile(self):
        print "B_SC.newFile(): Not implemented yet"

    def RaceChanged(self,a0):
        print "B_SC.RaceChanged(const QString&): Not implemented yet"

    def recalculate(self,a0):
        print "B_SC.recalculate(const QString&): Not implemented yet"

    def saveFile(self):
        print "B_SC.saveFile(): Not implemented yet"

    def ItemTypeChanged(self,a0):
        print "B_SC.ItemTypeChanged(int): Not implemented yet"

    def PieceTypeChanged(self,a0):
        print "B_SC.PieceTypeChanged(int): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("B_SC",s,c)
