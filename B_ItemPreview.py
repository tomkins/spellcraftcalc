# Form implementation generated from reading ui file 'ItemPreview.ui'
#
# Created: Sun Apr 4 17:55:23 2004
#      by: The Python User Interface Compiler (pyuic) 3.8
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_ItemPreview(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if name == None:
            self.setName('B_ItemPreview')

        self.resize(215,189)
        self.setSizePolicy(QSizePolicy(1,1,self.sizePolicy().hasHeightForWidth()))
        f = QFont(self.font())
        f.setFamily('Arial')
        self.setFont(f)
        self.setCaption(self.tr("Form1"))

        self.GroupBox1 = QGroupBox(self,'GroupBox1')
        self.GroupBox1.setGeometry(QRect(1,-2,210,111))
        self.GroupBox1.setSizePolicy(QSizePolicy(0,0,self.GroupBox1.sizePolicy().hasHeightForWidth()))
        GroupBox1_font = QFont(self.GroupBox1.font())
        self.GroupBox1.setFont(GroupBox1_font)
        self.GroupBox1.setTitle(self.tr("Stats"))

        self.Stat1 = QLabel(self.GroupBox1,'Stat1')
        self.Stat1.setGeometry(QRect(8,14,191,16))
        self.Stat1.setSizePolicy(QSizePolicy(3,3,self.Stat1.sizePolicy().hasHeightForWidth()))
        self.Stat1.setText(self.tr("[stat1]"))

        self.Stat2 = QLabel(self.GroupBox1,'Stat2')
        self.Stat2.setGeometry(QRect(8,29,191,16))
        self.Stat2.setText(self.tr("[stat2]"))

        self.Stat3 = QLabel(self.GroupBox1,'Stat3')
        self.Stat3.setGeometry(QRect(8,44,193,16))
        self.Stat3.setMinimumSize(QSize(193,0))
        self.Stat3.setText(self.tr("[stat3]"))

        self.Stat4 = QLabel(self.GroupBox1,'Stat4')
        self.Stat4.setGeometry(QRect(8,59,193,16))
        self.Stat4.setMinimumSize(QSize(193,14))
        self.Stat4.setText(self.tr("[stat4]"))

        self.Stat5 = QLabel(self.GroupBox1,'Stat5')
        self.Stat5.setGeometry(QRect(8,74,191,16))
        self.Stat5.setText(self.tr("[stat5]"))

        self.Stat6 = QLabel(self.GroupBox1,'Stat6')
        self.Stat6.setGeometry(QRect(8,90,191,16))
        self.Stat6.setText(self.tr("[stat6]"))

        self.GroupBox2 = QGroupBox(self,'GroupBox2')
        self.GroupBox2.setGeometry(QRect(2,109,209,79))
        self.GroupBox2.setSizePolicy(QSizePolicy(0,0,self.GroupBox2.sizePolicy().hasHeightForWidth()))
        self.GroupBox2.setTitle(self.tr("General Info"))

        self.TextLabel4 = QLabel(self.GroupBox2,'TextLabel4')
        self.TextLabel4.setGeometry(QRect(6,16,54,16))
        self.TextLabel4.setText(self.tr("Item Name:"))

        self.ItemName = QLabel(self.GroupBox2,'ItemName')
        self.ItemName.setGeometry(QRect(62,16,145,16))
        self.ItemName.setText(self.tr("[Name]"))

        self.ItemAF = QLabel(self.GroupBox2,'ItemAF')
        self.ItemAF.setGeometry(QRect(145,31,59,13))
        self.ItemAF.setText(self.tr("[dps/af]"))

        self.ItemLevel = QLabel(self.GroupBox2,'ItemLevel')
        self.ItemLevel.setGeometry(QRect(42,29,34,16))
        self.ItemLevel.setText(self.tr("[level]"))

        self.TextLabel8 = QLabel(self.GroupBox2,'TextLabel8')
        self.TextLabel8.setGeometry(QRect(97,29,47,16))
        self.TextLabel8.setText(self.tr("DPS/AF:"))

        self.TextLabel9 = QLabel(self.GroupBox2,'TextLabel9')
        self.TextLabel9.setGeometry(QRect(98,44,37,16))
        self.TextLabel9.setText(self.tr("Bonus:"))

        self.ItemQua = QLabel(self.GroupBox2,'ItemQua')
        self.ItemQua.setGeometry(QRect(48,44,35,16))
        self.ItemQua.setText(self.tr("[qua]"))

        self.TextLabel7 = QLabel(self.GroupBox2,'TextLabel7')
        self.TextLabel7.setGeometry(QRect(6,44,39,16))
        self.TextLabel7.setText(self.tr("Quality:"))

        self.TextLabel6 = QLabel(self.GroupBox2,'TextLabel6')
        self.TextLabel6.setGeometry(QRect(6,29,32,16))
        self.TextLabel6.setText(self.tr("Level:"))

        self.ItemBonus = QLabel(self.GroupBox2,'ItemBonus')
        self.ItemBonus.setGeometry(QRect(137,44,47,16))
        self.ItemBonus.setText(self.tr("[bonus]"))

        self.TextLabel10 = QLabel(self.GroupBox2,'TextLabel10')
        self.TextLabel10.setGeometry(QRect(98,59,31,16))
        self.TextLabel10.setText(self.tr("Utility:"))

        self.ItemUtility = QLabel(self.GroupBox2,'ItemUtility')
        self.ItemUtility.setGeometry(QRect(133,59,53,16))
        self.ItemUtility.setText(self.tr("[utility]"))

    def event(self,ev):
        ret = QWidget.event(self,ev)

        if ev.type() == QEvent.ApplicationFontChange:
            GroupBox1_font = QFont(self.GroupBox1.font())
            self.GroupBox1.setFont(GroupBox1_font)

        return ret
