# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QueryBox.ui'
#
# Created: Sun Feb  4 10:11:58 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_B_QueryBox(object):
    def setupUi(self, B_QueryBox):
        B_QueryBox.setObjectName("B_QueryBox")
        B_QueryBox.resize(QtCore.QSize(QtCore.QRect(0,0,255,49).size()).expandedTo(B_QueryBox.minimumSizeHint()))

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(5),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(B_QueryBox.sizePolicy().hasHeightForWidth())
        B_QueryBox.setSizePolicy(sizePolicy)
        B_QueryBox.setMinimumSize(QtCore.QSize(0,0))
        B_QueryBox.setMaximumSize(QtCore.QSize(16777215,16777215))

        self.hboxlayout = QtGui.QHBoxLayout(B_QueryBox)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.queryLabel = QtGui.QLabel(B_QueryBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queryLabel.sizePolicy().hasHeightForWidth())
        self.queryLabel.setSizePolicy(sizePolicy)
        self.queryLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.queryLabel.setObjectName("queryLabel")
        self.hboxlayout1.addWidget(self.queryLabel)

        self.statusLabel = QtGui.QLabel(B_QueryBox)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(4),QtGui.QSizePolicy.Policy(5))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusLabel.sizePolicy().hasHeightForWidth())
        self.statusLabel.setSizePolicy(sizePolicy)
        self.statusLabel.setMinimumSize(QtCore.QSize(20,0))
        self.statusLabel.setMaximumSize(QtCore.QSize(20,16777215))
        self.statusLabel.setObjectName("statusLabel")
        self.hboxlayout1.addWidget(self.statusLabel)
        self.hboxlayout.addLayout(self.hboxlayout1)

        self.retranslateUi(B_QueryBox)
        QtCore.QMetaObject.connectSlotsByName(B_QueryBox)

    def retranslateUi(self, B_QueryBox):
        B_QueryBox.setWindowTitle(QtGui.QApplication.translate("B_QueryBox", "Querying...", None, QtGui.QApplication.UnicodeUTF8))
        self.queryLabel.setText(QtGui.QApplication.translate("B_QueryBox", "Querying the database", None, QtGui.QApplication.UnicodeUTF8))

