# ReportWindow.py: Dark Age of Camelot Spellcrafting Calculator
# See http://kscraft.sourceforge.net/ for updates

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
from B_ReportWindow import *
from constants import *
import Item
import SC
import string
import re
import ReportParser
import sys
import os.path

def gemTypeSort(a, b):
    if MaterialGems.index(a) < MaterialGems.index(b):
        return -1
    elif MaterialGems.index(a) > MaterialGems.index(b):
        return 1
    else:
        return 0

def liquidSort(a, b):
    if LiquidsOrder.index(a) < LiquidsOrder.index(b):
        return -1
    elif LiquidsOrder.index(a) > LiquidsOrder.index(b):
        return 1
    else:
        return 0

def dustSort(a, b):
    if DustsOrder.index(a) < DustsOrder.index(b):
        return -1
    elif DustsOrder.index(a) > DustsOrder.index(b):
        return 1
    else:
        return 0
    
def gemNameSort(a, b):
    essence_re = re.compile("essence", re.IGNORECASE);
    shielding_re = re.compile("shielding", re.IGNORECASE);
    battle_re = re.compile("battle", re.IGNORECASE);
    war_re = re.compile("war", re.IGNORECASE);
    
    gemlevel_a, r = string.split(a, ' ', 1)
    gemlevel_b, r = string.split(b, ' ', 1)
    e_a = essence_re.search(a)
    s_a = shielding_re.search(a)
    b_a = battle_re.search(a)
    w_a = war_re.search(a)
    e_b = essence_re.search(b)
    s_b = shielding_re.search(b)
    b_b = battle_re.search(b)
    w_b = war_re.search(b)
    if GemNames.index(gemlevel_a) < GemNames.index(gemlevel_b):
        ret = -1
    elif GemNames.index(gemlevel_a) > GemNames.index(gemlevel_b):
        ret = 1
    else:
        ret = 0

    if ret != 0: return ret

    if e_a is not None:
        if e_b is not None: return ret
        else: return -1
    if s_a is not None:
        if s_b is not None: return ret
        elif e_b is not None: return 1
        else: return -1
    if b_a is not None:
        if s_b is not None: return 1
        elif e_b is not None: return 1
        elif b_b is not None: return ret
        else: return -1
    if w_a is not None:
        if s_b is not None: return 1
        elif e_b is not None: return 1
        elif b_b is not None: return 1
        elif w_b is not None: return ret
        else: return -1
    else: return ret

class ReportWindow(B_ReportWindow):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        B_ReportWindow.__init__(self,parent,name,modal,fl)
        #self.font().setPointSize(8)
        self.ReportText.setTextFormat(Qt.RichText)
        self.parent = parent
        self.gemnames = None
        self.materials = None
        self.prevMultiplier = 1
        self.totalcost = 0
        
    def materialsReport(self, itemlist, showslot = 0):
        self.MMLabel.show()
        self.MatMultiplier.show()
        self.setCaption('Materials Report')
        self.materials = { 'Gems' : { }, 'Liquids' : {}, 'Dusts': {} }
        self.gemnames = { }
        self.totalcost = 0
        if showslot == 0:
            lastslot = 4
        else:
            lastslot = showslot
        for loc, item in itemlist.items():
            activestate = item.getAttr('ActiveState')
            equipped = item.getAttr('Equipped')
            if activestate != 'player':
                continue
            for slot in range(max(showslot - 1,0), lastslot):
                if item.getSlotAttr(activestate, slot, 'Done') == '1' \
                        and showslot == 0 \
                        and self.parent.showDoneInMatsList:
                    continue
                gemtype = item.getSlotAttr('player', slot, 'Type')
                effect = item.getSlotAttr('player', slot, 'Effect')
                amount = item.getSlotAttr('player', slot, 'Amount')
                for mattype, matl in SC.getGemMaterials(item, slot, self.parent.realm).items():
                    for mat, val in matl.items():
                        if self.materials[mattype].has_key(mat):
                            self.materials[mattype][mat] += val
                        else:
                            self.materials[mattype][mat] = val
        
                if gemtype == 'Unused':
                    continue
                gemname = SC.getGemName(item, slot)
                if self.gemnames.has_key(gemname):
                    self.gemnames[gemname] += 1
                else:
                    self.gemnames[gemname] = 1

                costindex = ValuesLists[gemtype].index(amount)
                cost = GemCosts[costindex]
                if gemtype == 'Resist' or gemtype == 'Focus':
                    cost += 60 * costindex
                elif gemtype == 'Skill' and effect[0:4] == 'All ':
                    cost += 200 + 180 * costindex
                    #remakecost += 120 + 180 * costindex
                elif gemtype == 'Focus' and effect[0:4] == 'All ':
                    cost = cost * 3 + 180 * costindex
                    #remakecost = remakecost * 3 + 180 * costindex
                self.totalcost += cost
        keys = self.gemnames.keys()
        keys.sort(gemNameSort)
        self.gemnames = map(lambda(x): [x, self.gemnames.get(x)], keys)
        for type, matlist in self.materials.items():
            if type == 'Gems':
                keys = matlist.keys()
                keys.sort(gemTypeSort)
                matlist = map(lambda(x): [x, matlist.get(x)], keys)
            elif type == 'Liquids':
                keys = matlist.keys()
                keys.sort(liquidSort)
                matlist = map(lambda(x): [x, matlist.get(x)], keys)
            elif type == 'Dusts':
                keys = matlist.keys()
                keys.sort(dustSort)
                matlist = map(lambda(x): [x, matlist.get(x)], keys)
            self.materials[type] = matlist
        self.printMaterials()

    def printMaterials(self):
        materialsstr = '<b>Total Cost:</b> <font color="#FF0000">%s</font>\n' % SC.formatCost(self.totalcost)
        materialsstr += '<hr><center><b>Gem Names</b></center><ul>\n'
        for name, amount in self.gemnames:
            materialsstr += '<li>%d %s</li>\n' % (amount, name)
        materialsstr += '</ul><hr><center><b>Materials List</b></center><dl>\n'
        for type in ['Gems', 'Liquids', 'Dusts']:
            matlist = self.materials[type]
            materialsstr += '<dt><b>%s</b></dt>\n' % type
            for matl, val in matlist:
                materialsstr += '<dd>%d %s</dd>\n' % (val, matl)
        materialsstr += '</dl>\n'
        self.ReportText.setText(materialsstr, "html")

    def matMultiplierUpdate(self, multiplier):
        for i in range(0, len(self.gemnames)):
            name, amount = self.gemnames[i]
            self.gemnames[i] = [name, amount * multiplier / self.prevMultiplier]
        for type, matlist in self.materials.items():
            for i in range(0, len(matlist)):
                matl, val = matlist[i]
                self.materials[type][i] = [matl, val * multiplier / self.prevMultiplier]
        self.totalcost = self.totalcost * multiplier / self.prevMultiplier
        self.prevMultiplier = multiplier
        self.printMaterials()

    def collectStats(self, itemlist):
        skillTotals = { }
        focusTotals = { }
        totals = { 
            'str' : 0, 'con' : 0, 'dex' : 0, 'qui' : 0,
            'int' : 0, 'pie' : 0, 'cha' : 0, 'emp' : 0, 
            'hits' : 0,   'power' : 0,
            'body' : 0,   'cold' : 0,   'heat' : 0,
            'energy' : 0, 'matter' : 0, 'spirit' : 0, 
            'crush' : 0,  'thrust' : 0, 'slash' : 0
        }
        for key in GemLists['All']['Stat']:
          totals[key] = 0
        for key in GemLists['All']['Hits']:
          totals[key] = 0
        for key in GemLists['All']['Power']:
          totals[key] = 0
        for key in GemLists['All']['Resist']:
          totals[key] = 0
        totals['AF'] = 0
        capTotals = { }
        otherTotals = { }
        iteminfo = { }
        for key, item in itemlist.items():
            iteminfo[key] = { }
            iteminfo[key]['equipped'] = item.getAttr('Equipped')
            iteminfo[key]['activestate'] = item.getAttr('ActiveState')
            iteminfo[key]['level'] = item.getAttr('Level')
            iteminfo[key]['name'] = item.getAttr('ItemName')
            iteminfo[key]['quality'] = item.getAttr('ItemQuality')
            iteminfo[key]['af'] = item.getAttr('AFDPS')
            iteminfo[key]['bonus'] = item.getAttr('Bonus')
            iteminfo[key]['speed'] = item.getAttr('Speed')
            equipped = item.getAttr('Equipped')
            activestate = item.getAttr('ActiveState')
            if activestate == 'drop':
                endrng = 10
                iteminfo[key]['usedpoints'] = 0
                iteminfo[key]['availablepoints'] = 0
                iteminfo[key]['overcharge'] = 0
            else:
                endrng = 4
                imbue = SC.calcImbue(item)
                itemimbue = SC.getItemImbue(item)
                if (imbue - itemimbue) >= 6:
                    success = '<font color="#FF0000">Impossible!</font>\n'
                elif imbue > (itemimbue+0.5):
                    success = -OCStartPercentages[int(imbue-itemimbue)]
                    for i in range(0, 4):
                        if item.getSlotAttr(activestate, i, 'Type') == 'Unused':
                            success += GemQualOCModifiers['94']
                        else:
                            success += GemQualOCModifiers[item.getSlotAttr(activestate, i, 'Qua')]
                    success += ItemQualOCModifiers[item.getAttr('ItemQuality')]
                    success += (self.parent.crafterSkill - 500) / 10
                    if self.parent.crafterSkill <= 50: success -= 450
                    if success < 0:
                        success = '<font color="#FF0000">BOOM! (%d%%)</font>\n' % success
                    else:
                        success = '<font color="#00FF00">%d%%</font>\n' % success
                else:
                    success = 'None'
                iteminfo[key]['usedpoints'] = imbue
                iteminfo[key]['availablepoints'] = itemimbue
                iteminfo[key]['overcharge'] = success
            utility = 0
            for slot in range(0, endrng):
                    
                gemnum = 'gem%d' % (slot+1)
                iteminfo[key][gemnum] = { }
                gemtype = item.getSlotAttr(activestate, slot, 'Type')
                amount = item.getSlotAttr(activestate, slot, 'Amount')
                effect = item.getSlotAttr(activestate, slot, 'Effect')
                qua = item.getSlotAttr(activestate, slot, 'Qua')
                #gemtype = re.sub(' ' , '', gemtype)
                amount = re.sub('[^\d]', '', amount)
                if amount == '':
                    amount = 0
                else:
                    amount = int(amount)
                iteminfo[key][gemnum]['type'] = gemtype
                iteminfo[key][gemnum]['amount'] = amount
                iteminfo[key][gemnum]['effect'] = effect
                if gemtype == 'Cap Increase':
                    iteminfo[key][gemnum]['effect'] += ' Cap Increase'
                iteminfo[key][gemnum]['quality'] = qua
                if activestate == 'player':
                    iteminfo[key][gemnum]['name'] = SC.getGemName(item, slot)
                else:
                    iteminfo[key][gemnum]['name'] = ''
                if gemtype == 'Skill':
                        if effect == 'All Magic Skills'\
                            or effect == 'All Melee Weapon Skills'\
                            or effect == 'All Dual Wield Skills'\
                            or effect == 'All Archery Skills':

                            if effect == 'All Melee Weapon Skills':
                                utility += amount * 5
                            for e in AllBonusList[self.parent.realm][self.parent.charclass][effect]:
                                if effect == 'All Magic Skills'\
                                    or effect == 'All Dual Wield Skills'\
                                    or effect == 'All Archery Skills':
                                    utility += amount * 5
                                if equipped == '1':
                                    if not skillTotals.has_key(e):
                                        skillTotals[e] = amount
                                    else:
                                        skillTotals[e] += amount
                        else:           
                            utility += amount * 5
                            if equipped == '1':
                                if not skillTotals.has_key(effect):
                                    skillTotals[effect] = amount
                                else:
                                    skillTotals[effect] += amount
                elif gemtype == 'Focus':
                    utility += 1
                    if equipped == '1':
                        if effect == 'All Spell Lines':
                            for f in AllBonusList[self.parent.realm][self.parent.charclass][effect]:
                                focusTotals[f] = amount
                        else:
                            focusTotals[effect] = amount
                elif gemtype == 'Power':
                    utility += amount * 2
                    if equipped == '1':
                        totals[gemtype] += amount
                        totals[gemtype.lower()] += amount
                elif gemtype == 'Hits':
                    utility += amount / 4.0
                    if equipped == '1':
                        totals[gemtype] += amount
                        totals[gemtype.lower()] += amount
                elif gemtype == 'Resist':
                    utility += amount * 2
                    if equipped == '1':
                        totals[effect] += amount
                        totals[effect.lower()] += amount
                elif gemtype == 'Stat':
                    if effect == 'Acuity':
                        for e in AllBonusList[self.parent.realm][self.parent.charclass][effect]:
                            utility += amount * 2.0 / 3.0
                            if equipped == '1':
                                totals[e] += amount
                                totals[e[:3].lower()] += amount
                    else:
                        utility += amount * 2.0 / 3.0
                        if equipped == '1':
                            totals[effect] += amount
                            totals[effect[:3].lower()] += amount
                elif gemtype == 'Other Bonus':
                    if equipped == '1':
                        if effect == 'AF':
                            totals[effect] += amount
                        if not otherTotals.has_key(effect):
                            otherTotals[effect] = amount
                        else:
                            otherTotals[effect] += amount
                elif gemtype == 'Cap Increase':
                    if equipped == '1':
                        if effect == 'Acuity':
                            effect = AllBonusList[self.parent.realm][self.parent.charclass][effect][0]
                        if not capTotals.has_key(effect):
                            capTotals[effect] = amount
                        else:
                            capTotals[effect] += amount
                        if effect == 'Hits':
                            if capTotals['Hits'] > 200:
                                capTotals['Hits'] = 200 
                        elif capTotals[effect] > 25:
                            capTotals[effect] = 25
            iteminfo[key]['utility'] = utility

        for (key, val) in totals.items():
            if self.parent.includeRacials:
                if GemTables['All']['Resist'].has_key(string.capitalize(key)):
                    rr = str(getattr(self.parent, string.capitalize(key)+'RR').text())
                    if rr != '-':
                        val += int(rr[1:-1])
                        totals[key] = str(val) + ' (' + str(rr[1:-1]) + ')'
        return { 'Skills' : skillTotals, 'Focus' : focusTotals, 
    'Stats' : totals, 'Other' : otherTotals, 'Caps' : capTotals, 'Items' : iteminfo }
            
    def parseConfigReport(self, filename, itemlist):
        try:
            f = open(str(filename), 'r')
            reportstr = f.read()
            f.close()
        except IOError:
            QMessageBox.critical(None, 'Error!', 
                'Error opening file: ' + filename, 'OK')
            return

        self.MMLabel.hide()
        self.MatMultiplier.hide()
        self.setCaption('Config Report')
        info = self.collectStats(itemlist)
        rp = ReportParser.ReportParser()
        self.ReportText.setText(rp.parse(reportstr, info), "html")
        

    def saveToHTML(self):
        filename = QFileDialog.getSaveFileName('', "HTML (*.html)")
        if filename is not None and str(filename) != '':
            try:
                if re.compile('\.html$').search(str(filename)) is None:
                    filename = str(filename)
                    filename += '.html'
                f = open(str(filename), 'w')
                f.write('<HTML>'+str(self.ReportText.text())+'</HTML>')
                f.close()
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + filename, 'OK')

    def saveToText(self):
        filename = QFileDialog.getSaveFileName('', "Text (*.txt)")
        if filename is not None and str(filename) != '':
            try:
                if re.compile('\.txt$').search(str(filename)) is None:
                    filename = str(filename)
                    filename += '.txt'
                f = open(str(filename), 'w')
                txt = str(self.ReportText.text())
                txt = re.sub('<br>', '\n', txt)
                txt = re.sub('<td>', '    ', txt)
                #txt = re.sub('<tr>', '\n', txt)
                txt = re.sub('<hr>', '\n', txt)
                txt = re.sub('<li>', '\n', txt)
                txt = re.sub('<dt>', '\n', txt)
                #txt = re.sub('<dd>', '\n', txt)
                txt = re.sub('<.*?>', '', txt)
                txt = re.sub('\n\n(\n+)', '\n\n', txt)
                f.write(txt)
                f.close()
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + filename, 'OK')
        
    def closeWindow(self):
        self.done(1)                        
