# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ItemLevel.ui'
#
# Created: Fri Nov 25 02:51:32 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.15
#
# WARNING! All changes made in this file will be lost!


from qt import *
#Import the Custom Widgets
from SearchingCombo import *


class B_ItemLevel(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("B_ItemLevel")



        self.ButtonGroup3 = QButtonGroup(self,"ButtonGroup3")
        self.ButtonGroup3.setGeometry(QRect(6,6,117,111))
        self.ButtonGroup3.setLineWidth(0)

        self.Armor = QRadioButton(self.ButtonGroup3,"Armor")
        self.Armor.setGeometry(QRect(5,2,85,20))
        self.Armor.setChecked(1)

        self.ClothArmor = QRadioButton(self.ButtonGroup3,"ClothArmor")
        self.ClothArmor.setGeometry(QRect(5,23,85,20))

        self.Weapon = QRadioButton(self.ButtonGroup3,"Weapon")
        self.Weapon.setGeometry(QRect(3,45,85,20))

        self.Shield = QRadioButton(self.ButtonGroup3,"Shield")
        self.Shield.setGeometry(QRect(5,66,85,20))

        self.ReinforcedShield = QRadioButton(self.ButtonGroup3,"ReinforcedShield")
        self.ReinforcedShield.setGeometry(QRect(5,87,108,20))

        self.LevelLabel = QLabel(self,"LevelLabel")
        self.LevelLabel.setGeometry(QRect(130,10,45,16))

        self.Level = QLineEdit(self,"Level")
        self.Level.setGeometry(QRect(185,7,60,22))

        self.AFDPSLabel = QLabel(self,"AFDPSLabel")
        self.AFDPSLabel.setGeometry(QRect(130,53,45,16))

        self.AFDPS = QLineEdit(self,"AFDPS")
        self.AFDPS.setGeometry(QRect(185,50,60,22))

        self.ShieldType = SearchingCombo(self,"ShieldType")
        self.ShieldType.setGeometry(QRect(135,93,110,22))

        self.OK = QPushButton(self,"OK")
        self.OK.setGeometry(QRect(11,124,58,26))

        self.Cancel = QPushButton(self,"Cancel")
        self.Cancel.setGeometry(QRect(187,124,58,26))

        self.languageChange()

        self.resize(QSize(250,158).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.Armor,SIGNAL("clicked()"),self.TypeChanged)
        self.connect(self.ClothArmor,SIGNAL("clicked()"),self.TypeChanged)
        self.connect(self.Weapon,SIGNAL("clicked()"),self.TypeChanged)
        self.connect(self.Shield,SIGNAL("clicked()"),self.TypeChanged)
        self.connect(self.ReinforcedShield,SIGNAL("clicked()"),self.TypeChanged)
        self.connect(self.Level,SIGNAL("textChanged(const QString&)"),self.LevelChanged)
        self.connect(self.Level,SIGNAL("lostFocus()"),self.LevelDone)
        self.connect(self.AFDPS,SIGNAL("textChanged(const QString&)"),self.AFDPSChanged)
        self.connect(self.AFDPS,SIGNAL("lostFocus()"),self.AFDPSDone)
        self.connect(self.ShieldType,SIGNAL("activated(const QString&)"),self.ShieldChanged)
        self.connect(self.OK,SIGNAL("clicked()"),self.OkClicked)
        self.connect(self.Cancel,SIGNAL("clicked()"),self.CancelClicked)


    def languageChange(self):
        self.setCaption(self.__tr("Item Level"))
        self.ButtonGroup3.setTitle(QString.null)
        self.Armor.setText(self.__tr("Armor"))
        self.ClothArmor.setText(self.__tr("Cloth Armor"))
        self.Weapon.setText(self.__tr("Weapon"))
        self.Shield.setText(self.__tr("Shield"))
        self.ReinforcedShield.setText(self.__tr("Reinforced Sheild"))
        self.LevelLabel.setText(self.__tr("Level:"))
        self.AFDPSLabel.setText(self.__tr("AF/DPS:"))
        self.OK.setText(self.__tr("OK"))
        self.Cancel.setText(self.__tr("Cancel"))


    def TypeChanged(self):
        print "B_ItemLevel.TypeChanged(): Not implemented yet"

    def LevelChanged(self,a0):
        print "B_ItemLevel.LevelChanged(const QString&): Not implemented yet"

    def LevelDone(self):
        print "B_ItemLevel.LevelDone(): Not implemented yet"

    def AFDPSChanged(self,a0):
        print "B_ItemLevel.AFDPSChanged(const QString&): Not implemented yet"

    def AFDPSDone(self):
        print "B_ItemLevel.AFDPSDone(): Not implemented yet"

    def ShieldChanged(self,a0):
        print "B_ItemLevel.ShieldChanged(const QString&): Not implemented yet"

    def OkClicked(self):
        print "B_ItemLevel.OkClicked(): Not implemented yet"

    def CancelClicked(self):
        print "B_ItemLevel.CancelClicked(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("B_ItemLevel",s,c)
