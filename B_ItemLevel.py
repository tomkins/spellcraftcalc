# Form implementation generated from reading ui file 'ItemLevel.ui'
#
# Created: Sun Apr 4 17:55:22 2004
#      by: The Python User Interface Compiler (pyuic) 3.8
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_ItemLevel(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if name == None:
            self.setName('B_ItemLevel')

        self.resize(235,158)
        self.setCaption(self.tr("Item Level"))

        self.ButtonGroup3 = QButtonGroup(self,'ButtonGroup3')
        self.ButtonGroup3.setGeometry(QRect(20,9,117,111))
        self.ButtonGroup3.setLineWidth(0)
        self.ButtonGroup3.setTitle(self.tr(""))

        self.Armor = QRadioButton(self.ButtonGroup3,'Armor')
        self.Armor.setGeometry(QRect(3,2,85,20))
        self.Armor.setText(self.tr("Armor"))
        self.Armor.setChecked(1)

        self.ClothArmor = QRadioButton(self.ButtonGroup3,'ClothArmor')
        self.ClothArmor.setGeometry(QRect(3,23,85,20))
        self.ClothArmor.setText(self.tr("Cloth Armor"))

        self.Weapon = QRadioButton(self.ButtonGroup3,'Weapon')
        self.Weapon.setGeometry(QRect(3,45,85,20))
        self.Weapon.setText(self.tr("Weapon"))

        self.Shield = QRadioButton(self.ButtonGroup3,'Shield')
        self.Shield.setGeometry(QRect(3,66,85,20))
        self.Shield.setText(self.tr("Shield"))

        self.ReinforcedShield = QRadioButton(self.ButtonGroup3,'ReinforcedShield')
        self.ReinforcedShield.setGeometry(QRect(3,87,108,20))
        self.ReinforcedShield.setText(self.tr("Reinforced Sheild"))

        self.TextLabel1 = QLabel(self,'TextLabel1')
        self.TextLabel1.setGeometry(QRect(151,14,53,13))
        self.TextLabel1.setText(self.tr("AF or DPS"))

        self.OK = QPushButton(self,'OK')
        self.OK.setGeometry(QRect(30,124,81,26))
        self.OK.setText(self.tr("OK"))

        self.Cancel = QPushButton(self,'Cancel')
        self.Cancel.setGeometry(QRect(130,124,79,26))
        self.Cancel.setText(self.tr("Cancel"))

        self.ShieldType = QComboBox(0,self,'ShieldType')
        self.ShieldType.setGeometry(QRect(105,61,113,22))

        self.AFDPS = QLineEdit(self,'AFDPS')
        self.AFDPS.setGeometry(QRect(140,31,74,22))

        self.connect(self.ClothArmor,SIGNAL('clicked()'),self.TypeChanged)
        self.connect(self.Weapon,SIGNAL('clicked()'),self.TypeChanged)
        self.connect(self.Shield,SIGNAL('clicked()'),self.TypeChanged)
        self.connect(self.ReinforcedShield,SIGNAL('clicked()'),self.TypeChanged)
        self.connect(self.OK,SIGNAL('clicked()'),self.OK_pressed)
        self.connect(self.Cancel,SIGNAL('clicked()'),self.Cancel_pressed)
        self.connect(self.AFDPS,SIGNAL('textChanged(const QString&)'),self.FixInput)

    def Cancel_pressed(self):
        print 'B_ItemLevel.Cancel_pressed(): not implemented yet'

    def OK_pressed(self):
        print 'B_ItemLevel.OK_pressed(): not implemented yet'

    def TypeChanged(self):
        print 'B_ItemLevel.TypeChanged(): not implemented yet'

    def FixInput(self,a0):
        print 'B_ItemLevel.FixInput(const QString&): not implemented yet'
