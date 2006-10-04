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
    if not item.ActiveState == 'player': return 0
    if item.Level == '': return 0
    itemlevel = max(1,min(51,int(item.Level)))
    if (item.Level == item.AFDPS) \
            and (itemlevel % 2 == 1) and (itemlevel != 51):
        itemlevel = itemlevel - 1
    if item.ItemQuality == '':
        qualityindex = 0
    else:
        qualityindex = int(item.ItemQuality) - 94
    return ImbuePts[itemlevel - 1][qualityindex]

def calcImbue(item):
    if not item.ActiveState == 'player': return 0
    mvals = []
    for slot in item.slots():
        if slot.crafted():
            mvals.append(slot.gemImbue())
    maximbue = max(mvals)
    mvals.remove(maximbue)
    totalimbue = ((maximbue * 2 + sum(mvals)) / 2.0)
    return totalimbue

def computeOverchargeSuccess(imbue, itemimbue, item, crafterskill):
    success = -OCStartPercentages[int(imbue-itemimbue)]
    for i in range(0, 4):
        if item.slot(i).gemImbue() > 0 and GemQualOCModifiers.has_key(item.slot(i).qua()):
            success += GemQualOCModifiers[item.slot(i).qua()]
    success += ItemQualOCModifiers[item.ItemQuality]
    skillbonus = (int(crafterskill / 50) - 10) * 5
    if skillbonus > 50: skillbonus = 50
    success += skillbonus
    return success

# vim: set ts=4 sw=4 et:
