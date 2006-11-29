# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ItemLevel.ui'
#
# Created: Tue Nov 28 23:19:06 2006
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_ItemLevel(object):
    def setupUi(self, B_ItemLevel):
        B_ItemLevel.setObjectName("B_ItemLevel")
        B_ItemLevel.resize(QtCore.QSize(QtCore.QRect(0,0,250,158).size()).expandedTo(B_ItemLevel.minimumSizeHint()))

        self.ButtonGroup3 = QtGui.QGroupBox(B_ItemLevel)
        self.ButtonGroup3.setGeometry(QtCore.QRect(6,6,117,111))
        self.ButtonGroup3.setObjectName("ButtonGroup3")

        self.Armor = QtGui.QRadioButton(self.ButtonGroup3)
        self.Armor.setGeometry(QtCore.QRect(5,2,85,20))
        self.Armor.setChecked(True)
        self.Armor.setObjectName("Armor")

        self.ClothArmor = QtGui.QRadioButton(self.ButtonGroup3)
        self.ClothArmor.setGeometry(QtCore.QRect(5,23,85,20))
        self.ClothArmor.setObjectName("ClothArmor")

        self.Weapon = QtGui.QRadioButton(self.ButtonGroup3)
        self.Weapon.setGeometry(QtCore.QRect(3,45,85,20))
        self.Weapon.setObjectName("Weapon")

        self.Shield = QtGui.QRadioButton(self.ButtonGroup3)
        self.Shield.setGeometry(QtCore.QRect(5,66,85,20))
        self.Shield.setObjectName("Shield")

        self.ReinforcedShield = QtGui.QRadioButton(self.ButtonGroup3)
        self.ReinforcedShield.setGeometry(QtCore.QRect(5,87,108,20))
        self.ReinforcedShield.setObjectName("ReinforcedShield")

        self.LevelLabel = QtGui.QLabel(B_ItemLevel)
        self.LevelLabel.setGeometry(QtCore.QRect(130,10,45,16))
        self.LevelLabel.setObjectName("LevelLabel")

        self.Level = QtGui.QLineEdit(B_ItemLevel)
        self.Level.setGeometry(QtCore.QRect(185,7,60,22))
        self.Level.setObjectName("Level")

        self.AFDPSLabel = QtGui.QLabel(B_ItemLevel)
        self.AFDPSLabel.setGeometry(QtCore.QRect(130,53,45,16))
        self.AFDPSLabel.setObjectName("AFDPSLabel")

        self.AFDPS = QtGui.QLineEdit(B_ItemLevel)
        self.AFDPS.setGeometry(QtCore.QRect(185,50,60,22))
        self.AFDPS.setObjectName("AFDPS")

        self.ShieldType = SearchingCombo(B_ItemLevel)
        self.ShieldType.setGeometry(QtCore.QRect(135,93,110,22))
        self.ShieldType.setObjectName("ShieldType")

        self.OK = QtGui.QPushButton(B_ItemLevel)
        self.OK.setGeometry(QtCore.QRect(11,124,58,26))
        self.OK.setObjectName("OK")

        self.Cancel = QtGui.QPushButton(B_ItemLevel)
        self.Cancel.setGeometry(QtCore.QRect(187,124,58,26))
        self.Cancel.setObjectName("Cancel")

        self.retranslateUi(B_ItemLevel)

    def retranslateUi(self, B_ItemLevel):
        B_ItemLevel.setWindowTitle(QtGui.QApplication.translate("B_ItemLevel", "Item Level", None, QtGui.QApplication.UnicodeUTF8))
        self.Armor.setText(QtGui.QApplication.translate("B_ItemLevel", "Armor", None, QtGui.QApplication.UnicodeUTF8))
        self.ClothArmor.setText(QtGui.QApplication.translate("B_ItemLevel", "Cloth Armor", None, QtGui.QApplication.UnicodeUTF8))
        self.Weapon.setText(QtGui.QApplication.translate("B_ItemLevel", "Weapon", None, QtGui.QApplication.UnicodeUTF8))
        self.Shield.setText(QtGui.QApplication.translate("B_ItemLevel", "Shield", None, QtGui.QApplication.UnicodeUTF8))
        self.ReinforcedShield.setText(QtGui.QApplication.translate("B_ItemLevel", "Reinforced Sheild", None, QtGui.QApplication.UnicodeUTF8))
        self.LevelLabel.setText(QtGui.QApplication.translate("B_ItemLevel", "Level:", None, QtGui.QApplication.UnicodeUTF8))
        self.AFDPSLabel.setText(QtGui.QApplication.translate("B_ItemLevel", "AF/DPS:", None, QtGui.QApplication.UnicodeUTF8))
        self.OK.setText(QtGui.QApplication.translate("B_ItemLevel", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancel.setText(QtGui.QApplication.translate("B_ItemLevel", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

from SearchingCombo import SearchingCombo
