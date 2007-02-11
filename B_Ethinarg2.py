# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ethinarg2.ui'
#
# Created: Sat Feb 10 16:34:33 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_Ethinarg(object):
    def setupUi(self, B_Ethinarg):
        B_Ethinarg.setObjectName("B_Ethinarg")
        B_Ethinarg.resize(QtCore.QSize(QtCore.QRect(0,0,894,707).size()).expandedTo(B_Ethinarg.minimumSizeHint()))

        self.hboxlayout = QtGui.QHBoxLayout(B_Ethinarg)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.splitter = QtGui.QSplitter(B_Ethinarg)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.browser = QtGui.QTextBrowser(self.groupBox)
        self.browser.setObjectName("browser")
        self.vboxlayout1.addWidget(self.browser)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.openSearchButton = QtGui.QPushButton(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openSearchButton.sizePolicy().hasHeightForWidth())
        self.openSearchButton.setSizePolicy(sizePolicy)
        self.openSearchButton.setMinimumSize(QtCore.QSize(150,0))
        self.openSearchButton.setObjectName("openSearchButton")
        self.hboxlayout1.addWidget(self.openSearchButton)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.prevButton = QtGui.QPushButton(self.groupBox)
        self.prevButton.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevButton.sizePolicy().hasHeightForWidth())
        self.prevButton.setSizePolicy(sizePolicy)
        self.prevButton.setObjectName("prevButton")
        self.hboxlayout1.addWidget(self.prevButton)

        self.nextButton = QtGui.QPushButton(self.groupBox)
        self.nextButton.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setObjectName("nextButton")
        self.hboxlayout1.addWidget(self.nextButton)

        self.pageNum = QtGui.QLineEdit(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageNum.sizePolicy().hasHeightForWidth())
        self.pageNum.setSizePolicy(sizePolicy)
        self.pageNum.setMinimumSize(QtCore.QSize(60,0))
        self.pageNum.setMaximumSize(QtCore.QSize(60,16777215))
        self.pageNum.setObjectName("pageNum")
        self.hboxlayout1.addWidget(self.pageNum)

        self.goButton = QtGui.QPushButton(self.groupBox)
        self.goButton.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goButton.sizePolicy().hasHeightForWidth())
        self.goButton.setSizePolicy(sizePolicy)
        self.goButton.setObjectName("goButton")
        self.hboxlayout1.addWidget(self.goButton)

        self.pageStatus = QtGui.QLabel(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageStatus.sizePolicy().hasHeightForWidth())
        self.pageStatus.setSizePolicy(sizePolicy)
        self.pageStatus.setMinimumSize(QtCore.QSize(60,0))
        self.pageStatus.setMaximumSize(QtCore.QSize(100,16777215))
        self.pageStatus.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.pageStatus.setObjectName("pageStatus")
        self.hboxlayout1.addWidget(self.pageStatus)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.hboxlayout2.addWidget(self.label)

        self.usernameBox = QtGui.QLineEdit(self.groupBox_2)
        self.usernameBox.setObjectName("usernameBox")
        self.hboxlayout2.addWidget(self.usernameBox)
        self.vboxlayout3.addLayout(self.hboxlayout2)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.hboxlayout3.addWidget(self.label_2)

        self.passwordBox = QtGui.QLineEdit(self.groupBox_2)
        self.passwordBox.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordBox.setObjectName("passwordBox")
        self.hboxlayout3.addWidget(self.passwordBox)
        self.vboxlayout3.addLayout(self.hboxlayout3)

        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.vboxlayout4.setMargin(9)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setMargin(0)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.hboxlayout4.addWidget(self.label_6)

        self.realmCombo = SearchingCombo(self.groupBox_3)
        self.realmCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.realmCombo.setObjectName("realmCombo")
        self.hboxlayout4.addWidget(self.realmCombo)
        self.vboxlayout5.addLayout(self.hboxlayout4)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.hboxlayout5.addWidget(self.label_3)

        self.itemNameBox = QtGui.QLineEdit(self.groupBox_3)
        self.itemNameBox.setObjectName("itemNameBox")
        self.hboxlayout5.addWidget(self.itemNameBox)
        self.vboxlayout5.addLayout(self.hboxlayout5)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setSpacing(6)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.hboxlayout6.addWidget(self.label_4)

        self.slotCombo = SearchingCombo(self.groupBox_3)
        self.slotCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.slotCombo.setObjectName("slotCombo")
        self.hboxlayout6.addWidget(self.slotCombo)
        self.vboxlayout5.addLayout(self.hboxlayout6)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setMargin(0)
        self.hboxlayout7.setSpacing(6)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.hboxlayout7.addWidget(self.label_5)

        self.classCombo = SearchingCombo(self.groupBox_3)
        self.classCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.classCombo.setObjectName("classCombo")
        self.hboxlayout7.addWidget(self.classCombo)
        self.vboxlayout5.addLayout(self.hboxlayout7)

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setMargin(0)
        self.hboxlayout8.setSpacing(6)
        self.hboxlayout8.setObjectName("hboxlayout8")

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem1)

        self.queryButton = QtGui.QPushButton(self.groupBox_3)
        self.queryButton.setDefault(True)
        self.queryButton.setObjectName("queryButton")
        self.hboxlayout8.addWidget(self.queryButton)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem2)
        self.vboxlayout5.addLayout(self.hboxlayout8)

        self.hboxlayout9 = QtGui.QHBoxLayout()
        self.hboxlayout9.setMargin(0)
        self.hboxlayout9.setSpacing(6)
        self.hboxlayout9.setObjectName("hboxlayout9")

        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout9.addItem(spacerItem3)

        self.collapseButton = QtGui.QPushButton(self.groupBox_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(3),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collapseButton.sizePolicy().hasHeightForWidth())
        self.collapseButton.setSizePolicy(sizePolicy)
        self.collapseButton.setAutoDefault(False)
        self.collapseButton.setDefault(False)
        self.collapseButton.setObjectName("collapseButton")
        self.hboxlayout9.addWidget(self.collapseButton)

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout9.addItem(spacerItem4)
        self.vboxlayout5.addLayout(self.hboxlayout9)

        spacerItem5 = QtGui.QSpacerItem(20,311,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout5.addItem(spacerItem5)
        self.vboxlayout4.addLayout(self.vboxlayout5)
        self.vboxlayout3.addWidget(self.groupBox_3)
        self.vboxlayout2.addLayout(self.vboxlayout3)
        self.hboxlayout.addWidget(self.splitter)

        self.retranslateUi(B_Ethinarg)
        QtCore.QMetaObject.connectSlotsByName(B_Ethinarg)

    def retranslateUi(self, B_Ethinarg):
        B_Ethinarg.setWindowTitle(QtGui.QApplication.translate("B_Ethinarg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("B_Ethinarg", "Search Results", None, QtGui.QApplication.UnicodeUTF8))
        self.openSearchButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Open Search Pane", None, QtGui.QApplication.UnicodeUTF8))
        self.prevButton.setText(QtGui.QApplication.translate("B_Ethinarg", "< Prev", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Next >", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.pageStatus.setText(QtGui.QApplication.translate("B_Ethinarg", "100/100", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("B_Ethinarg", "Search Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("B_Ethinarg", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("B_Ethinarg", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("B_Ethinarg", "Search Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Realm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Class", None, QtGui.QApplication.UnicodeUTF8))
        self.queryButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Run Query", None, QtGui.QApplication.UnicodeUTF8))
        self.collapseButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Collapse >>", None, QtGui.QApplication.UnicodeUTF8))

from SearchingCombo import SearchingCombo
