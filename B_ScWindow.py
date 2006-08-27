# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScWindow.ui'
#
# Created: Sun Aug 27 15:32:16 2006
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

        self.GroupCharInfo = QGroupBox(self.centralWidget(),"GroupCharInfo")
        self.GroupCharInfo.setGeometry(QRect(613,3,165,182))

        self.LabelCharName = QLabel(self.GroupCharInfo,"LabelCharName")
        self.LabelCharName.setGeometry(QRect(6,16,37,21))

        self.CharName = QLineEdit(self.GroupCharInfo,"CharName")
        self.CharName.setGeometry(QRect(46,16,114,21))
        self.CharName.setFrameShape(QLineEdit.LineEditPanel)
        self.CharName.setFrameShadow(QLineEdit.Sunken)

        self.LabelRealm = QLabel(self.GroupCharInfo,"LabelRealm")
        self.LabelRealm.setGeometry(QRect(6,37,38,21))

        self.Realm = SearchingCombo(self.GroupCharInfo,"Realm")
        self.Realm.setGeometry(QRect(46,37,114,21))

        self.LabelCharClass = QLabel(self.GroupCharInfo,"LabelCharClass")
        self.LabelCharClass.setGeometry(QRect(6,59,38,21))

        self.CharClass = SearchingCombo(self.GroupCharInfo,"CharClass")
        self.CharClass.setGeometry(QRect(46,59,114,21))

        self.LabelCharRace = QLabel(self.GroupCharInfo,"LabelCharRace")
        self.LabelCharRace.setGeometry(QRect(6,81,38,21))

        self.CharRace = SearchingCombo(self.GroupCharInfo,"CharRace")
        self.CharRace.setGeometry(QRect(46,81,114,21))

        self.LabelCharLevel = QLabel(self.GroupCharInfo,"LabelCharLevel")
        self.LabelCharLevel.setGeometry(QRect(6,103,38,21))

        self.CharLevel = QLineEdit(self.GroupCharInfo,"CharLevel")
        self.CharLevel.setGeometry(QRect(46,103,37,21))

        self.TotalCostLabel = QLabel(self.GroupCharInfo,"TotalCostLabel")
        self.TotalCostLabel.setGeometry(QRect(6,126,30,16))

        self.TotalCost = QLabel(self.GroupCharInfo,"TotalCost")
        self.TotalCost.setGeometry(QRect(44,126,114,16))
        self.TotalCost.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TotalPriceLabel = QLabel(self.GroupCharInfo,"TotalPriceLabel")
        self.TotalPriceLabel.setGeometry(QRect(6,143,30,16))

        self.TotalPrice = QLabel(self.GroupCharInfo,"TotalPrice")
        self.TotalPrice.setGeometry(QRect(44,143,114,16))
        self.TotalPrice.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ItemTotalUtilityLabel = QLabel(self.GroupCharInfo,"ItemTotalUtilityLabel")
        self.ItemTotalUtilityLabel.setGeometry(QRect(6,160,70,16))

        self.ItemTotalUtility = QLabel(self.GroupCharInfo,"ItemTotalUtility")
        self.ItemTotalUtility.setGeometry(QRect(84,160,74,16))
        self.ItemTotalUtility.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.GroupStats = QGroupBox(self.centralWidget(),"GroupStats")
        self.GroupStats.setGeometry(QRect(5,3,94,182))

        self.StrengthLabel = QLabel(self.GroupStats,"StrengthLabel")
        self.StrengthLabel.setGeometry(QRect(6,16,28,16))

        self.Strength = QLabel(self.GroupStats,"Strength")
        self.Strength.setGeometry(QRect(35,16,20,16))
        self.Strength.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.StrengthCap = QLabel(self.GroupStats,"StrengthCap")
        self.StrengthCap.setGeometry(QRect(57,16,29,16))
        self.StrengthCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ConstitutionLabel = QLabel(self.GroupStats,"ConstitutionLabel")
        self.ConstitutionLabel.setGeometry(QRect(6,32,28,16))

        self.Constitution = QLabel(self.GroupStats,"Constitution")
        self.Constitution.setGeometry(QRect(35,32,20,16))
        self.Constitution.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ConstitutionCap = QLabel(self.GroupStats,"ConstitutionCap")
        self.ConstitutionCap.setGeometry(QRect(57,32,29,16))
        self.ConstitutionCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.DexterityLabel = QLabel(self.GroupStats,"DexterityLabel")
        self.DexterityLabel.setGeometry(QRect(6,48,28,16))

        self.Dexterity = QLabel(self.GroupStats,"Dexterity")
        self.Dexterity.setGeometry(QRect(35,48,20,16))
        self.Dexterity.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.DexterityCap = QLabel(self.GroupStats,"DexterityCap")
        self.DexterityCap.setGeometry(QRect(57,48,29,16))
        self.DexterityCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.QuicknessLabel = QLabel(self.GroupStats,"QuicknessLabel")
        self.QuicknessLabel.setGeometry(QRect(6,64,28,16))

        self.Quickness = QLabel(self.GroupStats,"Quickness")
        self.Quickness.setGeometry(QRect(35,64,20,16))
        self.Quickness.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.QuicknessCap = QLabel(self.GroupStats,"QuicknessCap")
        self.QuicknessCap.setGeometry(QRect(57,64,29,16))
        self.QuicknessCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.IntelligenceLabel = QLabel(self.GroupStats,"IntelligenceLabel")
        self.IntelligenceLabel.setGeometry(QRect(6,80,28,16))

        self.Intelligence = QLabel(self.GroupStats,"Intelligence")
        self.Intelligence.setGeometry(QRect(35,80,20,16))
        self.Intelligence.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.IntelligenceCap = QLabel(self.GroupStats,"IntelligenceCap")
        self.IntelligenceCap.setGeometry(QRect(57,80,29,16))
        self.IntelligenceCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.PietyLabel = QLabel(self.GroupStats,"PietyLabel")
        self.PietyLabel.setGeometry(QRect(6,96,28,16))

        self.Piety = QLabel(self.GroupStats,"Piety")
        self.Piety.setGeometry(QRect(35,96,20,16))
        self.Piety.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.PietyCap = QLabel(self.GroupStats,"PietyCap")
        self.PietyCap.setGeometry(QRect(57,96,29,16))
        self.PietyCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.CharismaLabel = QLabel(self.GroupStats,"CharismaLabel")
        self.CharismaLabel.setGeometry(QRect(6,112,28,16))

        self.Charisma = QLabel(self.GroupStats,"Charisma")
        self.Charisma.setGeometry(QRect(35,112,20,16))
        self.Charisma.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.CharismaCap = QLabel(self.GroupStats,"CharismaCap")
        self.CharismaCap.setGeometry(QRect(57,112,29,16))
        self.CharismaCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.EmpathyLabel = QLabel(self.GroupStats,"EmpathyLabel")
        self.EmpathyLabel.setGeometry(QRect(6,128,28,16))

        self.Empathy = QLabel(self.GroupStats,"Empathy")
        self.Empathy.setGeometry(QRect(35,128,20,16))
        self.Empathy.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.EmpathyCap = QLabel(self.GroupStats,"EmpathyCap")
        self.EmpathyCap.setGeometry(QRect(57,128,29,16))
        self.EmpathyCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.PowerLabel = QLabel(self.GroupStats,"PowerLabel")
        self.PowerLabel.setGeometry(QRect(6,144,28,16))

        self.Power = QLabel(self.GroupStats,"Power")
        self.Power.setGeometry(QRect(35,144,20,16))
        self.Power.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.PowerCap = QLabel(self.GroupStats,"PowerCap")
        self.PowerCap.setGeometry(QRect(57,144,29,16))
        self.PowerCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.HitsLabel = QLabel(self.GroupStats,"HitsLabel")
        self.HitsLabel.setGeometry(QRect(6,160,28,16))

        self.Hits = QLabel(self.GroupStats,"Hits")
        self.Hits.setGeometry(QRect(35,160,20,16))
        self.Hits.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.HitsCap = QLabel(self.GroupStats,"HitsCap")
        self.HitsCap.setGeometry(QRect(57,160,29,16))
        self.HitsCap.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.GroupResists = QGroupBox(self.centralWidget(),"GroupResists")
        self.GroupResists.setGeometry(QRect(105,3,90,182))

        self.BodyLabel = QLabel(self.GroupResists,"BodyLabel")
        self.BodyLabel.setGeometry(QRect(6,16,36,16))

        self.Body = QLabel(self.GroupResists,"Body")
        self.Body.setGeometry(QRect(44,16,17,16))
        self.Body.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.BodyRR = QLabel(self.GroupResists,"BodyRR")
        self.BodyRR.setGeometry(QRect(66,16,17,16))
        self.BodyRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ColdLabel = QLabel(self.GroupResists,"ColdLabel")
        self.ColdLabel.setGeometry(QRect(6,34,36,16))

        self.Cold = QLabel(self.GroupResists,"Cold")
        self.Cold.setGeometry(QRect(44,34,17,16))
        self.Cold.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ColdRR = QLabel(self.GroupResists,"ColdRR")
        self.ColdRR.setGeometry(QRect(66,34,17,16))
        self.ColdRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.HeatLabel = QLabel(self.GroupResists,"HeatLabel")
        self.HeatLabel.setGeometry(QRect(6,52,36,16))

        self.Heat = QLabel(self.GroupResists,"Heat")
        self.Heat.setGeometry(QRect(44,52,17,16))
        self.Heat.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.HeatRR = QLabel(self.GroupResists,"HeatRR")
        self.HeatRR.setGeometry(QRect(66,52,17,16))
        self.HeatRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.EnergyLabel = QLabel(self.GroupResists,"EnergyLabel")
        self.EnergyLabel.setGeometry(QRect(6,70,36,16))

        self.Energy = QLabel(self.GroupResists,"Energy")
        self.Energy.setGeometry(QRect(44,70,17,16))
        self.Energy.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.EnergyRR = QLabel(self.GroupResists,"EnergyRR")
        self.EnergyRR.setGeometry(QRect(66,70,17,16))
        self.EnergyRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.MatterLabel = QLabel(self.GroupResists,"MatterLabel")
        self.MatterLabel.setGeometry(QRect(6,88,36,16))

        self.Matter = QLabel(self.GroupResists,"Matter")
        self.Matter.setGeometry(QRect(44,88,17,16))
        self.Matter.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.MatterRR = QLabel(self.GroupResists,"MatterRR")
        self.MatterRR.setGeometry(QRect(66,88,17,16))
        self.MatterRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.SpiritLabel = QLabel(self.GroupResists,"SpiritLabel")
        self.SpiritLabel.setGeometry(QRect(6,106,36,16))

        self.Spirit = QLabel(self.GroupResists,"Spirit")
        self.Spirit.setGeometry(QRect(44,106,17,16))
        self.Spirit.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.SpiritRR = QLabel(self.GroupResists,"SpiritRR")
        self.SpiritRR.setGeometry(QRect(66,106,17,16))
        self.SpiritRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.CrushLabel = QLabel(self.GroupResists,"CrushLabel")
        self.CrushLabel.setGeometry(QRect(6,124,36,16))

        self.Crush = QLabel(self.GroupResists,"Crush")
        self.Crush.setGeometry(QRect(44,124,17,16))
        self.Crush.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.CrushRR = QLabel(self.GroupResists,"CrushRR")
        self.CrushRR.setGeometry(QRect(66,124,17,16))
        self.CrushRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ThrustLabel = QLabel(self.GroupResists,"ThrustLabel")
        self.ThrustLabel.setGeometry(QRect(6,142,36,16))

        self.Thrust = QLabel(self.GroupResists,"Thrust")
        self.Thrust.setGeometry(QRect(44,142,17,16))
        self.Thrust.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ThrustRR = QLabel(self.GroupResists,"ThrustRR")
        self.ThrustRR.setGeometry(QRect(66,142,17,16))
        self.ThrustRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.SlashLabel = QLabel(self.GroupResists,"SlashLabel")
        self.SlashLabel.setGeometry(QRect(6,160,36,16))

        self.Slash = QLabel(self.GroupResists,"Slash")
        self.Slash.setGeometry(QRect(44,160,17,16))
        self.Slash.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.SlashRR = QLabel(self.GroupResists,"SlashRR")
        self.SlashRR.setGeometry(QRect(66,160,17,16))
        self.SlashRR.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.GroupSkillsList = QGroupBox(self.centralWidget(),"GroupSkillsList")
        self.GroupSkillsList.setGeometry(QRect(201,3,160,182))

        self.SkillsList = QListBox(self.GroupSkillsList,"SkillsList")
        self.SkillsList.setGeometry(QRect(5,16,150,160))

        self.GroupOtherBonusList = QGroupBox(self.centralWidget(),"GroupOtherBonusList")
        self.GroupOtherBonusList.setGeometry(QRect(367,3,240,182))

        self.OtherBonusList = QListBox(self.GroupOtherBonusList,"OtherBonusList")
        self.OtherBonusList.setGeometry(QRect(5,15,230,160))

        self.GroupItemFrame = QGroupBox(self.centralWidget(),"GroupItemFrame")
        self.GroupItemFrame.setGeometry(QRect(3,235,776,265))
        self.GroupItemFrame.setFrameShape(QGroupBox.StyledPanel)
        self.GroupItemFrame.setFrameShadow(QGroupBox.Raised)

        self.ItemLevelLabel = QLabel(self.GroupItemFrame,"ItemLevelLabel")
        self.ItemLevelLabel.setGeometry(QRect(7,5,34,21))

        self.ItemLevel = QLineEdit(self.GroupItemFrame,"ItemLevel")
        self.ItemLevel.setGeometry(QRect(46,5,35,21))

        self.ItemLevelButton = QPushButton(self.GroupItemFrame,"ItemLevelButton")
        self.ItemLevelButton.setGeometry(QRect(81,5,21,21))

        self.ItemQualityLabel = QLabel(self.GroupItemFrame,"ItemQualityLabel")
        self.ItemQualityLabel.setGeometry(QRect(115,5,54,21))

        self.QualDrop = SearchingCombo(self.GroupItemFrame,"QualDrop")
        self.QualDrop.setGeometry(QRect(160,5,52,21))

        self.QualEdit = QLineEdit(self.GroupItemFrame,"QualEdit")
        self.QualEdit.setGeometry(QRect(160,5,51,21))

        self.ItemBonusLabel = QLabel(self.GroupItemFrame,"ItemBonusLabel")
        self.ItemBonusLabel.setGeometry(QRect(232,5,40,21))

        self.Bonus_Edit = QLineEdit(self.GroupItemFrame,"Bonus_Edit")
        self.Bonus_Edit.setGeometry(QRect(272,5,35,21))

        self.ItemAFDPSLabel = QLabel(self.GroupItemFrame,"ItemAFDPSLabel")
        self.ItemAFDPSLabel.setGeometry(QRect(315,5,55,21))

        self.AFDPS_Edit = QLineEdit(self.GroupItemFrame,"AFDPS_Edit")
        self.AFDPS_Edit.setGeometry(QRect(360,5,35,21))

        self.ItemSpeedLabel = QLabel(self.GroupItemFrame,"ItemSpeedLabel")
        self.ItemSpeedLabel.setGeometry(QRect(403,5,40,21))

        self.Speed_Edit = QLineEdit(self.GroupItemFrame,"Speed_Edit")
        self.Speed_Edit.setGeometry(QRect(443,5,35,21))

        self.Equipped = QCheckBox(self.GroupItemFrame,"Equipped")
        self.Equipped.setGeometry(QRect(509,5,71,21))

        self.ButtonGroup1 = QButtonGroup(self.GroupItemFrame,"ButtonGroup1")
        self.ButtonGroup1.setEnabled(1)
        self.ButtonGroup1.setGeometry(QRect(615,5,138,21))
        self.ButtonGroup1.setLineWidth(0)

        self.PlayerMade = QRadioButton(self.ButtonGroup1,"PlayerMade")
        self.PlayerMade.setGeometry(QRect(2,2,85,17))

        self.Drop = QRadioButton(self.ButtonGroup1,"Drop")
        self.Drop.setGeometry(QRect(92,2,52,17))
        self.Drop.setChecked(1)

        self.ItemName = QLineEdit(self.GroupItemFrame,"ItemName")
        self.ItemName.setGeometry(QRect(562,48,200,21))

        self.LabelGemType = QLabel(self.GroupItemFrame,"LabelGemType")
        self.LabelGemType.setGeometry(QRect(50,31,119,17))

        self.LabelGemAmount = QLabel(self.GroupItemFrame,"LabelGemAmount")
        self.LabelGemAmount.setGeometry(QRect(181,31,44,17))

        self.LabelGemEffect = QLabel(self.GroupItemFrame,"LabelGemEffect")
        self.LabelGemEffect.setGeometry(QRect(237,31,142,17))

        self.LabelGemQuality = QLabel(self.GroupItemFrame,"LabelGemQuality")
        self.LabelGemQuality.setGeometry(QRect(391,31,44,17))

        self.LabelGemPoints = QLabel(self.GroupItemFrame,"LabelGemPoints")
        self.LabelGemPoints.setGeometry(QRect(443,31,35,17))
        self.LabelGemPoints.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.LabelGemCost = QLabel(self.GroupItemFrame,"LabelGemCost")
        self.LabelGemCost.setGeometry(QRect(482,31,70,17))
        self.LabelGemCost.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ItemNameLabel = QLabel(self.GroupItemFrame,"ItemNameLabel")
        self.ItemNameLabel.setGeometry(QRect(562,31,70,17))

        self.Gem_Label_1 = QLabel(self.GroupItemFrame,"Gem_Label_1")
        self.Gem_Label_1.setGeometry(QRect(7,48,34,21))

        self.Type_1 = SearchingCombo(self.GroupItemFrame,"Type_1")
        self.Type_1.setGeometry(QRect(46,48,127,21))

        self.Amount_Edit_1 = QLineEdit(self.GroupItemFrame,"Amount_Edit_1")
        self.Amount_Edit_1.setGeometry(QRect(177,48,51,21))

        self.Amount_Drop_1 = SearchingCombo(self.GroupItemFrame,"Amount_Drop_1")
        self.Amount_Drop_1.setGeometry(QRect(177,48,52,21))

        self.Effect_1 = SearchingCombo(self.GroupItemFrame,"Effect_1")
        self.Effect_1.setEditable(1)
        self.Effect_1.setGeometry(QRect(233,48,150,21))

        self.Quality_1 = SearchingCombo(self.GroupItemFrame,"Quality_1")
        self.Quality_1.setGeometry(QRect(387,48,52,21))

        self.Points_1 = QLabel(self.GroupItemFrame,"Points_1")
        self.Points_1.setGeometry(QRect(443,48,35,21))
        self.Points_1.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_1 = QLabel(self.GroupItemFrame,"Cost_1")
        self.Cost_1.setGeometry(QRect(482,48,70,21))
        self.Cost_1.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_1 = QLabel(self.GroupItemFrame,"Name_1")
        self.Name_1.setGeometry(QRect(562,48,200,21))

        self.Gem_Label_2 = QLabel(self.GroupItemFrame,"Gem_Label_2")
        self.Gem_Label_2.setGeometry(QRect(7,69,34,21))

        self.Amount_Edit_2 = QLineEdit(self.GroupItemFrame,"Amount_Edit_2")
        self.Amount_Edit_2.setGeometry(QRect(177,69,51,21))

        self.Amount_Drop_2 = SearchingCombo(self.GroupItemFrame,"Amount_Drop_2")
        self.Amount_Drop_2.setGeometry(QRect(177,69,52,21))

        self.Type_2 = SearchingCombo(self.GroupItemFrame,"Type_2")
        self.Type_2.setGeometry(QRect(46,69,127,21))

        self.Effect_2 = SearchingCombo(self.GroupItemFrame,"Effect_2")
        self.Effect_2.setEditable(1)
        self.Effect_2.setGeometry(QRect(233,69,150,21))

        self.Quality_2 = SearchingCombo(self.GroupItemFrame,"Quality_2")
        self.Quality_2.setGeometry(QRect(387,69,52,21))

        self.Points_2 = QLabel(self.GroupItemFrame,"Points_2")
        self.Points_2.setGeometry(QRect(443,69,35,21))
        self.Points_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_2 = QLabel(self.GroupItemFrame,"Cost_2")
        self.Cost_2.setGeometry(QRect(482,69,70,21))
        self.Cost_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_2 = QLabel(self.GroupItemFrame,"Name_2")
        self.Name_2.setGeometry(QRect(562,69,200,21))

        self.Gem_Label_3 = QLabel(self.GroupItemFrame,"Gem_Label_3")
        self.Gem_Label_3.setGeometry(QRect(7,90,34,21))

        self.Type_3 = SearchingCombo(self.GroupItemFrame,"Type_3")
        self.Type_3.setGeometry(QRect(46,90,127,21))

        self.Amount_Edit_3 = QLineEdit(self.GroupItemFrame,"Amount_Edit_3")
        self.Amount_Edit_3.setGeometry(QRect(177,90,51,21))

        self.Amount_Drop_3 = SearchingCombo(self.GroupItemFrame,"Amount_Drop_3")
        self.Amount_Drop_3.setGeometry(QRect(177,90,52,21))

        self.Effect_3 = SearchingCombo(self.GroupItemFrame,"Effect_3")
        self.Effect_3.setEditable(1)
        self.Effect_3.setGeometry(QRect(233,90,150,21))

        self.Quality_3 = SearchingCombo(self.GroupItemFrame,"Quality_3")
        self.Quality_3.setGeometry(QRect(387,90,52,21))

        self.Points_3 = QLabel(self.GroupItemFrame,"Points_3")
        self.Points_3.setGeometry(QRect(443,90,35,21))
        self.Points_3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_3 = QLabel(self.GroupItemFrame,"Cost_3")
        self.Cost_3.setGeometry(QRect(482,90,70,21))
        self.Cost_3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_3 = QLabel(self.GroupItemFrame,"Name_3")
        self.Name_3.setGeometry(QRect(562,90,200,21))

        self.Gem_Label_4 = QLabel(self.GroupItemFrame,"Gem_Label_4")
        self.Gem_Label_4.setGeometry(QRect(7,111,34,21))

        self.Type_4 = SearchingCombo(self.GroupItemFrame,"Type_4")
        self.Type_4.setGeometry(QRect(46,111,127,21))

        self.Amount_Edit_4 = QLineEdit(self.GroupItemFrame,"Amount_Edit_4")
        self.Amount_Edit_4.setGeometry(QRect(177,111,51,21))

        self.Amount_Drop_4 = SearchingCombo(self.GroupItemFrame,"Amount_Drop_4")
        self.Amount_Drop_4.setGeometry(QRect(177,111,52,21))

        self.Effect_4 = SearchingCombo(self.GroupItemFrame,"Effect_4")
        self.Effect_4.setEditable(1)
        self.Effect_4.setGeometry(QRect(233,111,150,21))

        self.Quality_4 = SearchingCombo(self.GroupItemFrame,"Quality_4")
        self.Quality_4.setGeometry(QRect(387,111,52,21))

        self.Points_4 = QLabel(self.GroupItemFrame,"Points_4")
        self.Points_4.setGeometry(QRect(443,111,35,21))
        self.Points_4.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_4 = QLabel(self.GroupItemFrame,"Cost_4")
        self.Cost_4.setGeometry(QRect(482,111,70,21))
        self.Cost_4.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_4 = QLabel(self.GroupItemFrame,"Name_4")
        self.Name_4.setGeometry(QRect(562,111,200,21))

        self.Gem_Label_5 = QLabel(self.GroupItemFrame,"Gem_Label_5")
        self.Gem_Label_5.setGeometry(QRect(7,132,34,21))

        self.Type_5 = SearchingCombo(self.GroupItemFrame,"Type_5")
        self.Type_5.setGeometry(QRect(46,132,127,21))

        self.Amount_Edit_5 = QLineEdit(self.GroupItemFrame,"Amount_Edit_5")
        self.Amount_Edit_5.setGeometry(QRect(177,132,51,21))

        self.Amount_Drop_5 = SearchingCombo(self.GroupItemFrame,"Amount_Drop_5")
        self.Amount_Drop_5.setGeometry(QRect(177,132,52,21))

        self.Effect_5 = SearchingCombo(self.GroupItemFrame,"Effect_5")
        self.Effect_5.setEditable(1)
        self.Effect_5.setGeometry(QRect(233,132,206,21))

        self.Quality_5 = SearchingCombo(self.GroupItemFrame,"Quality_5")
        self.Quality_5.setGeometry(QRect(387,132,52,21))

        self.Points_5 = QLabel(self.GroupItemFrame,"Points_5")
        self.Points_5.setGeometry(QRect(443,132,35,21))
        self.Points_5.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Cost_5 = QLabel(self.GroupItemFrame,"Cost_5")
        self.Cost_5.setGeometry(QRect(482,132,70,21))
        self.Cost_5.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Name_5 = QLabel(self.GroupItemFrame,"Name_5")
        self.Name_5.setGeometry(QRect(562,132,200,21))

        self.Gem_Label_6 = QLabel(self.GroupItemFrame,"Gem_Label_6")
        self.Gem_Label_6.setGeometry(QRect(7,153,34,21))

        self.Type_6 = SearchingCombo(self.GroupItemFrame,"Type_6")
        self.Type_6.setGeometry(QRect(46,153,127,21))

        self.Amount_Edit_6 = QLineEdit(self.GroupItemFrame,"Amount_Edit_6")
        self.Amount_Edit_6.setGeometry(QRect(177,153,51,21))

        self.Effect_6 = SearchingCombo(self.GroupItemFrame,"Effect_6")
        self.Effect_6.setEditable(1)
        self.Effect_6.setGeometry(QRect(233,153,206,21))

        self.Gem_Label_7 = QLabel(self.GroupItemFrame,"Gem_Label_7")
        self.Gem_Label_7.setGeometry(QRect(7,174,34,21))

        self.Type_7 = SearchingCombo(self.GroupItemFrame,"Type_7")
        self.Type_7.setGeometry(QRect(46,174,127,21))

        self.Amount_Edit_7 = QLineEdit(self.GroupItemFrame,"Amount_Edit_7")
        self.Amount_Edit_7.setGeometry(QRect(177,174,51,21))

        self.Effect_7 = SearchingCombo(self.GroupItemFrame,"Effect_7")
        self.Effect_7.setEditable(1)
        self.Effect_7.setGeometry(QRect(233,174,206,21))

        self.Gem_Label_8 = QLabel(self.GroupItemFrame,"Gem_Label_8")
        self.Gem_Label_8.setGeometry(QRect(7,195,34,21))

        self.Type_8 = SearchingCombo(self.GroupItemFrame,"Type_8")
        self.Type_8.setGeometry(QRect(46,195,127,21))

        self.Amount_Edit_8 = QLineEdit(self.GroupItemFrame,"Amount_Edit_8")
        self.Amount_Edit_8.setGeometry(QRect(177,195,51,21))

        self.Effect_8 = SearchingCombo(self.GroupItemFrame,"Effect_8")
        self.Effect_8.setEditable(1)
        self.Effect_8.setGeometry(QRect(233,195,206,21))

        self.Gem_Label_9 = QLabel(self.GroupItemFrame,"Gem_Label_9")
        self.Gem_Label_9.setGeometry(QRect(7,216,34,21))

        self.Type_9 = SearchingCombo(self.GroupItemFrame,"Type_9")
        self.Type_9.setGeometry(QRect(46,216,127,21))

        self.Amount_Edit_9 = QLineEdit(self.GroupItemFrame,"Amount_Edit_9")
        self.Amount_Edit_9.setGeometry(QRect(177,216,51,21))

        self.Effect_9 = SearchingCombo(self.GroupItemFrame,"Effect_9")
        self.Effect_9.setEditable(1)
        self.Effect_9.setGeometry(QRect(233,216,206,21))

        self.Gem_Label_10 = QLabel(self.GroupItemFrame,"Gem_Label_10")
        self.Gem_Label_10.setGeometry(QRect(7,237,41,21))

        self.Type_10 = SearchingCombo(self.GroupItemFrame,"Type_10")
        self.Type_10.setGeometry(QRect(46,237,127,21))

        self.Amount_Edit_10 = QLineEdit(self.GroupItemFrame,"Amount_Edit_10")
        self.Amount_Edit_10.setGeometry(QRect(177,237,51,21))

        self.Effect_10 = SearchingCombo(self.GroupItemFrame,"Effect_10")
        self.Effect_10.setEditable(1)
        self.Effect_10.setGeometry(QRect(233,237,206,21))

        self.ItemImbueLabel = QLabel(self.GroupItemFrame,"ItemImbueLabel")
        self.ItemImbueLabel.setGeometry(QRect(370,178,73,17))

        self.ItemImbue = QLabel(self.GroupItemFrame,"ItemImbue")
        self.ItemImbue.setGeometry(QRect(443,178,35,17))
        self.ItemImbue.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ItemImbueSlashLabel = QLabel(self.GroupItemFrame,"ItemImbueSlashLabel")
        self.ItemImbueSlashLabel.setGeometry(QRect(487,178,8,17))

        self.ItemImbueTotal = QLabel(self.GroupItemFrame,"ItemImbueTotal")
        self.ItemImbueTotal.setGeometry(QRect(498,178,29,17))

        self.ItemOverchargeLabel = QLabel(self.GroupItemFrame,"ItemOverchargeLabel")
        self.ItemOverchargeLabel.setGeometry(QRect(370,195,73,17))

        self.ItemOvercharge = QLabel(self.GroupItemFrame,"ItemOvercharge")
        self.ItemOvercharge.setGeometry(QRect(443,195,90,17))
        self.ItemOvercharge.setAlignment(QLabel.AlignCenter)

        self.ItemCostLabel = QLabel(self.GroupItemFrame,"ItemCostLabel")
        self.ItemCostLabel.setGeometry(QRect(370,220,73,17))

        self.ItemCost = QLabel(self.GroupItemFrame,"ItemCost")
        self.ItemCost.setGeometry(QRect(482,220,70,17))
        self.ItemCost.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ItemPriceLabel = QLabel(self.GroupItemFrame,"ItemPriceLabel")
        self.ItemPriceLabel.setGeometry(QRect(370,237,73,17))

        self.ItemPrice = QLabel(self.GroupItemFrame,"ItemPrice")
        self.ItemPrice.setGeometry(QRect(482,237,70,17))
        self.ItemPrice.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.ItemUtilityLabel = QLabel(self.GroupItemFrame,"ItemUtilityLabel")
        self.ItemUtilityLabel.setGeometry(QRect(585,237,35,17))

        self.ItemUtility = QLabel(self.GroupItemFrame,"ItemUtility")
        self.ItemUtility.setGeometry(QRect(625,237,30,17))
        self.ItemUtility.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.LoadItem = QPushButton(self.GroupItemFrame,"LoadItem")
        self.LoadItem.setGeometry(QRect(683,165,79,26))

        self.CraftButton = QPushButton(self.GroupItemFrame,"CraftButton")
        self.CraftButton.setGeometry(QRect(683,199,79,26))

        self.SaveItem = QPushButton(self.GroupItemFrame,"SaveItem")
        self.SaveItem.setGeometry(QRect(683,199,79,26))

        self.ClearItem = QPushButton(self.GroupItemFrame,"ClearItem")
        self.ClearItem.setGeometry(QRect(683,233,79,26))

        self.PieceTab = MultiTabBar(self.centralWidget(),"PieceTab")
        self.PieceTab.setGeometry(QRect(3,190,776,46))

        self.languageChange()

        self.resize(QSize(781,525).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.PieceTab,SIGNAL("selected(int)"),self.PieceTabChanged)
        self.connect(self.PlayerMade,SIGNAL("toggled(bool)"),self.PlayerToggled)
        self.connect(self.Drop,SIGNAL("toggled(bool)"),self.DropToggled)
        self.connect(self.Type_1,SIGNAL("activated(const QString&)"),self.TypeChanged)
        self.connect(self.Type_2,SIGNAL("activated(const QString&)"),self.TypeChanged)
        self.connect(self.Type_3,SIGNAL("activated(const QString&)"),self.TypeChanged)
        self.connect(self.Type_4,SIGNAL("activated(const QString&)"),self.TypeChanged)
        self.connect(self.Type_5,SIGNAL("activated(const QString&)"),self.TypeChanged)
        self.connect(self.Type_6,SIGNAL("activated(const QString&)"),self.TypeChanged)
        self.connect(self.Type_7,SIGNAL("activated(const QString&)"),self.TypeChanged)
        self.connect(self.Type_8,SIGNAL("activated(const QString&)"),self.TypeChanged)
        self.connect(self.Type_9,SIGNAL("activated(const QString&)"),self.TypeChanged)
        self.connect(self.Type_10,SIGNAL("activated(const QString&)"),self.TypeChanged)
        self.connect(self.Amount_Drop_1,SIGNAL("activated(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Drop_2,SIGNAL("activated(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Drop_3,SIGNAL("activated(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Drop_4,SIGNAL("activated(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Drop_5,SIGNAL("activated(const QString&)"),self.AmountChanged)
        self.connect(self.Effect_1,SIGNAL("activated(const QString&)"),self.EffectChanged)
        self.connect(self.Effect_2,SIGNAL("activated(const QString&)"),self.EffectChanged)
        self.connect(self.Effect_3,SIGNAL("activated(const QString&)"),self.EffectChanged)
        self.connect(self.Effect_4,SIGNAL("activated(const QString&)"),self.EffectChanged)
        self.connect(self.Effect_5,SIGNAL("activated(const QString&)"),self.EffectChanged)
        self.connect(self.Effect_6,SIGNAL("activated(const QString&)"),self.EffectChanged)
        self.connect(self.Effect_7,SIGNAL("activated(const QString&)"),self.EffectChanged)
        self.connect(self.Effect_8,SIGNAL("activated(const QString&)"),self.EffectChanged)
        self.connect(self.Effect_9,SIGNAL("activated(const QString&)"),self.EffectChanged)
        self.connect(self.Effect_10,SIGNAL("activated(const QString&)"),self.EffectChanged)
        self.connect(self.QualDrop,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.ItemLevel,SIGNAL("textChanged(const QString&)"),self.recalculate)
        self.connect(self.Quality_1,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Quality_2,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Quality_3,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Quality_4,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.Quality_5,SIGNAL("activated(const QString&)"),self.recalculate)
        self.connect(self.ClearItem,SIGNAL("clicked()"),self.ClearCurrentItem)
        self.connect(self.Equipped,SIGNAL("clicked()"),self.EquippedClicked)
        self.connect(self.ItemLevelButton,SIGNAL("clicked()"),self.ItemLevelShow)
        self.connect(self.Amount_Edit_1,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_2,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_3,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_4,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_5,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_6,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_7,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_8,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_9,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
        self.connect(self.Amount_Edit_10,SIGNAL("textChanged(const QString&)"),self.AmountChanged)
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
        self.connect(self.CharRace,SIGNAL("activated(const QString&)"),self.RaceChanged)

        self.setTabOrder(self.CharName,self.Realm)
        self.setTabOrder(self.Realm,self.CharClass)
        self.setTabOrder(self.CharClass,self.CharRace)
        self.setTabOrder(self.CharRace,self.CharLevel)
        self.setTabOrder(self.CharLevel,self.PieceTab)
        self.setTabOrder(self.PieceTab,self.ItemLevel)
        self.setTabOrder(self.ItemLevel,self.ItemLevelButton)
        self.setTabOrder(self.ItemLevelButton,self.QualEdit)
        self.setTabOrder(self.QualEdit,self.QualDrop)
        self.setTabOrder(self.QualDrop,self.Bonus_Edit)
        self.setTabOrder(self.Bonus_Edit,self.AFDPS_Edit)
        self.setTabOrder(self.AFDPS_Edit,self.Speed_Edit)
        self.setTabOrder(self.Speed_Edit,self.Equipped)
        self.setTabOrder(self.Equipped,self.PlayerMade)
        self.setTabOrder(self.PlayerMade,self.Drop)
        self.setTabOrder(self.Drop,self.ItemName)
        self.setTabOrder(self.ItemName,self.Type_1)
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
        self.setTabOrder(self.Amount_Edit_5,self.Amount_Drop_5)
        self.setTabOrder(self.Amount_Drop_5,self.Effect_5)
        self.setTabOrder(self.Effect_5,self.Quality_5)
        self.setTabOrder(self.Quality_5,self.Type_6)
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
        self.setTabOrder(self.Effect_10,self.CraftButton)
        self.setTabOrder(self.CraftButton,self.LoadItem)
        self.setTabOrder(self.LoadItem,self.SaveItem)
        self.setTabOrder(self.SaveItem,self.ClearItem)
        self.setTabOrder(self.ClearItem,self.SkillsList)
        self.setTabOrder(self.SkillsList,self.OtherBonusList)


    def languageChange(self):
        self.setCaption(self.__tr("Spellcrafting Calculator"))
        self.GroupCharInfo.setTitle(self.__tr("Char Info"))
        self.LabelCharName.setText(self.__tr("Name:"))
        self.LabelRealm.setText(self.__tr("Realm:"))
        self.LabelCharClass.setText(self.__tr("Class:"))
        self.LabelCharRace.setText(self.__tr("Race:"))
        self.LabelCharLevel.setText(self.__tr("Level:"))
        self.TotalCostLabel.setText(self.__tr("Cost:"))
        self.TotalCost.setText(self.__tr("0"))
        self.TotalPriceLabel.setText(self.__tr("Price:"))
        self.TotalPrice.setText(self.__tr("0"))
        self.ItemTotalUtilityLabel.setText(self.__tr("Total Utility:"))
        self.ItemTotalUtility.setText(self.__tr("0.0"))
        self.GroupStats.setTitle(self.__tr("Stats"))
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
        self.GroupResists.setTitle(self.__tr("Resists"))
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
        self.GroupSkillsList.setTitle(self.__tr("Skills"))
        self.GroupOtherBonusList.setTitle(self.__tr("Other Bonuses"))
        self.GroupItemFrame.setTitle(QString.null)
        self.ItemLevelLabel.setText(self.__tr("Level:"))
        self.ItemLevelButton.setText(self.__tr("..."))
        self.ItemQualityLabel.setText(self.__tr("Quality:"))
        self.ItemBonusLabel.setText(self.__tr("Bonus:"))
        self.ItemAFDPSLabel.setText(self.__tr("AF/DPS:"))
        self.ItemSpeedLabel.setText(self.__tr("Speed:"))
        self.Equipped.setText(self.__tr("Equipped"))
        self.ButtonGroup1.setTitle(QString.null)
        self.PlayerMade.setText(self.__tr("Player Made"))
        self.Drop.setText(self.__tr("Drop"))
        self.LabelGemType.setText(self.__tr("Type"))
        self.LabelGemAmount.setText(self.__tr("Amount"))
        self.LabelGemEffect.setText(self.__tr("Effect"))
        self.LabelGemQuality.setText(self.__tr("Quality"))
        self.LabelGemPoints.setText(self.__tr("Points"))
        self.LabelGemCost.setText(self.__tr("Cost"))
        self.ItemNameLabel.setText(self.__tr("Name"))
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
        self.Points_5.setText(self.__tr("0.0"))
        self.Cost_5.setText(self.__tr("0c"))
        self.Name_5.setText(QString.null)
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
        self.ItemPriceLabel.setText(self.__tr("Item Price:"))
        self.ItemPrice.setText(QString.null)
        self.ItemUtilityLabel.setText(self.__tr("Utility:"))
        self.ItemUtility.setText(self.__tr("0.0"))
        self.LoadItem.setText(self.__tr("Load Item"))
        self.CraftButton.setText(self.__tr("Craft..."))
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

    def TypeChanged(self,a0):
        print "B_SC.TypeChanged(const QString&): Not implemented yet"

    def EffectChanged(self,a0):
        print "B_SC.EffectChanged(const QString&): Not implemented yet"

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
