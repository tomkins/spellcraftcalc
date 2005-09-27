# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ItemLevel.ui'
#
# Created: Tue Sep 27 10:37:00 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.15
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_ItemLevel(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("B_ItemLevel")



        self.ButtonGroup3 = QButtonGroup(self,"ButtonGroup3")
        self.ButtonGroup3.setGeometry(QRect(20,9,117,111))
        self.ButtonGroup3.setLineWidth(0)

        self.Armor = QRadioButton(self.ButtonGroup3,"Armor")
        self.Armor.setGeometry(QRect(3,2,85,20))
        self.Armor.setChecked(1)

        self.ClothArmor = QRadioButton(self.ButtonGroup3,"ClothArmor")
        self.ClothArmor.setGeometry(QRect(3,23,85,20))

        self.Weapon = QRadioButton(self.ButtonGroup3,"Weapon")
        self.Weapon.setGeometry(QRect(3,45,85,20))

        self.Shield = QRadioButton(self.ButtonGroup3,"Shield")
        self.Shield.setGeometry(QRect(3,66,85,20))

        self.ReinforcedShield = QRadioButton(self.ButtonGroup3,"ReinforcedShield")
        self.ReinforcedShield.setGeometry(QRect(3,87,108,20))

        self.TextLabel1 = QLabel(self,"TextLabel1")
        self.TextLabel1.setGeometry(QRect(151,14,53,13))

        self.OK = QPushButton(self,"OK")
        self.OK.setGeometry(QRect(30,124,81,26))

        self.Cancel = QPushButton(self,"Cancel")
        self.Cancel.setGeometry(QRect(130,124,79,26))

        self.ShieldType = QComboBox(0,self,"ShieldType")
        self.ShieldType.setGeometry(QRect(105,61,113,22))

        self.AFDPS = QLineEdit(self,"AFDPS")
        self.AFDPS.setGeometry(QRect(140,31,74,22))

        self.languageChange()

        self.resize(QSize(235,158).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.ClothArmor,SIGNAL("clicked()"),self.TypeChanged)
        self.connect(self.Weapon,SIGNAL("clicked()"),self.TypeChanged)
        self.connect(self.Shield,SIGNAL("clicked()"),self.TypeChanged)
        self.connect(self.ReinforcedShield,SIGNAL("clicked()"),self.TypeChanged)
        self.connect(self.OK,SIGNAL("clicked()"),self.OK_pressed)
        self.connect(self.Cancel,SIGNAL("clicked()"),self.Cancel_pressed)
        self.connect(self.AFDPS,SIGNAL("textChanged(const QString&)"),self.FixInput)


    def languageChange(self):
        self.setCaption(self.__tr("Item Level"))
        self.ButtonGroup3.setTitle(QString.null)
        self.Armor.setText(self.__tr("Armor"))
        self.ClothArmor.setText(self.__tr("Cloth Armor"))
        self.Weapon.setText(self.__tr("Weapon"))
        self.Shield.setText(self.__tr("Shield"))
        self.ReinforcedShield.setText(self.__tr("Reinforced Sheild"))
        self.TextLabel1.setText(self.__tr("AF or DPS"))
        self.OK.setText(self.__tr("OK"))
        self.Cancel.setText(self.__tr("Cancel"))


    def Cancel_pressed(self):
        print "B_ItemLevel.Cancel_pressed(): Not implemented yet"

    def OK_pressed(self):
        print "B_ItemLevel.OK_pressed(): Not implemented yet"

    def TypeChanged(self):
        print "B_ItemLevel.TypeChanged(): Not implemented yet"

    def FixInput(self,a0):
        print "B_ItemLevel.FixInput(const QString&): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("B_ItemLevel",s,c)
