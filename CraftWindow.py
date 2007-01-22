# CraftWindow.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from B_CraftWindow import *
from constants import *
import SC

class CraftWindow(QDialog, Ui_B_CraftWindow):
    def __init__(self,parent = None,name = None,modal = False,fl = Qt.Widget):
        QDialog.__init__(self,parent,fl)
        Ui_B_CraftWindow.setupUi(self,self)
        if (name):
            self.setObjectName(name)
        if (modal):
            self.setModal(modal)
        self.gems = []
        self.GemName = []
        self.GemCost = []
        self.GemMakes = []
        self.GemTime = []
        for i in range (0, 4):
            idx = i + 1
            self.GemName.append(getattr(self, 'Gem%dName' % idx))
            self.GemCost.append(getattr(self, 'Gem%dCost' % idx))
            self.GemMakes.append(getattr(self, 'Gem%dMakes' % idx))
            # Hide '0' values
            self.GemMakes[i].setSpecialValueText(" ")
            self.connect(self.GemMakes[i],SIGNAL("valueChanged(int)"),self.RemakeChanged)
            self.GemTime.append(getattr(self, 'Gem%dTime' % idx))
            self.connect(self.GemTime[i],SIGNAL("textChanged(const QString&)"),self.TimeChanged)
        self.connect(self.Close,SIGNAL("clicked()"),self.CloseWindow)
        self.parent = parent

    def loadgems(self, gems):
        materials = { 'Gems': { }, 'Dusts' : { }, 'Liquids' : { } }
        for slot in range(0, 4):
            while slot < len(gems) and (gems[slot].type() == 'Unused' 
                                     or gems[slot].slotType() != 'player'):
                del gems[slot]
        self.gems = gems
        for slot in range(0, 4):
            self.GemMakes[slot].setVisible(slot < len(gems))
            self.GemTime[slot].setVisible(slot < len(gems))
            self.GemCost[slot].setVisible(slot < len(gems))
            self.GemName[slot].setVisible(slot < len(gems))

            if slot >= len(gems):
                continue

            if (gems[slot].done() == '1'):
                nummakes = int(gems[slot].remakes()) + 1
            else:
                nummakes = 0
            self.GemMakes[slot].setValue(nummakes)

            self.GemName[slot].setText(gems[slot].gemName(self.parent.realm))

            gemamount = gems[slot].amount()
            
            self.GemTime[slot].setText(gems[slot].time())
            self.GemCost[slot].setText(SC.formatCost(gems[slot].gemCost()))
            
            self.GemMakes[slot].setValue(nummakes)
            self.GemName[slot].setText(gems[slot].gemName(self.parent.realm))
        self.computeMaterials()

    def computeMaterials(self):
        materials = { 'Used' : { 'Gems' : { }, 'Dusts' : {}, 'Liquids': {} },
            'Expected' : { 'Gems' : { }, 'Dusts' : {}, 'Liquids': {} } }
        totalcost = 0
        for slot in range(0, 4):
            if (slot >= len(self.gems)): continue
            if (self.gems[slot].done() == '1'):
                nummakes = int(self.gems[slot].remakes()) + 1
            else:
                nummakes = 0
            totalcost += self.gems[slot].gemCost() * nummakes
            for mattype, matl in self.gems[slot].gemMaterials(self.parent.realm).items():
                for mat, val in matl.items():
                    if (nummakes) > 0:
                        if materials['Used'][mattype].has_key(mat):
                            materials['Used'][mattype][mat] += val * nummakes
                        else:
                            materials['Used'][mattype][mat] = val * nummakes
                    if materials['Expected'][mattype].has_key(mat):
                        materials['Expected'][mattype][mat] += val
                    else:
                        materials['Expected'][mattype][mat] = val
        self.TotalCost.setText(SC.formatCost(totalcost))
        for matctl, matlist in ((self.MatsUsed, materials['Used'],),
                                (self.MatsExpected, materials['Expected'],),):
            matctl.clear()
            for mat in MaterialGems:
                if (matlist['Gems'].has_key(mat)):
                    matctl.append("%d %s Gem" % (matlist['Gems'][mat], mat))
            for mattype in ('Liquids', 'Dusts',):
                matsorted = list(matlist[mattype].items())
                matsorted.sort()
                for mat, val in matsorted:
                    matctl.append("%d %s" % (val, mat))

    def RemakeChanged(self, val):
        i = int(self.sender().objectName()[3]) - 1
        if val > 0:
            self.gems[i].setDone('1')
            self.gems[i].setRemakes(str(val - 1))
        else:
            self.gems[i].setDone('0')
            self.gems[i].setRemakes('0')
        self.computeMaterials()

    def TimeChanged(self,a0):
        i = int(self.sender().objectName()[3]) - 1
        self.gems[i].setTime(self.GemTime[i].text())

    def CloseWindow(self):
        self.done(1)

