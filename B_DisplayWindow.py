# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DisplayWindow.ui'
#
# Created: Fri Sep 29 17:30:13 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_DisplayWindow(object):
    def setupUi(self, B_DisplayWindow):
        B_DisplayWindow.setObjectName("B_DisplayWindow")
        B_DisplayWindow.resize(QtCore.QSize(QtCore.QRect(0,0,238,310).size()).expandedTo(B_DisplayWindow.minimumSizeHint()))

        self.PushButton1 = QtGui.QPushButton(B_DisplayWindow)
        self.PushButton1.setGeometry(QtCore.QRect(69,270,93,26))
        self.PushButton1.setObjectName("PushButton1")

        self.DisplayText = QtGui.QListWidget(B_DisplayWindow)
        self.DisplayText.setGeometry(QtCore.QRect(8,4,221,256))
        self.DisplayText.setObjectName("DisplayText")

        self.retranslateUi(B_DisplayWindow)

    def retranslateUi(self, B_DisplayWindow):
        self.PushButton1.setText(QtGui.QApplication.translate("B_DisplayWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
