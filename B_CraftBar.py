# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CraftBar.ui'
#
# Created: Thu Oct  5 08:47:42 2006
#      by: PyQt4 UI code generator 4.0.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui, Qt3Support

class Ui_B_CraftBar(object):
    def setupUi(self, B_CraftBar):
        B_CraftBar.setObjectName("B_CraftBar")
        B_CraftBar.resize(QtCore.QSize(QtCore.QRect(0,0,594,563).size()).expandedTo(B_CraftBar.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(B_CraftBar)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Maximum,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.TextLabel1 = QtGui.QLabel(B_CraftBar)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLabel1.sizePolicy().hasHeightForWidth())
        self.TextLabel1.setSizePolicy(sizePolicy)
        self.TextLabel1.setObjectName("TextLabel1")
        self.hboxlayout.addWidget(self.TextLabel1)

        self.DaocPath = QtGui.QLineEdit(B_CraftBar)
        self.DaocPath.setObjectName("DaocPath")
        self.hboxlayout.addWidget(self.DaocPath)

        self.PathSelectButton = QtGui.QPushButton(B_CraftBar)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(0),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PathSelectButton.sizePolicy().hasHeightForWidth())
        self.PathSelectButton.setSizePolicy(sizePolicy)
        self.PathSelectButton.setMinimumSize(QtCore.QSize(28,28))
        self.PathSelectButton.setMaximumSize(QtCore.QSize(28,28))
        self.PathSelectButton.setBaseSize(QtCore.QSize(28,28))
        self.PathSelectButton.setObjectName("PathSelectButton")
        self.hboxlayout.addWidget(self.PathSelectButton)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Maximum,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.vboxlayout1.addLayout(self.hboxlayout)

        self.TextLabel2 = QtGui.QLabel(B_CraftBar)
        self.TextLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.TextLabel2.setObjectName("TextLabel2")
        self.vboxlayout1.addWidget(self.TextLabel2)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.GroupBox20 = QtGui.QGroupBox(B_CraftBar)
        self.GroupBox20.setObjectName("GroupBox20")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.GroupBox20)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.vboxlayout4 = QtGui.QVBoxLayout()
        self.vboxlayout4.setMargin(0)
        self.vboxlayout4.setSpacing(6)
        self.vboxlayout4.setObjectName("vboxlayout4")

        self.TextLabel4 = QtGui.QLabel(self.GroupBox20)
        self.TextLabel4.setObjectName("TextLabel4")
        self.vboxlayout4.addWidget(self.TextLabel4)

        self.CharList = QtGui.QTableView(self.GroupBox20)
        self.CharList.setObjectName("CharList")
        self.vboxlayout4.addWidget(self.CharList)
        self.vboxlayout3.addLayout(self.vboxlayout4)
        self.vboxlayout2.addWidget(self.GroupBox20)

        self.TextLabel14 = QtGui.QLabel(B_CraftBar)

        font = QtGui.QFont(self.TextLabel14.font())
        font.setFamily("Lucida Grande")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.TextLabel14.setFont(font)
        self.TextLabel14.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.TextLabel14.setObjectName("TextLabel14")
        self.vboxlayout2.addWidget(self.TextLabel14)

        spacerItem2 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem2)
        self.hboxlayout1.addLayout(self.vboxlayout2)

        self.vboxlayout5 = QtGui.QVBoxLayout()
        self.vboxlayout5.setMargin(0)
        self.vboxlayout5.setSpacing(6)
        self.vboxlayout5.setObjectName("vboxlayout5")

        self.GroupBox19 = QtGui.QGroupBox(B_CraftBar)
        self.GroupBox19.setObjectName("GroupBox19")

        self.vboxlayout6 = QtGui.QVBoxLayout(self.GroupBox19)
        self.vboxlayout6.setMargin(9)
        self.vboxlayout6.setSpacing(6)
        self.vboxlayout6.setObjectName("vboxlayout6")

        self.vboxlayout7 = QtGui.QVBoxLayout()
        self.vboxlayout7.setMargin(0)
        self.vboxlayout7.setSpacing(6)
        self.vboxlayout7.setObjectName("vboxlayout7")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setMargin(0)
        self.gridlayout.setSpacing(0)
        self.gridlayout.setObjectName("gridlayout")

        self.FeetSelect = QtGui.QCheckBox(self.GroupBox19)
        self.FeetSelect.setObjectName("FeetSelect")
        self.gridlayout.addWidget(self.FeetSelect,2,1,1,1)

        self.THSelect = QtGui.QCheckBox(self.GroupBox19)
        self.THSelect.setObjectName("THSelect")
        self.gridlayout.addWidget(self.THSelect,2,2,1,1)

        self.ArmsSelect = QtGui.QCheckBox(self.GroupBox19)
        self.ArmsSelect.setObjectName("ArmsSelect")
        self.gridlayout.addWidget(self.ArmsSelect,1,0,1,1)

        self.ChestSelect = QtGui.QCheckBox(self.GroupBox19)
        self.ChestSelect.setObjectName("ChestSelect")
        self.gridlayout.addWidget(self.ChestSelect,0,0,1,1)

        self.RHSelect = QtGui.QCheckBox(self.GroupBox19)
        self.RHSelect.setObjectName("RHSelect")
        self.gridlayout.addWidget(self.RHSelect,0,2,1,1)

        self.HeadSelect = QtGui.QCheckBox(self.GroupBox19)
        self.HeadSelect.setObjectName("HeadSelect")
        self.gridlayout.addWidget(self.HeadSelect,2,0,1,1)

        self.HandsSelect = QtGui.QCheckBox(self.GroupBox19)
        self.HandsSelect.setObjectName("HandsSelect")
        self.gridlayout.addWidget(self.HandsSelect,1,1,1,1)

        self.LegsSelect = QtGui.QCheckBox(self.GroupBox19)
        self.LegsSelect.setObjectName("LegsSelect")
        self.gridlayout.addWidget(self.LegsSelect,0,1,1,1)

        self.LHSelect = QtGui.QCheckBox(self.GroupBox19)
        self.LHSelect.setObjectName("LHSelect")
        self.gridlayout.addWidget(self.LHSelect,1,2,1,1)

        spacerItem3 = QtGui.QSpacerItem(76,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem3,3,0,1,1)

        self.RangedSelect = QtGui.QCheckBox(self.GroupBox19)
        self.RangedSelect.setObjectName("RangedSelect")
        self.gridlayout.addWidget(self.RangedSelect,3,1,1,1)

        spacerItem4 = QtGui.QSpacerItem(78,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem4,3,2,1,1)
        self.vboxlayout7.addLayout(self.gridlayout)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(6)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.TextLabel7 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel7.setObjectName("TextLabel7")
        self.hboxlayout2.addWidget(self.TextLabel7)

        self.HotbarNum = QtGui.QSpinBox(self.GroupBox19)
        self.HotbarNum.setMaximum(30)
        self.HotbarNum.setMinimum(1)
        self.HotbarNum.setObjectName("HotbarNum")
        self.hboxlayout2.addWidget(self.HotbarNum)

        spacerItem5 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem5)
        self.vboxlayout7.addLayout(self.hboxlayout2)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.TextLabel8 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TextLabel8.setObjectName("TextLabel8")
        self.hboxlayout3.addWidget(self.TextLabel8)

        self.HotbarPos = QtGui.QSpinBox(self.GroupBox19)
        self.HotbarPos.setMaximum(10)
        self.HotbarPos.setMinimum(1)
        self.HotbarPos.setObjectName("HotbarPos")
        self.hboxlayout3.addWidget(self.HotbarPos)

        spacerItem6 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem6)
        self.vboxlayout7.addLayout(self.hboxlayout3)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setSpacing(6)
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.TextLabel10 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel10.setObjectName("TextLabel10")
        self.hboxlayout4.addWidget(self.TextLabel10)

        self.EndBar = QtGui.QLabel(self.GroupBox19)
        self.EndBar.setObjectName("EndBar")
        self.hboxlayout4.addWidget(self.EndBar)

        self.TextLabel11 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel11.setObjectName("TextLabel11")
        self.hboxlayout4.addWidget(self.TextLabel11)

        self.EndPos = QtGui.QLabel(self.GroupBox19)
        self.EndPos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.EndPos.setObjectName("EndPos")
        self.hboxlayout4.addWidget(self.EndPos)
        self.vboxlayout7.addLayout(self.hboxlayout4)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setMargin(0)
        self.hboxlayout5.setSpacing(6)
        self.hboxlayout5.setObjectName("hboxlayout5")

        spacerItem7 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem7)

        self.TextLabel15 = QtGui.QLabel(self.GroupBox19)
        self.TextLabel15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TextLabel15.setObjectName("TextLabel15")
        self.hboxlayout5.addWidget(self.TextLabel15)

        self.NumGems = QtGui.QLabel(self.GroupBox19)
        self.NumGems.setObjectName("NumGems")
        self.hboxlayout5.addWidget(self.NumGems)

        spacerItem8 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem8)
        self.vboxlayout7.addLayout(self.hboxlayout5)
        self.vboxlayout6.addLayout(self.vboxlayout7)
        self.vboxlayout5.addWidget(self.GroupBox19)

        self.hboxlayout6 = QtGui.QHBoxLayout()
        self.hboxlayout6.setMargin(0)
        self.hboxlayout6.setSpacing(6)
        self.hboxlayout6.setObjectName("hboxlayout6")

        spacerItem9 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem9)

        self.LoadGemsButton = QtGui.QPushButton(B_CraftBar)
        self.LoadGemsButton.setObjectName("LoadGemsButton")
        self.hboxlayout6.addWidget(self.LoadGemsButton)

        spacerItem10 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout6.addItem(spacerItem10)
        self.vboxlayout5.addLayout(self.hboxlayout6)

        self.GroupBox21 = QtGui.QGroupBox(B_CraftBar)
        self.GroupBox21.setObjectName("GroupBox21")

        self.hboxlayout7 = QtGui.QHBoxLayout(self.GroupBox21)
        self.hboxlayout7.setMargin(9)
        self.hboxlayout7.setSpacing(6)
        self.hboxlayout7.setObjectName("hboxlayout7")

        self.TextLabel9 = QtGui.QLabel(self.GroupBox21)

        font = QtGui.QFont(self.TextLabel9.font())
        font.setFamily("Lucida Grande")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        self.TextLabel9.setFont(font)
        self.TextLabel9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.TextLabel9.setObjectName("TextLabel9")
        self.hboxlayout7.addWidget(self.TextLabel9)
        self.vboxlayout5.addWidget(self.GroupBox21)
        self.hboxlayout1.addLayout(self.vboxlayout5)
        self.vboxlayout1.addLayout(self.hboxlayout1)

        self.hboxlayout8 = QtGui.QHBoxLayout()
        self.hboxlayout8.setMargin(0)
        self.hboxlayout8.setSpacing(6)
        self.hboxlayout8.setObjectName("hboxlayout8")

        spacerItem11 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem11)

        self.PushButton19 = QtGui.QPushButton(B_CraftBar)
        self.PushButton19.setObjectName("PushButton19")
        self.hboxlayout8.addWidget(self.PushButton19)

        spacerItem12 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout8.addItem(spacerItem12)
        self.vboxlayout1.addLayout(self.hboxlayout8)
        self.vboxlayout.addLayout(self.vboxlayout1)

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
        self.GroupBox19.setTitle(QtGui.QApplication.translate("B_CraftBar", "Gems To Load", None, QtGui.QApplication.UnicodeUTF8))
        self.FeetSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Feet", None, QtGui.QApplication.UnicodeUTF8))
        self.THSelect.setText(QtGui.QApplication.translate("B_CraftBar", "2 Handed", None, QtGui.QApplication.UnicodeUTF8))
        self.ArmsSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Arms", None, QtGui.QApplication.UnicodeUTF8))
        self.ChestSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Chest", None, QtGui.QApplication.UnicodeUTF8))
        self.RHSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Right Hand", None, QtGui.QApplication.UnicodeUTF8))
        self.HeadSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Head", None, QtGui.QApplication.UnicodeUTF8))
        self.HandsSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Hands", None, QtGui.QApplication.UnicodeUTF8))
        self.LegsSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Legs", None, QtGui.QApplication.UnicodeUTF8))
        self.LHSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Left Hand", None, QtGui.QApplication.UnicodeUTF8))
        self.RangedSelect.setText(QtGui.QApplication.translate("B_CraftBar", "Ranged", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel7.setText(QtGui.QApplication.translate("B_CraftBar", "Hotbar # to Start At:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel8.setText(QtGui.QApplication.translate("B_CraftBar", "Hotbar Position to Start At:", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel10.setText(QtGui.QApplication.translate("B_CraftBar", "Ending Bar:", None, QtGui.QApplication.UnicodeUTF8))
        self.EndBar.setText(QtGui.QApplication.translate("B_CraftBar", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel11.setText(QtGui.QApplication.translate("B_CraftBar", "Position:", None, QtGui.QApplication.UnicodeUTF8))
        self.EndPos.setText(QtGui.QApplication.translate("B_CraftBar", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.TextLabel15.setText(QtGui.QApplication.translate("B_CraftBar", "Total Number of Gems to Load:", None, QtGui.QApplication.UnicodeUTF8))
        self.NumGems.setText(QtGui.QApplication.translate("B_CraftBar", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadGemsButton.setText(QtGui.QApplication.translate("B_CraftBar", "Load Gems", None, QtGui.QApplication.UnicodeUTF8))
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
        self.PushButton19.setText(QtGui.QApplication.translate("B_CraftBar", "Close", None, QtGui.QApplication.UnicodeUTF8))
