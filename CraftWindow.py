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
        self.connect(self.Gem1Remakes,SIGNAL("valueChanged(int)"),self.Remake1Changed)
        self.connect(self.Gem2Remakes,SIGNAL("valueChanged(int)"),self.Remake2Changed)
        self.connect(self.Gem3Remakes,SIGNAL("valueChanged(int)"),self.Remake3Changed)
        self.connect(self.Gem4Remakes,SIGNAL("valueChanged(int)"),self.Remake4Changed)
        self.connect(self.Gem1Done,SIGNAL("clicked()"),self.Gem1Clicked)
        self.connect(self.Gem2Done,SIGNAL("clicked()"),self.Gem2Clicked)
        self.connect(self.Gem3Done,SIGNAL("clicked()"),self.Gem3Clicked)
        self.connect(self.Gem4Done,SIGNAL("clicked()"),self.Gem4Clicked)
        self.connect(self.Gem1Time,SIGNAL("textChanged(const QString&)"),self.Time1Changed)
        self.connect(self.Gem2Time,SIGNAL("textChanged(const QString&)"),self.Time2Changed)
        self.connect(self.Gem3Time,SIGNAL("textChanged(const QString&)"),self.Time3Changed)
        self.connect(self.Gem4Time,SIGNAL("textChanged(const QString&)"),self.Time4Changed)
        self.connect(self.ExpMultiplier,SIGNAL("valueChanged(int)"),self.computeMaterials)
        self.connect(self.Close,SIGNAL("clicked()"),self.CloseWindow)
        #self.font().setPointSize(8)
        self.currentItem = None
        self.totalCost = 0
        self.prevVals = [0, 0, 0, 0]
        self.parent = parent
        
    def loadItem(self, item):
        self.currentItem = item
        materials = { 'Gems': { }, 'Dusts' : { }, 'Liquids' : { } }
        for slot in range(0, 4):
            gemqua = getattr(self, 'Gem%dQua' % (slot+1))
            gemname = getattr(self, 'Gem%dName' % (slot+1))
            gemremakes = getattr(self, 'Gem%dRemakes' % (slot+1))
            gemtime = getattr(self, 'Gem%dTime' % (slot+1))
            gemcost = getattr(self, 'Gem%dCost' % (slot+1))
            gemdone = getattr(self, 'Gem%dDone' % (slot+1))
            gemtype = item.slot(slot).type()
            gemdone = int(item.slot(slot).done())
            gemamount = item.slot(slot).amount()
            
            gemqua.setText('%s%%' % item.slot(slot).qua())
            gemtime.setText(item.slot(slot).time())

            numremakes = int(item.slot(slot).remakes())
            self.prevVals[slot] = numremakes
            cost = item.slot(slot).gemCost(numremakes)
            self.totalCost += cost
            gemcost.setText(SC.formatCost(cost))
            
            if gemdone:
                getattr(self, 'Gem%dDone' % (slot+1)).setChecked(1)

            gemremakes.setValue(numremakes)
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
        prevcost = self.currentItem.slot(slotindex).gemCost(self.prevVals[slotindex])
        self.prevVals[slotindex] = val
        cost = self.currentItem.slot(slotindex).gemCost(val)
        self.totalCost += (cost - prevcost)
        gemcost = getattr(self, 'Gem%dCost' % (slotindex+1))
        gemcost.setText(SC.formatCost(cost))
        self.TotalCost.setText(SC.formatCost(self.totalCost))
        
    def Gem1Clicked(self):
        if self.Gem1Done.isChecked():
            done = '1'
        else:
            done = '0'
        self.currentItem.slot(0).setDone(done)
        self.computeMaterials()

    def Gem2Clicked(self):
        if self.Gem2Done.isChecked():
            done = '1'
        else:
            done = '0'
        self.currentItem.slot(1).setDone(done)
        self.computeMaterials()

    def Gem3Clicked(self):
        if self.Gem3Done.isChecked():
            done = '1'
        else:
            done = '0'
        self.currentItem.slot(2).setDone(done)
        self.computeMaterials()

    def Gem4Clicked(self):
        if self.Gem4Done.isChecked():
            done = '1'
        else:
            done = '0'
        self.currentItem.slot(3).setDone(done)
        self.computeMaterials()

    def Remake1Changed(self, val):
        self.currentItem.slot(0).setTime(self.Gem1Remakes.text())
        self.recomputeCosts(0, val)
        self.computeMaterials()

    def Remake2Changed(self, val):
        self.currentItem.slot(1).setTime(self.Gem1Remakes.text())
        self.recomputeCosts(1, val)
        self.computeMaterials()

    def Remake3Changed(self, val):
        self.currentItem.slot(2).setTime(self.Gem1Remakes.text())
        self.recomputeCosts(2, val)
        self.computeMaterials()

    def Remake4Changed(self, val):
        self.currentItem.slot(3).setTime(self.Gem1Remakes.text())
        self.recomputeCosts(3, val)
        self.computeMaterials()

    def CloseWindow(self):
        self.done(1)

    def Time1Changed(self,a0):
        self.currentItem.slot(0).setTime(self.Gem1Time.text())

    def Time2Changed(self,a0):
        self.currentItem.slot(1).setTime(self.Gem1Time.text())

    def Time3Changed(self,a0):
        self.currentItem.slot(2).setTime(self.Gem1Time.text())

    def Time4Changed(self,a0):
        self.currentItem.slot(3).setTime(self.Gem1Time.text())
