# ReportWindow.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from B_ReportWindow import *
from Character import *
from constants import *
from htmlplus import *
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

def gemNameSort(a, b):
    ## XXX need to be static singletons...
    essence_re = re.compile("essence", re.IGNORECASE);
    shielding_re = re.compile("shielding", re.IGNORECASE);
    battle_re = re.compile("battle", re.IGNORECASE);
    war_re = re.compile("war", re.IGNORECASE);
    tincture_re = re.compile("tincture", re.IGNORECASE);
    
    t_a = tincture_re.search(a)
    t_b = tincture_re.search(b)
    if not (t_a is None and t_b is None):
        if t_a is None: return  -1
        if t_b is None: return  1
        return cmp(a, b)
        
    gemlevel_a, r = string.split(a, ' ', 1)
    gemlevel_b, r = string.split(b, ' ', 1)
    if GemNames.index(gemlevel_a) < GemNames.index(gemlevel_b):
        return -1
    elif GemNames.index(gemlevel_a) > GemNames.index(gemlevel_b):
        return 1

    e_a = essence_re.search(a)
    e_b = essence_re.search(b)
    if e_a is not None:
        if e_b is not None: return cmp(a, b)
        else: return -1

    s_a = shielding_re.search(a)
    s_b = shielding_re.search(b)
    if s_a is not None:
        if s_b is not None: return cmp(a, b)
        elif e_b is not None: return 1
        else: return -1

    b_a = battle_re.search(a)
    b_b = battle_re.search(b)
    if b_a is not None:
        if s_b is not None: return 1
        elif e_b is not None: return 1
        elif b_b is not None: return cmp(a, b)
        else: return -1

    w_a = war_re.search(a)
    w_b = war_re.search(b)
    if w_a is not None:
        if s_b is not None: return 1
        elif e_b is not None: return 1
        elif b_b is not None: return 1
        elif w_b is not None: return cmp(a, b)
        else: return -1
    
    return cmp(a, b)


class ReportWindow(QDialog, Ui_B_ReportWindow):
    def __init__(self,parent = None,name = None,modal = False,fl = Qt.Widget):
        QDialog.__init__(self,parent,fl)
        Ui_B_ReportWindow.setupUi(self,self)
        if (name):
            self.setObjectName(name)
        if (modal):
            self.setModal(modal)

        self.connect(self.PushButton2,SIGNAL("clicked()"),self.closeWindow)
        self.connect(self.PushButton1,SIGNAL("clicked()"),self.saveToHTML)
        self.connect(self.PushButton1_2,SIGNAL("clicked()"),self.saveToText)
        self.connect(self.MatMultiplier,SIGNAL("valueChanged(int)"),self.matMultiplierUpdate)

        #self.font().setPointSize(8)
        #self.ReportText.setTextFormat(Qt.RichText)
        self.parent = parent
        self.gemnames = None
        self.materials = None
        self.prevMultiplier = 1
        self.totalcost = 0
        
    def materialsReport(self, itemlist, showslot = 0):
        self.MMLabel.show()
        self.MatMultiplier.show()
        self.setWindowTitle('Materials Report')
        self.materials = { 'Gems' : { }, 'Liquids' : {}, 'Dusts': {} }
        self.gemnames = { }
        self.totalcost = 0
        if showslot == 0:
            lastslot = 6
        else:
            lastslot = showslot
        for loc, item in itemlist.items():
            if item.ActiveState != 'player':
                continue
            for slot in range(max(showslot - 1,0), lastslot):
                if item.slot(slot).done() == '1' \
                        and showslot == 0 \
                        and self.parent.showDoneInMatsList:
                    continue
                gemtype = item.slot(slot).type()
                effect = item.slot(slot).effect()
                amount = item.slot(slot).amount()
                for mattype, matl in item.slot(slot).gemMaterials(self.parent.realm).items():
                    for mat, val in matl.items():
                        if self.materials[mattype].has_key(mat):
                            self.materials[mattype][mat] += val
                        else:
                            self.materials[mattype][mat] = val
        
                if gemtype == 'Unused':
                    continue
                gemname = item.slot(slot).gemName(self.parent.realm)
                if self.gemnames.has_key(gemname):
                    self.gemnames[gemname] += 1
                else:
                    self.gemnames[gemname] = 1

                cost = item.slot(slot).gemCost()
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
                keys.sort()
                matlist = map(lambda(x): [x, matlist.get(x)], keys)
            elif type == 'Dusts':
                keys = matlist.keys()
                keys.sort()
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
        self.reportHtml = materialsstr
        self.ReportText.setHtml(self.reportHtml)

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
            iteminfo[key]['equipped'] = item.Equipped
            iteminfo[key]['activestate'] = item.ActiveState
            iteminfo[key]['level'] = item.Level
            iteminfo[key]['name'] = item.ItemName
            iteminfo[key]['quality'] = item.ItemQuality
            iteminfo[key]['af'] = item.AFDPS
            iteminfo[key]['bonus'] = item.Bonus
            iteminfo[key]['speed'] = item.Speed
            if item.ActiveState == 'drop':
                iteminfo[key]['usedpoints'] = 0
                iteminfo[key]['availablepoints'] = 0
                iteminfo[key]['overcharge'] = 0
            else:
                imbue = item.totalImbue()
                itemimbue = item.itemImbue()
                if (imbue - itemimbue) >= 6:
                    success = 'Impossible!'
                elif imbue > (itemimbue+0.5):
                    success = item.overchargeSuccess(self.parent.crafterSkill)
                    if success < 0:
                        success = '%d%% (BOOM!)' % success
                    else:
                        success = '%d%%' % success
                else:
                    success = 'None'
                iteminfo[key]['usedpoints'] = imbue
                iteminfo[key]['availablepoints'] = itemimbue
                iteminfo[key]['overcharge'] = success
            utility = 0
            for slot in range(0, item.slotCount()):
                gemnum = 'gem%d' % (slot+1)
                iteminfo[key][gemnum] = { }
                gemtype = item.slot(slot).type()
                amount = item.slot(slot).amount()
                effect = item.slot(slot).effect()
                qua = item.slot(slot).qua()
                #gemtype = re.sub(' ' , '', gemtype)
                amount = re.sub('[^\d]', '', amount)
                if amount == '':
                    amount = 0
                else:
                    amount = int(amount)
                iteminfo[key][gemnum]['type'] = gemtype
                iteminfo[key][gemnum]['amount'] = amount
                if gemtype in ('Unused', 'Stat', 'Hits', 'Power', 'Skill',):
                    iteminfo[key][gemnum]['effect'] = effect
                elif gemtype[0:5] == 'Other':
                    iteminfo[key][gemnum]['effect'] = effect +' '+ gemtype[6:]
                else:
                    iteminfo[key][gemnum]['effect'] = effect +' '+ gemtype
                iteminfo[key][gemnum]['quality'] = qua
                if item.slot(slot).slotType() == 'player':
                    iteminfo[key][gemnum]['name'] = item.slot(slot).gemName(self.parent.realm)
                else:
                    iteminfo[key][gemnum]['name'] = ''
                utility += item.slot(slot).gemUtility()
                if not item.Equipped == '1':
                    continue
                if gemtype == 'Skill':
                    if effect[0:4] == 'All ':
                        effects = AllBonusList[self.parent.realm][self.parent.charclass][effect]
                    else:
                        effects = (effect,)
                    for effect in effects:
                        if not skillTotals.has_key(effect):
                            skillTotals[effect] = amount
                        else:
                            skillTotals[effect] += amount
                elif gemtype == 'Focus':
                    if effect == 'All Spell Lines':
                        for f in AllBonusList[self.parent.realm][self.parent.charclass][effect]:
                            focusTotals[f] = amount
                    else:
                        focusTotals[effect] = amount
                elif gemtype == 'Power':
                    totals[gemtype] += amount
                    totals[gemtype.lower()] += amount
                elif gemtype == 'Hits':
                    totals[gemtype] += amount
                    totals[gemtype.lower()] += amount
                elif gemtype == 'Resist':
                    totals[effect] += amount
                    totals[effect.lower()] += amount
                elif gemtype == 'Stat':
                    if effect == 'Acuity':
                        for e in AllBonusList[self.parent.realm][self.parent.charclass][effect]:
                            totals[e] += amount
                            totals[e[:3].lower()] += amount
                    else:
                        totals[effect] += amount
                        totals[effect[:3].lower()] += amount
                elif gemtype == 'Other Bonus':
                    if effect == 'AF':
                        totals[effect] += amount
                    if not otherTotals.has_key(effect):
                        otherTotals[effect] = amount
                    else:
                        otherTotals[effect] += amount
                elif gemtype == 'PvE Bonus':
                    if not otherTotals.has_key(effect + " PvE"):
                        otherTotals[effect + " PvE"] = amount
                    else:
                        otherTotals[effect + " PvE"] += amount
                elif gemtype == 'Cap Increase':
                    if effect == 'Acuity':
                        effect = AllBonusList[self.parent.realm][self.parent.charclass][effect][0]
                    if not capTotals.has_key(effect):
                        capTotals[effect] = amount
                    else:
                        capTotals[effect] += amount
                    if effect == 'Hits':
                        if capTotals['Hits'] > 200:
                            capTotals['Hits'] = 200 
                    elif capTotals[effect] > 26:
                        capTotals[effect] = 26
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
        self.setWindowTitle('Config Report')
        info = self.collectStats(itemlist)
        rp = ReportParser.ReportParser()
        self.reportHtml = rp.parse(reportstr, info)
        self.ReportText.setHtml(self.reportHtml)

    def saveToHTML(self):
        filename = QFileDialog.getSaveFileName(self, "Save HTML Report", "", "HTML (*.html);;All Files (*.*)")
        if filename is not None and str(filename) != '':
            try:
                if re.compile('\.html$').search(str(filename)) is None:
                    filename = str(filename)
                    filename += '.html'
                f = open(str(filename), 'w')
                f.write('<HTML>'+self.reportHtml+'</HTML>')
                f.close()
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + filename, 'OK')

    def saveToText(self):
        filename = QFileDialog.getSaveFileName(self, "Save Text Report", "", "Text (*.txt);;All Files (*.*)")
        if filename is not None and str(filename) != '':
            try:
                if re.compile('\.txt$').search(str(filename)) is None:
                    filename = str(filename)
                    filename += '.txt'
                f = open(str(filename), 'w')
                #f.write(str(self.ReportText.toPlainText()))
                w = DimWriter(f)
                s = ObtuseFormatter(w)
                p = HTMLPlusParser(s)
                p.feed(self.reportHtml)
                p.close()
                w.flush()
                f.close()
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + filename, 'OK')
        
    def closeWindow(self):
        self.done(1)                        
