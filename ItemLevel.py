from qt import *
from constants import *
from B_ItemLevel import *
import re

class ItemLevel(B_ItemLevel):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        B_ItemLevel.__init__(self,parent,name,modal,fl)
        self.ShieldType.insertStrList(list(ShieldTypes))
        self.AFDPS.setText('102')
        self.level = 51
        self.ShieldType.setEnabled(0)

    def OK_pressed(self):
        self.computeLevel()
        self.done(self.level)

    def computeLevel(self):
        if self.Armor.isChecked():
            self.level = int(str(self.AFDPS.text())) / 2
        elif self.ClothArmor.isChecked():
            self.level = int(str(self.AFDPS.text()))
        elif self.Weapon.isChecked():
            self.level = int((float(str(self.AFDPS.text())) - 1.2) / 0.3)
        elif self.Shield.isChecked():
            if self.ShieldType.currentItem() == 0:
                self.level = 2
            else:
                self.level = self.ShieldType.currentItem() * 5
        elif self.ReinforcedShield.isChecked():
            self.level = (self.ShieldType.currentItem() + 1) * 5 + 1
            
    def TypeChanged(self):
        if self.Armor.isChecked():
            self.AFDPS.setText('102')
            self.AFDPS.setEnabled(1)
            self.ShieldType.setEnabled(0)
        elif self.ClothArmor.isChecked():
            self.AFDPS.setText('51')
            self.AFDPS.setEnabled(1)
            self.ShieldType.setEnabled(0)
        elif self.Weapon.isChecked():
            self.AFDPS.setText('16.5')
            self.AFDPS.setEnabled(1)
            self.ShieldType.setEnabled(0)
        elif self.Shield.isChecked():
            self.AFDPS.setEnabled(0)
            self.ShieldType.setEnabled(1)
        elif self.ReinforcedShield.isChecked():
            self.AFDPS.setEnabled(0)
            self.ShieldType.setEnabled(1)
        
    def Cancel_pressed(self):
        self.done(-1)

    def FixInput(self,a0):
        esc = re.sub('[^\d.]', '', str(self.AFDPS.text()))
        self.AFDPS.setText(esc)
