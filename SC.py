# SC.py: Dark Age of Camelot Spellcrafting Calculator
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

from Item import *
from constants import *
import string
import sys

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
    if not GemTables.has_key(realm): return ''
    if not GemTables[realm].has_key(gemtype): return ''
    gemlist = GemTables[realm][gemtype]
    amount = item.getSlotAttr(gemstate, slot, 'Amount')
    amountlist = ValuesLists[gemtype]
    if not amount in amountlist: return ''
    amountindex = amountlist.index(amount)
    effect = item.getSlotAttr(gemstate, slot, 'Effect')
    if not gemlist.has_key(effect): 
      gemlist = GemTables['All'][gemtype]
      if not gemlist.has_key(effect): return ''
    gemname = GemNames[amountindex]
    gemmiddle = gemlist[effect]
    gemend = GemSubName[gemtype]
    gemname += ' ' + gemmiddle + ' ' + gemend
    return string.strip(gemname)

def getGemNameParts(gemname):
    #returns level, liquid prefix and dust suffix
    if gemname == '':
        return ['','','']
    gemwords = string.split(gemname, ' ', 3)
    if gemwords[0] not in GemNames:
        return ['','','']
    # Prefix (two words distinguish some borked gems)
    if gemwords[1] not in GemLiquids:
	dbg = "Could not find liquid " + gemwords[1] + "\r\n"
        gemwords[1] += " " + gemwords[2]
        if gemwords[1] not in GemLiquids:
            return ['','','']
    # Suffix (may include second prefix word) to distinguish dust
    gemwords[2] = " ".join(gemwords[2:])
    if gemwords[2] not in GemDusts:
	dbg = "Could not find dust " + gemwords[2] + "\r\n"
        gemwords[2] = gemwords[3]
        if gemwords[2] not in GemDusts:
            return ['','','']
    if len(gemwords) > 3:
        gemwords.pop()
    return gemwords

def getGemMaterials(item, slot, realm):
    ret = { 'Gems' : { }, 'Dusts' : { }, 'Liquids' : { } }
    gemstate = item.getAttr('ActiveState')
    gemname = getGemName(item, slot)
    if gemname == '': return ret
    gemlevel, gemliquid, gemdust = getGemNameParts(gemname)
    if gemlevel == '': return ret

    gemtype = item.getSlotAttr(gemstate, slot, 'Type')
    gemindex = GemNames.index(gemlevel)

    if gemliquid == 'Brilliant':
        ret['Gems'][MaterialGems[gemindex]] = 3
    else:
        ret['Gems'][MaterialGems[gemindex]] = 1

    if gemliquid == 'Brilliant' or gemliquid == 'Finesse':
        ret['Dusts'][GemDusts[gemdust]] = (gemindex * 5) + 1
        ret['Liquids'][GemLiquids[gemliquid][0]] = (gemindex * 6) + 2
        ret['Liquids'][GemLiquids[gemliquid][1]] = (gemindex * 6) + 2
        ret['Liquids'][GemLiquids[gemliquid][2]] = (gemindex * 6) + 2
    elif gemtype == 'Focus' or gemtype == 'Resist':
        ret['Dusts'][GemDusts[gemdust]] = (gemindex * 5) + 1
        ret['Liquids'][GemLiquids[gemliquid]] = gemindex + 1
    else:
        ret['Dusts'][GemDusts[gemdust]] = (gemindex * 4) + 1
        ret['Liquids'][GemLiquids[gemliquid]] = gemindex + 1
    
    return ret

def getItemImbue(item):
    itemlevel = int(item.getAttr('Level'))
    if (item.getAttr('Level') == item.getAttr('AFDPS')) \
            and (itemlevel % 2 == 1) and (itemlevel != 51):
        itemlevel = itemlevel - 1
    if item.getAttr('ItemQuality') == '':
        item.loadAttr('ItemQuality', '94')
    if itemlevel == '':
        itemimbue = 0
    else:
        itemimbue = ImbuePts[itemlevel - 1]\
                            [int(item.getAttr('ItemQuality')) - 94]

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
        return (0, 1)
    gemname = getGemName(item, i)
    if gemname == '': return (0, 1)
    gemlevel, gemliquid, gemdust = getGemNameParts(gemname)
    if gemlevel == '': return (0, 1)
    costindex = ValuesLists[gemtype].index(str(amount))
    cost = GemCosts[costindex]
    remakecost = RemakeCosts[costindex]
    if gemtype == 'Resist' or gemtype == 'Focus':
        cost += 60 * costindex
        remakecost += 60 * costindex
    elif gemliquid == 'Finesse':
        cost += 200 + 180 * costindex
        remakecost += 120 + 180 * costindex
    elif gemliquid == 'Brilliant':
        cost = cost * 3 + 180 * costindex
        remakecost = remakecost * 3 + 180 * costindex
    cost += remakecost * int(item.getSlotAttr(itemtype, i, 'Remakes'))
    return (cost, costindex+1)

# vim: set ts=4 sw=4 et:
