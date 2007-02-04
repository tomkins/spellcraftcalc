# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ethinarg.ui'
#
# Created: Sun Feb  4 01:22:30 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_Ethinarg(object):
    def setupUi(self, B_Ethinarg):
        B_Ethinarg.setObjectName("B_Ethinarg")
        B_Ethinarg.resize(QtCore.QSize(QtCore.QRect(0,0,655,547).size()).expandedTo(B_Ethinarg.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(B_Ethinarg)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.groupBox = QtGui.QGroupBox(B_Ethinarg)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.browser = QtGui.QTextBrowser(self.groupBox)
        self.browser.setObjectName("browser")
        self.vboxlayout2.addWidget(self.browser)
        self.vboxlayout1.addWidget(self.groupBox)

        self.groupBox_2 = QtGui.QGroupBox(B_Ethinarg)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setMargin(0)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)

        self.usernameBox = QtGui.QLineEdit(self.groupBox_2)
        self.usernameBox.setObjectName("usernameBox")
        self.hboxlayout.addWidget(self.usernameBox)

        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.hboxlayout.addWidget(self.label_2)

        self.passwordBox = QtGui.QLineEdit(self.groupBox_2)
        self.passwordBox.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordBox.setObjectName("passwordBox")
        self.hboxlayout.addWidget(self.passwordBox)
        self.vboxlayout4.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.hboxlayout1.addWidget(self.label_3)

        self.itemNameBox = QtGui.QLineEdit(self.groupBox_2)
        self.itemNameBox.setObjectName("itemNameBox")
        self.hboxlayout1.addWidget(self.itemNameBox)
        self.vboxlayout4.addLayout(self.hboxlayout1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.hboxlayout2.addWidget(self.label_4)

        self.slotCombo = QtGui.QComboBox(self.groupBox_2)
        self.slotCombo.setObjectName("slotCombo")
        self.hboxlayout2.addWidget(self.slotCombo)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem)
        self.vboxlayout4.addLayout(self.hboxlayout2)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem1)

        self.queryButton = QtGui.QPushButton(self.groupBox_2)
        self.queryButton.setObjectName("queryButton")
        self.hboxlayout3.addWidget(self.queryButton)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)
        self.vboxlayout4.addLayout(self.hboxlayout3)
        self.vboxlayout3.addLayout(self.vboxlayout4)
        self.vboxlayout1.addWidget(self.groupBox_2)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(B_Ethinarg)
        QtCore.QMetaObject.connectSlotsByName(B_Ethinarg)

    def retranslateUi(self, B_Ethinarg):
        B_Ethinarg.setWindowTitle(QtGui.QApplication.translate("B_Ethinarg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("B_Ethinarg", "Search Results", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("B_Ethinarg", "Search Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("B_Ethinarg", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("B_Ethinarg", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Slot", None, QtGui.QApplication.UnicodeUTF8))
        self.queryButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Run Query", None, QtGui.QApplication.UnicodeUTF8))

