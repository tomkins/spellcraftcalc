# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportWindow.ui'
#
# Created: Thu Oct  5 16:47:49 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui, Qt3Support

class Ui_B_ReportWindow(object):
    def setupUi(self, B_ReportWindow):
        B_ReportWindow.setObjectName("B_ReportWindow")
        B_ReportWindow.resize(QtCore.QSize(QtCore.QRect(0,0,566,565).size()).expandedTo(B_ReportWindow.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(B_ReportWindow)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.ReportText = QtGui.QTextBrowser(B_ReportWindow)
        self.ReportText.setObjectName("ReportText")
        self.vboxlayout1.addWidget(self.ReportText)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.PushButton1 = QtGui.QPushButton(B_ReportWindow)
        self.PushButton1.setObjectName("PushButton1")
        self.hboxlayout.addWidget(self.PushButton1)

        self.PushButton1_2 = QtGui.QPushButton(B_ReportWindow)
        self.PushButton1_2.setObjectName("PushButton1_2")
        self.hboxlayout.addWidget(self.PushButton1_2)

        spacerItem = QtGui.QSpacerItem(16,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.MatMultiplier = QtGui.QSpinBox(B_ReportWindow)
        self.MatMultiplier.setMinimum(1)
        self.MatMultiplier.setProperty("value",QtCore.QVariant(1))
        self.MatMultiplier.setObjectName("MatMultiplier")
        self.hboxlayout.addWidget(self.MatMultiplier)

        self.MMLabel = QtGui.QLabel(B_ReportWindow)
        self.MMLabel.setObjectName("MMLabel")
        self.hboxlayout.addWidget(self.MMLabel)
        self.vboxlayout1.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)

        self.PushButton2 = QtGui.QPushButton(B_ReportWindow)
        self.PushButton2.setObjectName("PushButton2")
        self.hboxlayout1.addWidget(self.PushButton2)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(B_ReportWindow)
        QtCore.QMetaObject.connectSlotsByName(B_ReportWindow)

    def retranslateUi(self, B_ReportWindow):
        B_ReportWindow.setWindowTitle(QtGui.QApplication.translate("B_ReportWindow", "B_ReportWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.PushButton1.setText(QtGui.QApplication.translate("B_ReportWindow", "Save As HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.PushButton1_2.setText(QtGui.QApplication.translate("B_ReportWindow", "Save As Text", None, QtGui.QApplication.UnicodeUTF8))
        self.MMLabel.setText(QtGui.QApplication.translate("B_ReportWindow", "Materials Multiplier", None, QtGui.QApplication.UnicodeUTF8))
        self.PushButton2.setText(QtGui.QApplication.translate("B_ReportWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
