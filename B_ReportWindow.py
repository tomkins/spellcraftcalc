# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportWindow.ui4'
#
# Created: Wed Sep 06 17:41:33 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_ReportWindow(object):
    def setupUi(self, B_ReportWindow):
        B_ReportWindow.setObjectName("B_ReportWindow")
        B_ReportWindow.resize(QtCore.QSize(QtCore.QRect(0,0,573,480).size()).expandedTo(B_ReportWindow.minimumSizeHint()))

        self.ReportText = QtGui.QTextBrowser(B_ReportWindow)
        self.ReportText.setGeometry(QtCore.QRect(10,9,569,430))
        self.ReportText.setObjectName("ReportText")

        self.PushButton1 = QtGui.QPushButton(B_ReportWindow)
        self.PushButton1.setGeometry(QtCore.QRect(35,447,93,26))
        self.PushButton1.setObjectName("PushButton1")

        self.PushButton1_2 = QtGui.QPushButton(B_ReportWindow)
        self.PushButton1_2.setGeometry(QtCore.QRect(149,447,93,26))
        self.PushButton1_2.setObjectName("PushButton1_2")

        self.PushButton2 = QtGui.QPushButton(B_ReportWindow)
        self.PushButton2.setGeometry(QtCore.QRect(446,448,93,26))
        self.PushButton2.setObjectName("PushButton2")

        self.MMLabel = QtGui.QLabel(B_ReportWindow)
        self.MMLabel.setGeometry(QtCore.QRect(298,451,91,16))
        self.MMLabel.setObjectName("MMLabel")

        self.MatMultiplier = QtGui.QSpinBox(B_ReportWindow)
        self.MatMultiplier.setGeometry(QtCore.QRect(256,449,37,21))
        self.MatMultiplier.setMinimum(1)
        self.MatMultiplier.setProperty("value",QtCore.QVariant(1))
        self.MatMultiplier.setObjectName("MatMultiplier")

        self.retranslateUi(B_ReportWindow)

    def retranslateUi(self, B_ReportWindow):
        B_ReportWindow.setWindowTitle(QtGui.QApplication.translate("B_ReportWindow", "B_ReportWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.PushButton1.setText(QtGui.QApplication.translate("B_ReportWindow", "Save As HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.PushButton1_2.setText(QtGui.QApplication.translate("B_ReportWindow", "Save As Text", None, QtGui.QApplication.UnicodeUTF8))
        self.PushButton2.setText(QtGui.QApplication.translate("B_ReportWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.MMLabel.setText(QtGui.QApplication.translate("B_ReportWindow", "Materials Multiplier", None, QtGui.QApplication.UnicodeUTF8))
