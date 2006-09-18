# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CraftWindow.ui4'
#
# Created: Wed Sep 06 17:41:28 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_CraftWindow(object):
    def setupUi(self, B_CraftWindow):
        B_CraftWindow.setObjectName("B_CraftWindow")
        B_CraftWindow.resize(QtCore.QSize(QtCore.QRect(0,0,523,373).size()).expandedTo(B_CraftWindow.minimumSizeHint()))

        self.TextLabel8 = QtGui.QLabel(B_CraftWindow)
        self.TextLabel8.setGeometry(QtCore.QRect(365,338,57,16))
        self.TextLabel8.setObjectName("TextLabel8")

        self.Close = QtGui.QPushButton(B_CraftWindow)
        self.Close.setGeometry(QtCore.QRect(228,336,84,29))
        self.Close.setObjectName("Close")

        self.TotalCost = QtGui.QLabel(B_CraftWindow)
        self.TotalCost.setGeometry(QtCore.QRect(421,338,103,16))
        self.TotalCost.setObjectName("TotalCost")

        self.GroupBox1 = QtGui.QGroupBox(B_CraftWindow)
        self.GroupBox1.setGeometry(QtCore.QRect(9,7,523,324))
        self.GroupBox1.setObjectName("GroupBox1")

        self.TextLabel1 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel1.setGeometry(QtCore.QRect(15,20,36,16))
        self.TextLabel1.setObjectName("TextLabel1")

        self.TextLabel5 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel5.setGeometry(QtCore.QRect(323,20,50,16))
        self.TextLabel5.setObjectName("TextLabel5")

        self.TextLabel6 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel6.setGeometry(QtCore.QRect(382,20,46,16))
        self.TextLabel6.setObjectName("TextLabel6")

        self.TextLabel7 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel7.setGeometry(QtCore.QRect(438,20,30,16))
        self.TextLabel7.setObjectName("TextLabel7")

        self.Gem1Cost = QtGui.QLabel(self.GroupBox1)
        self.Gem1Cost.setGeometry(QtCore.QRect(442,41,73,21))
        self.Gem1Cost.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.Gem1Cost.setObjectName("Gem1Cost")

        self.Gem3Cost = QtGui.QLabel(self.GroupBox1)
        self.Gem3Cost.setGeometry(QtCore.QRect(442,88,73,21))
        self.Gem3Cost.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.Gem3Cost.setObjectName("Gem3Cost")

        self.Gem3Name = QtGui.QLabel(self.GroupBox1)
        self.Gem3Name.setGeometry(QtCore.QRect(138,88,163,21))
        self.Gem3Name.setObjectName("Gem3Name")

        self.Gem4Name = QtGui.QLabel(self.GroupBox1)
        self.Gem4Name.setGeometry(QtCore.QRect(138,112,163,21))
        self.Gem4Name.setObjectName("Gem4Name")

        self.Gem3Time = QtGui.QLineEdit(self.GroupBox1)
        self.Gem3Time.setGeometry(QtCore.QRect(382,88,47,21))
        self.Gem3Time.setObjectName("Gem3Time")

        self.Gem4Time = QtGui.QLineEdit(self.GroupBox1)
        self.Gem4Time.setGeometry(QtCore.QRect(382,111,47,21))
        self.Gem4Time.setObjectName("Gem4Time")

        self.TextLabel2 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel2.setGeometry(QtCore.QRect(108,20,36,16))
        self.TextLabel2.setObjectName("TextLabel2")

        self.Gem2Done = QtGui.QCheckBox(self.GroupBox1)
        self.Gem2Done.setGeometry(QtCore.QRect(15,64,59,21))
        self.Gem2Done.setObjectName("Gem2Done")

        self.Gem3Done = QtGui.QCheckBox(self.GroupBox1)
        self.Gem3Done.setGeometry(QtCore.QRect(15,88,57,21))
        self.Gem3Done.setObjectName("Gem3Done")

        self.Gem4Done = QtGui.QCheckBox(self.GroupBox1)
        self.Gem4Done.setGeometry(QtCore.QRect(15,112,57,21))
        self.Gem4Done.setObjectName("Gem4Done")

        self.Gem1Qua = QtGui.QLabel(self.GroupBox1)
        self.Gem1Qua.setGeometry(QtCore.QRect(103,41,28,21))
        self.Gem1Qua.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Gem1Qua.setObjectName("Gem1Qua")

        self.Gem3Remakes = QtGui.QSpinBox(self.GroupBox1)
        self.Gem3Remakes.setGeometry(QtCore.QRect(321,88,54,21))
        self.Gem3Remakes.setObjectName("Gem3Remakes")

        self.Gem4Remakes = QtGui.QSpinBox(self.GroupBox1)
        self.Gem4Remakes.setGeometry(QtCore.QRect(321,112,54,21))
        self.Gem4Remakes.setObjectName("Gem4Remakes")

        self.Gem2Qua = QtGui.QLabel(self.GroupBox1)
        self.Gem2Qua.setGeometry(QtCore.QRect(103,64,28,21))
        self.Gem2Qua.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Gem2Qua.setObjectName("Gem2Qua")

        self.Gem3Qua = QtGui.QLabel(self.GroupBox1)
        self.Gem3Qua.setGeometry(QtCore.QRect(103,88,28,21))
        self.Gem3Qua.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Gem3Qua.setObjectName("Gem3Qua")

        self.Gem4Qua = QtGui.QLabel(self.GroupBox1)
        self.Gem4Qua.setGeometry(QtCore.QRect(103,112,28,21))
        self.Gem4Qua.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.Gem4Qua.setObjectName("Gem4Qua")

        self.Gem1Name = QtGui.QLabel(self.GroupBox1)
        self.Gem1Name.setGeometry(QtCore.QRect(138,41,163,21))
        self.Gem1Name.setObjectName("Gem1Name")

        self.Gem2Name = QtGui.QLabel(self.GroupBox1)
        self.Gem2Name.setGeometry(QtCore.QRect(138,64,163,21))
        self.Gem2Name.setObjectName("Gem2Name")

        self.Gem1Remakes = QtGui.QSpinBox(self.GroupBox1)
        self.Gem1Remakes.setGeometry(QtCore.QRect(321,41,54,21))
        self.Gem1Remakes.setObjectName("Gem1Remakes")

        self.Gem2Remakes = QtGui.QSpinBox(self.GroupBox1)
        self.Gem2Remakes.setGeometry(QtCore.QRect(321,64,54,21))
        self.Gem2Remakes.setObjectName("Gem2Remakes")

        self.Gem1Time = QtGui.QLineEdit(self.GroupBox1)
        self.Gem1Time.setGeometry(QtCore.QRect(382,41,47,21))
        self.Gem1Time.setObjectName("Gem1Time")

        self.Gem2Time = QtGui.QLineEdit(self.GroupBox1)
        self.Gem2Time.setGeometry(QtCore.QRect(382,64,47,21))
        self.Gem2Time.setObjectName("Gem2Time")

        self.Gem2Cost = QtGui.QLabel(self.GroupBox1)
        self.Gem2Cost.setGeometry(QtCore.QRect(442,64,73,21))
        self.Gem2Cost.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.Gem2Cost.setObjectName("Gem2Cost")

        self.Gem4Cost = QtGui.QLabel(self.GroupBox1)
        self.Gem4Cost.setGeometry(QtCore.QRect(442,112,73,21))
        self.Gem4Cost.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignLeft)
        self.Gem4Cost.setObjectName("Gem4Cost")

        self.Gem1Done = QtGui.QCheckBox(self.GroupBox1)
        self.Gem1Done.setGeometry(QtCore.QRect(15,41,59,21))
        self.Gem1Done.setObjectName("Gem1Done")

        self.GroupBox2_2 = QtGui.QGroupBox(self.GroupBox1)
        self.GroupBox2_2.setGeometry(QtCore.QRect(266,142,240,175))
        self.GroupBox2_2.setObjectName("GroupBox2_2")

        self.MatsUsed = QtGui.QTextEdit(self.GroupBox2_2)
        self.MatsUsed.setGeometry(QtCore.QRect(8,16,225,153))
        self.MatsUsed.setObjectName("MatsUsed")

        self.GroupBox2_2_2 = QtGui.QGroupBox(self.GroupBox1)
        self.GroupBox2_2_2.setGeometry(QtCore.QRect(13,141,240,175))
        self.GroupBox2_2_2.setObjectName("GroupBox2_2_2")

        self.MatsExpected = QtGui.QTextEdit(self.GroupBox2_2_2)
        self.MatsExpected.setGeometry(QtCore.QRect(8,16,225,153))
        self.MatsExpected.setObjectName("MatsExpected")

        self.TextLabel1_2 = QtGui.QLabel(B_CraftWindow)
        self.TextLabel1_2.setGeometry(QtCore.QRect(35,341,94,16))
        self.TextLabel1_2.setObjectName("TextLabel1_2")

        self.ExpMultiplier = QtGui.QSpinBox(B_CraftWindow)
        self.ExpMultiplier.setGeometry(QtCore.QRect(130,339,54,21))
        self.ExpMultiplier.setObjectName("ExpMultiplier")

        self.retranslateUi(B_CraftWindow)

    def retranslateUi(self, B_CraftWindow):
        B_CraftWindow.setWindowTitle(QtGui.QApplication.translate("B_CraftWindow", "Working Item Detail", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel8.setText(QtGui.QApplication.translate("B_CraftWindow", "Total Cost:", None, QtGui.QApplication.UnicodeUTF8))
        self.Close.setText(QtGui.QApplication.translate("B_CraftWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.TotalCost.setText(QtGui.QApplication.translate("B_CraftWindow", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox1.setTitle(QtGui.QApplication.translate("B_CraftWindow", "Gems", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1.setText(QtGui.QApplication.translate("B_CraftWindow", "Done:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel5.setText(QtGui.QApplication.translate("B_CraftWindow", "Remakes:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel6.setText(QtGui.QApplication.translate("B_CraftWindow", "Time (m):", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel7.setText(QtGui.QApplication.translate("B_CraftWindow", "Cost:", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem1Cost.setText(QtGui.QApplication.translate("B_CraftWindow", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem3Cost.setText(QtGui.QApplication.translate("B_CraftWindow", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem3Name.setText(QtGui.QApplication.translate("B_CraftWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem4Name.setText(QtGui.QApplication.translate("B_CraftWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem3Time.setText(QtGui.QApplication.translate("B_CraftWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem4Time.setText(QtGui.QApplication.translate("B_CraftWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2.setText(QtGui.QApplication.translate("B_CraftWindow", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem2Done.setText(QtGui.QApplication.translate("B_CraftWindow", "Gem 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem3Done.setText(QtGui.QApplication.translate("B_CraftWindow", "Gem 3:", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem4Done.setText(QtGui.QApplication.translate("B_CraftWindow", "Gem 4:", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem1Qua.setText(QtGui.QApplication.translate("B_CraftWindow", "99%", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem2Qua.setText(QtGui.QApplication.translate("B_CraftWindow", "99%", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem3Qua.setText(QtGui.QApplication.translate("B_CraftWindow", "99%", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem4Qua.setText(QtGui.QApplication.translate("B_CraftWindow", "99%", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem1Name.setText(QtGui.QApplication.translate("B_CraftWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem2Name.setText(QtGui.QApplication.translate("B_CraftWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem1Time.setText(QtGui.QApplication.translate("B_CraftWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem2Time.setText(QtGui.QApplication.translate("B_CraftWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem2Cost.setText(QtGui.QApplication.translate("B_CraftWindow", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem4Cost.setText(QtGui.QApplication.translate("B_CraftWindow", "0c", None, QtGui.QApplication.UnicodeUTF8))
        self.Gem1Done.setText(QtGui.QApplication.translate("B_CraftWindow", "Gem 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox2_2.setTitle(QtGui.QApplication.translate("B_CraftWindow", "Materials (used)", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox2_2_2.setTitle(QtGui.QApplication.translate("B_CraftWindow", "Materials (expected)", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2.setText(QtGui.QApplication.translate("B_CraftWindow", "Expected Multiplier", None, QtGui.QApplication.UnicodeUTF8))
