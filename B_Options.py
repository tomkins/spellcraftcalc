# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Options.ui4'
#
# Created: Wed Sep 06 17:41:39 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_Options(object):
    def setupUi(self, B_Options):
        B_Options.setObjectName("B_Options")
        B_Options.resize(QtCore.QSize(QtCore.QRect(0,0,364,295).size()).expandedTo(B_Options.minimumSizeHint()))

        self.OK = QtGui.QPushButton(B_Options)
        self.OK.setGeometry(QtCore.QRect(52,265,93,26))
        self.OK.setObjectName("OK")

        self.Cancel = QtGui.QPushButton(B_Options)
        self.Cancel.setGeometry(QtCore.QRect(207,265,93,26))
        self.Cancel.setObjectName("Cancel")

        self.Tab = QtGui.QTabWidget(B_Options)
        self.Tab.setEnabled(True)
        self.Tab.setGeometry(QtCore.QRect(10,6,353,259))
        self.Tab.setObjectName("Tab")

        self.General = QtGui.QWidget()
        self.General.setObjectName("General")

        self.TextLabel1 = QtGui.QLabel(self.General)
        self.TextLabel1.setGeometry(QtCore.QRect(18,17,61,22))
        self.TextLabel1.setObjectName("TextLabel1")

        self.Skill = QtGui.QComboBox(self.General)
        self.Skill.setGeometry(QtCore.QRect(89,17,81,22))
        self.Skill.setObjectName("Skill")

        self.CapDistance = QtGui.QCheckBox(self.General)
        self.CapDistance.setGeometry(QtCore.QRect(18,75,250,17))
        self.CapDistance.setObjectName("CapDistance")

        self.ShowDoneGems = QtGui.QCheckBox(self.General)
        self.ShowDoneGems.setGeometry(QtCore.QRect(18,100,250,17))
        self.ShowDoneGems.setObjectName("ShowDoneGems")

        self.IncludeRR = QtGui.QCheckBox(self.General)
        self.IncludeRR.setGeometry(QtCore.QRect(18,125,250,17))
        self.IncludeRR.setChecked(True)
        self.IncludeRR.setObjectName("IncludeRR")

        self.HideNonClassSkills = QtGui.QCheckBox(self.General)
        self.HideNonClassSkills.setGeometry(QtCore.QRect(18,150,250,17))
        self.HideNonClassSkills.setChecked(True)
        self.HideNonClassSkills.setObjectName("HideNonClassSkills")

        self.Coop = QtGui.QCheckBox(self.General)
        self.Coop.setGeometry(QtCore.QRect(18,175,250,17))
        self.Coop.setObjectName("Coop")

        self.TextLabel2_5 = QtGui.QLabel(self.General)
        self.TextLabel2_5.setGeometry(QtCore.QRect(40,192,250,14))
        self.TextLabel2_5.setObjectName("TextLabel2_5")
        self.Tab.addTab(self.General, "")

        self.Notes = QtGui.QWidget()
        self.Notes.setObjectName("Notes")

        self.TextLabel2_2 = QtGui.QLabel(self.Notes)
        self.TextLabel2_2.setGeometry(QtCore.QRect(12,6,82,16))
        self.TextLabel2_2.setObjectName("TextLabel2_2")

        self.NoteText = QtGui.QTextEdit(self.Notes)
        self.NoteText.setGeometry(QtCore.QRect(13,26,321,154))
        self.NoteText.setObjectName("NoteText")
        self.Tab.addTab(self.Notes, "")

        self.Price = QtGui.QWidget()
        self.Price.setObjectName("Price")

        self.GroupBox1 = QtGui.QGroupBox(self.Price)
        self.GroupBox1.setGeometry(QtCore.QRect(4,1,95,115))
        self.GroupBox1.setObjectName("GroupBox1")

        self.TextLabel1_2 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel1_2.setGeometry(QtCore.QRect(5,15,28,16))
        self.TextLabel1_2.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.TextLabel1_2.setObjectName("TextLabel1_2")

        self.TextLabel1_2_3 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel1_2_3.setGeometry(QtCore.QRect(2,71,31,16))
        self.TextLabel1_2_3.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.TextLabel1_2_3.setObjectName("TextLabel1_2_3")

        self.TextLabel1_2_2 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel1_2_2.setGeometry(QtCore.QRect(8,42,24,16))
        self.TextLabel1_2_2.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.TextLabel1_2_2.setObjectName("TextLabel1_2_2")

        self.TextLabel2_3 = QtGui.QLabel(self.GroupBox1)
        self.TextLabel2_3.setGeometry(QtCore.QRect(26,94,43,16))
        self.TextLabel2_3.setObjectName("TextLabel2_3")

        self.PPGem = QtGui.QLineEdit(self.GroupBox1)
        self.PPGem.setGeometry(QtCore.QRect(37,14,52,22))
        self.PPGem.setObjectName("PPGem")

        self.PPItem = QtGui.QLineEdit(self.GroupBox1)
        self.PPItem.setGeometry(QtCore.QRect(37,41,52,22))
        self.PPItem.setObjectName("PPItem")

        self.PPOrder = QtGui.QLineEdit(self.GroupBox1)
        self.PPOrder.setGeometry(QtCore.QRect(37,69,52,22))
        self.PPOrder.setObjectName("PPOrder")

        self.GroupBox2 = QtGui.QGroupBox(self.Price)
        self.GroupBox2.setGeometry(QtCore.QRect(101,1,109,115))
        self.GroupBox2.setObjectName("GroupBox2")

        self.TextLabel3 = QtGui.QLabel(self.GroupBox2)
        self.TextLabel3.setGeometry(QtCore.QRect(4,17,41,13))
        self.TextLabel3.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.TextLabel3.setObjectName("TextLabel3")

        self.TextLabel4 = QtGui.QLabel(self.GroupBox2)
        self.TextLabel4.setGeometry(QtCore.QRect(6,44,36,13))
        self.TextLabel4.setAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
        self.TextLabel4.setObjectName("TextLabel4")

        self.TextLabel5 = QtGui.QLabel(self.GroupBox2)
        self.TextLabel5.setGeometry(QtCore.QRect(91,17,16,16))
        self.TextLabel5.setObjectName("TextLabel5")

        self.TextLabel6 = QtGui.QLabel(self.GroupBox2)
        self.TextLabel6.setGeometry(QtCore.QRect(9,94,92,16))
        self.TextLabel6.setObjectName("TextLabel6")

        self.QualLevel = QtGui.QComboBox(self.GroupBox2)
        self.QualLevel.setGeometry(QtCore.QRect(48,41,50,22))
        self.QualLevel.setObjectName("QualLevel")

        self.QualMarkup = QtGui.QLineEdit(self.GroupBox2)
        self.QualMarkup.setGeometry(QtCore.QRect(49,14,40,22))
        self.QualMarkup.setObjectName("QualMarkup")

        self.QualInclude = QtGui.QCheckBox(self.GroupBox2)
        self.QualInclude.setGeometry(QtCore.QRect(8,72,59,17))
        self.QualInclude.setObjectName("QualInclude")

        self.GroupBox3 = QtGui.QGroupBox(self.Price)
        self.GroupBox3.setGeometry(QtCore.QRect(214,1,131,115))
        self.GroupBox3.setObjectName("GroupBox3")

        self.TextLabel7 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel7.setGeometry(QtCore.QRect(60,16,44,16))
        self.TextLabel7.setObjectName("TextLabel7")

        self.TextLabel8 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel8.setGeometry(QtCore.QRect(59,43,63,16))
        self.TextLabel8.setObjectName("TextLabel8")

        self.TextLabel9 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel9.setGeometry(QtCore.QRect(60,71,66,16))
        self.TextLabel9.setObjectName("TextLabel9")

        self.TextLabel10 = QtGui.QLabel(self.GroupBox3)
        self.TextLabel10.setGeometry(QtCore.QRect(77,93,47,16))
        self.TextLabel10.setObjectName("TextLabel10")

        self.PPImbue = QtGui.QLineEdit(self.GroupBox3)
        self.PPImbue.setGeometry(QtCore.QRect(5,41,50,22))
        self.PPImbue.setObjectName("PPImbue")

        self.PPInclude = QtGui.QCheckBox(self.GroupBox3)
        self.PPInclude.setGeometry(QtCore.QRect(5,94,59,17))
        self.PPInclude.setObjectName("PPInclude")

        self.PPLevel = QtGui.QLineEdit(self.GroupBox3)
        self.PPLevel.setGeometry(QtCore.QRect(5,14,50,22))
        self.PPLevel.setObjectName("PPLevel")

        self.PPOC = QtGui.QLineEdit(self.GroupBox3)
        self.PPOC.setGeometry(QtCore.QRect(5,69,50,22))
        self.PPOC.setObjectName("PPOC")

        self.GroupBox4 = QtGui.QGroupBox(self.Price)
        self.GroupBox4.setGeometry(QtCore.QRect(4,119,98,65))
        self.GroupBox4.setObjectName("GroupBox4")

        self.TextLabel11 = QtGui.QLabel(self.GroupBox4)
        self.TextLabel11.setGeometry(QtCore.QRect(59,19,16,16))
        self.TextLabel11.setObjectName("TextLabel11")

        self.TextLabel12 = QtGui.QLabel(self.GroupBox4)
        self.TextLabel12.setGeometry(QtCore.QRect(5,43,90,16))
        self.TextLabel12.setObjectName("TextLabel12")

        self.GenMarkup = QtGui.QLineEdit(self.GroupBox4)
        self.GenMarkup.setGeometry(QtCore.QRect(8,16,46,22))
        self.GenMarkup.setObjectName("GenMarkup")

        self.GroupBox5 = QtGui.QGroupBox(self.Price)
        self.GroupBox5.setGeometry(QtCore.QRect(106,120,166,64))
        self.GroupBox5.setObjectName("GroupBox5")

        self.TextLabel13 = QtGui.QLabel(self.GroupBox5)
        self.TextLabel13.setGeometry(QtCore.QRect(7,17,25,16))
        self.TextLabel13.setObjectName("TextLabel13")

        self.TextLabel14 = QtGui.QLabel(self.GroupBox5)
        self.TextLabel14.setGeometry(QtCore.QRect(85,17,31,16))
        self.TextLabel14.setObjectName("TextLabel14")

        self.TextLabel15 = QtGui.QLabel(self.GroupBox5)
        self.TextLabel15.setGeometry(QtCore.QRect(99,42,51,16))
        self.TextLabel15.setObjectName("TextLabel15")

        self.Tier = QtGui.QComboBox(self.GroupBox5)
        self.Tier.setGeometry(QtCore.QRect(32,15,40,22))
        self.Tier.setObjectName("Tier")

        self.TierPrice = QtGui.QLineEdit(self.GroupBox5)
        self.TierPrice.setGeometry(QtCore.QRect(118,15,42,22))
        self.TierPrice.setObjectName("TierPrice")

        self.TierInclude = QtGui.QCheckBox(self.GroupBox5)
        self.TierInclude.setGeometry(QtCore.QRect(6,42,59,17))
        self.TierInclude.setObjectName("TierInclude")

        self.GroupBox6 = QtGui.QGroupBox(self.Price)
        self.GroupBox6.setGeometry(QtCore.QRect(274,120,69,64))
        self.GroupBox6.setObjectName("GroupBox6")

        self.HourInclude = QtGui.QCheckBox(self.GroupBox6)
        self.HourInclude.setGeometry(QtCore.QRect(4,42,59,17))
        self.HourInclude.setObjectName("HourInclude")

        self.HourPrice = QtGui.QLineEdit(self.GroupBox6)
        self.HourPrice.setGeometry(QtCore.QRect(4,15,58,22))
        self.HourPrice.setObjectName("HourPrice")

        self.TextLabel2_4 = QtGui.QLabel(self.Price)
        self.TextLabel2_4.setGeometry(QtCore.QRect(44,209,276,16))
        self.TextLabel2_4.setObjectName("TextLabel2_4")

        self.CostInPrice = QtGui.QCheckBox(self.Price)
        self.CostInPrice.setGeometry(QtCore.QRect(112,189,119,17))
        self.CostInPrice.setChecked(True)
        self.CostInPrice.setObjectName("CostInPrice")
        self.Tab.addTab(self.Price, "")

        self.retranslateUi(B_Options)

    def retranslateUi(self, B_Options):
        B_Options.setWindowTitle(QtGui.QApplication.translate("B_Options", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.OK.setText(QtGui.QApplication.translate("B_Options", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.Cancel.setText(QtGui.QApplication.translate("B_Options", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1.setText(QtGui.QApplication.translate("B_Options", "Crafter Skill:", None, QtGui.QApplication.UnicodeUTF8))
        self.CapDistance.setText(QtGui.QApplication.translate("B_Options", "Show Distance To Cap (instead of total)", None, QtGui.QApplication.UnicodeUTF8))
        self.ShowDoneGems.setText(QtGui.QApplication.translate("B_Options", "\"Done\" Gems do not show up in Materials List", None, QtGui.QApplication.UnicodeUTF8))
        self.IncludeRR.setText(QtGui.QApplication.translate("B_Options", "Include Racial Resists in Totals", None, QtGui.QApplication.UnicodeUTF8))
        self.HideNonClassSkills.setText(QtGui.QApplication.translate("B_Options", "Hide Skills not usable by this Class", None, QtGui.QApplication.UnicodeUTF8))
        self.Coop.setText(QtGui.QApplication.translate("B_Options", "Co-op / PvP Server", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_5.setText(QtGui.QApplication.translate("B_Options", "(Lets you access items from all realms)", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.General), QtGui.QApplication.translate("B_Options", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_2.setText(QtGui.QApplication.translate("B_Options", "Template Notes:", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.Notes), QtGui.QApplication.translate("B_Options", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox1.setTitle(QtGui.QApplication.translate("B_Options", "Price per", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2.setText(QtGui.QApplication.translate("B_Options", "Gem:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2_3.setText(QtGui.QApplication.translate("B_Options", "Order:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel1_2_2.setText(QtGui.QApplication.translate("B_Options", "Item:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_3.setText(QtGui.QApplication.translate("B_Options", "(cost+ X)", None, QtGui.QApplication.UnicodeUTF8))
        self.PPGem.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.PPItem.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.PPOrder.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox2.setTitle(QtGui.QApplication.translate("B_Options", "Gem qual markup", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel3.setText(QtGui.QApplication.translate("B_Options", "Markup:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel4.setText(QtGui.QApplication.translate("B_Options", "Quality:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel5.setText(QtGui.QApplication.translate("B_Options", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel6.setText(QtGui.QApplication.translate("B_Options", "(cost + (cost * X%))", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "94", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "95", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "96", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "97", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "98", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "99", None, QtGui.QApplication.UnicodeUTF8))
        self.QualLevel.addItem(QtGui.QApplication.translate("B_Options", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.QualMarkup.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.QualInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox3.setTitle(QtGui.QApplication.translate("B_Options", "Price per lvl/point", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel7.setText(QtGui.QApplication.translate("B_Options", "per level", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel8.setText(QtGui.QApplication.translate("B_Options", "per imbue pt.", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel9.setText(QtGui.QApplication.translate("B_Options", "per O/C pt.", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel10.setText(QtGui.QApplication.translate("B_Options", "(cost + X)", None, QtGui.QApplication.UnicodeUTF8))
        self.PPImbue.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.PPInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.PPLevel.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.PPOC.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox4.setTitle(QtGui.QApplication.translate("B_Options", "General Markup", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel11.setText(QtGui.QApplication.translate("B_Options", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel12.setText(QtGui.QApplication.translate("B_Options", "(cost + (cost * X%))", None, QtGui.QApplication.UnicodeUTF8))
        self.GenMarkup.setText(QtGui.QApplication.translate("B_Options", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox5.setTitle(QtGui.QApplication.translate("B_Options", "Price by gem tier", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel13.setText(QtGui.QApplication.translate("B_Options", "Tier:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel14.setText(QtGui.QApplication.translate("B_Options", "Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel15.setText(QtGui.QApplication.translate("B_Options", "(cost + X)", None, QtGui.QApplication.UnicodeUTF8))
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
        self.TierPrice.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TierInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.GroupBox6.setTitle(QtGui.QApplication.translate("B_Options", "Per hour", None, QtGui.QApplication.UnicodeUTF8))
        self.HourInclude.setText(QtGui.QApplication.translate("B_Options", "Include", None, QtGui.QApplication.UnicodeUTF8))
        self.HourPrice.setText(QtGui.QApplication.translate("B_Options", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel2_4.setText(QtGui.QApplication.translate("B_Options", "All numbers (except percentages) are in amounts of Gold.", None, QtGui.QApplication.UnicodeUTF8))
        self.CostInPrice.setText(QtGui.QApplication.translate("B_Options", "Include cost in price", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.Price), QtGui.QApplication.translate("B_Options", "Price", None, QtGui.QApplication.UnicodeUTF8))
