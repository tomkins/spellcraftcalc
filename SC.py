# SC.py: Dark Age of Camelot Spellcrafting Calculator (main Window)
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

from Item import *
from constants import *
import string

def formatCost(cost):
    plat = (cost / 10000000) % 1000
    gold = (cost / 10000) % 1000
    silver = (cost / 100) % 100
    copper = cost % 100
    str = ''
    if plat > 0:
        str += '%dp ' % plat
    if gold > 0 or plat > 0:
        str += '%dg ' % gold
    if silver > 0 or gold > 0 or plat > 0:
        str += '%ds ' % silver
    str += '%dc' % copper
    return str

def getGemName(item, slot):
    gemstate = item.getAttr('ActiveState')
    gemtype = item.getSlotAttr(gemstate, slot, 'Type')
    realm = item.getAttr('Realm')
    if gemtype == 'Unused': return ''
    gemlist = eval('%sList' % gemtype, globals(), globals())
    amountlist = eval('%sValues' % gemtype, globals(), globals())
    amountindex = amountlist.index(item.getSlotAttr(gemstate, slot, 'Amount'))
    effect = item.getSlotAttr(gemstate, slot, 'Effect')
    gemname = GemNames[amountindex]
    gemend = GemSubName[gemtype]
    if type(gemlist) == types.ListType:
        effectindex = map(lambda(x):x[0], gemlist).index(effect)
        gemmiddle = gemlist[effectindex][1]
    else:
        effectindex = map(lambda(x):x[0], gemlist[realm]).index(effect)
        gemmiddle = gemlist[realm][effectindex][1]
    gemname += ' ' + gemmiddle + ' ' + gemend
    return string.strip(gemname)

def getGemMaterials(item, slot, realm):
    gemstate = item.getAttr('ActiveState')
    gemname = getGemName(item, slot)
    ret = { 'Gems' : { }, 'Dusts' : { }, 'Liquids' : { } }
    if gemname == '': return ret
    gemlevel, gemname2 = string.split(gemname, ' ', 1)
    gemliquid, gemdust = string.split(gemname2, ' ', 1)

    # Fix some inconsistencies
    if gemname2 == 'Steaming Fervor Sigil':
        gemliquid = 'Heated'

    gemtype = item.getSlotAttr(gemstate, slot, 'Type')
    gemindex = GemNames.index(gemlevel)

    ret['Gems'][MaterialGems[gemindex]] = 1
    if gemtype == 'Focus' or gemtype == 'Resist':
        ret['Dusts'][GemDusts[gemdust]] = (gemindex * 5) + 1
    else:
        ret['Dusts'][GemDusts[gemdust]] = (gemindex * 4) + 1
    ret['Liquids'][GemLiquids[gemliquid]] = gemindex + 1
    
    return ret

def getItemImbue(item):
    itemlevel = item.getAttr('Level')
    if item.getAttr('ItemQuality') == '':
        item.loadAttr('ItemQuality', '94')
    if itemlevel == '':
        itemimbue = 0
    else:
        itemimbue = ImbuePts[int(itemlevel)-1]\
                [int(item.getAttr('ItemQuality'))-94]

    return itemimbue

def calcImbue(item):
    itemtype = item.getAttr('ActiveState')
    if itemtype == 'drop': return 0
    mvals = []
    for i in range(0, 4):
        type = item.getSlotAttr(itemtype, i, 'Type')
        amount = item.getSlotAttr(itemtype, i, 'Amount')
        if amount == '': 
            mval = 0.0
        elif type == 'Focus':
            mval = 1.0
        elif type == 'Unused':
            mval = 0.0
        elif type == 'Stat':
            mval = ((int(amount) - 1) / 3.0) * 2 + 1
        elif type == 'Resist' or type == 'Power':
            mval = (int(amount) - 1) * 2
            if mval == 0: mval = 1.0
        elif type == 'Hits':
            mval = int(amount) / 4.0
        elif type == 'Skill':
            mval = (int(amount) - 1) * 5.0
            if mval == 0: mval = 1.0    
        mvals.append(mval)
    maximbue = max(mvals)
    mvals.remove(maximbue)
    totalimbue = ((maximbue * 2 + sum(mvals)) / 2.0)
    return totalimbue

def computeOverchargeSuccess(imbue, itemimbue, item, crafterskill):
    success = -OCStartPercentages[int(imbue-itemimbue)]
    for i in range(0, 4):
        if item.getSlotAttr(activestate, i, 'Type') == 'Unused':
            success += GemQualOCModifiers['94']
        else:
            success += GemQualOCModifiers[item.getSlotAttr(activestate, i, 'Qua')]
    success += ItemQualOCModifiers[item.getAttr('ItemQuality')]
    success += (crafterSkill - 500) / 10
    if crafterSkill <= 50: success -= 450
    return success

def computeGemCost(item, i):
    itemtype = item.getAttr('ActiveState')
    
    gemtype = re.sub(' ', '', item.getSlotAttr(itemtype, i, 'Type'))
    if item.getSlotAttr(itemtype, i, 'Amount') == '':
        amount = 0
    else:
        amount = int(item.getSlotAttr(itemtype, i, 'Amount'))
    if amount == '' or gemtype == 'Unused' or amount == 0 or itemtype == 'drop':
        cost = 0    
        remakecost = 0
        costindex = 0
    else:
        costindex = eval('%sValues' % gemtype, globals(), globals()).index(str(amount))
        cost = GemCosts[costindex]
        remakecost = RemakeCosts[costindex] * int(item.getSlotAttr(itemtype, i, 'Remakes'))
        if gemtype == 'Resist' or gemtype == 'Focus':
            cost += 60 * costindex
            if remakecost > 0:
                remakecost += 60 * costindex
    return (cost + remakecost, costindex+1)

# vim: set ts=4 sw=4 et:
