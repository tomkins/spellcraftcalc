# SC.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

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
    skillbonus = (int(crafterSkill / 50) - 10) * 5
    if skillbonus > 50: skillbonus = 50
    success += skillbonus
    return success

# vim: set ts=4 sw=4 et:
