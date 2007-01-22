# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ScWindow.ui'
#
# Created: Sun Jan 21 19:48:18 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_SC(object):
    def setupUi(self, B_SC):
        B_SC.setObjectName("B_SC")
        B_SC.resize(QtCore.QSize(QtCore.QRect(0,0,761,510).size()).expandedTo(B_SC.minimumSizeHint()))

        self.ScWinFrame = QtGui.QWidget(B_SC)
        self.ScWinFrame.setObjectName("ScWinFrame")

        self.gridlayout = QtGui.QGridLayout(self.ScWinFrame)
        self.gridlayout.setMargin(3)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.GroupCharInfo = GroupFrame(self.ScWinFrame)
        self.GroupCharInfo.setObjectName("GroupCharInfo")

        self.gridlayout1 = QtGui.QGridLayout(self.GroupCharInfo)
        self.gridlayout1.setMargin(4)
        self.gridlayout1.setSpacing(0)
        self.gridlayout1.setObjectName("gridlayout1")

        self.LabelCharName = QtGui.QLabel(self.GroupCharInfo)
        self.LabelCharName.setTextFormat(QtCore.Qt.PlainText)
        self.LabelCharName.setObjectName("LabelCharName")
        self.gridlayout1.addWidget(self.LabelCharName,0,0,1,1)

        self.CharName = QtGui.QLineEdit(self.GroupCharInfo)
        self.CharName.setObjectName("CharName")
        self.gridlayout1.addWidget(self.CharName,0,1,1,2)

        self.LabelRealm = QtGui.QLabel(self.GroupCharInfo)
        self.LabelRealm.setTextFormat(QtCore.Qt.PlainText)
        self.LabelRealm.setObjectName("LabelRealm")
        self.gridlayout1.addWidget(self.LabelRealm,1,0,1,1)

        self.Realm = SearchingCombo(self.GroupCharInfo)
        self.Realm.setObjectName("Realm")
        self.gridlayout1.addWidget(self.Realm,1,1,1,2)

        self.LabelCharClass = QtGui.QLabel(self.GroupCharInfo)
        self.LabelCharClass.setTextFormat(QtCore.Qt.PlainText)
        self.LabelCharClass.setObjectName("LabelCharClass")
        self.gridlayout1.addWidget(self.LabelCharClass,2,0,1,1)

        self.CharClass = SearchingCombo(self.GroupCharInfo)
        self.CharClass.setObjectName("CharClass")
        self.gridlayout1.addWidget(self.CharClass,2,1,1,2)

        self.LabelCharRace = QtGui.QLabel(self.GroupCharInfo)
        self.LabelCharRace.setTextFormat(QtCore.Qt.PlainText)
        self.LabelCharRace.setObjectName("LabelCharRace")
        self.gridlayout1.addWidget(self.LabelCharRace,3,0,1,1)

        self.CharRace = SearchingCombo(self.GroupCharInfo)
        self.CharRace.setObjectName("CharRace")
        self.gridlayout1.addWidget(self.CharRace,3,1,1,2)

        self.LabelCharLevel = QtGui.QLabel(self.GroupCharInfo)
        self.LabelCharLevel.setTextFormat(QtCore.Qt.PlainText)
        self.LabelCharLevel.setObjectName("LabelCharLevel")
        self.gridlayout1.addWidget(self.LabelCharLevel,4,0,1,1)

        self.CharLevel = QtGui.QLineEdit(self.GroupCharInfo)
        self.CharLevel.setObjectName("CharLevel")
        self.gridlayout1.addWidget(self.CharLevel,4,1,1,2)

        self.LabelOutfitName = QtGui.QLabel(self.GroupCharInfo)
        self.LabelOutfitName.setTextFormat(QtCore.Qt.PlainText)
        self.LabelOutfitName.setObjectName("LabelOutfitName")
        self.gridlayout1.addWidget(self.LabelOutfitName,5,0,1,1)

        self.OutfitName = SearchingCombo(self.GroupCharInfo)
        self.OutfitName.setEditable(True)
        self.OutfitName.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.OutfitName.setDuplicatesEnabled(True)
        self.OutfitName.setObjectName("OutfitName")
        self.gridlayout1.addWidget(self.OutfitName,5,1,1,2)

        spacerItem = QtGui.QSpacerItem(5,4,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        self.gridlayout1.addItem(spacerItem,6,0,1,3)

        self.LabelTotalCost = QtGui.QLabel(self.GroupCharInfo)
        self.LabelTotalCost.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelTotalCost.setObjectName("LabelTotalCost")
        self.gridlayout1.addWidget(self.LabelTotalCost,7,0,1,1)

        self.TotalCost = QtGui.QLabel(self.GroupCharInfo)
        self.TotalCost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotalCost.setObjectName("TotalCost")
        self.gridlayout1.addWidget(self.TotalCost,7,1,1,2)

        self.LabelTotalPrice = QtGui.QLabel(self.GroupCharInfo)
        self.LabelTotalPrice.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelTotalPrice.setObjectName("LabelTotalPrice")
        self.gridlayout1.addWidget(self.LabelTotalPrice,8,0,1,1)

        self.TotalPrice = QtGui.QLabel(self.GroupCharInfo)
        self.TotalPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotalPrice.setObjectName("TotalPrice")
        self.gridlayout1.addWidget(self.TotalPrice,8,1,1,2)

        self.LabelTotalUtility = QtGui.QLabel(self.GroupCharInfo)
        self.LabelTotalUtility.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LabelTotalUtility.setObjectName("LabelTotalUtility")
        self.gridlayout1.addWidget(self.LabelTotalUtility,9,0,1,2)

        self.TotalUtility = QtGui.QLabel(self.GroupCharInfo)
        self.TotalUtility.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotalUtility.setObjectName("TotalUtility")
        self.gridlayout1.addWidget(self.TotalUtility,9,2,1,1)

        spacerItem1 = QtGui.QSpacerItem(5,2,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.MinimumExpanding)
        self.gridlayout1.addItem(spacerItem1,10,0,1,3)
        self.gridlayout.addWidget(self.GroupCharInfo,0,0,1,1)

        spacerItem2 = QtGui.QSpacerItem(3,1,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem2,0,1,1,1)

        self.GroupStats = GroupFrame(self.ScWinFrame)
        self.GroupStats.setObjectName("GroupStats")

        self.gridlayout2 = QtGui.QGridLayout(self.GroupStats)
        self.gridlayout2.setMargin(4)
        self.gridlayout2.setSpacing(0)
        self.gridlayout2.setObjectName("gridlayout2")

        self.StrengthLabel = QtGui.QLabel(self.GroupStats)
        self.StrengthLabel.setObjectName("StrengthLabel")
        self.gridlayout2.addWidget(self.StrengthLabel,0,0,1,1)

        self.Strength = QtGui.QLabel(self.GroupStats)
        self.Strength.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Strength.setObjectName("Strength")
        self.gridlayout2.addWidget(self.Strength,0,1,1,1)

        self.StrengthCap = QtGui.QLabel(self.GroupStats)
        self.StrengthCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.StrengthCap.setObjectName("StrengthCap")
        self.gridlayout2.addWidget(self.StrengthCap,0,2,1,1)

        self.ConstitutionLabel = QtGui.QLabel(self.GroupStats)
        self.ConstitutionLabel.setObjectName("ConstitutionLabel")
        self.gridlayout2.addWidget(self.ConstitutionLabel,1,0,1,1)

        self.Constitution = QtGui.QLabel(self.GroupStats)
        self.Constitution.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Constitution.setObjectName("Constitution")
        self.gridlayout2.addWidget(self.Constitution,1,1,1,1)

        self.ConstitutionCap = QtGui.QLabel(self.GroupStats)
        self.ConstitutionCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ConstitutionCap.setObjectName("ConstitutionCap")
        self.gridlayout2.addWidget(self.ConstitutionCap,1,2,1,1)

        self.DexterityLabel = QtGui.QLabel(self.GroupStats)
        self.DexterityLabel.setObjectName("DexterityLabel")
        self.gridlayout2.addWidget(self.DexterityLabel,2,0,1,1)

        self.Dexterity = QtGui.QLabel(self.GroupStats)
        self.Dexterity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Dexterity.setObjectName("Dexterity")
        self.gridlayout2.addWidget(self.Dexterity,2,1,1,1)

        self.DexterityCap = QtGui.QLabel(self.GroupStats)
        self.DexterityCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DexterityCap.setObjectName("DexterityCap")
        self.gridlayout2.addWidget(self.DexterityCap,2,2,1,1)

        self.QuicknessLabel = QtGui.QLabel(self.GroupStats)
        self.QuicknessLabel.setObjectName("QuicknessLabel")
        self.gridlayout2.addWidget(self.QuicknessLabel,3,0,1,1)

        self.Quickness = QtGui.QLabel(self.GroupStats)
        self.Quickness.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Quickness.setObjectName("Quickness")
        self.gridlayout2.addWidget(self.Quickness,3,1,1,1)

        self.QuicknessCap = QtGui.QLabel(self.GroupStats)
        self.QuicknessCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.QuicknessCap.setObjectName("QuicknessCap")
        self.gridlayout2.addWidget(self.QuicknessCap,3,2,1,1)

        self.IntelligenceLabel = QtGui.QLabel(self.GroupStats)
        self.IntelligenceLabel.setObjectName("IntelligenceLabel")
        self.gridlayout2.addWidget(self.IntelligenceLabel,4,0,1,1)

        self.Intelligence = QtGui.QLabel(self.GroupStats)
        self.Intelligence.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Intelligence.setObjectName("Intelligence")
        self.gridlayout2.addWidget(self.Intelligence,4,1,1,1)

        self.IntelligenceCap = QtGui.QLabel(self.GroupStats)
        self.IntelligenceCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.IntelligenceCap.setObjectName("IntelligenceCap")
        self.gridlayout2.addWidget(self.IntelligenceCap,4,2,1,1)

        self.PietyLabel = QtGui.QLabel(self.GroupStats)
        self.PietyLabel.setObjectName("PietyLabel")
        self.gridlayout2.addWidget(self.PietyLabel,5,0,1,1)

        self.Piety = QtGui.QLabel(self.GroupStats)
        self.Piety.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Piety.setObjectName("Piety")
        self.gridlayout2.addWidget(self.Piety,5,1,1,1)

        self.PietyCap = QtGui.QLabel(self.GroupStats)
        self.PietyCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PietyCap.setObjectName("PietyCap")
        self.gridlayout2.addWidget(self.PietyCap,5,2,1,1)

        self.CharismaLabel = QtGui.QLabel(self.GroupStats)
        self.CharismaLabel.setObjectName("CharismaLabel")
        self.gridlayout2.addWidget(self.CharismaLabel,6,0,1,1)

        self.Charisma = QtGui.QLabel(self.GroupStats)
        self.Charisma.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Charisma.setObjectName("Charisma")
        self.gridlayout2.addWidget(self.Charisma,6,1,1,1)

        self.CharismaCap = QtGui.QLabel(self.GroupStats)
        self.CharismaCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CharismaCap.setObjectName("CharismaCap")
        self.gridlayout2.addWidget(self.CharismaCap,6,2,1,1)

        self.EmpathyLabel = QtGui.QLabel(self.GroupStats)
        self.EmpathyLabel.setObjectName("EmpathyLabel")
        self.gridlayout2.addWidget(self.EmpathyLabel,7,0,1,1)

        self.Empathy = QtGui.QLabel(self.GroupStats)
        self.Empathy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Empathy.setObjectName("Empathy")
        self.gridlayout2.addWidget(self.Empathy,7,1,1,1)

        self.EmpathyCap = QtGui.QLabel(self.GroupStats)
        self.EmpathyCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EmpathyCap.setObjectName("EmpathyCap")
        self.gridlayout2.addWidget(self.EmpathyCap,7,2,1,1)

        self.AcuityLabel = QtGui.QLabel(self.GroupStats)
        self.AcuityLabel.setObjectName("AcuityLabel")
        self.gridlayout2.addWidget(self.AcuityLabel,8,0,1,1)

        self.Acuity = QtGui.QLabel(self.GroupStats)
        self.Acuity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Acuity.setObjectName("Acuity")
        self.gridlayout2.addWidget(self.Acuity,8,1,1,1)

        self.AcuityCap = QtGui.QLabel(self.GroupStats)
        self.AcuityCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AcuityCap.setObjectName("AcuityCap")
        self.gridlayout2.addWidget(self.AcuityCap,8,2,1,1)

        self.PowerLabel = QtGui.QLabel(self.GroupStats)
        self.PowerLabel.setObjectName("PowerLabel")
        self.gridlayout2.addWidget(self.PowerLabel,9,0,1,1)

        self.Power = QtGui.QLabel(self.GroupStats)
        self.Power.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Power.setObjectName("Power")
        self.gridlayout2.addWidget(self.Power,9,1,1,1)

        self.PowerCap = QtGui.QLabel(self.GroupStats)
        self.PowerCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PowerCap.setObjectName("PowerCap")
        self.gridlayout2.addWidget(self.PowerCap,9,2,1,1)

        self.PowerPoolLabel = QtGui.QLabel(self.GroupStats)
        self.PowerPoolLabel.setObjectName("PowerPoolLabel")
        self.gridlayout2.addWidget(self.PowerPoolLabel,10,0,1,1)

        self.PowerPool = QtGui.QLabel(self.GroupStats)
        self.PowerPool.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PowerPool.setObjectName("PowerPool")
        self.gridlayout2.addWidget(self.PowerPool,10,1,1,1)

        self.PowerPoolCap = QtGui.QLabel(self.GroupStats)
        self.PowerPoolCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PowerPoolCap.setObjectName("PowerPoolCap")
        self.gridlayout2.addWidget(self.PowerPoolCap,10,2,1,1)

        self.AFLabel = QtGui.QLabel(self.GroupStats)
        self.AFLabel.setObjectName("AFLabel")
        self.gridlayout2.addWidget(self.AFLabel,11,0,1,1)

        self.AF = QtGui.QLabel(self.GroupStats)
        self.AF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AF.setObjectName("AF")
        self.gridlayout2.addWidget(self.AF,11,1,1,1)

        self.AFCap = QtGui.QLabel(self.GroupStats)
        self.AFCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.AFCap.setObjectName("AFCap")
        self.gridlayout2.addWidget(self.AFCap,11,2,1,1)

        self.HitsLabel = QtGui.QLabel(self.GroupStats)
        self.HitsLabel.setObjectName("HitsLabel")
        self.gridlayout2.addWidget(self.HitsLabel,12,0,1,1)

        self.Hits = QtGui.QLabel(self.GroupStats)
        self.Hits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Hits.setObjectName("Hits")
        self.gridlayout2.addWidget(self.Hits,12,1,1,1)

        self.HitsCap = QtGui.QLabel(self.GroupStats)
        self.HitsCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.HitsCap.setObjectName("HitsCap")
        self.gridlayout2.addWidget(self.HitsCap,12,2,1,1)

        spacerItem3 = QtGui.QSpacerItem(5,0,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.MinimumExpanding)
        self.gridlayout2.addItem(spacerItem3,13,0,1,3)
        self.gridlayout.addWidget(self.GroupStats,0,2,1,1)

        spacerItem4 = QtGui.QSpacerItem(3,0,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem4,0,3,1,1)

        self.GroupResists = GroupFrame(self.ScWinFrame)
        self.GroupResists.setObjectName("GroupResists")

        self.gridlayout3 = QtGui.QGridLayout(self.GroupResists)
        self.gridlayout3.setMargin(4)
        self.gridlayout3.setSpacing(0)
        self.gridlayout3.setObjectName("gridlayout3")

        self.BodyLabel = QtGui.QLabel(self.GroupResists)
        self.BodyLabel.setObjectName("BodyLabel")
        self.gridlayout3.addWidget(self.BodyLabel,0,0,1,1)

        self.Body = QtGui.QLabel(self.GroupResists)
        self.Body.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Body.setObjectName("Body")
        self.gridlayout3.addWidget(self.Body,0,1,1,1)

        self.BodyCap = QtGui.QLabel(self.GroupResists)
        self.BodyCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BodyCap.setObjectName("BodyCap")
        self.gridlayout3.addWidget(self.BodyCap,0,2,1,1)

        self.ColdLabel = QtGui.QLabel(self.GroupResists)
        self.ColdLabel.setObjectName("ColdLabel")
        self.gridlayout3.addWidget(self.ColdLabel,1,0,1,1)

        self.Cold = QtGui.QLabel(self.GroupResists)
        self.Cold.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Cold.setObjectName("Cold")
        self.gridlayout3.addWidget(self.Cold,1,1,1,1)

        self.ColdCap = QtGui.QLabel(self.GroupResists)
        self.ColdCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ColdCap.setObjectName("ColdCap")
        self.gridlayout3.addWidget(self.ColdCap,1,2,1,1)

        self.HeatLabel = QtGui.QLabel(self.GroupResists)
        self.HeatLabel.setObjectName("HeatLabel")
        self.gridlayout3.addWidget(self.HeatLabel,2,0,1,1)

        self.Heat = QtGui.QLabel(self.GroupResists)
        self.Heat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Heat.setObjectName("Heat")
        self.gridlayout3.addWidget(self.Heat,2,1,1,1)

        self.HeatCap = QtGui.QLabel(self.GroupResists)
        self.HeatCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.HeatCap.setObjectName("HeatCap")
        self.gridlayout3.addWidget(self.HeatCap,2,2,1,1)

        self.EnergyLabel = QtGui.QLabel(self.GroupResists)
        self.EnergyLabel.setObjectName("EnergyLabel")
        self.gridlayout3.addWidget(self.EnergyLabel,3,0,1,1)

        self.Energy = QtGui.QLabel(self.GroupResists)
        self.Energy.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Energy.setObjectName("Energy")
        self.gridlayout3.addWidget(self.Energy,3,1,1,1)

        self.EnergyCap = QtGui.QLabel(self.GroupResists)
        self.EnergyCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EnergyCap.setObjectName("EnergyCap")
        self.gridlayout3.addWidget(self.EnergyCap,3,2,1,1)

        self.MatterLabel = QtGui.QLabel(self.GroupResists)
        self.MatterLabel.setObjectName("MatterLabel")
        self.gridlayout3.addWidget(self.MatterLabel,4,0,1,1)

        self.Matter = QtGui.QLabel(self.GroupResists)
        self.Matter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Matter.setObjectName("Matter")
        self.gridlayout3.addWidget(self.Matter,4,1,1,1)

        self.MatterCap = QtGui.QLabel(self.GroupResists)
        self.MatterCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MatterCap.setObjectName("MatterCap")
        self.gridlayout3.addWidget(self.MatterCap,4,2,1,1)

        self.SpiritLabel = QtGui.QLabel(self.GroupResists)
        self.SpiritLabel.setObjectName("SpiritLabel")
        self.gridlayout3.addWidget(self.SpiritLabel,5,0,1,1)

        self.Spirit = QtGui.QLabel(self.GroupResists)
        self.Spirit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Spirit.setObjectName("Spirit")
        self.gridlayout3.addWidget(self.Spirit,5,1,1,1)

        self.SpiritCap = QtGui.QLabel(self.GroupResists)
        self.SpiritCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SpiritCap.setObjectName("SpiritCap")
        self.gridlayout3.addWidget(self.SpiritCap,5,2,1,1)

        self.CrushLabel = QtGui.QLabel(self.GroupResists)
        self.CrushLabel.setObjectName("CrushLabel")
        self.gridlayout3.addWidget(self.CrushLabel,6,0,1,1)

        self.Crush = QtGui.QLabel(self.GroupResists)
        self.Crush.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Crush.setObjectName("Crush")
        self.gridlayout3.addWidget(self.Crush,6,1,1,1)

        self.CrushCap = QtGui.QLabel(self.GroupResists)
        self.CrushCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CrushCap.setObjectName("CrushCap")
        self.gridlayout3.addWidget(self.CrushCap,6,2,1,1)

        self.ThrustLabel = QtGui.QLabel(self.GroupResists)
        self.ThrustLabel.setObjectName("ThrustLabel")
        self.gridlayout3.addWidget(self.ThrustLabel,7,0,1,1)

        self.Thrust = QtGui.QLabel(self.GroupResists)
        self.Thrust.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Thrust.setObjectName("Thrust")
        self.gridlayout3.addWidget(self.Thrust,7,1,1,1)

        self.ThrustCap = QtGui.QLabel(self.GroupResists)
        self.ThrustCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ThrustCap.setObjectName("ThrustCap")
        self.gridlayout3.addWidget(self.ThrustCap,7,2,1,1)

        self.SlashLabel = QtGui.QLabel(self.GroupResists)
        self.SlashLabel.setObjectName("SlashLabel")
        self.gridlayout3.addWidget(self.SlashLabel,8,0,1,1)

        self.Slash = QtGui.QLabel(self.GroupResists)
        self.Slash.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Slash.setObjectName("Slash")
        self.gridlayout3.addWidget(self.Slash,8,1,1,1)

        self.SlashCap = QtGui.QLabel(self.GroupResists)
        self.SlashCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SlashCap.setObjectName("SlashCap")
        self.gridlayout3.addWidget(self.SlashCap,8,2,1,1)

        self.EssenceLabel = QtGui.QLabel(self.GroupResists)
        self.EssenceLabel.setObjectName("EssenceLabel")
        self.gridlayout3.addWidget(self.EssenceLabel,9,0,1,1)

        self.Essence = QtGui.QLabel(self.GroupResists)
        self.Essence.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Essence.setObjectName("Essence")
        self.gridlayout3.addWidget(self.Essence,9,1,1,1)

        self.EssenceCap = QtGui.QLabel(self.GroupResists)
        self.EssenceCap.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.EssenceCap.setObjectName("EssenceCap")
        self.gridlayout3.addWidget(self.EssenceCap,9,2,1,1)

        spacerItem5 = QtGui.QSpacerItem(5,0,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.MinimumExpanding)
        self.gridlayout3.addItem(spacerItem5,10,0,1,3)
        self.gridlayout.addWidget(self.GroupResists,0,4,1,1)

        spacerItem6 = QtGui.QSpacerItem(3,1,QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem6,0,5,1,1)

        self.GroupSkillsList = GroupFrame(self.ScWinFrame)
        self.GroupSkillsList.setObjectName("GroupSkillsList")

        self.gridlayout4 = QtGui.QGridLayout(self.GroupSkillsList)
        self.gridlayout4.setMargin(4)
        self.gridlayout4.setSpacing(0)
        self.gridlayout4.setObjectName("gridlayout4")

        self.SkillsList = QtGui.QListView(self.GroupSkillsList)
        self.SkillsList.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.SkillsList.setFrameShape(QtGui.QFrame.NoFrame)
        self.SkillsList.setFrameShadow(QtGui.QFrame.Plain)
        self.SkillsList.setLineWidth(0)
        self.SkillsList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SkillsList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.SkillsList.setAutoScroll(True)
        self.SkillsList.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.SkillsList.setWrapping(True)
        self.SkillsList.setResizeMode(QtGui.QListView.Adjust)
        self.SkillsList.setObjectName("SkillsList")
        self.gridlayout4.addWidget(self.SkillsList,0,0,1,1)
        self.gridlayout.addWidget(self.GroupSkillsList,0,6,1,1)

        spacerItem7 = QtGui.QSpacerItem(1,4,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        self.gridlayout.addItem(spacerItem7,1,0,1,7)

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setObjectName("vboxlayout")

        self.PieceTab = MultiTabBar(self.ScWinFrame)
        self.PieceTab.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.PieceTab.setObjectName("PieceTab")
        self.vboxlayout.addWidget(self.PieceTab)

        spacerItem8 = QtGui.QSpacerItem(1,1,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        self.vboxlayout.addItem(spacerItem8)

        self.GroupItemFrame = MultiTabFrame(self.ScWinFrame)
        self.GroupItemFrame.setObjectName("GroupItemFrame")

        self.gridlayout5 = QtGui.QGridLayout(self.GroupItemFrame)
        self.gridlayout5.setMargin(6)
        self.gridlayout5.setSpacing(0)
        self.gridlayout5.setObjectName("gridlayout5")

        spacerItem9 = QtGui.QSpacerItem(0,0,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        self.gridlayout5.addItem(spacerItem9,0,0,1,10)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(0)
        self.hboxlayout.setObjectName("hboxlayout")

        self.ItemLevelLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemLevelLabel.setTextFormat(QtCore.Qt.PlainText)
        self.ItemLevelLabel.setObjectName("ItemLevelLabel")
        self.hboxlayout.addWidget(self.ItemLevelLabel)

        self.ItemLevel = QtGui.QLineEdit(self.GroupItemFrame)
        self.ItemLevel.setObjectName("ItemLevel")
        self.hboxlayout.addWidget(self.ItemLevel)

        self.ItemLevelButton = QtGui.QPushButton(self.GroupItemFrame)
        self.ItemLevelButton.setMaximumSize(QtCore.QSize(21,21))
        self.ItemLevelButton.setObjectName("ItemLevelButton")
        self.hboxlayout.addWidget(self.ItemLevelButton)

        spacerItem10 = QtGui.QSpacerItem(5,1,QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem10)

        self.ItemQualityLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemQualityLabel.setTextFormat(QtCore.Qt.PlainText)
        self.ItemQualityLabel.setObjectName("ItemQualityLabel")
        self.hboxlayout.addWidget(self.ItemQualityLabel)

        self.QualDrop = SearchingCombo(self.GroupItemFrame)
        self.QualDrop.setObjectName("QualDrop")
        self.hboxlayout.addWidget(self.QualDrop)

        self.QualEdit = QtGui.QLineEdit(self.GroupItemFrame)
        self.QualEdit.setObjectName("QualEdit")
        self.hboxlayout.addWidget(self.QualEdit)

        spacerItem11 = QtGui.QSpacerItem(5,1,QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem11)

        self.ItemBonusLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemBonusLabel.setTextFormat(QtCore.Qt.PlainText)
        self.ItemBonusLabel.setObjectName("ItemBonusLabel")
        self.hboxlayout.addWidget(self.ItemBonusLabel)

        self.Bonus_Edit = QtGui.QLineEdit(self.GroupItemFrame)
        self.Bonus_Edit.setObjectName("Bonus_Edit")
        self.hboxlayout.addWidget(self.Bonus_Edit)

        spacerItem12 = QtGui.QSpacerItem(5,1,QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem12)

        self.ItemAFDPSLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemAFDPSLabel.setTextFormat(QtCore.Qt.PlainText)
        self.ItemAFDPSLabel.setObjectName("ItemAFDPSLabel")
        self.hboxlayout.addWidget(self.ItemAFDPSLabel)

        self.AFDPS_Edit = QtGui.QLineEdit(self.GroupItemFrame)
        self.AFDPS_Edit.setObjectName("AFDPS_Edit")
        self.hboxlayout.addWidget(self.AFDPS_Edit)

        spacerItem13 = QtGui.QSpacerItem(5,1,QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem13)

        self.ItemSpeedLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemSpeedLabel.setTextFormat(QtCore.Qt.PlainText)
        self.ItemSpeedLabel.setObjectName("ItemSpeedLabel")
        self.hboxlayout.addWidget(self.ItemSpeedLabel)

        self.Speed_Edit = QtGui.QLineEdit(self.GroupItemFrame)
        self.Speed_Edit.setObjectName("Speed_Edit")
        self.hboxlayout.addWidget(self.Speed_Edit)

        spacerItem14 = QtGui.QSpacerItem(5,1,QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem14)

        self.ItemNameLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemNameLabel.setTextFormat(QtCore.Qt.PlainText)
        self.ItemNameLabel.setObjectName("ItemNameLabel")
        self.hboxlayout.addWidget(self.ItemNameLabel)

        self.ItemNameCombo = SearchingCombo(self.GroupItemFrame)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(3),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ItemNameCombo.sizePolicy().hasHeightForWidth())
        self.ItemNameCombo.setSizePolicy(sizePolicy)
        self.ItemNameCombo.setEditable(True)
        self.ItemNameCombo.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.ItemNameCombo.setDuplicatesEnabled(True)
        self.ItemNameCombo.setObjectName("ItemNameCombo")
        self.hboxlayout.addWidget(self.ItemNameCombo)

        spacerItem15 = QtGui.QSpacerItem(5,1,QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem15)

        self.Equipped = QtGui.QCheckBox(self.GroupItemFrame)
        self.Equipped.setObjectName("Equipped")
        self.hboxlayout.addWidget(self.Equipped)
        self.gridlayout5.addLayout(self.hboxlayout,1,0,1,10)

        self.LabelGemType = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemType.setObjectName("LabelGemType")
        self.gridlayout5.addWidget(self.LabelGemType,2,1,1,1)

        self.LabelGemAmount = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemAmount.setObjectName("LabelGemAmount")
        self.gridlayout5.addWidget(self.LabelGemAmount,2,2,1,1)

        self.LabelGemEffect = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemEffect.setObjectName("LabelGemEffect")
        self.gridlayout5.addWidget(self.LabelGemEffect,2,3,1,1)

        self.LabelGemMakes = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemMakes.setObjectName("LabelGemMakes")
        self.gridlayout5.addWidget(self.LabelGemMakes,2,4,1,1)

        self.LabelRequirement = QtGui.QLabel(self.GroupItemFrame)
        self.LabelRequirement.setObjectName("LabelRequirement")
        self.gridlayout5.addWidget(self.LabelRequirement,2,4,1,3)

        self.LabelGemPoints = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemPoints.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelGemPoints.setObjectName("LabelGemPoints")
        self.gridlayout5.addWidget(self.LabelGemPoints,2,5,1,1)

        self.LabelGemCost = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemCost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LabelGemCost.setObjectName("LabelGemCost")
        self.gridlayout5.addWidget(self.LabelGemCost,2,6,1,1)

        spacerItem16 = QtGui.QSpacerItem(5,1,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem16,2,7,13,1)

        self.LabelGemName = QtGui.QLabel(self.GroupItemFrame)
        self.LabelGemName.setObjectName("LabelGemName")
        self.gridlayout5.addWidget(self.LabelGemName,2,8,1,2)

        spacerItem17 = QtGui.QSpacerItem(5,5,QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem17,2,8,12,2)

        self.Gem_Label_1 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_1.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_1.setObjectName("Gem_Label_1")
        self.gridlayout5.addWidget(self.Gem_Label_1,3,0,1,1)

        self.Type_1 = SearchingCombo(self.GroupItemFrame)
        self.Type_1.setObjectName("Type_1")
        self.gridlayout5.addWidget(self.Type_1,3,1,1,1)

        self.Amount_Edit_1 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_1.setObjectName("Amount_Edit_1")
        self.gridlayout5.addWidget(self.Amount_Edit_1,3,2,1,1)

        self.Amount_Drop_1 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_1.setObjectName("Amount_Drop_1")
        self.gridlayout5.addWidget(self.Amount_Drop_1,3,2,1,1)

        self.Effect_1 = SearchingCombo(self.GroupItemFrame)
        self.Effect_1.setEditable(True)
        self.Effect_1.setObjectName("Effect_1")
        self.gridlayout5.addWidget(self.Effect_1,3,3,1,1)

        self.Makes_1 = QtGui.QSpinBox(self.GroupItemFrame)
        self.Makes_1.setObjectName("Makes_1")
        self.gridlayout5.addWidget(self.Makes_1,3,4,1,1)

        self.Requirement_1 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_1.setObjectName("Requirement_1")
        self.gridlayout5.addWidget(self.Requirement_1,3,4,1,3)

        self.Points_1 = QtGui.QLabel(self.GroupItemFrame)
        self.Points_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Points_1.setObjectName("Points_1")
        self.gridlayout5.addWidget(self.Points_1,3,5,1,1)

        self.Cost_1 = QtGui.QLabel(self.GroupItemFrame)
        self.Cost_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Cost_1.setObjectName("Cost_1")
        self.gridlayout5.addWidget(self.Cost_1,3,6,1,1)

        self.Name_1 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_1.setObjectName("Name_1")
        self.gridlayout5.addWidget(self.Name_1,3,8,1,2)

        self.Gem_Label_2 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_2.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_2.setObjectName("Gem_Label_2")
        self.gridlayout5.addWidget(self.Gem_Label_2,4,0,1,1)

        self.Type_2 = SearchingCombo(self.GroupItemFrame)
        self.Type_2.setObjectName("Type_2")
        self.gridlayout5.addWidget(self.Type_2,4,1,1,1)

        self.Amount_Edit_2 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_2.setObjectName("Amount_Edit_2")
        self.gridlayout5.addWidget(self.Amount_Edit_2,4,2,1,1)

        self.Amount_Drop_2 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_2.setObjectName("Amount_Drop_2")
        self.gridlayout5.addWidget(self.Amount_Drop_2,4,2,1,1)

        self.Effect_2 = SearchingCombo(self.GroupItemFrame)
        self.Effect_2.setEditable(True)
        self.Effect_2.setObjectName("Effect_2")
        self.gridlayout5.addWidget(self.Effect_2,4,3,1,1)

        self.Makes_2 = QtGui.QSpinBox(self.GroupItemFrame)
        self.Makes_2.setObjectName("Makes_2")
        self.gridlayout5.addWidget(self.Makes_2,4,4,1,1)

        self.Requirement_2 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_2.setObjectName("Requirement_2")
        self.gridlayout5.addWidget(self.Requirement_2,4,4,1,3)

        self.Points_2 = QtGui.QLabel(self.GroupItemFrame)
        self.Points_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Points_2.setObjectName("Points_2")
        self.gridlayout5.addWidget(self.Points_2,4,5,1,1)

        self.Cost_2 = QtGui.QLabel(self.GroupItemFrame)
        self.Cost_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Cost_2.setObjectName("Cost_2")
        self.gridlayout5.addWidget(self.Cost_2,4,6,1,1)

        self.Name_2 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_2.setObjectName("Name_2")
        self.gridlayout5.addWidget(self.Name_2,4,8,1,2)

        self.Gem_Label_3 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_3.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_3.setObjectName("Gem_Label_3")
        self.gridlayout5.addWidget(self.Gem_Label_3,5,0,1,1)

        self.Type_3 = SearchingCombo(self.GroupItemFrame)
        self.Type_3.setObjectName("Type_3")
        self.gridlayout5.addWidget(self.Type_3,5,1,1,1)

        self.Amount_Edit_3 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_3.setObjectName("Amount_Edit_3")
        self.gridlayout5.addWidget(self.Amount_Edit_3,5,2,1,1)

        self.Amount_Drop_3 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_3.setObjectName("Amount_Drop_3")
        self.gridlayout5.addWidget(self.Amount_Drop_3,5,2,1,1)

        self.Effect_3 = SearchingCombo(self.GroupItemFrame)
        self.Effect_3.setEditable(True)
        self.Effect_3.setObjectName("Effect_3")
        self.gridlayout5.addWidget(self.Effect_3,5,3,1,1)

        self.Makes_3 = QtGui.QSpinBox(self.GroupItemFrame)
        self.Makes_3.setObjectName("Makes_3")
        self.gridlayout5.addWidget(self.Makes_3,5,4,1,1)

        self.Requirement_3 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_3.setObjectName("Requirement_3")
        self.gridlayout5.addWidget(self.Requirement_3,5,4,1,3)

        self.Points_3 = QtGui.QLabel(self.GroupItemFrame)
        self.Points_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Points_3.setObjectName("Points_3")
        self.gridlayout5.addWidget(self.Points_3,5,5,1,1)

        self.Cost_3 = QtGui.QLabel(self.GroupItemFrame)
        self.Cost_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Cost_3.setObjectName("Cost_3")
        self.gridlayout5.addWidget(self.Cost_3,5,6,1,1)

        self.Name_3 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_3.setObjectName("Name_3")
        self.gridlayout5.addWidget(self.Name_3,5,8,1,2)

        self.Gem_Label_4 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_4.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_4.setObjectName("Gem_Label_4")
        self.gridlayout5.addWidget(self.Gem_Label_4,6,0,1,1)

        self.Type_4 = SearchingCombo(self.GroupItemFrame)
        self.Type_4.setObjectName("Type_4")
        self.gridlayout5.addWidget(self.Type_4,6,1,1,1)

        self.Amount_Edit_4 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_4.setObjectName("Amount_Edit_4")
        self.gridlayout5.addWidget(self.Amount_Edit_4,6,2,1,1)

        self.Amount_Drop_4 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_4.setObjectName("Amount_Drop_4")
        self.gridlayout5.addWidget(self.Amount_Drop_4,6,2,1,1)

        self.Effect_4 = SearchingCombo(self.GroupItemFrame)
        self.Effect_4.setEditable(True)
        self.Effect_4.setObjectName("Effect_4")
        self.gridlayout5.addWidget(self.Effect_4,6,3,1,1)

        self.Makes_4 = QtGui.QSpinBox(self.GroupItemFrame)
        self.Makes_4.setObjectName("Makes_4")
        self.gridlayout5.addWidget(self.Makes_4,6,4,1,1)

        self.Requirement_4 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_4.setObjectName("Requirement_4")
        self.gridlayout5.addWidget(self.Requirement_4,6,4,1,3)

        self.Points_4 = QtGui.QLabel(self.GroupItemFrame)
        self.Points_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Points_4.setObjectName("Points_4")
        self.gridlayout5.addWidget(self.Points_4,6,5,1,1)

        self.Cost_4 = QtGui.QLabel(self.GroupItemFrame)
        self.Cost_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Cost_4.setObjectName("Cost_4")
        self.gridlayout5.addWidget(self.Cost_4,6,6,1,1)

        self.Name_4 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_4.setObjectName("Name_4")
        self.gridlayout5.addWidget(self.Name_4,6,8,1,2)

        self.Gem_Label_5 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_5.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_5.setObjectName("Gem_Label_5")
        self.gridlayout5.addWidget(self.Gem_Label_5,7,0,1,1)

        self.Type_5 = SearchingCombo(self.GroupItemFrame)
        self.Type_5.setObjectName("Type_5")
        self.gridlayout5.addWidget(self.Type_5,7,1,1,1)

        self.Amount_Edit_5 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_5.setObjectName("Amount_Edit_5")
        self.gridlayout5.addWidget(self.Amount_Edit_5,7,2,1,1)

        self.Amount_Drop_5 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_5.setObjectName("Amount_Drop_5")
        self.gridlayout5.addWidget(self.Amount_Drop_5,7,2,1,1)

        self.Effect_5 = SearchingCombo(self.GroupItemFrame)
        self.Effect_5.setEditable(True)
        self.Effect_5.setObjectName("Effect_5")
        self.gridlayout5.addWidget(self.Effect_5,7,3,1,1)

        self.Requirement_5 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_5.setObjectName("Requirement_5")
        self.gridlayout5.addWidget(self.Requirement_5,7,4,1,3)

        self.Name_5 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_5.setObjectName("Name_5")
        self.gridlayout5.addWidget(self.Name_5,7,8,1,2)

        self.LabelRequirement2 = QtGui.QLabel(self.GroupItemFrame)
        self.LabelRequirement2.setObjectName("LabelRequirement2")
        self.gridlayout5.addWidget(self.LabelRequirement2,7,8,1,2)

        self.Gem_Label_6 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_6.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_6.setObjectName("Gem_Label_6")
        self.gridlayout5.addWidget(self.Gem_Label_6,8,0,1,1)

        self.Type_6 = SearchingCombo(self.GroupItemFrame)
        self.Type_6.setObjectName("Type_6")
        self.gridlayout5.addWidget(self.Type_6,8,1,1,1)

        self.Amount_Edit_6 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_6.setObjectName("Amount_Edit_6")
        self.gridlayout5.addWidget(self.Amount_Edit_6,8,2,1,1)

        self.Amount_Drop_6 = SearchingCombo(self.GroupItemFrame)
        self.Amount_Drop_6.setObjectName("Amount_Drop_6")
        self.gridlayout5.addWidget(self.Amount_Drop_6,8,2,1,1)

        self.Effect_6 = SearchingCombo(self.GroupItemFrame)
        self.Effect_6.setEditable(True)
        self.Effect_6.setObjectName("Effect_6")
        self.gridlayout5.addWidget(self.Effect_6,8,3,1,1)

        self.Requirement_6 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_6.setObjectName("Requirement_6")
        self.gridlayout5.addWidget(self.Requirement_6,8,4,1,3)

        self.Name_6 = QtGui.QLabel(self.GroupItemFrame)
        self.Name_6.setObjectName("Name_6")
        self.gridlayout5.addWidget(self.Name_6,8,8,1,2)

        self.Gem_Label_7 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_7.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_7.setObjectName("Gem_Label_7")
        self.gridlayout5.addWidget(self.Gem_Label_7,9,0,1,1)

        self.Type_7 = SearchingCombo(self.GroupItemFrame)
        self.Type_7.setObjectName("Type_7")
        self.gridlayout5.addWidget(self.Type_7,9,1,1,1)

        self.Amount_Edit_7 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_7.setObjectName("Amount_Edit_7")
        self.gridlayout5.addWidget(self.Amount_Edit_7,9,2,1,1)

        self.Effect_7 = SearchingCombo(self.GroupItemFrame)
        self.Effect_7.setEditable(True)
        self.Effect_7.setObjectName("Effect_7")
        self.gridlayout5.addWidget(self.Effect_7,9,3,1,1)

        self.Requirement_7 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_7.setObjectName("Requirement_7")
        self.gridlayout5.addWidget(self.Requirement_7,9,4,1,3)

        self.Gem_Label_8 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_8.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_8.setObjectName("Gem_Label_8")
        self.gridlayout5.addWidget(self.Gem_Label_8,10,0,1,1)

        self.Type_8 = SearchingCombo(self.GroupItemFrame)
        self.Type_8.setObjectName("Type_8")
        self.gridlayout5.addWidget(self.Type_8,10,1,1,1)

        self.Amount_Edit_8 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_8.setObjectName("Amount_Edit_8")
        self.gridlayout5.addWidget(self.Amount_Edit_8,10,2,1,1)

        self.Effect_8 = SearchingCombo(self.GroupItemFrame)
        self.Effect_8.setEditable(True)
        self.Effect_8.setObjectName("Effect_8")
        self.gridlayout5.addWidget(self.Effect_8,10,3,1,1)

        self.Requirement_8 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_8.setObjectName("Requirement_8")
        self.gridlayout5.addWidget(self.Requirement_8,10,4,1,3)

        self.Gem_Label_9 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_9.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_9.setObjectName("Gem_Label_9")
        self.gridlayout5.addWidget(self.Gem_Label_9,11,0,1,1)

        self.Type_9 = SearchingCombo(self.GroupItemFrame)
        self.Type_9.setObjectName("Type_9")
        self.gridlayout5.addWidget(self.Type_9,11,1,1,1)

        self.Amount_Edit_9 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_9.setObjectName("Amount_Edit_9")
        self.gridlayout5.addWidget(self.Amount_Edit_9,11,2,1,1)

        self.Effect_9 = SearchingCombo(self.GroupItemFrame)
        self.Effect_9.setEditable(True)
        self.Effect_9.setObjectName("Effect_9")
        self.gridlayout5.addWidget(self.Effect_9,11,3,1,1)

        self.Requirement_9 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_9.setObjectName("Requirement_9")
        self.gridlayout5.addWidget(self.Requirement_9,11,4,1,3)

        self.Gem_Label_10 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_10.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_10.setObjectName("Gem_Label_10")
        self.gridlayout5.addWidget(self.Gem_Label_10,12,0,1,1)

        self.Type_10 = SearchingCombo(self.GroupItemFrame)
        self.Type_10.setObjectName("Type_10")
        self.gridlayout5.addWidget(self.Type_10,12,1,1,1)

        self.Amount_Edit_10 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_10.setObjectName("Amount_Edit_10")
        self.gridlayout5.addWidget(self.Amount_Edit_10,12,2,1,1)

        self.Effect_10 = SearchingCombo(self.GroupItemFrame)
        self.Effect_10.setEditable(True)
        self.Effect_10.setObjectName("Effect_10")
        self.gridlayout5.addWidget(self.Effect_10,12,3,1,1)

        self.Requirement_10 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_10.setObjectName("Requirement_10")
        self.gridlayout5.addWidget(self.Requirement_10,12,4,1,3)

        self.Gem_Label_11 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_11.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_11.setObjectName("Gem_Label_11")
        self.gridlayout5.addWidget(self.Gem_Label_11,13,0,1,1)

        self.Type_11 = SearchingCombo(self.GroupItemFrame)
        self.Type_11.setObjectName("Type_11")
        self.gridlayout5.addWidget(self.Type_11,13,1,1,1)

        self.Amount_Edit_11 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_11.setObjectName("Amount_Edit_11")
        self.gridlayout5.addWidget(self.Amount_Edit_11,13,2,1,1)

        self.Effect_11 = SearchingCombo(self.GroupItemFrame)
        self.Effect_11.setEditable(True)
        self.Effect_11.setObjectName("Effect_11")
        self.gridlayout5.addWidget(self.Effect_11,13,3,1,1)

        self.Requirement_11 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_11.setObjectName("Requirement_11")
        self.gridlayout5.addWidget(self.Requirement_11,13,4,1,3)

        self.Gem_Label_12 = QtGui.QLabel(self.GroupItemFrame)
        self.Gem_Label_12.setTextFormat(QtCore.Qt.PlainText)
        self.Gem_Label_12.setObjectName("Gem_Label_12")
        self.gridlayout5.addWidget(self.Gem_Label_12,14,0,1,1)

        self.Type_12 = SearchingCombo(self.GroupItemFrame)
        self.Type_12.setObjectName("Type_12")
        self.gridlayout5.addWidget(self.Type_12,14,1,1,1)

        self.Amount_Edit_12 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Amount_Edit_12.setObjectName("Amount_Edit_12")
        self.gridlayout5.addWidget(self.Amount_Edit_12,14,2,1,1)

        self.Effect_12 = SearchingCombo(self.GroupItemFrame)
        self.Effect_12.setEditable(True)
        self.Effect_12.setObjectName("Effect_12")
        self.gridlayout5.addWidget(self.Effect_12,14,3,1,1)

        self.Requirement_12 = QtGui.QLineEdit(self.GroupItemFrame)
        self.Requirement_12.setObjectName("Requirement_12")
        self.gridlayout5.addWidget(self.Requirement_12,14,4,1,3)

        spacerItem18 = QtGui.QSpacerItem(5,5,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem18,8,0,7,3)

        spacerItem19 = QtGui.QSpacerItem(5,5,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem19,8,3,1,4)

        spacerItem20 = QtGui.QSpacerItem(5,5,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem20,9,3,1,4)

        self.ItemImbueLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemImbueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ItemImbueLabel.setObjectName("ItemImbueLabel")
        self.gridlayout5.addWidget(self.ItemImbueLabel,10,3,1,2)

        self.ItemImbue = QtGui.QLabel(self.GroupItemFrame)
        self.ItemImbue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ItemImbue.setObjectName("ItemImbue")
        self.gridlayout5.addWidget(self.ItemImbue,10,5,1,1)

        self.ItemImbueTotal = QtGui.QLabel(self.GroupItemFrame)
        self.ItemImbueTotal.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ItemImbueTotal.setObjectName("ItemImbueTotal")
        self.gridlayout5.addWidget(self.ItemImbueTotal,10,6,1,1)

        self.ItemOverchargeLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemOverchargeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ItemOverchargeLabel.setObjectName("ItemOverchargeLabel")
        self.gridlayout5.addWidget(self.ItemOverchargeLabel,11,3,1,2)

        self.ItemOvercharge = QtGui.QLabel(self.GroupItemFrame)
        self.ItemOvercharge.setAlignment(QtCore.Qt.AlignCenter)
        self.ItemOvercharge.setObjectName("ItemOvercharge")
        self.gridlayout5.addWidget(self.ItemOvercharge,11,5,1,2)

        self.ItemCostLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemCostLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ItemCostLabel.setObjectName("ItemCostLabel")
        self.gridlayout5.addWidget(self.ItemCostLabel,12,3,1,2)

        self.ItemCost = QtGui.QLabel(self.GroupItemFrame)
        self.ItemCost.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ItemCost.setObjectName("ItemCost")
        self.gridlayout5.addWidget(self.ItemCost,12,5,1,2)

        self.ItemPriceLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemPriceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ItemPriceLabel.setObjectName("ItemPriceLabel")
        self.gridlayout5.addWidget(self.ItemPriceLabel,13,3,1,2)

        self.ItemPrice = QtGui.QLabel(self.GroupItemFrame)
        self.ItemPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ItemPrice.setObjectName("ItemPrice")
        self.gridlayout5.addWidget(self.ItemPrice,13,5,1,2)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.ItemUtilityLabel = QtGui.QLabel(self.GroupItemFrame)
        self.ItemUtilityLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ItemUtilityLabel.setObjectName("ItemUtilityLabel")
        self.hboxlayout1.addWidget(self.ItemUtilityLabel)

        self.ItemUtility = QtGui.QLabel(self.GroupItemFrame)
        self.ItemUtility.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ItemUtility.setObjectName("ItemUtility")
        self.hboxlayout1.addWidget(self.ItemUtility)
        self.gridlayout5.addLayout(self.hboxlayout1,14,8,1,1)

        spacerItem21 = QtGui.QSpacerItem(20,5,QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem21,14,9,1,1)
        self.vboxlayout.addWidget(self.GroupItemFrame)
        self.gridlayout.addLayout(self.vboxlayout,2,0,1,7)
        B_SC.setCentralWidget(self.ScWinFrame)
        self.LabelCharName.setBuddy(self.CharName)
        self.LabelOutfitName.setBuddy(self.OutfitName)
        self.ItemLevelLabel.setBuddy(self.ItemLevel)
        self.ItemNameLabel.setBuddy(self.ItemNameCombo)

        self.retranslateUi(B_SC)
        QtCore.QMetaObject.connectSlotsByName(B_SC)
        B_SC.setTabOrder(self.CharName,self.Realm)
        B_SC.setTabOrder(self.Realm,self.CharClass)
        B_SC.setTabOrder(self.CharClass,self.CharRace)
        B_SC.setTabOrder(self.CharRace,self.CharLevel)
        B_SC.setTabOrder(self.CharLevel,self.OutfitName)
        B_SC.setTabOrder(self.OutfitName,self.PieceTab)
        B_SC.setTabOrder(self.PieceTab,self.ItemLevel)
        B_SC.setTabOrder(self.ItemLevel,self.ItemLevelButton)
        B_SC.setTabOrder(self.ItemLevelButton,self.QualEdit)
        B_SC.setTabOrder(self.QualEdit,self.QualDrop)
        B_SC.setTabOrder(self.QualDrop,self.Bonus_Edit)
        B_SC.setTabOrder(self.Bonus_Edit,self.AFDPS_Edit)
        B_SC.setTabOrder(self.AFDPS_Edit,self.Speed_Edit)
        B_SC.setTabOrder(self.Speed_Edit,self.ItemNameCombo)
        B_SC.setTabOrder(self.ItemNameCombo,self.Equipped)
        B_SC.setTabOrder(self.Equipped,self.Type_1)
        B_SC.setTabOrder(self.Type_1,self.Amount_Edit_1)
        B_SC.setTabOrder(self.Amount_Edit_1,self.Amount_Drop_1)
        B_SC.setTabOrder(self.Amount_Drop_1,self.Effect_1)
        B_SC.setTabOrder(self.Effect_1,self.Makes_1)
        B_SC.setTabOrder(self.Makes_1,self.Requirement_1)
        B_SC.setTabOrder(self.Requirement_1,self.Type_2)
        B_SC.setTabOrder(self.Type_2,self.Amount_Edit_2)
        B_SC.setTabOrder(self.Amount_Edit_2,self.Amount_Drop_2)
        B_SC.setTabOrder(self.Amount_Drop_2,self.Effect_2)
        B_SC.setTabOrder(self.Effect_2,self.Makes_2)
        B_SC.setTabOrder(self.Makes_2,self.Requirement_2)
        B_SC.setTabOrder(self.Requirement_2,self.Type_3)
        B_SC.setTabOrder(self.Type_3,self.Amount_Edit_3)
        B_SC.setTabOrder(self.Amount_Edit_3,self.Amount_Drop_3)
        B_SC.setTabOrder(self.Amount_Drop_3,self.Effect_3)
        B_SC.setTabOrder(self.Effect_3,self.Makes_3)
        B_SC.setTabOrder(self.Makes_3,self.Requirement_3)
        B_SC.setTabOrder(self.Requirement_3,self.Type_4)
        B_SC.setTabOrder(self.Type_4,self.Amount_Edit_4)
        B_SC.setTabOrder(self.Amount_Edit_4,self.Amount_Drop_4)
        B_SC.setTabOrder(self.Amount_Drop_4,self.Effect_4)
        B_SC.setTabOrder(self.Effect_4,self.Makes_4)
        B_SC.setTabOrder(self.Makes_4,self.Requirement_4)
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

    def retranslateUi(self, B_SC):
        B_SC.setWindowTitle(QtGui.QApplication.translate("B_SC", "Spellcrafting Calculator", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelCharName.setText(QtGui.QApplication.translate("B_SC", "&Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelRealm.setText(QtGui.QApplication.translate("B_SC", "Realm: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelCharClass.setText(QtGui.QApplication.translate("B_SC", "Class: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelCharRace.setText(QtGui.QApplication.translate("B_SC", "Race: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelCharLevel.setText(QtGui.QApplication.translate("B_SC", "Level: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelOutfitName.setText(QtGui.QApplication.translate("B_SC", "&Outfit: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelTotalCost.setText(QtGui.QApplication.translate("B_SC", "Cost: ", None, QtGui.QApplication.UnicodeUTF8))
        self.TotalCost.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelTotalPrice.setText(QtGui.QApplication.translate("B_SC", "Price: ", None, QtGui.QApplication.UnicodeUTF8))
        self.TotalPrice.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelTotalUtility.setText(QtGui.QApplication.translate("B_SC", "Total Utility: ", None, QtGui.QApplication.UnicodeUTF8))
        self.TotalUtility.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
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
        self.AcuityLabel.setText(QtGui.QApplication.translate("B_SC", "ACU: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Acuity.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.AcuityCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.PowerLabel.setText(QtGui.QApplication.translate("B_SC", "Pow: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Power.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.PowerCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.PowerPoolLabel.setText(QtGui.QApplication.translate("B_SC", "PP%: ", None, QtGui.QApplication.UnicodeUTF8))
        self.PowerPool.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.PowerPoolCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.AFLabel.setText(QtGui.QApplication.translate("B_SC", "AF: ", None, QtGui.QApplication.UnicodeUTF8))
        self.AF.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.AFCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.HitsLabel.setText(QtGui.QApplication.translate("B_SC", "Hits: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Hits.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.HitsCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.BodyLabel.setText(QtGui.QApplication.translate("B_SC", "Body: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Body.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.BodyCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.ColdLabel.setText(QtGui.QApplication.translate("B_SC", "Cold: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Cold.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.ColdCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.HeatLabel.setText(QtGui.QApplication.translate("B_SC", "Heat: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Heat.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.HeatCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.EnergyLabel.setText(QtGui.QApplication.translate("B_SC", "Energy: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Energy.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.EnergyCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.MatterLabel.setText(QtGui.QApplication.translate("B_SC", "Matter: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Matter.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.MatterCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.SpiritLabel.setText(QtGui.QApplication.translate("B_SC", "Spirit: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Spirit.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.SpiritCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.CrushLabel.setText(QtGui.QApplication.translate("B_SC", "Crush: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Crush.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.CrushCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.ThrustLabel.setText(QtGui.QApplication.translate("B_SC", "Thrust: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Thrust.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.ThrustCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.SlashLabel.setText(QtGui.QApplication.translate("B_SC", "Slash: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Slash.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.SlashCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.EssenceLabel.setText(QtGui.QApplication.translate("B_SC", "Essence: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Essence.setText(QtGui.QApplication.translate("B_SC", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.EssenceCap.setText(QtGui.QApplication.translate("B_SC", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemLevelLabel.setText(QtGui.QApplication.translate("B_SC", "&Level: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemLevelButton.setText(QtGui.QApplication.translate("B_SC", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemQualityLabel.setText(QtGui.QApplication.translate("B_SC", "Quality: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemBonusLabel.setText(QtGui.QApplication.translate("B_SC", "Bonus: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemAFDPSLabel.setText(QtGui.QApplication.translate("B_SC", "AF/DPS: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemSpeedLabel.setText(QtGui.QApplication.translate("B_SC", "Speed: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemNameLabel.setText(QtGui.QApplication.translate("B_SC", "&Item: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Equipped.setText(QtGui.QApplication.translate("B_SC", "Equi&pped", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemType.setText(QtGui.QApplication.translate("B_SC", " Type", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemAmount.setText(QtGui.QApplication.translate("B_SC", " Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemEffect.setText(QtGui.QApplication.translate("B_SC", " Effect", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemMakes.setText(QtGui.QApplication.translate("B_SC", " Makes", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelRequirement.setText(QtGui.QApplication.translate("B_SC", " Requirement", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemPoints.setText(QtGui.QApplication.translate("B_SC", "Points", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemCost.setText(QtGui.QApplication.translate("B_SC", "Unit Cost", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelGemName.setText(QtGui.QApplication.translate("B_SC", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_1.setText(QtGui.QApplication.translate("B_SC", "Slot &1: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Points_1.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.Cost_1.setText(QtGui.QApplication.translate("B_SC", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_2.setText(QtGui.QApplication.translate("B_SC", "Slot &2: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Points_2.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.Cost_2.setText(QtGui.QApplication.translate("B_SC", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_3.setText(QtGui.QApplication.translate("B_SC", "Slot &3: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Points_3.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.Cost_3.setText(QtGui.QApplication.translate("B_SC", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_4.setText(QtGui.QApplication.translate("B_SC", "Slot &4: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Points_4.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.Cost_4.setText(QtGui.QApplication.translate("B_SC", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_5.setText(QtGui.QApplication.translate("B_SC", "Slot &5: ", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelRequirement2.setText(QtGui.QApplication.translate("B_SC", "(Requirement)", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_6.setText(QtGui.QApplication.translate("B_SC", "Slot &6: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_7.setText(QtGui.QApplication.translate("B_SC", "Slot &7: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_8.setText(QtGui.QApplication.translate("B_SC", "Slot &8: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_9.setText(QtGui.QApplication.translate("B_SC", "Slot &9: ", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_10.setText(QtGui.QApplication.translate("B_SC", "Slot 1&0:", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_11.setText(QtGui.QApplication.translate("B_SC", "Slot 11&- ", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem_Label_12.setText(QtGui.QApplication.translate("B_SC", "Slot 12&=", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemImbueLabel.setText(QtGui.QApplication.translate("B_SC", "Imbue Points: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemImbue.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemImbueTotal.setText(QtGui.QApplication.translate("B_SC", " / 0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemOverchargeLabel.setText(QtGui.QApplication.translate("B_SC", "Overcharge: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemOvercharge.setText(QtGui.QApplication.translate("B_SC", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemCostLabel.setText(QtGui.QApplication.translate("B_SC", "Item Cost: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemPriceLabel.setText(QtGui.QApplication.translate("B_SC", "Item Price: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemUtilityLabel.setText(QtGui.QApplication.translate("B_SC", "Utility: ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItemUtility.setText(QtGui.QApplication.translate("B_SC", "0.0", None, QtGui.QApplication.UnicodeUTF8))

from SearchingCombo import SearchingCombo
from MultiTabBar import MultiTabBar, MultiTabFrame
from GroupFrame import GroupFrame
