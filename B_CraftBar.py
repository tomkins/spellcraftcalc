# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CraftBar.ui'
#
# Created: Fri Sep 29 17:30:17 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_CraftBar(object):
    def setupUi(self, B_CraftBar):
        B_CraftBar.setObjectName("B_CraftBar")
        B_CraftBar.resize(QtCore.QSize(QtCore.QRect(0,0,490,451).size()).expandedTo(B_CraftBar.minimumSizeHint()))

        self.TextLabel1 = QtGui.QLabel(B_CraftBar)
        self.TextLabel1.setGeometry(QtCore.QRect(22,17,103,16))
        self.TextLabel1.setObjectName("TextLabel1")

        self.PathSelectButton = QtGui.QPushButton(B_CraftBar)
        self.PathSelectButton.setGeometry(QtCore.QRect(425,13,28,26))
        self.PathSelectButton.setObjectName("PathSelectButton")

        self.TextLabel2 = QtGui.QLabel(B_CraftBar)
        self.TextLabel2.setGeometry(QtCore.QRect(174,39,191,16))
        self.TextLabel2.setObjectName("TextLabel2")

        self.DaocPath = QtGui.QLineEdit(B_CraftBar)
        self.DaocPath.setGeometry(QtCore.QRect(129,14,295,22))
        self.DaocPath.setObjectName("DaocPath")

        self.GroupBox20 = QtGui.QGroupBox(B_CraftBar)
        self.GroupBox20.setGeometry(QtCore.QRect(10,57,217,243))
        self.GroupBox20.setObjectName("GroupBox20")

        self.TextLabel4 = QtGui.QLabel(self.GroupBox20)
        self.TextLabel4.setGeometry(QtCore.QRect(38,20,134,16))
        self.TextLabel4.setObjectName("TextLabel4")

        self.CharList = QtGui.QTableView(self.GroupBox20)
        self.CharList.setGeometry(QtCore.QRect(5,44,205,193))
        self.CharList.setObjectName("CharList")

        self.TextLabel14 = QtGui.QLabel(B_CraftBar)
        self.TextLabel14.setGeometry(QtCore.QRect(39,304,154,41))
        self.TextLabel14.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        self.TextLabel14.setObjectName("TextLabel14")

        self.GroupBox21 = QtGui.QGroupBox(B_CraftBar)
        self.GroupBox21.setGeometry(QtCore.QRect(229,274,261,143))
        self.GroupBox21.setObjectName("GroupBox21")

        self.TextLabel9 = QtGui.QLabel(self.GroupBox21)
        self.TextLabel9.setGeometry(QtCore.QRect(5,6,250,134))
        self.TextLabel9.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignLeft)
        self.TextLabel9.setObjectName("TextLabel9")

        self.GroupBox19 = QtGui.QGroupBox(B_CraftBar)
        self.GroupBox19.setGeometry(QtCore.QRect(254,57,213,189))
        self.GroupBox19.setObjectName("GroupBox19")

        self.TextLabel1_2 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel1_2.setGeometry(QtCore.QRect(69,9,73,16))
        self.TextLabel1_2.setObjectName("TextLabel1_2")

        self.HotbarNum = QtGui.QSpinBox(self.GroupBox19)
        self.HotbarNum.setGeometry(QtCore.QRect(145,103,54,21))
        self.HotbarNum.setMaximum(30)
        self.HotbarNum.setMinimum(1)
        self.HotbarNum.setObjectName("HotbarNum")

        self.TextLabel10 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel10.setGeometry(QtCore.QRect(12,152,59,13))
        self.TextLabel10.setObjectName("TextLabel10")

        self.NumGems = QtGui.QLabel(self.GroupBox19)
        self.NumGems.setGeometry(QtCore.QRect(164,168,28,16))
        self.NumGems.setObjectName("NumGems")

        self.EndPos = QtGui.QLabel(self.GroupBox19)
        self.EndPos.setGeometry(QtCore.QRect(139,150,26,16))
        self.EndPos.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.EndPos.setObjectName("EndPos")

        self.EndBar = QtGui.QLabel(self.GroupBox19)
        self.EndBar.setGeometry(QtCore.QRect(73,150,22,16))
        self.EndBar.setObjectName("EndBar")

        self.TextLabel15 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel15.setGeometry(QtCore.QRect(11,168,152,16))
        self.TextLabel15.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.TextLabel15.setObjectName("TextLabel15")

        self.TextLabel8 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel8.setGeometry(QtCore.QRect(5,129,132,16))
        self.TextLabel8.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.TextLabel8.setObjectName("TextLabel8")

        self.TextLabel7 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel7.setGeometry(QtCore.QRect(40,105,97,16))
        self.TextLabel7.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.TextLabel7.setObjectName("TextLabel7")

        self.HotbarPos = QtGui.QSpinBox(self.GroupBox19)
        self.HotbarPos.setGeometry(QtCore.QRect(145,127,54,21))
        self.HotbarPos.setMaximum(10)
        self.HotbarPos.setMinimum(1)
        self.HotbarPos.setObjectName("HotbarPos")

        self.TextLabel11 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel11.setGeometry(QtCore.QRect(94,150,44,16))
        self.TextLabel11.setObjectName("TextLabel11")

        self.ArmsSelect = QtGui.QCheckBox(self.GroupBox19)
        self.ArmsSelect.setGeometry(QtCore.QRect(9,47,47,17))
        self.ArmsSelect.setObjectName("ArmsSelect")

        self.HeadSelect = QtGui.QCheckBox(self.GroupBox19)
        self.HeadSelect.setGeometry(QtCore.QRect(9,66,50,17))
        self.HeadSelect.setObjectName("HeadSelect")

        self.LegsSelect = QtGui.QCheckBox(self.GroupBox19)
        self.LegsSelect.setGeometry(QtCore.QRect(68,28,49,17))
        self.LegsSelect.setObjectName("LegsSelect")

        self.HandsSelect = QtGui.QCheckBox(self.GroupBox19)
        self.HandsSelect.setGeometry(QtCore.QRect(68,47,54,17))
        self.HandsSelect.setObjectName("HandsSelect")

        self.FeetSelect = QtGui.QCheckBox(self.GroupBox19)
        self.FeetSelect.setGeometry(QtCore.QRect(68,66,45,17))
        self.FeetSelect.setObjectName("FeetSelect")

        self.RangedSelect = QtGui.QCheckBox(self.GroupBox19)
        self.RangedSelect.setGeometry(QtCore.QRect(68,85,64,17))
        self.RangedSelect.setObjectName("RangedSelect")

        self.RHSelect = QtGui.QCheckBox(self.GroupBox19)
        self.RHSelect.setGeometry(QtCore.QRect(124,28,78,17))
        self.RHSelect.setObjectName("RHSelect")

        self.LHSelect = QtGui.QCheckBox(self.GroupBox19)
        self.LHSelect.setGeometry(QtCore.QRect(124,47,84,17))
        self.LHSelect.setObjectName("LHSelect")

        self.THSelect = QtGui.QCheckBox(self.GroupBox19)
        self.THSelect.setGeometry(QtCore.QRect(124,66,71,17))
        self.THSelect.setObjectName("THSelect")

        self.ChestSelect = QtGui.QCheckBox(self.GroupBox19)
        self.ChestSelect.setGeometry(QtCore.QRect(9,28,50,17))
        self.ChestSelect.setObjectName("ChestSelect")

        self.LoadGemsButton = QtGui.QPushButton(B_CraftBar)
        self.LoadGemsButton.setGeometry(QtCore.QRect(311,246,99,26))
        self.LoadGemsButton.setObjectName("LoadGemsButton")

        self.PushButton19 = QtGui.QPushButton(B_CraftBar)
        self.PushButton19.setGeometry(QtCore.QRect(198,422,99,26))
        self.PushButton19.setObjectName("PushButton19")

        self.retranslateUi(B_CraftBar)
        QtCore.QObject.connect(self.PushButton19,QtCore.SIGNAL("clicked()"),B_CraftBar.accept)
        QtCore.QMetaObject.connectSlotsByName(B_CraftBar)

    def retranslateUi(self, B_CraftBar):
        B_CraftBar.setWindowTitle(QtGui.QApplication.translate("B_CraftBar", "Craft Bar Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1.setText(QtGui.QApplication.translate("B_CraftBar", "Path to DAoC Folder:", None, QtGui.QApplication.UnicodeUTF8))
        self.PathSelectButton.setText(QtGui.QApplication.translate("B_CraftBar", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2.setText(QtGui.QApplication.translate("B_CraftBar", "(i.e. C:\\Mythic\\[Atlantis, Camelot, Isles])", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox20.setTitle(QtGui.QApplication.translate("B_CraftBar", "Character", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel4.setText(QtGui.QApplication.translate("B_CraftBar", "Select Character to Modify:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel14.setText(QtGui.QApplication.translate("B_CraftBar", "You must be logged out of \n"
        "the selected character for \n"
        "the changes to be made", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel9.setText(QtGui.QApplication.translate("B_CraftBar", "This dialog lets you automatically set up hotbars for \n"
        "crafting gems. It takes all \"non-finished\" gems and \n"
        "places them in order on your hotbars starting at the \n"
        "bar and position you specify. It will place all the gems \n"
        "consecutively, so make sure you do not have \n"
        "anything on your bars in that range. If you do not \n"
        "leave enough space, it will error w/o changing your \n"
        "bars. A backup copy of your character will be saved \n"
        "in [charname]_bak-[server].ini in your DAoC folder.\n"
        "Removing the _bak will restore your settings.", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox19.setTitle(QtGui.QApplication.translate("B_CraftBar", "Hotbar", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2.setText(QtGui.QApplication.translate("B_CraftBar", "Gems to Load:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel10.setText(QtGui.QApplication.translate("B_CraftBar", "Ending Bar:", None, QtGui.QApplication.UnicodeUTF8))
        self.NumGems.setText(QtGui.QApplication.translate("B_CraftBar", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.EndPos.setText(QtGui.QApplication.translate("B_CraftBar", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.EndBar.setText(QtGui.QApplication.translate("B_CraftBar", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel15.setText(QtGui.QApplication.translate("B_CraftBar", "Total Number of Gems to Load:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel8.setText(QtGui.QApplication.translate("B_CraftBar", "Hotbar Position to Start At:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel7.setText(QtGui.QApplication.translate("B_CraftBar", "Hotbar # to Start At:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel11.setText(QtGui.QApplication.translate("B_CraftBar", "Position:", None, QtGui.QApplication.UnicodeUTF8))
        self.ArmsSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Arms", None, QtGui.QApplication.UnicodeUTF8))
        self.HeadSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Head", None, QtGui.QApplication.UnicodeUTF8))
        self.LegsSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Legs", None, QtGui.QApplication.UnicodeUTF8))
        self.HandsSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Hands", None, QtGui.QApplication.UnicodeUTF8))
        self.FeetSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Feet", None, QtGui.QApplication.UnicodeUTF8))
        self.RangedSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Ranged", None, QtGui.QApplication.UnicodeUTF8))
        self.RHSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Right Hand", None, QtGui.QApplication.UnicodeUTF8))
        self.LHSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Left Hand", None, QtGui.QApplication.UnicodeUTF8))
        self.THSelect.setText(QtGui.QApplication.translate("B_CraftBar", "2 Handed", None, QtGui.QApplication.UnicodeUTF8))
        self.ChestSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Chest", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadGemsButton.setText(QtGui.QApplication.translate("B_CraftBar", "Load Gems", None, QtGui.QApplication.UnicodeUTF8))
        self.PushButton19.setText(QtGui.QApplication.translate("B_CraftBar", "Close", None, QtGui.QApplication.UnicodeUTF8))
