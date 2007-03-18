# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ethinarg.ui'
#
# Created: Sun Mar 18 15:21:05 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_Ethinarg(object):
    def setupUi(self, B_Ethinarg):
        B_Ethinarg.setObjectName("B_Ethinarg")
        B_Ethinarg.resize(QtCore.QSize(QtCore.QRect(0,0,900,609).size()).expandedTo(B_Ethinarg.minimumSizeHint()))

        self.hboxlayout = QtGui.QHBoxLayout(B_Ethinarg)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.splitter = QtGui.QSplitter(B_Ethinarg)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.groupBox = QtGui.QGroupBox(self.splitter)
        self.groupBox.setObjectName("groupBox")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.browser = QtGui.QTextBrowser(self.groupBox)
        self.browser.setObjectName("browser")
        self.vboxlayout2.addWidget(self.browser)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

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

        self.openSearchButton = QtGui.QPushButton(self.groupBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openSearchButton.sizePolicy().hasHeightForWidth())
        self.openSearchButton.setSizePolicy(sizePolicy)
        self.openSearchButton.setMinimumSize(QtCore.QSize(150,0))
        self.openSearchButton.setCheckable(True)
        self.openSearchButton.setObjectName("openSearchButton")
        self.hboxlayout1.addWidget(self.openSearchButton)
        self.vboxlayout2.addLayout(self.hboxlayout1)
        self.vboxlayout1.addLayout(self.vboxlayout2)

        self.groupBox_2 = QtGui.QGroupBox(self.splitter)
        self.groupBox_2.setObjectName("groupBox_2")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setMargin(0)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

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
        self.vboxlayout4.addLayout(self.hboxlayout2)

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
        self.vboxlayout4.addLayout(self.hboxlayout3)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.hboxlayout4.addWidget(self.label_6)

        self.realmCombo = SearchingCombo(self.groupBox_2)
        self.realmCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.realmCombo.setObjectName("realmCombo")
        self.hboxlayout4.addWidget(self.realmCombo)
        self.vboxlayout4.addLayout(self.hboxlayout4)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.hboxlayout5.addWidget(self.label_3)

        self.itemNameBox = QtGui.QLineEdit(self.groupBox_2)
        self.itemNameBox.setObjectName("itemNameBox")
        self.hboxlayout5.addWidget(self.itemNameBox)
        self.vboxlayout4.addLayout(self.hboxlayout5)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setSpacing(6)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.hboxlayout6.addWidget(self.label_4)

        self.slotCombo = SearchingCombo(self.groupBox_2)
        self.slotCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.slotCombo.setObjectName("slotCombo")
        self.hboxlayout6.addWidget(self.slotCombo)
        self.vboxlayout4.addLayout(self.hboxlayout6)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setMargin(0)
        self.hboxlayout7.setSpacing(6)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.hboxlayout7.addWidget(self.label_5)

        self.classCombo = SearchingCombo(self.groupBox_2)
        self.classCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.classCombo.setObjectName("classCombo")
        self.hboxlayout7.addWidget(self.classCombo)
        self.vboxlayout4.addLayout(self.hboxlayout7)

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setMargin(0)
        self.hboxlayout8.setSpacing(6)
        self.hboxlayout8.setObjectName("hboxlayout8")

        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.hboxlayout8.addWidget(self.label_7)

        self.minLevelCombo = SearchingCombo(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minLevelCombo.sizePolicy().hasHeightForWidth())
        self.minLevelCombo.setSizePolicy(sizePolicy)
        self.minLevelCombo.setMinimumSize(QtCore.QSize(55,0))
        self.minLevelCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.minLevelCombo.setObjectName("minLevelCombo")
        self.hboxlayout8.addWidget(self.minLevelCombo)

        self.label_8 = QtGui.QLabel(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.hboxlayout8.addWidget(self.label_8)

        self.maxLevelCombo = SearchingCombo(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxLevelCombo.sizePolicy().hasHeightForWidth())
        self.maxLevelCombo.setSizePolicy(sizePolicy)
        self.maxLevelCombo.setMinimumSize(QtCore.QSize(55,0))
        self.maxLevelCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.maxLevelCombo.setObjectName("maxLevelCombo")
        self.hboxlayout8.addWidget(self.maxLevelCombo)
        self.vboxlayout4.addLayout(self.hboxlayout8)

        self.hboxlayout9 = QtGui.QHBoxLayout()
        self.hboxlayout9.setMargin(0)
        self.hboxlayout9.setSpacing(6)
        self.hboxlayout9.setObjectName("hboxlayout9")

        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.hboxlayout9.addWidget(self.label_13)

        self.locationCombo = SearchingCombo(self.groupBox_2)
        self.locationCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.locationCombo.setObjectName("locationCombo")
        self.hboxlayout9.addWidget(self.locationCombo)
        self.vboxlayout4.addLayout(self.hboxlayout9)

        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setMargin(0)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.hboxlayout10 = QtGui.QHBoxLayout()
        self.hboxlayout10.setMargin(0)
        self.hboxlayout10.setSpacing(6)
        self.hboxlayout10.setObjectName("hboxlayout10")

        self.label_9 = QtGui.QLabel(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.hboxlayout10.addWidget(self.label_9)

        self.line = QtGui.QFrame(self.groupBox_2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hboxlayout10.addWidget(self.line)
        self.vboxlayout5.addLayout(self.hboxlayout10)

        self.bonus1Combo = SearchingCombo(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(13),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bonus1Combo.sizePolicy().hasHeightForWidth())
        self.bonus1Combo.setSizePolicy(sizePolicy)
        self.bonus1Combo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bonus1Combo.setObjectName("bonus1Combo")
        self.vboxlayout5.addWidget(self.bonus1Combo)
        self.vboxlayout4.addLayout(self.vboxlayout5)

        self.vboxlayout6 = QtGui.QVBoxLayout()
        self.vboxlayout6.setMargin(0)
        self.vboxlayout6.setSpacing(6)
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.hboxlayout11 = QtGui.QHBoxLayout()
        self.hboxlayout11.setMargin(0)
        self.hboxlayout11.setSpacing(6)
        self.hboxlayout11.setObjectName("hboxlayout11")

        self.label_10 = QtGui.QLabel(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.hboxlayout11.addWidget(self.label_10)

        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.hboxlayout11.addWidget(self.line_2)
        self.vboxlayout6.addLayout(self.hboxlayout11)

        self.bonus2Combo = SearchingCombo(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(13),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bonus2Combo.sizePolicy().hasHeightForWidth())
        self.bonus2Combo.setSizePolicy(sizePolicy)
        self.bonus2Combo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bonus2Combo.setObjectName("bonus2Combo")
        self.vboxlayout6.addWidget(self.bonus2Combo)
        self.vboxlayout4.addLayout(self.vboxlayout6)

        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setMargin(0)
        self.vboxlayout7.setSpacing(6)
        self.vboxlayout7.setObjectName("vboxlayout7")

        self.hboxlayout12 = QtGui.QHBoxLayout()
        self.hboxlayout12.setMargin(0)
        self.hboxlayout12.setSpacing(6)
        self.hboxlayout12.setObjectName("hboxlayout12")

        self.label_11 = QtGui.QLabel(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.hboxlayout12.addWidget(self.label_11)

        self.line_3 = QtGui.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.hboxlayout12.addWidget(self.line_3)
        self.vboxlayout7.addLayout(self.hboxlayout12)

        self.bonus3Combo = SearchingCombo(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(13),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bonus3Combo.sizePolicy().hasHeightForWidth())
        self.bonus3Combo.setSizePolicy(sizePolicy)
        self.bonus3Combo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.bonus3Combo.setObjectName("bonus3Combo")
        self.vboxlayout7.addWidget(self.bonus3Combo)
        self.vboxlayout4.addLayout(self.vboxlayout7)

        self.vboxlayout8 = QtGui.QVBoxLayout()
        self.vboxlayout8.setMargin(0)
        self.vboxlayout8.setSpacing(6)
        self.vboxlayout8.setObjectName("vboxlayout8")

        self.hboxlayout13 = QtGui.QHBoxLayout()
        self.hboxlayout13.setMargin(0)
        self.hboxlayout13.setSpacing(6)
        self.hboxlayout13.setObjectName("hboxlayout13")

        self.label_12 = QtGui.QLabel(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.hboxlayout13.addWidget(self.label_12)

        self.line_4 = QtGui.QFrame(self.groupBox_2)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.hboxlayout13.addWidget(self.line_4)
        self.vboxlayout8.addLayout(self.hboxlayout13)

        self.magicalCombo = SearchingCombo(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(13),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.magicalCombo.sizePolicy().hasHeightForWidth())
        self.magicalCombo.setSizePolicy(sizePolicy)
        self.magicalCombo.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.magicalCombo.setObjectName("magicalCombo")
        self.vboxlayout8.addWidget(self.magicalCombo)
        self.vboxlayout4.addLayout(self.vboxlayout8)

        self.hboxlayout14 = QtGui.QHBoxLayout()
        self.hboxlayout14.setMargin(0)
        self.hboxlayout14.setSpacing(6)
        self.hboxlayout14.setObjectName("hboxlayout14")

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout14.addItem(spacerItem1)

        self.queryButton = QtGui.QPushButton(self.groupBox_2)
        self.queryButton.setDefault(True)
        self.queryButton.setObjectName("queryButton")
        self.hboxlayout14.addWidget(self.queryButton)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout14.addItem(spacerItem2)
        self.vboxlayout4.addLayout(self.hboxlayout14)

        spacerItem3 = QtGui.QSpacerItem(20,311,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout4.addItem(spacerItem3)
        self.vboxlayout3.addLayout(self.vboxlayout4)
        self.vboxlayout.addWidget(self.splitter)

        self.hboxlayout15 = QtGui.QHBoxLayout()
        self.hboxlayout15.setMargin(0)
        self.hboxlayout15.setSpacing(6)
        self.hboxlayout15.setObjectName("hboxlayout15")

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout15.addItem(spacerItem4)

        self.closeButton = QtGui.QPushButton(B_Ethinarg)
        self.closeButton.setObjectName("closeButton")
        self.hboxlayout15.addWidget(self.closeButton)

        spacerItem5 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout15.addItem(spacerItem5)
        self.vboxlayout.addLayout(self.hboxlayout15)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.retranslateUi(B_Ethinarg)
        QtCore.QMetaObject.connectSlotsByName(B_Ethinarg)

    def retranslateUi(self, B_Ethinarg):
        B_Ethinarg.setWindowTitle(QtGui.QApplication.translate("B_Ethinarg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("B_Ethinarg", "Ethinarg\'s Item Database Search Results", None, QtGui.QApplication.UnicodeUTF8))
        self.prevButton.setText(QtGui.QApplication.translate("B_Ethinarg", "< Prev", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Next >", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.pageStatus.setText(QtGui.QApplication.translate("B_Ethinarg", "100/100", None, QtGui.QApplication.UnicodeUTF8))
        self.openSearchButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Open Search Pane", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("B_Ethinarg", "Search Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("B_Ethinarg", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("B_Ethinarg", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Realm", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Class", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Level", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("B_Ethinarg", "~", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("B_Ethinarg", "Item Location", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("B_Ethinarg", "Bonus 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("B_Ethinarg", "Bonus 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("B_Ethinarg", "Bonus 3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("B_Ethinarg", "Magical Ability", None, QtGui.QApplication.UnicodeUTF8))
        self.queryButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Run Query", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("B_Ethinarg", "Close", None, QtGui.QApplication.UnicodeUTF8))

from SearchingCombo import SearchingCombo
