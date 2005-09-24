# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ItemPreview.ui'
#
# Created: Sat Sep 24 00:50:59 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.15
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_ItemPreview(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("B_ItemPreview")

        self.setSizePolicy(QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum,0,0,self.sizePolicy().hasHeightForWidth()))
        f = QFont(self.font())
        f.setFamily("Arial")
        self.setFont(f)


        self.GroupBox1 = QGroupBox(self,"GroupBox1")
        self.GroupBox1.setGeometry(QRect(1,-2,210,111))
        self.GroupBox1.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.GroupBox1.sizePolicy().hasHeightForWidth()))
        GroupBox1_font = QFont(self.GroupBox1.font())
        self.GroupBox1.setFont(GroupBox1_font)

        self.Stat1 = QLabel(self.GroupBox1,"Stat1")
        self.Stat1.setGeometry(QRect(8,14,191,16))
        self.Stat1.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding,QSizePolicy.MinimumExpanding,0,0,self.Stat1.sizePolicy().hasHeightForWidth()))

        self.Stat2 = QLabel(self.GroupBox1,"Stat2")
        self.Stat2.setGeometry(QRect(8,29,191,16))

        self.Stat3 = QLabel(self.GroupBox1,"Stat3")
        self.Stat3.setGeometry(QRect(8,44,193,16))
        self.Stat3.setMinimumSize(QSize(193,0))

        self.Stat4 = QLabel(self.GroupBox1,"Stat4")
        self.Stat4.setGeometry(QRect(8,59,193,16))
        self.Stat4.setMinimumSize(QSize(193,14))

        self.Stat5 = QLabel(self.GroupBox1,"Stat5")
        self.Stat5.setGeometry(QRect(8,74,191,16))

        self.Stat6 = QLabel(self.GroupBox1,"Stat6")
        self.Stat6.setGeometry(QRect(8,90,191,16))

        self.GroupBox2 = QGroupBox(self,"GroupBox2")
        self.GroupBox2.setGeometry(QRect(2,109,209,79))
        self.GroupBox2.setSizePolicy(QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed,0,0,self.GroupBox2.sizePolicy().hasHeightForWidth()))

        self.TextLabel4 = QLabel(self.GroupBox2,"TextLabel4")
        self.TextLabel4.setGeometry(QRect(6,16,54,16))

        self.ItemName = QLabel(self.GroupBox2,"ItemName")
        self.ItemName.setGeometry(QRect(62,16,145,16))

        self.ItemAF = QLabel(self.GroupBox2,"ItemAF")
        self.ItemAF.setGeometry(QRect(145,31,59,13))

        self.ItemLevel = QLabel(self.GroupBox2,"ItemLevel")
        self.ItemLevel.setGeometry(QRect(42,29,34,16))

        self.TextLabel8 = QLabel(self.GroupBox2,"TextLabel8")
        self.TextLabel8.setGeometry(QRect(97,29,47,16))

        self.TextLabel9 = QLabel(self.GroupBox2,"TextLabel9")
        self.TextLabel9.setGeometry(QRect(98,44,37,16))

        self.ItemQua = QLabel(self.GroupBox2,"ItemQua")
        self.ItemQua.setGeometry(QRect(48,44,35,16))

        self.TextLabel7 = QLabel(self.GroupBox2,"TextLabel7")
        self.TextLabel7.setGeometry(QRect(6,44,39,16))

        self.TextLabel6 = QLabel(self.GroupBox2,"TextLabel6")
        self.TextLabel6.setGeometry(QRect(6,29,32,16))

        self.ItemBonus = QLabel(self.GroupBox2,"ItemBonus")
        self.ItemBonus.setGeometry(QRect(137,44,47,16))

        self.TextLabel10 = QLabel(self.GroupBox2,"TextLabel10")
        self.TextLabel10.setGeometry(QRect(98,59,31,16))

        self.ItemUtility = QLabel(self.GroupBox2,"ItemUtility")
        self.ItemUtility.setGeometry(QRect(133,59,53,16))

        self.languageChange()

        self.resize(QSize(215,189).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Form1"))
        self.GroupBox1.setTitle(self.__tr("Stats"))
        self.Stat1.setText(self.__tr("[stat1]"))
        self.Stat2.setText(self.__tr("[stat2]"))
        self.Stat3.setText(self.__tr("[stat3]"))
        self.Stat4.setText(self.__tr("[stat4]"))
        self.Stat5.setText(self.__tr("[stat5]"))
        self.Stat6.setText(self.__tr("[stat6]"))
        self.GroupBox2.setTitle(self.__tr("General Info"))
        self.TextLabel4.setText(self.__tr("Item Name:"))
        self.ItemName.setText(self.__tr("[Name]"))
        self.ItemAF.setText(self.__tr("[dps/af]"))
        self.ItemLevel.setText(self.__tr("[level]"))
        self.TextLabel8.setText(self.__tr("DPS/AF:"))
        self.TextLabel9.setText(self.__tr("Bonus:"))
        self.ItemQua.setText(self.__tr("[qua]"))
        self.TextLabel7.setText(self.__tr("Quality:"))
        self.TextLabel6.setText(self.__tr("Level:"))
        self.ItemBonus.setText(self.__tr("[bonus]"))
        self.TextLabel10.setText(self.__tr("Utility:"))
        self.ItemUtility.setText(self.__tr("[utility]"))


    def __tr(self,s,c = None):
        return qApp.translate("B_ItemPreview",s,c)
