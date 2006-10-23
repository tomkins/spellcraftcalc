# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Options.ui'
#
# Created: Sun Oct 22 21:32:44 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_Options(object):
    def setupUi(self, B_Options):
        B_Options.setObjectName("B_Options")
        B_Options.resize(QtCore.QSize(QtCore.QRect(0,0,636,443).size()).expandedTo(B_Options.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(B_Options)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.Tab = QtGui.QTabWidget(B_Options)
        self.Tab.setEnabled(True)
        self.Tab.setObjectName("Tab")

        self.General = QtGui.QWidget()
        self.General.setObjectName("General")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.General)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setMargin(0)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.TextLabel1 = QtGui.QLabel(self.General)
        self.TextLabel1.setObjectName("TextLabel1")
        self.hboxlayout.addWidget(self.TextLabel1)

        self.Skill = QtGui.QComboBox(self.General)
        self.Skill.setObjectName("Skill")
        self.hboxlayout.addWidget(self.Skill)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout3.addLayout(self.hboxlayout)

        self.CapDistance = QtGui.QCheckBox(self.General)
        self.CapDistance.setObjectName("CapDistance")
        self.vboxlayout3.addWidget(self.CapDistance)

        self.ShowDoneGems = QtGui.QCheckBox(self.General)
        self.ShowDoneGems.setObjectName("ShowDoneGems")
        self.vboxlayout3.addWidget(self.ShowDoneGems)

        self.IncludeRR = QtGui.QCheckBox(self.General)
        self.IncludeRR.setChecked(True)
        self.IncludeRR.setObjectName("IncludeRR")
        self.vboxlayout3.addWidget(self.IncludeRR)

        self.HideNonClassSkills = QtGui.QCheckBox(self.General)
        self.HideNonClassSkills.setChecked(True)
        self.HideNonClassSkills.setObjectName("HideNonClassSkills")
        self.vboxlayout3.addWidget(self.HideNonClassSkills)

        self.Coop = QtGui.QCheckBox(self.General)
        self.Coop.setObjectName("Coop")
        self.vboxlayout3.addWidget(self.Coop)

        self.TextLabel2_5 = QtGui.QLabel(self.General)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabel2_5.sizePolicy().hasHeightForWidth())
        self.TextLabel2_5.setSizePolicy(sizePolicy)
        self.TextLabel2_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TextLabel2_5.setObjectName("TextLabel2_5")
        self.vboxlayout3.addWidget(self.TextLabel2_5)

        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem1)
        self.vboxlayout2.addLayout(self.vboxlayout3)
        self.Tab.addTab(self.General, "")

        self.Notes = QtGui.QWidget()
        self.Notes.setObjectName("Notes")

        self.vboxlayout4 = QtGui.QVBoxLayout(self.Notes)
        self.vboxlayout4.setMargin(9)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setMargin(0)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.TextLabel2_2 = QtGui.QLabel(self.Notes)
        self.TextLabel2_2.setObjectName("TextLabel2_2")
        self.vboxlayout5.addWidget(self.TextLabel2_2)

        self.NoteText = QtGui.QTextEdit(self.Notes)
        self.NoteText.setObjectName("NoteText")
        self.vboxlayout5.addWidget(self.NoteText)
        self.vboxlayout4.addLayout(self.vboxlayout5)
        self.Tab.addTab(self.Notes, "")

        self.Price = QtGui.QWidget()
        self.Price.setObjectName("Price")

        self.widget = QtGui.QWidget(self.Price)
        self.widget.setGeometry(QtCore.QRect(10,302,594,23))
        self.widget.setObjectName("widget")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)

        self.CostInPrice = QtGui.QCheckBox(self.widget)
        self.CostInPrice.setChecked(True)
        self.CostInPrice.setObjectName("CostInPrice")
        self.hboxlayout1.addWidget(self.CostInPrice)

        spacerItem3 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem3)

        self.widget1 = QtGui.QWidget(self.Price)
        self.widget1.setGeometry(QtCore.QRect(10,331,594,22))
        self.widget1.setObjectName("widget1")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.widget1)
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem4)

        self.TextLabel2_4 = QtGui.QLabel(self.widget1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(4))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabel2_4.sizePolicy().hasHeightForWidth())
        self.TextLabel2_4.setSizePolicy(sizePolicy)
        self.TextLabel2_4.setObjectName("TextLabel2_4")
        self.hboxlayout2.addWidget(self.TextLabel2_4)

        spacerItem5 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem5)

        self.GroupBox4 = QtGui.QGroupBox(self.Price)
        self.GroupBox4.setGeometry(QtCore.QRect(11,186,226,109))
        self.GroupBox4.setObjectName("GroupBox4")

        self.vboxlayout6 = QtGui.QVBoxLayout(self.GroupBox4)
        self.vboxlayout6.setMargin(9)
        self.vboxlayout6.setSpacing(6)
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setMargin(0)
        self.vboxlayout7.setSpacing(6)
        self.vboxlayout7.setObjectName("vboxlayout7")

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.GenMarkup = QtGui.QLineEdit(self.GroupBox4)
        self.GenMarkup.setObjectName("GenMarkup")
        self.hboxlayout3.addWidget(self.GenMarkup)

        self.TextLabel11 = QtGui.QLabel(self.GroupBox4)
        self.TextLabel11.setObjectName("TextLabel11")
        self.hboxlayout3.addWidget(self.TextLabel11)
        self.vboxlayout7.addLayout(self.hboxlayout3)

        self.TextLabel12 = QtGui.QLabel(self.GroupBox4)
        self.TextLabel12.setObjectName("TextLabel12")
        self.vboxlayout7.addWidget(self.TextLabel12)
        self.vboxlayout6.addLayout(self.vboxlayout7)

        self.GroupBox5 = QtGui.QGroupBox(self.Price)
        self.GroupBox5.setGeometry(QtCore.QRect(243,186,187,109))
        self.GroupBox5.setObjectName("GroupBox5")

        self.vboxlayout8 = QtGui.QVBoxLayout(self.GroupBox5)
        self.vboxlayout8.setMargin(9)
        self.vboxlayout8.setSpacing(6)
        self.vboxlayout8.setObjectName("vboxlayout8")

        self.vboxlayout9 = QtGui.QVBoxLayout()
        self.vboxlayout9.setMargin(0)
        self.vboxlayout9.setSpacing(6)
        self.vboxlayout9.setObjectName("vboxlayout9")

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.TextLabel13 = QtGui.QLabel(self.GroupBox5)
        self.TextLabel13.setObjectName("TextLabel13")
        self.hboxlayout4.addWidget(self.TextLabel13)

        self.Tier = QtGui.QComboBox(self.GroupBox5)
        self.Tier.setObjectName("Tier")
        self.hboxlayout4.addWidget(self.Tier)

        self.TextLabel14 = QtGui.QLabel(self.GroupBox5)
        self.TextLabel14.setObjectName("TextLabel14")
        self.hboxlayout4.addWidget(self.TextLabel14)

        self.TierPrice = QtGui.QLineEdit(self.GroupBox5)
        self.TierPrice.setObjectName("TierPrice")
        self.hboxlayout4.addWidget(self.TierPrice)
        self.vboxlayout9.addLayout(self.hboxlayout4)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.TierInclude = QtGui.QCheckBox(self.GroupBox5)
        self.TierInclude.setObjectName("TierInclude")
        self.hboxlayout5.addWidget(self.TierInclude)

        self.TextLabel15 = QtGui.QLabel(self.GroupBox5)
        self.TextLabel15.setObjectName("TextLabel15")
        self.hboxlayout5.addWidget(self.TextLabel15)
        self.vboxlayout9.addLayout(self.hboxlayout5)
        self.vboxlayout8.addLayout(self.vboxlayout9)

        self.GroupBox6 = QtGui.QGroupBox(self.Price)
        self.GroupBox6.setGeometry(QtCore.QRect(436,186,167,109))
        self.GroupBox6.setObjectName("GroupBox6")

        self.vboxlayout10 = QtGui.QVBoxLayout(self.GroupBox6)
        self.vboxlayout10.setMargin(9)
        self.vboxlayout10.setSpacing(6)
        self.vboxlayout10.setObjectName("vboxlayout10")

        self.vboxlayout11 = QtGui.QVBoxLayout()
        self.vboxlayout11.setMargin(0)
        self.vboxlayout11.setSpacing(6)
        self.vboxlayout11.setObjectName("vboxlayout11")

        self.HourPrice = QtGui.QLineEdit(self.GroupBox6)
        self.HourPrice.setObjectName("HourPrice")
        self.vboxlayout11.addWidget(self.HourPrice)

        self.HourInclude = QtGui.QCheckBox(self.GroupBox6)
        self.HourInclude.setObjectName("HourInclude")
        self.vboxlayout11.addWidget(self.HourInclude)
        self.vboxlayout10.addLayout(self.vboxlayout11)

        self.GroupBox1 = QtGui.QGroupBox(self.Price)
        self.GroupBox1.setGeometry(QtCore.QRect(11,11,145,169))
        self.GroupBox1.setObjectName("GroupBox1")

        self.vboxlayout12 = QtGui.QVBoxLayout(self.GroupBox1)
        self.vboxlayout12.setMargin(9)
        self.vboxlayout12.setSpacing(6)
        self.vboxlayout12.setObjectName("vboxlayout12")

        self.vboxlayout13 = QtGui.QVBoxLayout()
        self.vboxlayout13.setMargin(0)
        self.vboxlayout13.setSpacing(6)
        self.vboxlayout13.setObjectName("vboxlayout13")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.PPGem = QtGui.QLineEdit(self.GroupBox1)
        self.PPGem.setObjectName("PPGem")
        self.gridlayout.addWidget(self.PPGem,0,1,1,1)

        self.TextLabel1_2 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel1_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel1_2.setObjectName("TextLabel1_2")
        self.gridlayout.addWidget(self.TextLabel1_2,0,0,1,1)

        self.PPOrder = QtGui.QLineEdit(self.GroupBox1)
        self.PPOrder.setObjectName("PPOrder")
        self.gridlayout.addWidget(self.PPOrder,2,1,1,1)

        self.TextLabel1_2_2 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel1_2_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel1_2_2.setObjectName("TextLabel1_2_2")
        self.gridlayout.addWidget(self.TextLabel1_2_2,1,0,1,1)

        self.TextLabel1_2_3 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel1_2_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel1_2_3.setObjectName("TextLabel1_2_3")
        self.gridlayout.addWidget(self.TextLabel1_2_3,2,0,1,1)

        self.PPItem = QtGui.QLineEdit(self.GroupBox1)
        self.PPItem.setObjectName("PPItem")
        self.gridlayout.addWidget(self.PPItem,1,1,1,1)
        self.vboxlayout13.addLayout(self.gridlayout)

        self.TextLabel2_3 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel2_3.setAlignment(QtCore.Qt.AlignCenter)
        self.TextLabel2_3.setObjectName("TextLabel2_3")
        self.vboxlayout13.addWidget(self.TextLabel2_3)
        self.vboxlayout12.addLayout(self.vboxlayout13)

        self.GroupBox2 = QtGui.QGroupBox(self.Price)
        self.GroupBox2.setGeometry(QtCore.QRect(162,11,203,169))
        self.GroupBox2.setObjectName("GroupBox2")

        self.vboxlayout14 = QtGui.QVBoxLayout(self.GroupBox2)
        self.vboxlayout14.setMargin(9)
        self.vboxlayout14.setSpacing(6)
        self.vboxlayout14.setObjectName("vboxlayout14")

        self.vboxlayout15 = QtGui.QVBoxLayout()
        self.vboxlayout15.setMargin(0)
        self.vboxlayout15.setSpacing(6)
        self.vboxlayout15.setObjectName("vboxlayout15")

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setSpacing(6)
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.TextLabel3 = QtGui.QLabel(self.GroupBox2)
        self.TextLabel3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel3.setObjectName("TextLabel3")
        self.hboxlayout6.addWidget(self.TextLabel3)

        self.QualMarkup = QtGui.QLineEdit(self.GroupBox2)
        self.QualMarkup.setObjectName("QualMarkup")
        self.hboxlayout6.addWidget(self.QualMarkup)

        self.TextLabel5 = QtGui.QLabel(self.GroupBox2)
        self.TextLabel5.setObjectName("TextLabel5")
        self.hboxlayout6.addWidget(self.TextLabel5)
        self.vboxlayout15.addLayout(self.hboxlayout6)

        self.hboxlayout7 = QtGui.QHBoxLayout()
        self.hboxlayout7.setMargin(0)
        self.hboxlayout7.setSpacing(6)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.TextLabel4 = QtGui.QLabel(self.GroupBox2)
        self.TextLabel4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TextLabel4.setObjectName("TextLabel4")
        self.hboxlayout7.addWidget(self.TextLabel4)

        self.QualLevel = QtGui.QComboBox(self.GroupBox2)
        self.QualLevel.setObjectName("QualLevel")
        self.hboxlayout7.addWidget(self.QualLevel)

        spacerItem6 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout7.addItem(spacerItem6)
        self.vboxlayout15.addLayout(self.hboxlayout7)

        self.QualInclude = QtGui.QCheckBox(self.GroupBox2)
        self.QualInclude.setObjectName("QualInclude")
        self.vboxlayout15.addWidget(self.QualInclude)

        self.TextLabel6 = QtGui.QLabel(self.GroupBox2)
        self.TextLabel6.setAlignment(QtCore.Qt.AlignCenter)
        self.TextLabel6.setWordWrap(True)
        self.TextLabel6.setObjectName("TextLabel6")
        self.vboxlayout15.addWidget(self.TextLabel6)
        self.vboxlayout14.addLayout(self.vboxlayout15)

        self.GroupBox3 = QtGui.QGroupBox(self.Price)
        self.GroupBox3.setGeometry(QtCore.QRect(371,11,232,169))
        self.GroupBox3.setObjectName("GroupBox3")

        self.vboxlayout16 = QtGui.QVBoxLayout(self.GroupBox3)
        self.vboxlayout16.setMargin(9)
        self.vboxlayout16.setSpacing(6)
        self.vboxlayout16.setObjectName("vboxlayout16")

        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setMargin(0)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.PPInclude = QtGui.QCheckBox(self.GroupBox3)
        self.PPInclude.setObjectName("PPInclude")
        self.gridlayout1.addWidget(self.PPInclude,3,0,1,1)

        self.PPImbue = QtGui.QLineEdit(self.GroupBox3)
        self.PPImbue.setObjectName("PPImbue")
        self.gridlayout1.addWidget(self.PPImbue,1,0,1,2)

        self.TextLabel10 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel10.setObjectName("TextLabel10")
        self.gridlayout1.addWidget(self.TextLabel10,3,1,1,4)

        self.TextLabel9 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel9.setObjectName("TextLabel9")
        self.gridlayout1.addWidget(self.TextLabel9,2,3,1,2)

        self.PPOC = QtGui.QLineEdit(self.GroupBox3)
        self.PPOC.setObjectName("PPOC")
        self.gridlayout1.addWidget(self.PPOC,2,0,1,3)

        self.TextLabel8 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel8.setObjectName("TextLabel8")
        self.gridlayout1.addWidget(self.TextLabel8,1,2,1,3)

        self.PPLevel = QtGui.QLineEdit(self.GroupBox3)
        self.PPLevel.setObjectName("PPLevel")
        self.gridlayout1.addWidget(self.PPLevel,0,0,1,4)

        self.TextLabel7 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel7.setObjectName("TextLabel7")
        self.gridlayout1.addWidget(self.TextLabel7,0,4,1,1)
        self.vboxlayout16.addLayout(self.gridlayout1)
        self.Tab.addTab(self.Price, "")
        self.vboxlayout1.addWidget(self.Tab)

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setMargin(0)
        self.hboxlayout8.setSpacing(25)
        self.hboxlayout8.setObjectName("hboxlayout8")

        spacerItem7 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem7)

        self.OK = QtGui.QPushButton(B_Options)
        self.OK.setObjectName("OK")
        self.hboxlayout8.addWidget(self.OK)

        self.Cancel = QtGui.QPushButton(B_Options)
        self.Cancel.setObjectName("Cancel")
        self.hboxlayout8.addWidget(self.Cancel)

        spacerItem8 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem8)
        self.vboxlayout1.addLayout(self.hboxlayout8)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(B_Options)
        QtCore.QMetaObject.connectSlotsByName(B_Options)

    def retranslateUi(self, B_Options):
        B_Options.setWindowTitle(QtGui.QApplication.translate("B_Options", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1.setText(QtGui.QApplication.translate("B_Options", "Crafter Skill:", None, QtGui.QApplication.UnicodeUTF8))
        self.CapDistance.setText(QtGui.QApplication.translate("B_Options", "Show Distance To Cap (instead of total)", None, QtGui.QApplication.UnicodeUTF8))
        self.ShowDoneGems.setText(QtGui.QApplication.translate("B_Options", "Hide \"Done\" Gems in Materials List", None, QtGui.QApplication.UnicodeUTF8))
        self.IncludeRR.setText(QtGui.QApplication.translate("B_Options", "Include Racial Resists in Totals", None, QtGui.QApplication.UnicodeUTF8))
        self.HideNonClassSkills.setText(QtGui.QApplication.translate("B_Options", "Hide Skills not usable by this Class", None, QtGui.QApplication.UnicodeUTF8))
        self.Coop.setText(QtGui.QApplication.translate("B_Options", "Co-op / PvP Server", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_5.setText(QtGui.QApplication.translate("B_Options", "        (Lets you access items from all realms)", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.General), QtGui.QApplication.translate("B_Options", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_2.setText(QtGui.QApplication.translate("B_Options", "Template Notes:", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.Notes), QtGui.QApplication.translate("B_Options", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.CostInPrice.setText(QtGui.QApplication.translate("B_Options", "Include cost in price", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_4.setText(QtGui.QApplication.translate("B_Options", "All numbers (except percentages) are in amounts of Gold.", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox4.setTitle(QtGui.QApplication.translate("B_Options", "General Markup", None, QtGui.QApplication.UnicodeUTF8))
        self.GenMarkup.setText(QtGui.QApplication.translate("B_Options", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel11.setText(QtGui.QApplication.translate("B_Options", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel12.setText(QtGui.QApplication.translate("B_Options", "(cost + (cost * X%))", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox5.setTitle(QtGui.QApplication.translate("B_Options", "Price by gem tier", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel13.setText(QtGui.QApplication.translate("B_Options", "Tier:", None, QtGui.QApplication.UnicodeUTF8))
        self.Tier.addItem(QtGui.QApplication.translate("B_Options", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.Tier.addItem(QtGui.QApplication.translate("B_Options", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.Tier.addItem(QtGui.QApplication.translate("B_Options", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.Tier.addItem(QtGui.QApplication.translate("B_Options", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.Tier.addItem(QtGui.QApplication.translate("B_Options", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.Tier.addItem(QtGui.QApplication.translate("B_Options", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.Tier.addItem(QtGui.QApplication.translate("B_Options", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.Tier.addItem(QtGui.QApplication.translate("B_Options", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.Tier.addItem(QtGui.QApplication.translate("B_Options", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.Tier.addItem(QtGui.QApplication.translate("B_Options", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel14.setText(QtGui.QApplication.translate("B_Options", "Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.TierPrice.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TierInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel15.setText(QtGui.QApplication.translate("B_Options", "(cost + X)", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox6.setTitle(QtGui.QApplication.translate("B_Options", "Per hour", None, QtGui.QApplication.UnicodeUTF8))
        self.HourPrice.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.HourInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox1.setTitle(QtGui.QApplication.translate("B_Options", "Price per", None, QtGui.QApplication.UnicodeUTF8))
        self.PPGem.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2.setText(QtGui.QApplication.translate("B_Options", "Gem:", None, QtGui.QApplication.UnicodeUTF8))
        self.PPOrder.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2_2.setText(QtGui.QApplication.translate("B_Options", "Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2_3.setText(QtGui.QApplication.translate("B_Options", "Order:", None, QtGui.QApplication.UnicodeUTF8))
        self.PPItem.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_3.setText(QtGui.QApplication.translate("B_Options", "(cost+ X)", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox2.setTitle(QtGui.QApplication.translate("B_Options", "Gem qual markup", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel3.setText(QtGui.QApplication.translate("B_Options", "Markup:", None, QtGui.QApplication.UnicodeUTF8))
        self.QualMarkup.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel5.setText(QtGui.QApplication.translate("B_Options", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel4.setText(QtGui.QApplication.translate("B_Options", "Quality:", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "94", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "95", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "96", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "97", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "98", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "99", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.QualInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel6.setText(QtGui.QApplication.translate("B_Options", "(cost + (cost * X%))", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox3.setTitle(QtGui.QApplication.translate("B_Options", "Price per lvl/point", None, QtGui.QApplication.UnicodeUTF8))
        self.PPInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.PPImbue.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel10.setText(QtGui.QApplication.translate("B_Options", "(cost + X)", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel9.setText(QtGui.QApplication.translate("B_Options", "per O/C pt.", None, QtGui.QApplication.UnicodeUTF8))
        self.PPOC.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel8.setText(QtGui.QApplication.translate("B_Options", "per imbue pt.", None, QtGui.QApplication.UnicodeUTF8))
        self.PPLevel.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel7.setText(QtGui.QApplication.translate("B_Options", "per level", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.Price), QtGui.QApplication.translate("B_Options", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.OK.setText(QtGui.QApplication.translate("B_Options", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancel.setText(QtGui.QApplication.translate("B_Options", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
