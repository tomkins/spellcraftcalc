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
        self.GemRemakes = []
        self.GemDone = []
        self.GemTime = []
        self.GemCost = []
        for i in range (0, 4):
            idx = i + 1
            self.GemRemakes.append(getattr(self, 'Gem%dRemakes' % idx))
            self.connect(self.GemRemakes[i],SIGNAL("valueChanged(int)"),self.RemakeChanged)
            self.GemDone.append(getattr(self, 'Gem%dDone' % idx))
            self.connect(self.GemDone[i],SIGNAL("clicked()"),self.GemClicked)
            self.GemTime.append(getattr(self, 'Gem%dTime' % idx))
            self.connect(self.GemTime[i],SIGNAL("textChanged(const QString&)"),self.TimeChanged)
            self.GemCost.append(getattr(self, 'Gem%dCost' % idx))
        self.connect(self.ExpMultiplier,SIGNAL("valueChanged(int)"),self.computeMaterials)
        self.connect(self.Close,SIGNAL("clicked()"),self.CloseWindow)
        self.currentItem = None
        self.totalCost = 0
        self.gemCosts = [0, 0, 0, 0]
        self.parent = parent

    def loadItem(self, item):
        self.currentItem = item
        materials = { 'Gems': { }, 'Dusts' : { }, 'Liquids' : { } }
        for slot in range(0, 4):
            gemqua = getattr(self, 'Gem%dQua' % (slot+1))
            gemname = getattr(self, 'Gem%dName' % (slot+1))
            gemcost = getattr(self, 'Gem%dCost' % (slot+1))
            gemtype = item.slot(slot).type()
            gemamount = item.slot(slot).amount()
            
            gemqua.setText('%s%%' % item.slot(slot).qua())
            self.GemTime[slot].setText(item.slot(slot).time())

            numremakes = int(item.slot(slot).remakes())
            self.gemCosts[slot] = item.slot(slot).gemCost(numremakes)
            self.totalCost += self.gemCosts[slot]
            gemcost.setText(SC.formatCost(self.gemCosts[slot]))
            
            if item.slot(slot).done() == '1':
                self.GemDone[slot].setChecked(1)

            self.GemRemakes[slot].setValue(numremakes)
            gemname.setText(item.slot(slot).gemName())

        self.TotalCost.setText(SC.formatCost(self.totalCost))
        self.ExpMultiplier.setValue(6)
        self.computeMaterials()

    def computeMaterials(self):
        materials = { 'Used' : { 'Gems' : { }, 'Dusts' : {}, 'Liquids': {} },
            'Expected' : { 'Gems' : { }, 'Dusts' : {}, 'Liquids': {} } }
        expmultiplier = int(self.ExpMultiplier.value())
        for slot in range(0, 4):
            numremakes = int(self.currentItem.slot(slot).remakes())
            done = int(self.currentItem.slot(slot).done())
            for mattype, matl in self.currentItem.slot(slot).gemMaterials().items():
                for mat, val in matl.items():
                    if materials['Used'][mattype].has_key(mat):
                        materials['Used'][mattype][mat] += val * (numremakes + 1)
                    else:
                        materials['Used'][mattype][mat] = val * (numremakes + 1)
                    if not done:
                        if materials['Expected'][mattype].has_key(mat):
                            materials['Expected'][mattype][mat] += val * (expmultiplier)
                        else:
                            materials['Expected'][mattype][mat] = val * (expmultiplier)
        self.MatsUsed.clear()
        self.MatsExpected.clear()
        for mat, val in materials['Used']['Gems'].items():
            self.MatsUsed.append("%d %s Gem" % (val, mat))
        for mat, val in materials['Used']['Dusts'].items():
            self.MatsUsed.append("%d %s" % (val, mat))
        for mat, val in materials['Used']['Liquids'].items():
            self.MatsUsed.append("%d %s" % (val, mat))
        for mat, val in materials['Expected']['Gems'].items():
            self.MatsExpected.append("%d %s Gem" % (val, mat))
        for mat, val in materials['Expected']['Dusts'].items():
            self.MatsExpected.append("%d %s" % (val, mat))
        for mat, val in materials['Expected']['Liquids'].items():
            self.MatsExpected.append("%d %s" % (val, mat))

    def recomputeCosts(self, slotindex, val):
        self.gemCosts[slotindex] = self.currentItem.slot(slotindex).gemCost(val)
        self.GemCost[slotindex].setText(SC.formatCost(self.gemCosts[slotindex]))
        self.totalCost = 0
        for slot in range(0, 4):
            self.totalCost += self.gemCosts[slot]
        self.TotalCost.setText(SC.formatCost(self.totalCost))
        
    def GemClicked(self):
        i = int(self.sender().objectName()[3]) - 1
        if self.GemDone[i].isChecked():
            done = '1'
        else:
            done = '0'
        self.currentItem.slot(i).setDone(done)
        self.computeMaterials()

    def RemakeChanged(self, val):
        i = int(self.sender().objectName()[3]) - 1
        self.currentItem.slot(i).setRemakes(self.GemRemakes[i].text())
        self.recomputeCosts(i, val)
        self.computeMaterials()

    def TimeChanged(self,a0):
        i = int(self.sender().objectName()[3]) - 1
        self.currentItem.slot(i).setTime(self.GemTime[i].text())

    def CloseWindow(self):
        self.done(1)

