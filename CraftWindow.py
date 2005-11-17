# CraftWindow.py: Dark Age of Camelot Spellcrafting Calculator
# See http://www.ugcs.caltech.edu/~jlamanna/daoc/sccalc/index.html for updates

# Copyright (C) 2003,  James Lamanna (jlamanna@ugcs.caltech.edu)

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

from qt import *
from B_CraftWindow import *
from constants import *
import SC

class CraftWindow(B_CraftWindow):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        B_CraftWindow.__init__(self,parent,name,modal,fl)
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
            gemtype = item.getSlotAttr('player', slot, 'Type')
            gemdone = int(item.getSlotAttr('player', slot, 'Done'))
            gemamount = item.getSlotAttr('player', slot, 'Amount')
            
            gemqua.setText('%s%%' % item.getSlotAttr('player', slot, 'Qua'))
            gemtime.setText(item.getSlotAttr('player', slot, 'Time'))

            numremakes = int(item.getSlotAttr('player', slot, 'Remakes'))
            self.prevVals[slot] = numremakes
            cost = self.computeRemakesCost(slot, numremakes)
            self.totalCost += cost
            gemcost.setText(SC.formatCost(cost))
            
            if gemdone:
                getattr(self, 'Gem%dDone' % (slot+1)).setChecked(1)

            gemremakes.setValue(numremakes)
            gemname.setText(SC.getGemName(item, slot))

        self.TotalCost.setText(SC.formatCost(self.totalCost))
        self.ExpMultiplier.setValue(6)
        self.computeMaterials()

    def computeMaterials(self):
        materials = { 'Used' : { 'Gems' : { }, 'Dusts' : {}, 'Liquids': {} },
            'Expected' : { 'Gems' : { }, 'Dusts' : {}, 'Liquids': {} } }
        expmultiplier = int(self.ExpMultiplier.value())
        for slot in range(0, 4):
            numremakes = int(self.currentItem.getSlotAttr('player', slot, 'Remakes'))
            done = int(self.currentItem.getSlotAttr('player', slot, 'Done'))
            for mattype, matl in SC.getGemMaterials(self.currentItem, slot, self.parent.realm).items():
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
            self.MatsUsed.insertLine('%d %s Gem' % (val, mat))
        for mat, val in materials['Used']['Dusts'].items():
            self.MatsUsed.insertLine('%d %s' % (val, mat))
        for mat, val in materials['Used']['Liquids'].items():
            self.MatsUsed.insertLine('%d %s' % (val, mat))
        for mat, val in materials['Expected']['Gems'].items():
            self.MatsExpected.insertLine('%d %s Gem' % (val, mat))
        for mat, val in materials['Expected']['Dusts'].items():
            self.MatsExpected.insertLine('%d %s' % (val, mat))
        for mat, val in materials['Expected']['Liquids'].items():
            self.MatsExpected.insertLine('%d %s' % (val, mat))

    def computeRemakesCost(self, slotindex, remakes):
        gemtype = self.currentItem.getSlotAttr('player', slotindex, 'Type')
        if gemtype == 'Unused': return 0
        gemamount = self.currentItem.getSlotAttr('player', slotindex, 'Amount')
        costindex = ValuesLists[gemtype].index(gemamount)
        basecost = GemCosts[costindex]
        remakecost = RemakeCosts[costindex]
        if gemtype == 'Resist' or gemtype == 'Focus':
            basecost += 60 * costindex
            if remakecost > 0:
                remakecost += 60 * costindex
        cost = int(basecost + (remakes * remakecost))
        self.currentItem.loadSlotAttr('player', slotindex, 'Remakes', remakes)
        return cost

    def recomputeCosts(self, slotindex, val):
        prevcost = self.computeRemakesCost(slotindex, self.prevVals[slotindex])
        self.prevVals[slotindex] = val
        cost = self.computeRemakesCost(slotindex, val)
        self.totalCost += (cost - prevcost)
        gemcost = getattr(self, 'Gem%dCost' % (slotindex+1))
        gemcost.setText(SC.formatCost(cost))
        self.TotalCost.setText(SC.formatCost(self.totalCost))
        
    def Gem1Clicked(self):
        if self.Gem1Done.isChecked():
            self.currentItem.loadSlotAttr('player', 0, 'Done', '1')
        else:
            self.currentItem.loadSlotAttr('player', 0, 'Done', '0')
        self.computeMaterials()

    def Gem2Clicked(self):
        if self.Gem2Done.isChecked():
            self.currentItem.loadSlotAttr('player', 1, 'Done', '1')
        else:
            self.currentItem.loadSlotAttr('player', 1, 'Done', '0')
        self.computeMaterials()

    def Gem3Clicked(self):
        if self.Gem3Done.isChecked():
            self.currentItem.loadSlotAttr('player', 2, 'Done', '1')
        else:
            self.currentItem.loadSlotAttr('player', 2, 'Done', '0')
        self.computeMaterials()

    def Gem4Clicked(self):
        if self.Gem4Done.isChecked():
            self.currentItem.loadSlotAttr('player', 3, 'Done', '1')
        else:
            self.currentItem.loadSlotAttr('player', 3, 'Done', '0')
        self.computeMaterials()

    def Remake1Changed(self, val):
        self.recomputeCosts(0, val)
        self.computeMaterials()

    def Remake2Changed(self, val):
        self.recomputeCosts(1, val)
        self.computeMaterials()

    def Remake3Changed(self, val):
        self.recomputeCosts(2, val)
        self.computeMaterials()

    def Remake4Changed(self, val):
        self.recomputeCosts(3, val)
        self.computeMaterials()

    def CloseWindow(self):
        self.done(1)

    def Time1Changed(self,a0):
        self.currentItem.loadSlotAttr('player', 0, 'Time', str(self.Gem1Time.text()))

    def Time2Changed(self,a0):
        self.currentItem.loadSlotAttr('player', 1, 'Time', str(self.Gem2Time.text()))

    def Time3Changed(self,a0):
        self.currentItem.loadSlotAttr('player', 2, 'Time', str(self.Gem3Time.text()))

    def Time4Changed(self,a0):
        self.currentItem.loadSlotAttr('player', 3, 'Time', str(self.Gem4Time.text()))
