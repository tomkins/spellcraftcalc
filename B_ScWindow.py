# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScWindow.ui'
#
# Created: Tue Oct 03 22:15:07 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from MultiTabBar4 import MultiTabBar4
from MultiTabBar4 import MultiTabFrame
from SearchingCombo import SearchingCombo
from PyQt4 import QtCore, QtGui

class Ui_B_SC(object):
    def setupUi(self, B_SC):
        B_SC.setObjectName("B_SC")
        B_SC.resize(QtCore.QSize(QtCore.QRect(0,0,781,567).size()).expandedTo(B_SC.minimumSizeHint()))

        self.ScWinFrame = QtGui.QWidget(B_SC)
        self.ScWinFrame.setObjectName("ScWinFrame")

        self.GroupCharInfo = QtGui.QGroupBox(self.ScWinFrame)
        self.GroupCharInfo.setGeometry(QtCore.QRect(613,3,165,182))
        self.GroupCharInfo.setObjectName("GroupCharInfo")

        self.LabelCharName = QtGui.QLabel(self.GroupCharInfo)
        self.LabelCharName.setGeometry(QtCore.QRect(6,16,37,21))
        self.LabelCharName.setObjectName("LabelCharName")

        self.CharName = QtGui.QLineEdit(self.GroupCharInfo)
        self.CharName.setGeometry(QtCore.QRect(46,16,114,21))
        self.CharName.setObjectName("CharName")

        self.LabelRealm = QtGui.QLabel(self.GroupCharInfo)
        self.LabelRealm.setGeometry(QtCore.QRect(6,37,38,21))
        self.LabelRealm.setObjectName("LabelRealm")

        self.Realm = SearchingCombo(self.GroupCharInfo)
        self.Realm.setGeometry(QtCore.QRect(46,37,114,21))
        self.Realm.setObjectName("Realm")

        self.LabelCharClass = QtGui.QLabel(self.GroupCharInfo)
        self.LabelCharClass.setGeometry(QtCore.QRect(6,59,38,21))
        self.LabelCharClass.setObjectName("LabelCharClass")

        self.CharClass = SearchingCombo(self.GroupCharInfo)
        self.CharClass.setGeometry(QtCore.QRect(46,59,114,21))
        self.CharClass.setObjectName("CharClass")

        self.LabelCharRace = QtGui.QLabel(self.GroupCharInfo)
        self.LabelCharRace.setGeometry(QtCore.QRect(6,81,38,21))
        self.LabelCharRace.setObjectName("LabelCharRace")

        self.CharRace = SearchingCombo(self.GroupCharInfo)
        self.CharRace.setGeometry(QtCore.QRect(46,81,114,21))
        self.CharRace.setObjectName("CharRace")

        self.LabelCharLevel = QtGui.QLabel(self.GroupCharInfo)
        self.LabelCharLevel.setGeometry(QtCore.QRect(6,103,38,21))
        self.LabelCharLevel.setObjectName("LabelCharLevel")

        self.CharLevel = QtGui.QLineEdit(self.GroupCharInfo)
        self.CharLevel.setGeometry(QtCore.QRect(46,103,37,21))
        self.CharLevel.setObjectName("CharLevel")

        self.LabelTotalCost = QtGui.QLabel(self.GroupCharInfo)
        self.LabelTotalCost.setGeometry(QtCore.QRect(6,126,30,16))
        self.LabelTotalCost.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.LabelTotalCost.setObjectName("LabelTotalCost")

        self.TotalCost = QtGui.QLabel(self.GroupCharInfo)
        self.TotalCost.setGeometry(QtCore.QRect(44,126,114,16))
        self.TotalCost.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.TotalCost.setObjectName("TotalCost")

        self.LabelTotalPrice = QtGui.QLabel(self.GroupCharInfo)
        self.LabelTotalPrice.setGeometry(QtCore.QRect(6,143,30,16))
        self.LabelTotalPrice.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.LabelTotalPrice.setObjectName("LabelTotalPrice")

        self.TotalPrice = QtGui.QLabel(self.GroupCharInfo)
        self.TotalPrice.setGeometry(QtCore.QRect(44,143,114,16))
        self.TotalPrice.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.TotalPrice.setObjectName("TotalPrice")

        self.LabelTotalUtility = QtGui.QLabel(self.GroupCharInfo)
        self.LabelTotalUtility.setGeometry(QtCore.QRect(6,160,70,16))
        self.LabelTotalUtility.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.LabelTotalUtility.setObjectName("LabelTotalUtility")

        self.TotalUtility = QtGui.QLabel(self.GroupCharInfo)
        self.TotalUtility.setGeometry(QtCore.QRect(84,160,74,16))
        self.TotalUtility.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.TotalUtility.setObjectName("TotalUtility")

        self.GroupStats = QtGui.QGroupBox(self.ScWinFrame)
        self.GroupStats.setGeometry(QtCore.QRect(5,3,94,182))
        self.GroupStats.setObjectName("GroupStats")

        self.StrengthLabel = QtGui.QLabel(self.GroupStats)
        self.StrengthLabel.setGeometry(QtCore.QRect(6,16,28,16))
        self.StrengthLabel.setObjectName("StrengthLabel")

        self.Strength = QtGui.QLabel(self.GroupStats)
        self.Strength.setGeometry(QtCore.QRect(35,16,20,16))
        self.Strength.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Strength.setObjectName("Strength")

        self.StrengthCap = QtGui.QLabel(self.GroupStats)
        self.StrengthCap.setGeometry(QtCore.QRect(57,16,29,16))
        self.StrengthCap.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.StrengthCap.setObjectName("StrengthCap")

        self.ConstitutionLabel = QtGui.QLabel(self.GroupStats)
        self.ConstitutionLabel.setGeometry(QtCore.QRect(6,32,28,16))
        self.ConstitutionLabel.setObjectName("ConstitutionLabel")

        self.Constitution = QtGui.QLabel(self.GroupStats)
        self.Constitution.setGeometry(QtCore.QRect(35,32,20,16))
        self.Constitution.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Constitution.setObjectName("Constitution")

        self.ConstitutionCap = QtGui.QLabel(self.GroupStats)
        self.ConstitutionCap.setGeometry(QtCore.QRect(57,32,29,16))
        self.ConstitutionCap.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ConstitutionCap.setObjectName("ConstitutionCap")

        self.DexterityLabel = QtGui.QLabel(self.GroupStats)
        self.DexterityLabel.setGeometry(QtCore.QRect(6,48,28,16))
        self.DexterityLabel.setObjectName("DexterityLabel")

        self.Dexterity = QtGui.QLabel(self.GroupStats)
        self.Dexterity.setGeometry(QtCore.QRect(35,48,20,16))
        self.Dexterity.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Dexterity.setObjectName("Dexterity")

        self.DexterityCap = QtGui.QLabel(self.GroupStats)
        self.DexterityCap.setGeometry(QtCore.QRect(57,48,29,16))
        self.DexterityCap.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.DexterityCap.setObjectName("DexterityCap")

        self.QuicknessLabel = QtGui.QLabel(self.GroupStats)
        self.QuicknessLabel.setGeometry(QtCore.QRect(6,64,28,16))
        self.QuicknessLabel.setObjectName("QuicknessLabel")

        self.Quickness = QtGui.QLabel(self.GroupStats)
        self.Quickness.setGeometry(QtCore.QRect(35,64,20,16))
        self.Quickness.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Quickness.setObjectName("Quickness")

        self.QuicknessCap = QtGui.QLabel(self.GroupStats)
        self.QuicknessCap.setGeometry(QtCore.QRect(57,64,29,16))
        self.QuicknessCap.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.QuicknessCap.setObjectName("QuicknessCap")

        self.IntelligenceLabel = QtGui.QLabel(self.GroupStats)
        self.IntelligenceLabel.setGeometry(QtCore.QRect(6,80,28,16))
        self.IntelligenceLabel.setObjectName("IntelligenceLabel")

        self.Intelligence = QtGui.QLabel(self.GroupStats)
        self.Intelligence.setGeometry(QtCore.QRect(35,80,20,16))
        self.Intelligence.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Intelligence.setObjectName("Intelligence")

        self.IntelligenceCap = QtGui.QLabel(self.GroupStats)
        self.IntelligenceCap.setGeometry(QtCore.QRect(57,80,29,16))
        self.IntelligenceCap.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.IntelligenceCap.setObjectName("IntelligenceCap")

        self.PietyLabel = QtGui.QLabel(self.GroupStats)
        self.PietyLabel.setGeometry(QtCore.QRect(6,96,28,16))
        self.PietyLabel.setObjectName("PietyLabel")

        self.Piety = QtGui.QLabel(self.GroupStats)
        self.Piety.setGeometry(QtCore.QRect(35,96,20,16))
        self.Piety.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Piety.setObjectName("Piety")

        self.PietyCap = QtGui.QLabel(self.GroupStats)
        self.PietyCap.setGeometry(QtCore.QRect(57,96,29,16))
        self.PietyCap.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.PietyCap.setObjectName("PietyCap")

        self.CharismaLabel = QtGui.QLabel(self.GroupStats)
        self.CharismaLabel.setGeometry(QtCore.QRect(6,112,28,16))
        self.CharismaLabel.setObjectName("CharismaLabel")

        self.Charisma = QtGui.QLabel(self.GroupStats)
        self.Charisma.setGeometry(QtCore.QRect(35,112,20,16))
        self.Charisma.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Charisma.setObjectName("Charisma")

        self.CharismaCap = QtGui.QLabel(self.GroupStats)
        self.CharismaCap.setGeometry(QtCore.QRect(57,112,29,16))
        self.CharismaCap.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.CharismaCap.setObjectName("CharismaCap")

        self.EmpathyLabel = QtGui.QLabel(self.GroupStats)
        self.EmpathyLabel.setGeometry(QtCore.QRect(6,128,28,16))
        self.EmpathyLabel.setObjectName("EmpathyLabel")

        self.Empathy = QtGui.QLabel(self.GroupStats)
        self.Empathy.setGeometry(QtCore.QRect(35,128,20,16))
        self.Empathy.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Empathy.setObjectName("Empathy")

        self.EmpathyCap = QtGui.QLabel(self.GroupStats)
        self.EmpathyCap.setGeometry(QtCore.QRect(57,128,29,16))
        self.EmpathyCap.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.EmpathyCap.setObjectName("EmpathyCap")

        self.PowerLabel = QtGui.QLabel(self.GroupStats)
        self.PowerLabel.setGeometry(QtCore.QRect(6,144,28,16))
        self.PowerLabel.setObjectName("PowerLabel")

        self.Power = QtGui.QLabel(self.GroupStats)
        self.Power.setGeometry(QtCore.QRect(35,144,20,16))
        self.Power.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Power.setObjectName("Power")

        self.PowerCap = QtGui.QLabel(self.GroupStats)
        self.PowerCap.setGeometry(QtCore.QRect(57,144,29,16))
        self.PowerCap.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.PowerCap.setObjectName("PowerCap")

        self.HitsLabel = QtGui.QLabel(self.GroupStats)
        self.HitsLabel.setGeometry(QtCore.QRect(6,160,28,16))
        self.HitsLabel.setObjectName("HitsLabel")

        self.Hits = QtGui.QLabel(self.GroupStats)
        self.Hits.setGeometry(QtCore.QRect(35,160,20,16))
        self.Hits.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Hits.setObjectName("Hits")

        self.HitsCap = QtGui.QLabel(self.GroupStats)
        self.HitsCap.setGeometry(QtCore.QRect(57,160,29,16))
        self.HitsCap.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.HitsCap.setObjectName("HitsCap")

        self.GroupResists = QtGui.QGroupBox(self.ScWinFrame)
        self.GroupResists.setGeometry(QtCore.QRect(105,3,90,182))
        self.GroupResists.setObjectName("GroupResists")

        self.BodyLabel = QtGui.QLabel(self.GroupResists)
        self.BodyLabel.setGeometry(QtCore.QRect(6,16,36,16))
        self.BodyLabel.setObjectName("BodyLabel")

        self.Body = QtGui.QLabel(self.GroupResists)
        self.Body.setGeometry(QtCore.QRect(44,16,17,16))
        self.Body.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Body.setObjectName("Body")

        self.BodyRR = QtGui.QLabel(self.GroupResists)
        self.BodyRR.setGeometry(QtCore.QRect(66,16,17,16))
        self.BodyRR.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.BodyRR.setObjectName("BodyRR")

        self.ColdLabel = QtGui.QLabel(self.GroupResists)
        self.ColdLabel.setGeometry(QtCore.QRect(6,34,36,16))
        self.ColdLabel.setObjectName("ColdLabel")

        self.Cold = QtGui.QLabel(self.GroupResists)
        self.Cold.setGeometry(QtCore.QRect(44,34,17,16))
        self.Cold.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Cold.setObjectName("Cold")

        self.ColdRR = QtGui.QLabel(self.GroupResists)
        self.ColdRR.setGeometry(QtCore.QRect(66,34,17,16))
        self.ColdRR.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ColdRR.setObjectName("ColdRR")

        self.HeatLabel = QtGui.QLabel(self.GroupResists)
        self.HeatLabel.setGeometry(QtCore.QRect(6,52,36,16))
        self.HeatLabel.setObjectName("HeatLabel")

        self.Heat = QtGui.QLabel(self.GroupResists)
        self.Heat.setGeometry(QtCore.QRect(44,52,17,16))
        self.Heat.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Heat.setObjectName("Heat")

        self.HeatRR = QtGui.QLabel(self.GroupResists)
        self.HeatRR.setGeometry(QtCore.QRect(66,52,17,16))
        self.HeatRR.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.HeatRR.setObjectName("HeatRR")

        self.EnergyLabel = QtGui.QLabel(self.GroupResists)
        self.EnergyLabel.setGeometry(QtCore.QRect(6,70,36,16))
        self.EnergyLabel.setObjectName("EnergyLabel")

        self.Energy = QtGui.QLabel(self.GroupResists)
        self.Energy.setGeometry(QtCore.QRect(44,70,17,16))
        self.Energy.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Energy.setObjectName("Energy")

        self.EnergyRR = QtGui.QLabel(self.GroupResists)
        self.EnergyRR.setGeometry(QtCore.QRect(66,70,17,16))
        self.EnergyRR.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.EnergyRR.setObjectName("EnergyRR")

        self.MatterLabel = QtGui.QLabel(self.GroupResists)
        self.MatterLabel.setGeometry(QtCore.QRect(6,88,36,16))
        self.MatterLabel.setObjectName("MatterLabel")

        self.Matter = QtGui.QLabel(self.GroupResists)
        self.Matter.setGeometry(QtCore.QRect(44,88,17,16))
        self.Matter.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Matter.setObjectName("Matter")

        self.MatterRR = QtGui.QLabel(self.GroupResists)
        self.MatterRR.setGeometry(QtCore.QRect(66,88,17,16))
        self.MatterRR.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.MatterRR.setObjectName("MatterRR")

        self.SpiritLabel = QtGui.QLabel(self.GroupResists)
        self.SpiritLabel.setGeometry(QtCore.QRect(6,106,36,16))
        self.SpiritLabel.setObjectName("SpiritLabel")

        self.Spirit = QtGui.QLabel(self.GroupResists)
        self.Spirit.setGeometry(QtCore.QRect(44,106,17,16))
        self.Spirit.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Spirit.setObjectName("Spirit")

        self.SpiritRR = QtGui.QLabel(self.GroupResists)
        self.SpiritRR.setGeometry(QtCore.QRect(66,106,17,16))
        self.SpiritRR.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.SpiritRR.setObjectName("SpiritRR")

        self.CrushLabel = QtGui.QLabel(self.GroupResists)
        self.CrushLabel.setGeometry(QtCore.QRect(6,124,36,16))
        self.CrushLabel.setObjectName("CrushLabel")

        self.Crush = QtGui.QLabel(self.GroupResists)
        self.Crush.setGeometry(QtCore.QRect(44,124,17,16))
        self.Crush.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Crush.setObjectName("Crush")

        self.CrushRR = QtGui.QLabel(self.GroupResists)
        self.CrushRR.setGeometry(QtCore.QRect(66,124,17,16))
        self.CrushRR.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.CrushRR.setObjectName("CrushRR")

        self.ThrustLabel = QtGui.QLabel(self.GroupResists)
        self.ThrustLabel.setGeometry(QtCore.QRect(6,142,36,16))
        self.ThrustLabel.setObjectName("ThrustLabel")

        self.Thrust = QtGui.QLabel(self.GroupResists)
        self.Thrust.setGeometry(QtCore.QRect(44,142,17,16))
        self.Thrust.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Thrust.setObjectName("Thrust")

        self.ThrustRR = QtGui.QLabel(self.GroupResists)
        self.ThrustRR.setGeometry(QtCore.QRect(66,142,17,16))
        self.ThrustRR.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ThrustRR.setObjectName("ThrustRR")

        self.SlashLabel = QtGui.QLabel(self.GroupResists)
        self.SlashLabel.setGeometry(QtCore.QRect(6,160,36,16))
        self.SlashLabel.setObjectName("SlashLabel")

        self.Slash = QtGui.QLabel(self.GroupResists)
        self.Slash.setGeometry(QtCore.QRect(44,160,17,16))
        self.Slash.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Slash.setObjectName("Slash")

        self.SlashRR = QtGui.QLabel(self.GroupResists)
        self.SlashRR.setGeometry(QtCore.QRect(66,160,17,16))
        self.SlashRR.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.SlashRR.setObjectName("SlashRR")

        self.GroupSkillsList = QtGui.QGroupBox(self.ScWinFrame)
        self.GroupSkillsList.setGeometry(QtCore.QRect(201,3,160,182))
        self.GroupSkillsList.setObjectName("GroupSkillsList")

        self.SkillsList = QtGui.QListWidget(self.GroupSkillsList)
        self.SkillsList.setGeometry(QtCore.QRect(5,16,150,160))
        self.SkillsList.setObjectName("SkillsList")

        self.GroupOtherBonusList = QtGui.QGroupBox(self.ScWinFrame)
        self.GroupOtherBonusList.setGeometry(QtCore.QRect(367,3,240,182))
        self.GroupOtherBonusList.setObjectName("GroupOtherBonusList")

        self.OtherBonusList = QtGui.QListWidget(self.GroupOtherBonusList)
        self.OtherBonusList.setGeometry(QtCore.QRect(5,15,230,160))
        self.OtherBonusList.setObjectName("OtherBonusList")

        self.GroupItemFrame = MultiTabFrame(self.ScWinFrame)
        self.GroupItemFrame.setGeometry(QtCore.QRect(3,235,776,307))
        self.GroupItemFrame.setObjectName("GroupItemFrame")

        self.ItemLevelLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemLevelLabel.setGeometry(QtCore.QRect(7,5,34,21))
        self.ItemLevelLabel.setObjectName("ItemLevelLabel")

        self.ItemLevel = QtGui.QLineEdit(self.GroupItemFrame)
        self.ItemLevel.setGeometry(QtCore.QRect(46,5,35,21))
        self.ItemLevel.setObjectName("ItemLevel")

        self.ItemLevelButton = QtGui.QPushButton(self.GroupItemFrame)
        self.ItemLevelButton.setGeometry(QtCore.QRect(81,5,21,21))
        self.ItemLevelButton.setMaximumSize(QtCore.QSize(21,21))
        self.ItemLevelButton.setObjectName("ItemLevelButton")

        self.ItemQualityLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemQualityLabel.setGeometry(QtCore.QRect(115,5,54,21))
        self.ItemQualityLabel.setObjectName("ItemQualityLabel")

        self.QualDrop = SearchingCombo(self.GroupItemFrame)
        self.QualDrop.setGeometry(QtCore.QRect(160,5,52,21))
        self.QualDrop.setObjectName("QualDrop")

        self.QualEdit = QtGui.QLineEdit(self.GroupItemFrame)
        self.QualEdit.setGeometry(QtCore.QRect(160,5,52,21))
        self.QualEdit.setObjectName("QualEdit")

        self.ItemBonusLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemBonusLabel.setGeometry(QtCore.QRect(232,5,40,21))
        self.ItemBonusLabel.setObjectName("ItemBonusLabel")

        self.Bonus_Edit = QtGui.QLineEdit(self.GroupItemFrame)
        self.Bonus_Edit.setGeometry(QtCore.QRect(272,5,35,21))
        self.Bonus_Edit.setObjectName("Bonus_Edit")

        self.ItemAFDPSLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemAFDPSLabel.setGeometry(QtCore.QRect(315,5,55,21))
        self.ItemAFDPSLabel.setObjectName("ItemAFDPSLabel")

        self.AFDPS_Edit = QtGui.QLineEdit(self.GroupItemFrame)
        self.AFDPS_Edit.setGeometry(QtCore.QRect(360,5,35,21))
        self.AFDPS_Edit.setObjectName("AFDPS_Edit")

        self.ItemSpeedLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemSpeedLabel.setGeometry(QtCore.QRect(403,5,40,21))
        self.ItemSpeedLabel.setObjectName("ItemSpeedLabel")

        self.Speed_Edit = QtGui.QLineEdit(self.GroupItemFrame)
        self.Speed_Edit.setGeometry(QtCore.QRect(443,5,35,21))
        self.Speed_Edit.setObjectName("Speed_Edit")

        self.Equipped = QtGui.QCheckBox(self.GroupItemFrame)
        self.Equipped.setGeometry(QtCore.QRect(509,5,71,21))
        self.Equipped.setObjectName("Equipped")

        self.DropCraftButtonFrame = QtGui.QFrame(self.GroupItemFrame)
        self.DropCraftButtonFrame.setEnabled(True)
        self.DropCraftButtonFrame.setGeometry(QtCore.QRect(617,5,136,21))
        self.DropCraftButtonFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.DropCraftButtonFrame.setObjectName("DropCraftButtonFrame")

        self.PlayerMade = QtGui.QRadioButton(self.DropCraftButtonFrame)
        self.PlayerMade.setGeometry(QtCore.QRect(0,0,85,21))
        self.PlayerMade.setObjectName("PlayerMade")

        self.Drop = QtGui.QRadioButton(self.DropCraftButtonFrame)
        self.Drop.setGeometry(QtCore.QRect(86,0,52,21))
        self.Drop.setChecked(True)
        self.Drop.setObjectName("Drop")

        self.ItemName = QtGui.QLineEdit(self.GroupItemFrame)
        self.ItemName.setGeometry(QtCore.QRect(562,48,200,21))
        self.ItemName.setObjectName("ItemName")

        self.LabelGemType = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemType.setGeometry(QtCore.QRect(50,31,119,17))
        self.LabelGemType.setObjectName("LabelGemType")

        self.LabelGemAmount = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemAmount.setGeometry(QtCore.QRect(181,31,44,17))
        self.LabelGemAmount.setObjectName("LabelGemAmount")

        self.LabelGemEffect = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemEffect.setGeometry(QtCore.QRect(237,31,142,17))
        self.LabelGemEffect.setObjectName("LabelGemEffect")

        self.LabelRequirement = QtGui.QLabel(self.GroupItemFrame)
        self.LabelRequirement.setGeometry(QtCore.QRect(391,31,100,21))
        self.LabelRequirement.setObjectName("LabelRequirement")

        self.LabelGemQuality = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemQuality.setGeometry(QtCore.QRect(391,31,44,17))
        self.LabelGemQuality.setObjectName("LabelGemQuality")

        self.LabelGemPoints = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemPoints.setGeometry(QtCore.QRect(443,31,35,17))
        self.LabelGemPoints.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.LabelGemPoints.setObjectName("LabelGemPoints")

        self.LabelGemCost = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemCost.setGeometry(QtCore.QRect(482,31,70,17))
        self.LabelGemCost.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.LabelGemCost.setObjectName("LabelGemCost")

        self.LabelItemName = QtGui.QLabel(self.GroupItemFrame)
        self.LabelItemName.setGeometry(QtCore.QRect(562,31,70,17))
        self.LabelItemName.setObjectName("LabelItemName")

        self.Gem_Label_1 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_1.setGeometry(QtCore.QRect(7,48,34,21))
        self.Gem_Label_1.setObjectName("Gem_Label_1")

        self.Type_1 = SearchingCombo(self.GroupItemFrame)
        self.Type_1.setGeometry(QtCore.QRect(46,48,127,21))
        self.Type_1.setObjectName("Type_1")

        self.Amount_Edit_1 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_1.setGeometry(QtCore.QRect(177,48,51,21))
        self.Amount_Edit_1.setObjectName("Amount_Edit_1")

        self.Amount_Drop_1 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_1.setGeometry(QtCore.QRect(177,48,52,21))
        self.Amount_Drop_1.setObjectName("Amount_Drop_1")

        self.Effect_1 = SearchingCombo(self.GroupItemFrame)
        self.Effect_1.setEditable(True)
        self.Effect_1.setGeometry(QtCore.QRect(233,48,150,21))
        self.Effect_1.setObjectName("Effect_1")

        self.Quality_1 = SearchingCombo(self.GroupItemFrame)
        self.Quality_1.setGeometry(QtCore.QRect(387,48,52,21))
        self.Quality_1.setObjectName("Quality_1")

        self.Requirement_1 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_1.setGeometry(QtCore.QRect(387,48,165,21))
        self.Requirement_1.setObjectName("Requirement_1")

        self.Points_1 = QtGui.QLabel(self.GroupItemFrame)
        self.Points_1.setGeometry(QtCore.QRect(443,48,35,21))
        self.Points_1.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Points_1.setObjectName("Points_1")

        self.Cost_1 = QtGui.QLabel(self.GroupItemFrame)
        self.Cost_1.setGeometry(QtCore.QRect(482,48,70,21))
        self.Cost_1.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Cost_1.setObjectName("Cost_1")

        self.Name_1 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_1.setGeometry(QtCore.QRect(562,48,200,21))
        self.Name_1.setObjectName("Name_1")

        self.Gem_Label_2 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_2.setGeometry(QtCore.QRect(7,69,34,21))
        self.Gem_Label_2.setObjectName("Gem_Label_2")

        self.Amount_Edit_2 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_2.setGeometry(QtCore.QRect(177,69,51,21))
        self.Amount_Edit_2.setObjectName("Amount_Edit_2")

        self.Amount_Drop_2 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_2.setGeometry(QtCore.QRect(177,69,52,21))
        self.Amount_Drop_2.setObjectName("Amount_Drop_2")

        self.Type_2 = SearchingCombo(self.GroupItemFrame)
        self.Type_2.setGeometry(QtCore.QRect(46,69,127,21))
        self.Type_2.setObjectName("Type_2")

        self.Effect_2 = SearchingCombo(self.GroupItemFrame)
        self.Effect_2.setEditable(True)
        self.Effect_2.setGeometry(QtCore.QRect(233,69,150,21))
        self.Effect_2.setObjectName("Effect_2")

        self.Quality_2 = SearchingCombo(self.GroupItemFrame)
        self.Quality_2.setGeometry(QtCore.QRect(387,69,52,21))
        self.Quality_2.setObjectName("Quality_2")

        self.Requirement_2 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_2.setGeometry(QtCore.QRect(387,69,165,21))
        self.Requirement_2.setObjectName("Requirement_2")

        self.Points_2 = QtGui.QLabel(self.GroupItemFrame)
        self.Points_2.setGeometry(QtCore.QRect(443,69,35,21))
        self.Points_2.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Points_2.setObjectName("Points_2")

        self.Cost_2 = QtGui.QLabel(self.GroupItemFrame)
        self.Cost_2.setGeometry(QtCore.QRect(482,69,70,21))
        self.Cost_2.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Cost_2.setObjectName("Cost_2")

        self.Name_2 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_2.setGeometry(QtCore.QRect(562,69,200,21))
        self.Name_2.setObjectName("Name_2")

        self.Gem_Label_3 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_3.setGeometry(QtCore.QRect(7,90,34,21))
        self.Gem_Label_3.setObjectName("Gem_Label_3")

        self.Type_3 = SearchingCombo(self.GroupItemFrame)
        self.Type_3.setGeometry(QtCore.QRect(46,90,127,21))
        self.Type_3.setObjectName("Type_3")

        self.Amount_Edit_3 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_3.setGeometry(QtCore.QRect(177,90,51,21))
        self.Amount_Edit_3.setObjectName("Amount_Edit_3")

        self.Amount_Drop_3 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_3.setGeometry(QtCore.QRect(177,90,52,21))
        self.Amount_Drop_3.setObjectName("Amount_Drop_3")

        self.Effect_3 = SearchingCombo(self.GroupItemFrame)
        self.Effect_3.setEditable(True)
        self.Effect_3.setGeometry(QtCore.QRect(233,90,150,21))
        self.Effect_3.setObjectName("Effect_3")

        self.Quality_3 = SearchingCombo(self.GroupItemFrame)
        self.Quality_3.setGeometry(QtCore.QRect(387,90,52,21))
        self.Quality_3.setObjectName("Quality_3")

        self.Requirement_3 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_3.setGeometry(QtCore.QRect(387,90,165,21))
        self.Requirement_3.setObjectName("Requirement_3")

        self.Points_3 = QtGui.QLabel(self.GroupItemFrame)
        self.Points_3.setGeometry(QtCore.QRect(443,90,35,21))
        self.Points_3.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Points_3.setObjectName("Points_3")

        self.Cost_3 = QtGui.QLabel(self.GroupItemFrame)
        self.Cost_3.setGeometry(QtCore.QRect(482,90,70,21))
        self.Cost_3.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Cost_3.setObjectName("Cost_3")

        self.Name_3 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_3.setGeometry(QtCore.QRect(562,90,200,21))
        self.Name_3.setObjectName("Name_3")

        self.Gem_Label_4 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_4.setGeometry(QtCore.QRect(7,111,34,21))
        self.Gem_Label_4.setObjectName("Gem_Label_4")

        self.Type_4 = SearchingCombo(self.GroupItemFrame)
        self.Type_4.setGeometry(QtCore.QRect(46,111,127,21))
        self.Type_4.setObjectName("Type_4")

        self.Amount_Edit_4 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_4.setGeometry(QtCore.QRect(177,111,51,21))
        self.Amount_Edit_4.setObjectName("Amount_Edit_4")

        self.Amount_Drop_4 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_4.setGeometry(QtCore.QRect(177,111,52,21))
        self.Amount_Drop_4.setObjectName("Amount_Drop_4")

        self.Effect_4 = SearchingCombo(self.GroupItemFrame)
        self.Effect_4.setEditable(True)
        self.Effect_4.setGeometry(QtCore.QRect(233,111,150,21))
        self.Effect_4.setObjectName("Effect_4")

        self.Quality_4 = SearchingCombo(self.GroupItemFrame)
        self.Quality_4.setGeometry(QtCore.QRect(387,111,52,21))
        self.Quality_4.setObjectName("Quality_4")

        self.Requirement_4 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_4.setGeometry(QtCore.QRect(387,111,165,21))
        self.Requirement_4.setObjectName("Requirement_4")

        self.Points_4 = QtGui.QLabel(self.GroupItemFrame)
        self.Points_4.setGeometry(QtCore.QRect(443,111,35,21))
        self.Points_4.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Points_4.setObjectName("Points_4")

        self.Cost_4 = QtGui.QLabel(self.GroupItemFrame)
        self.Cost_4.setGeometry(QtCore.QRect(482,111,70,21))
        self.Cost_4.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Cost_4.setObjectName("Cost_4")

        self.Name_4 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_4.setGeometry(QtCore.QRect(562,111,200,21))
        self.Name_4.setObjectName("Name_4")

        self.Gem_Label_5 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_5.setGeometry(QtCore.QRect(7,132,34,21))
        self.Gem_Label_5.setObjectName("Gem_Label_5")

        self.Type_5 = SearchingCombo(self.GroupItemFrame)
        self.Type_5.setGeometry(QtCore.QRect(46,132,127,21))
        self.Type_5.setObjectName("Type_5")

        self.Amount_Edit_5 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_5.setGeometry(QtCore.QRect(177,132,51,21))
        self.Amount_Edit_5.setObjectName("Amount_Edit_5")

        self.Amount_Drop_5 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_5.setGeometry(QtCore.QRect(177,132,52,21))
        self.Amount_Drop_5.setObjectName("Amount_Drop_5")

        self.Effect_5 = SearchingCombo(self.GroupItemFrame)
        self.Effect_5.setEditable(True)
        self.Effect_5.setGeometry(QtCore.QRect(233,132,150,21))
        self.Effect_5.setObjectName("Effect_5")

        self.Requirement_5 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_5.setGeometry(QtCore.QRect(387,132,165,21))
        self.Requirement_5.setObjectName("Requirement_5")

        self.Name_5 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_5.setGeometry(QtCore.QRect(562,132,200,21))
        self.Name_5.setObjectName("Name_5")

        self.Gem_Label_6 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_6.setGeometry(QtCore.QRect(7,153,34,21))
        self.Gem_Label_6.setObjectName("Gem_Label_6")

        self.Type_6 = SearchingCombo(self.GroupItemFrame)
        self.Type_6.setGeometry(QtCore.QRect(46,153,127,21))
        self.Type_6.setObjectName("Type_6")

        self.Amount_Edit_6 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_6.setGeometry(QtCore.QRect(177,153,51,21))
        self.Amount_Edit_6.setObjectName("Amount_Edit_6")

        self.Amount_Drop_6 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_6.setGeometry(QtCore.QRect(177,153,52,21))
        self.Amount_Drop_6.setObjectName("Amount_Drop_6")

        self.Effect_6 = SearchingCombo(self.GroupItemFrame)
        self.Effect_6.setEditable(True)
        self.Effect_6.setGeometry(QtCore.QRect(233,153,150,21))
        self.Effect_6.setObjectName("Effect_6")

        self.Requirement_6 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_6.setGeometry(QtCore.QRect(387,153,165,21))
        self.Requirement_6.setObjectName("Requirement_6")

        self.Name_6 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_6.setGeometry(QtCore.QRect(562,153,200,21))
        self.Name_6.setObjectName("Name_6")

        self.LabelRequirement2 = QtGui.QLabel(self.GroupItemFrame)
        self.LabelRequirement2.setGeometry(QtCore.QRect(391,174,100,21))
        self.LabelRequirement2.setObjectName("LabelRequirement2")

        self.Gem_Label_7 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_7.setGeometry(QtCore.QRect(7,174,34,21))
        self.Gem_Label_7.setObjectName("Gem_Label_7")

        self.Type_7 = SearchingCombo(self.GroupItemFrame)
        self.Type_7.setGeometry(QtCore.QRect(46,174,127,21))
        self.Type_7.setObjectName("Type_7")

        self.Amount_Edit_7 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_7.setGeometry(QtCore.QRect(177,174,51,21))
        self.Amount_Edit_7.setObjectName("Amount_Edit_7")

        self.Effect_7 = SearchingCombo(self.GroupItemFrame)
        self.Effect_7.setEditable(True)
        self.Effect_7.setGeometry(QtCore.QRect(233,174,150,21))
        self.Effect_7.setObjectName("Effect_7")

        self.Requirement_7 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_7.setGeometry(QtCore.QRect(387,174,165,21))
        self.Requirement_7.setObjectName("Requirement_7")

        self.Gem_Label_8 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_8.setGeometry(QtCore.QRect(7,195,34,21))
        self.Gem_Label_8.setObjectName("Gem_Label_8")

        self.Type_8 = SearchingCombo(self.GroupItemFrame)
        self.Type_8.setGeometry(QtCore.QRect(46,195,127,21))
        self.Type_8.setObjectName("Type_8")

        self.Amount_Edit_8 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_8.setGeometry(QtCore.QRect(177,195,51,21))
        self.Amount_Edit_8.setObjectName("Amount_Edit_8")

        self.Effect_8 = SearchingCombo(self.GroupItemFrame)
        self.Effect_8.setEditable(True)
        self.Effect_8.setGeometry(QtCore.QRect(233,195,150,21))
        self.Effect_8.setObjectName("Effect_8")

        self.Requirement_8 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_8.setGeometry(QtCore.QRect(387,195,165,21))
        self.Requirement_8.setObjectName("Requirement_8")

        self.Gem_Label_9 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_9.setGeometry(QtCore.QRect(7,216,34,21))
        self.Gem_Label_9.setObjectName("Gem_Label_9")

        self.Type_9 = SearchingCombo(self.GroupItemFrame)
        self.Type_9.setGeometry(QtCore.QRect(46,216,127,21))
        self.Type_9.setObjectName("Type_9")

        self.Amount_Edit_9 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_9.setGeometry(QtCore.QRect(177,216,51,21))
        self.Amount_Edit_9.setObjectName("Amount_Edit_9")

        self.Effect_9 = SearchingCombo(self.GroupItemFrame)
        self.Effect_9.setEditable(True)
        self.Effect_9.setGeometry(QtCore.QRect(233,216,150,21))
        self.Effect_9.setObjectName("Effect_9")

        self.Requirement_9 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_9.setGeometry(QtCore.QRect(387,216,165,21))
        self.Requirement_9.setObjectName("Requirement_9")

        self.Gem_Label_10 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_10.setGeometry(QtCore.QRect(7,237,41,21))
        self.Gem_Label_10.setObjectName("Gem_Label_10")

        self.Type_10 = SearchingCombo(self.GroupItemFrame)
        self.Type_10.setGeometry(QtCore.QRect(46,237,127,21))
        self.Type_10.setObjectName("Type_10")

        self.Amount_Edit_10 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_10.setGeometry(QtCore.QRect(177,237,51,21))
        self.Amount_Edit_10.setObjectName("Amount_Edit_10")

        self.Effect_10 = SearchingCombo(self.GroupItemFrame)
        self.Effect_10.setEditable(True)
        self.Effect_10.setGeometry(QtCore.QRect(233,237,150,21))
        self.Effect_10.setObjectName("Effect_10")

        self.Requirement_10 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_10.setGeometry(QtCore.QRect(387,237,165,21))
        self.Requirement_10.setObjectName("Requirement_10")

        self.Gem_Label_11 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_11.setGeometry(QtCore.QRect(7,258,41,21))
        self.Gem_Label_11.setObjectName("Gem_Label_11")

        self.Type_11 = SearchingCombo(self.GroupItemFrame)
        self.Type_11.setGeometry(QtCore.QRect(46,258,127,21))
        self.Type_11.setObjectName("Type_11")

        self.Amount_Edit_11 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_11.setGeometry(QtCore.QRect(177,258,51,21))
        self.Amount_Edit_11.setObjectName("Amount_Edit_11")

        self.Effect_11 = SearchingCombo(self.GroupItemFrame)
        self.Effect_11.setEditable(True)
        self.Effect_11.setGeometry(QtCore.QRect(233,258,150,21))
        self.Effect_11.setObjectName("Effect_11")

        self.Requirement_11 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_11.setGeometry(QtCore.QRect(387,258,165,21))
        self.Requirement_11.setObjectName("Requirement_11")

        self.Gem_Label_12 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_12.setGeometry(QtCore.QRect(7,279,41,21))
        self.Gem_Label_12.setObjectName("Gem_Label_12")

        self.Type_12 = SearchingCombo(self.GroupItemFrame)
        self.Type_12.setGeometry(QtCore.QRect(46,279,127,21))
        self.Type_12.setObjectName("Type_12")

        self.Amount_Edit_12 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_12.setGeometry(QtCore.QRect(177,279,51,21))
        self.Amount_Edit_12.setObjectName("Amount_Edit_12")

        self.Effect_12 = SearchingCombo(self.GroupItemFrame)
        self.Effect_12.setEditable(True)
        self.Effect_12.setGeometry(QtCore.QRect(233,279,150,21))
        self.Effect_12.setObjectName("Effect_12")

        self.Requirement_12 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_12.setGeometry(QtCore.QRect(387,279,165,21))
        self.Requirement_12.setObjectName("Requirement_12")

        self.ItemImbueLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemImbueLabel.setGeometry(QtCore.QRect(370,178,73,17))
        self.ItemImbueLabel.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ItemImbueLabel.setObjectName("ItemImbueLabel")

        self.ItemImbue = QtGui.QLabel(self.GroupItemFrame)
        self.ItemImbue.setGeometry(QtCore.QRect(443,178,35,17))
        self.ItemImbue.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ItemImbue.setObjectName("ItemImbue")

        self.ItemImbueTotal = QtGui.QLabel(self.GroupItemFrame)
        self.ItemImbueTotal.setGeometry(QtCore.QRect(487,178,40,17))
        self.ItemImbueTotal.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.ItemImbueTotal.setObjectName("ItemImbueTotal")

        self.ItemOverchargeLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemOverchargeLabel.setGeometry(QtCore.QRect(370,195,73,17))
        self.ItemOverchargeLabel.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ItemOverchargeLabel.setObjectName("ItemOverchargeLabel")

        self.ItemOvercharge = QtGui.QLabel(self.GroupItemFrame)
        self.ItemOvercharge.setGeometry(QtCore.QRect(443,195,90,17))
        self.ItemOvercharge.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.ItemOvercharge.setObjectName("ItemOvercharge")

        self.ItemCostLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemCostLabel.setGeometry(QtCore.QRect(370,220,73,17))
        self.ItemCostLabel.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ItemCostLabel.setObjectName("ItemCostLabel")

        self.ItemCost = QtGui.QLabel(self.GroupItemFrame)
        self.ItemCost.setGeometry(QtCore.QRect(482,220,70,17))
        self.ItemCost.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ItemCost.setObjectName("ItemCost")

        self.ItemPriceLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemPriceLabel.setGeometry(QtCore.QRect(370,237,73,17))
        self.ItemPriceLabel.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ItemPriceLabel.setObjectName("ItemPriceLabel")

        self.ItemPrice = QtGui.QLabel(self.GroupItemFrame)
        self.ItemPrice.setGeometry(QtCore.QRect(482,237,70,17))
        self.ItemPrice.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ItemPrice.setObjectName("ItemPrice")

        self.ItemUtilityLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemUtilityLabel.setGeometry(QtCore.QRect(585,237,35,17))
        self.ItemUtilityLabel.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ItemUtilityLabel.setObjectName("ItemUtilityLabel")

        self.ItemUtility = QtGui.QLabel(self.GroupItemFrame)
        self.ItemUtility.setGeometry(QtCore.QRect(625,237,30,17))
        self.ItemUtility.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.ItemUtility.setObjectName("ItemUtility")

        self.PieceTab = MultiTabBar4(self.ScWinFrame)
        self.PieceTab.setGeometry(QtCore.QRect(3,190,776,46))
        self.PieceTab.setObjectName("PieceTab")
        B_SC.setCentralWidget(self.ScWinFrame)

        self.retranslateUi(B_SC)
        B_SC.setTabOrder(self.CharName,self.Realm)
        B_SC.setTabOrder(self.Realm,self.CharClass)
        B_SC.setTabOrder(self.CharClass,self.CharRace)
        B_SC.setTabOrder(self.CharRace,self.CharLevel)
        B_SC.setTabOrder(self.CharLevel,self.PieceTab)
        B_SC.setTabOrder(self.PieceTab,self.ItemLevel)
        B_SC.setTabOrder(self.ItemLevel,self.ItemLevelButton)
        B_SC.setTabOrder(self.ItemLevelButton,self.QualEdit)
        B_SC.setTabOrder(self.QualEdit,self.QualDrop)
        B_SC.setTabOrder(self.QualDrop,self.Bonus_Edit)
        B_SC.setTabOrder(self.Bonus_Edit,self.AFDPS_Edit)
        B_SC.setTabOrder(self.AFDPS_Edit,self.Speed_Edit)
        B_SC.setTabOrder(self.Speed_Edit,self.Equipped)
        B_SC.setTabOrder(self.Equipped,self.PlayerMade)
        B_SC.setTabOrder(self.PlayerMade,self.Drop)
        B_SC.setTabOrder(self.Drop,self.ItemName)
        B_SC.setTabOrder(self.ItemName,self.Type_1)
        B_SC.setTabOrder(self.Type_1,self.Amount_Edit_1)
        B_SC.setTabOrder(self.Amount_Edit_1,self.Amount_Drop_1)
        B_SC.setTabOrder(self.Amount_Drop_1,self.Effect_1)
        B_SC.setTabOrder(self.Effect_1,self.Quality_1)
        B_SC.setTabOrder(self.Quality_1,self.Requirement_1)
        B_SC.setTabOrder(self.Requirement_1,self.Type_2)
        B_SC.setTabOrder(self.Type_2,self.Amount_Edit_2)
        B_SC.setTabOrder(self.Amount_Edit_2,self.Amount_Drop_2)
        B_SC.setTabOrder(self.Amount_Drop_2,self.Effect_2)
        B_SC.setTabOrder(self.Effect_2,self.Quality_2)
        B_SC.setTabOrder(self.Quality_2,self.Requirement_2)
        B_SC.setTabOrder(self.Requirement_2,self.Type_3)
        B_SC.setTabOrder(self.Type_3,self.Amount_Edit_3)
        B_SC.setTabOrder(self.Amount_Edit_3,self.Amount_Drop_3)
        B_SC.setTabOrder(self.Amount_Drop_3,self.Effect_3)
        B_SC.setTabOrder(self.Effect_3,self.Quality_3)
        B_SC.setTabOrder(self.Quality_3,self.Requirement_3)
        B_SC.setTabOrder(self.Requirement_3,self.Type_4)
        B_SC.setTabOrder(self.Type_4,self.Amount_Edit_4)
        B_SC.setTabOrder(self.Amount_Edit_4,self.Amount_Drop_4)
        B_SC.setTabOrder(self.Amount_Drop_4,self.Effect_4)
        B_SC.setTabOrder(self.Effect_4,self.Quality_4)
        B_SC.setTabOrder(self.Quality_4,self.Requirement_4)
        B_SC.setTabOrder(self.Requirement_4,self.Type_5)
        B_SC.setTabOrder(self.Type_5,self.Amount_Edit_5)
        B_SC.setTabOrder(self.Amount_Edit_5,self.Amount_Drop_5)
        B_SC.setTabOrder(self.Amount_Drop_5,self.Effect_5)
        B_SC.setTabOrder(self.Effect_5,self.Requirement_5)
        B_SC.setTabOrder(self.Requirement_5,self.Type_6)
        B_SC.setTabOrder(self.Type_6,self.Amount_Edit_6)
        B_SC.setTabOrder(self.Amount_Edit_6,self.Amount_Drop_6)
        B_SC.setTabOrder(self.Amount_Drop_6,self.Effect_6)
        B_SC.setTabOrder(self.Effect_6,self.Requirement_6)
        B_SC.setTabOrder(self.Requirement_6,self.Type_7)
        B_SC.setTabOrder(self.Type_7,self.Amount_Edit_7)
        B_SC.setTabOrder(self.Amount_Edit_7,self.Effect_7)
        B_SC.setTabOrder(self.Effect_7,self.Requirement_7)
        B_SC.setTabOrder(self.Requirement_7,self.Type_8)
        B_SC.setTabOrder(self.Type_8,self.Amount_Edit_8)
        B_SC.setTabOrder(self.Amount_Edit_8,self.Effect_8)
        B_SC.setTabOrder(self.Effect_8,self.Requirement_8)
        B_SC.setTabOrder(self.Requirement_8,self.Type_9)
        B_SC.setTabOrder(self.Type_9,self.Amount_Edit_9)
        B_SC.setTabOrder(self.Amount_Edit_9,self.Effect_9)
        B_SC.setTabOrder(self.Effect_9,self.Requirement_9)
        B_SC.setTabOrder(self.Requirement_9,self.Type_10)
        B_SC.setTabOrder(self.Type_10,self.Amount_Edit_10)
        B_SC.setTabOrder(self.Amount_Edit_10,self.Effect_10)
        B_SC.setTabOrder(self.Effect_10,self.Requirement_10)
        B_SC.setTabOrder(self.Requirement_10,self.Type_11)
        B_SC.setTabOrder(self.Type_11,self.Amount_Edit_11)
        B_SC.setTabOrder(self.Amount_Edit_11,self.Effect_11)
        B_SC.setTabOrder(self.Effect_11,self.Requirement_11)
        B_SC.setTabOrder(self.Requirement_11,self.Type_12)
        B_SC.setTabOrder(self.Type_12,self.Amount_Edit_12)
        B_SC.setTabOrder(self.Amount_Edit_12,self.Effect_12)
        B_SC.setTabOrder(self.Effect_12,self.Requirement_12)
        B_SC.setTabOrder(self.Requirement_12,self.SkillsList)
        B_SC.setTabOrder(self.SkillsList,self.OtherBonusList)

    def retranslateUi(self, B_SC):
        B_SC.setWindowTitle(QtGui.QApplication.translate("B_SC", "Spellcrafting Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupCharInfo.setTitle(QtGui.QApplication.translate("B_SC", "Char Info", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelCharName.setText(QtGui.QApplication.translate("B_SC", "Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelRealm.setText(QtGui.QApplication.translate("B_SC", "Realm: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelCharClass.setText(QtGui.QApplication.translate("B_SC", "Class: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelCharRace.setText(QtGui.QApplication.translate("B_SC", "Race: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelCharLevel.setText(QtGui.QApplication.translate("B_SC", "Level: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelTotalCost.setText(QtGui.QApplication.translate("B_SC", "Cost: ", None, QtGui.QApplication.UnicodeUTF8))
        self.TotalCost.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelTotalPrice.setText(QtGui.QApplication.translate("B_SC", "Price: ", None, QtGui.QApplication.UnicodeUTF8))
        self.TotalPrice.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelTotalUtility.setText(QtGui.QApplication.translate("B_SC", "Total Utility: ", None, QtGui.QApplication.UnicodeUTF8))
        self.TotalUtility.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupStats.setTitle(QtGui.QApplication.translate("B_SC", "Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.StrengthLabel.setText(QtGui.QApplication.translate("B_SC", "STR: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Strength.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.StrengthCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.ConstitutionLabel.setText(QtGui.QApplication.translate("B_SC", "CON: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Constitution.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.ConstitutionCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.DexterityLabel.setText(QtGui.QApplication.translate("B_SC", "DEX: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Dexterity.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.DexterityCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.QuicknessLabel.setText(QtGui.QApplication.translate("B_SC", "QUI: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Quickness.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.QuicknessCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.IntelligenceLabel.setText(QtGui.QApplication.translate("B_SC", "INT: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Intelligence.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.IntelligenceCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.PietyLabel.setText(QtGui.QApplication.translate("B_SC", "PIE: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Piety.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.PietyCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.CharismaLabel.setText(QtGui.QApplication.translate("B_SC", "CHA: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Charisma.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.CharismaCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.EmpathyLabel.setText(QtGui.QApplication.translate("B_SC", "EMP: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Empathy.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.EmpathyCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.PowerLabel.setText(QtGui.QApplication.translate("B_SC", "Pow: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Power.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.PowerCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.HitsLabel.setText(QtGui.QApplication.translate("B_SC", "Hits: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Hits.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.HitsCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupResists.setTitle(QtGui.QApplication.translate("B_SC", "Resists", None, QtGui.QApplication.UnicodeUTF8))
        self.BodyLabel.setText(QtGui.QApplication.translate("B_SC", "Body: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Body.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.BodyRR.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.ColdLabel.setText(QtGui.QApplication.translate("B_SC", "Cold: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Cold.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.ColdRR.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.HeatLabel.setText(QtGui.QApplication.translate("B_SC", "Heat: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Heat.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.HeatRR.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.EnergyLabel.setText(QtGui.QApplication.translate("B_SC", "Energy: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Energy.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.EnergyRR.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.MatterLabel.setText(QtGui.QApplication.translate("B_SC", "Matter: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Matter.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.MatterRR.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.SpiritLabel.setText(QtGui.QApplication.translate("B_SC", "Spirit: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Spirit.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.SpiritRR.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.CrushLabel.setText(QtGui.QApplication.translate("B_SC", "Crush: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Crush.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.CrushRR.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.ThrustLabel.setText(QtGui.QApplication.translate("B_SC", "Thrust: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Thrust.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.ThrustRR.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.SlashLabel.setText(QtGui.QApplication.translate("B_SC", "Slash: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Slash.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.SlashRR.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupSkillsList.setTitle(QtGui.QApplication.translate("B_SC", "Skills", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupOtherBonusList.setTitle(QtGui.QApplication.translate("B_SC", "Other Bonuses", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemLevelLabel.setText(QtGui.QApplication.translate("B_SC", "Level: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemLevelButton.setText(QtGui.QApplication.translate("B_SC", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemQualityLabel.setText(QtGui.QApplication.translate("B_SC", "Quality: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemBonusLabel.setText(QtGui.QApplication.translate("B_SC", "Bonus: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemAFDPSLabel.setText(QtGui.QApplication.translate("B_SC", "AF/DPS: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemSpeedLabel.setText(QtGui.QApplication.translate("B_SC", "Speed: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Equipped.setText(QtGui.QApplication.translate("B_SC", "Equipped", None, QtGui.QApplication.UnicodeUTF8))
        self.PlayerMade.setText(QtGui.QApplication.translate("B_SC", "Player Made", None, QtGui.QApplication.UnicodeUTF8))
        self.Drop.setText(QtGui.QApplication.translate("B_SC", "Drop", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemType.setText(QtGui.QApplication.translate("B_SC", " Type", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemAmount.setText(QtGui.QApplication.translate("B_SC", " Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemEffect.setText(QtGui.QApplication.translate("B_SC", " Effect", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelRequirement.setText(QtGui.QApplication.translate("B_SC", " Requirement", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemQuality.setText(QtGui.QApplication.translate("B_SC", " Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemPoints.setText(QtGui.QApplication.translate("B_SC", "Points", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemCost.setText(QtGui.QApplication.translate("B_SC", "Cost", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelItemName.setText(QtGui.QApplication.translate("B_SC", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_1.setText(QtGui.QApplication.translate("B_SC", "Slot 1: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Points_1.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.Cost_1.setText(QtGui.QApplication.translate("B_SC", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_2.setText(QtGui.QApplication.translate("B_SC", "Slot 2: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Points_2.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.Cost_2.setText(QtGui.QApplication.translate("B_SC", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_3.setText(QtGui.QApplication.translate("B_SC", "Slot 3: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Points_3.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.Cost_3.setText(QtGui.QApplication.translate("B_SC", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_4.setText(QtGui.QApplication.translate("B_SC", "Slot 4: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Points_4.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.Cost_4.setText(QtGui.QApplication.translate("B_SC", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_5.setText(QtGui.QApplication.translate("B_SC", "Slot 5: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_6.setText(QtGui.QApplication.translate("B_SC", "Slot 6: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelRequirement2.setText(QtGui.QApplication.translate("B_SC", " (Requirement)", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_7.setText(QtGui.QApplication.translate("B_SC", "Slot 7: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_8.setText(QtGui.QApplication.translate("B_SC", "Slot 8: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_9.setText(QtGui.QApplication.translate("B_SC", "Slot 9: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_10.setText(QtGui.QApplication.translate("B_SC", "Slot 10:", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_11.setText(QtGui.QApplication.translate("B_SC", "Slot 11:", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_12.setText(QtGui.QApplication.translate("B_SC", "Slot 12:", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemImbueLabel.setText(QtGui.QApplication.translate("B_SC", "Imbue Points: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemImbue.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemImbueTotal.setText(QtGui.QApplication.translate("B_SC", " / 0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemOverchargeLabel.setText(QtGui.QApplication.translate("B_SC", "Overcharge: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemOvercharge.setText(QtGui.QApplication.translate("B_SC", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemCostLabel.setText(QtGui.QApplication.translate("B_SC", "Item Cost: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemPriceLabel.setText(QtGui.QApplication.translate("B_SC", "Item Price: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemUtilityLabel.setText(QtGui.QApplication.translate("B_SC", "Utility: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemUtility.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
