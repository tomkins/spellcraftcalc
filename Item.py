# Item.py: Dark Age of Camelot Spellcrafting Calculator 
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from xml.dom.minidom import *
from constants import *
import string
import XMLHelper
import re
import types
from PyQt4.QtGui import *
from MyStringIO import UnicodeStringIO
import sys

class ItemSlot:
    def __init__(self, slottype='player', type='Unused', amount='0', effect='',
                 qua='94', time='0', remakes='0', done='0', requirement=''):
        self.__dict__ = { 
            'SlotType' : unicode(slottype),
            'Type': '', 'Effect' : '', 'Amount' : '', 'Requirement' : '',
            'Qua' : '', 'Time' : '',   'Remakes' : '', 'Done' : '', }
        self.setAll(type, amount, effect, qua, time, remakes, done, requirement)

    def setAll(self, type='Unused', amount='0', effect='',
               qua='94', time='0', remakes='0', done='0',
               requirement=''):
        self.Type = unicode(type)
        self.Amount = unicode(amount)
        self.Effect = unicode(effect)
        self.Qua = unicode(qua)
        self.Time = unicode(time)
        self.Remakes = unicode(remakes)
        self.Done = unicode(done)
        self.Requirement = unicode(requirement)
        self.fixEffect()
        self.CraftOk = False

    def asXML(self,document,slotnode):
        if self.SlotType == 'player':
            keys = ['Type', 'Effect', 'Amount', 'Qua', 'Remakes', 'Time', 'Done', ]
        else:
            keys = ['Type', 'Effect', 'Amount', 'Requirement', ]
        for attrkey in keys:
            valnode = document.createElement(unicode(attrkey))
            valtext = document.createTextNode(self.getAttr(attrkey))
            valnode.appendChild(valtext)
            slotnode.appendChild(valnode)

    def getAttr(self, attrname):
        if self.__dict__.has_key(attrname):
            return self.__dict__[attrname]

    def setAttr(self, attrname, value):
        self.CraftOk = False
        if self.__dict__.has_key(attrname):
            self.__dict__[attrname] = unicode(value)

    def fixEffect(self):
        if FixEffectsTable.has_key(self.Effect):
            self.Effect = FixEffectsTable[self.Effect]
        if self.Type == 'Focus' and len(self.Effect) > 6 and self.Effect[-6:] == ' Focus':
            self.Effect = self.Effect[:-6]

    def slotType(self):
        return self.SlotType
    def setSlotType(self, slottype):
        self.CraftOk = False
        self.SlotType=unicode(slottype)

    def type(self):
        return self.Type
    def setType(self, type):
        self.CraftOk = False
        if type == 'Unused' or type == '':
            self.setAll()
        else:
            self.Type=unicode(type)

    def amount(self):
        if self.Type == 'Unused': return ''
        return self.Amount
    def setAmount(self, amount):
        self.CraftOk = False
        if amount == '': amount = '0'
        self.Amount = unicode(amount)

    def effect(self):
        return self.Effect
    def setEffect(self, effect):
        self.CraftOk = False
        self.Effect = unicode(effect)

    def requirement(self):
        return self.Requirement
    def setRequirement(self, requirement):
        self.CraftOk = False
        self.Requirement = unicode(requirement)

    def qua(self):
        return self.Qua
    def setQua(self, qua):
        self.CraftOk = False
        if qua == '': qua = '94'
        self.Qua = unicode(qua)

    def quaIndex(self):
        if self.Qua in QualityValues:
            return QualityValues.index(self.Qua)
        return -1

    def time(self):
        return self.Time
    def setTime(self, time):
        if time == '': time = '0'
        self.Time = unicode(time)

    def remakes(self):
        return self.Remakes
    def setRemakes(self, remakes):
        if remakes == '': remakes = '0'
        self.Remakes = unicode(remakes)

    def done(self):
        return self.Done
    def setDone(self, done):
        if done == '': done = '0'
        self.Done = unicode(done)

    def crafted(self):
        if self.CraftOk: return True
        if not self.SlotType == 'player': return False
        if self.Type == '' or self.Type == 'Unused': return False
        if self.Effect == '': return False
        if self.Amount == '' or self.Amount == '0': return False
        if self.gemLevel() < 0: return False
        if self.quaIndex < 0: return False
        self.CraftOk = True
        return self.CraftOk

    def gemLevel(self):
        if not ValuesLists.has_key(self.Type): return -1
        amountlist = ValuesLists[self.Type]
        if not isinstance(amountlist, tuple):
            if not amountlist.has_key(self.Effect): return -1
            amountlist = amountlist[self.Effect]
        if not self.Amount in amountlist: return -1
        return amountlist.index(self.Amount) + 1

    def gemImbue(self):
        mval = 0
        if not self.crafted(): return 0.0
        if self.Type == 'Stat':
            return ((int(self.Amount) - 1) / 3.0) * 2.0 + 1.0
        if self.Type == 'Hits':
            return int(self.Amount) / 4.0
        if self.Type == 'Resist' or self.Type == 'Power':
            mval = (int(self.Amount) - 1) * 2.0
        elif self.Type == 'Skill':
            mval = (int(self.Amount) - 1) * 5.0
        if (mval < 1): return 1.0
        return mval

    def gemUtility(self):
        mval = 0.0
        if self.Amount == '0':
            pass
        elif self.Type == 'Stat':
            mval = ((int(self.Amount) - 1) / 3.0) * 2.0 + 1.0
        elif self.Type == 'Resist' or self.Type == 'Power':
            mval = (int(self.Amount) - 1) * 2.0
            if int(self.Amount) == 1: mval = 1.0
        elif self.Type == 'Skill':
            mval = (int(self.Amount) - 1) * 5.0
            if int(self.Amount) == 1: mval = 1.0
        elif self.Type == 'Focus':
            mval = 1.0
        elif self.Type == 'Hits':
            return int(self.Amount) / 4.0
        return mval

    def gemName(self, realm):
        if not GemTables.has_key(realm): return ''
        if not self.crafted():
            return ''
        amountindex = self.gemLevel() - 1
        if self.Type[-6:] == 'Effect':
            if not EffectTypeNames.has_key(self.Type): return ''
            if not EffectItemNames.has_key(self.Effect): return ''
            return string.strip(EffectItemNames[self.Effect][0]
                    + ' ' + EffectTypeNames[self.Type][0]
                    + ' ' + EffectItemNames[self.Effect][1]
                    + ' ' + EffectMetal[realm][amountindex]
                    + ' ' + EffectTypeNames[self.Type][1])
        if not GemTables[realm].has_key(self.Type): return ''
        gemlist = GemTables[realm][self.Type]
        if not gemlist.has_key(self.Effect):
            gemlist = GemTables['All'][self.Type]
            if not gemlist.has_key(self.Effect): return ''
        return string.strip(GemNames[amountindex]
                + ' ' + gemlist[self.Effect][0]
                + ' ' + gemlist[self.Effect][1])

    def gemMaterials(self, realm):
        ret = { 'Gems' : { }, 'Dusts' : { }, 'Liquids' : { } }
        if not self.crafted() or not GemTables.has_key(realm):
            return ret
        gemindex = self.gemLevel() - 1
        gemlist = GemTables[realm][self.Type]
        if not gemlist.has_key(self.Effect):
            gemlist = GemTables['All'][self.Type]
            if not gemlist.has_key(self.Effect): return ''
        gemdust = gemlist[self.Effect][2]
        gemliquid = gemlist[self.Effect][3]
        ret['Gems'][MaterialGems[gemindex]] = 1
        if self.Effect[0:4] == 'All ':
            if self.Type == 'Focus':
                ret['Gems'][MaterialGems[gemindex]] = 3
            ret['Dusts'][gemdust] = (gemindex * 5) + 1
            ret['Liquids'][gemliquid[0]] = (gemindex * 6) + 2
            ret['Liquids'][gemliquid[1]] = (gemindex * 6) + 2
            ret['Liquids'][gemliquid[2]] = (gemindex * 6) + 2
        elif self.Type == 'Focus' or self.Type == 'Resist':
            ret['Dusts'][gemdust] = (gemindex * 5) + 1
            ret['Liquids'][gemliquid] = gemindex + 1
        else:
            ret['Dusts'][gemdust] = (gemindex * 4) + 1
            ret['Liquids'][gemliquid] = gemindex + 1
        return ret

    def gemCost(self, tries=0):
        if not self.crafted():
            return 0
        if tries > 0:
            remakes = tries
        else:
            remakes = int(self.Remakes) + 1
            if self.Done == '0':
                remakes += EstimatedMakes[self.quaIndex()] - 1
        costindex = self.gemLevel() - 1
        cost = GemCosts[costindex]
        remakecost = RemakeCosts[costindex]
        if self.Effect[0:4] == 'All ':
            if self.Type == 'Focus':
                cost = cost * 3 + 180 * costindex
                remakecost = remakecost * 3 + 180 * costindex
            else:
                cost += 200 + 180 * costindex
                remakecost += 120 + 180 * costindex
        elif self.Type == 'Resist' or self.Type == 'Focus':
            cost += 60 * costindex
            remakecost += 60 * costindex
        cost += remakecost * remakes
        return cost


class Item:
    def __init__(self, state='', loc='', realm='All'):
        self.__dict__ = { 
            'ActiveState' : state,
            'Equipped' : '0',
            'Location': loc,
            'Realm' : realm,
            'Level' : '51',
            'ItemQuality' : '99',
            'ItemName' : '',
            'AFDPS' : '',
            'Speed' : '',
            'Bonus' : '',
        }

        self.itemslots = list()
        self.next = None

        if len(loc) > 0:
            if loc in JewelTabList:
                self.Equipped = '1'
            elif loc in PieceTabList:
                if loc in PieceTabList[:8]:
                    self.Equipped = '1'
                else:
                    self.Equipped = '0'
            if len(state) == 0:
                if loc in JewelTabList:
                    self.ActiveState = 'drop'
                elif loc in PieceTabList:
                    self.ActiveState = 'player'

        self.itemslots = self.makeSlots()

    def makeSlots(self, type=''):
        if type == '':
            type = self.ActiveState

        slots = []

        if type == 'drop':
            for slot in range(0, 12):
                slots.append(ItemSlot(type))
        elif type == 'player':
            for slot in range(0, 4):
                slots.append(ItemSlot(type))
            slots.append(ItemSlot('crafted'))
            slots.append(ItemSlot('unused'))

        return slots

    def copy(self):
        item = Item()
        item.ActiveState = self.ActiveState
        item.Location = self.Location
        item.Realm = self.Realm
        item.Equipped = self.Equipped
        item.Level = self.Level
        item.ItemQuality = self.ItemQuality
        item.ItemName = self.ItemName
        item.AFDPS = self.AFDPS
        item.Speed = self.Speed
        item.Bonus = self.Bonus
        item.itemslots = self.itemslots[:]
        item.next = self.next
        return item

    def slot(self, index):
        return self.itemslots[index]

    def slotCount(self):
        return len(self.itemslots)

    def slots(self):
        return list(self.itemslots)

    def loadAttr(self, attrname, attrval):
        if self.__dict__.has_key(attrname):
            self.__dict__[attrname] = attrval
            #eval(self.attrs[attrname] + ' = ' + attrval)
            #if attrname == 'ItemName':
            #    print 'loadAttr ' + attrval
            #    print 'loadAttr direct ' + self.ItemName

    def getAttr(self, attrname):
        if self.__dict__.has_key(attrname):
            return self.__dict__[attrname]

    def __repr__(self):
        return unicode(self.itemslots)
        
    def asXML(self):
        document = Document()
        rootnode = document.createElement(unicode('SCItem'))
        document.appendChild(rootnode)
        for key in ['ActiveState', 'Location', 'Realm',
            'ItemName', 'AFDPS', 'Speed', 'Bonus',
            'ItemQuality', 'Equipped', 'Level']:
            val = getattr(self, key)
            if val == '': continue
            elem = document.createElement(key)
            elem.appendChild(document.createTextNode(val))
            rootnode.appendChild(elem)

        for num in range(0,len(self.itemslots)):
            if self.itemslots[num].type() == "Unused": continue
            slotnode = document.createElement(unicode('SLOT'))
            slotnode.setAttribute(unicode("Number"), unicode(num))
            self.itemslots[num].asXML(document,slotnode)
            rootnode.appendChild(slotnode)
        return document

    def utility(self, skilltable):
        utility = 0.0
        for slot in self.slots():
            gemtype = slot.type()
            if gemtype == 'Unused': continue
            amount = int(slot.amount())
            if slot.type() == 'Skill':
                #if slot.effect()[0:4] == 'All Magic Skills':
                #    for e in skilltable[effect]:
                #        utility += amount * 5
                #else:
                utility += amount * 5
            elif gemtype == 'Focus':
                utility += 1
            elif gemtype == 'Power':
                utility += amount * 2
            elif gemtype == 'Hits':
                utility += amount / 4.0
            elif gemtype == 'Resist':
                utility += amount * 2
            elif gemtype == 'Stat':
                utility += amount * 2.0 / 3.0
        return utility
    
    def save(self, filename):
        try:
            f = file(filename, 'w')
        except IOError:
            QMessageBox.critical(None, 'Error!', 
                'Error opening file: ' + filename, 'OK')
            return
        f.write(XMLHelper.writexml(self.asXML(), UnicodeStringIO(), '', '\t', '\n'))
        f.close()

    def load(self, filename, silent = 0):
        try:
            f = file(filename, 'r')
        except IOError:
            if not silent:
                QMessageBox.critical(None, 'Error!', 
                    'Error opening item file: ' + filename, 'OK')
            return -2

        docstr = f.read()
        if re.compile('^<\?xml').match(docstr) is not None:
            try:
                xmldoc = parseString(docstr)
                items = xmldoc.getElementsByTagName('SCItem')
                self.loadFromXML(items[0])
            except:
                if not silent:
                    QMessageBox.critical(None, 'Error!', 
                        'Error loading item:', 'OK')
                f.close()
                return -1
        else:
            f.seek(0)
            if re.compile('^QUALITY').match(docstr) is None:
                self.importLela(f)
            else:
                self.loadLelaItemFromSCC(0, f.readlines(), self.Realm, True)
        f.close()

    def loadFromXML(self, itemnode, namehint = ''):
        slots = {}
        for child in itemnode.childNodes:
            if child.nodeType == Node.TEXT_NODE: continue
            if self.__dict__.has_key(child.tagName):
                #if child.tagName == 'ItemName':
                #    print 'ItemName'
                #print XMLHelper.getText(child.childNodes)
                setattr(self, child.tagName, XMLHelper.getText(child.childNodes))
                #exec('%s = "%s"' % (self.attrs[child.tagName],
                #    XMLHelper.getText(child.childNodes)))
                if child.tagName == 'ActiveState':
                    self.itemslots = self.makeSlots()
            elif child.tagName == 'SLOT':
                slotval = child.getAttribute("Number")
                itemslot = self.itemslots[slotnum]
                for attr in child.childNodes:
                    if attr.nodeType == Node.TEXT_NODE: continue
                    val = XMLHelper.getText(attr.childNodes)
                    if itemslot.__dict__.has_key(attr.tagName):
                        itemslot.setAttr(attr.tagName, val)
                    itemslot.fixEffect()
            elif child.tagName[-4:] == "ITEM":
                # Legacy nested DROPITEM/PLAYERITEM slots
                type = string.lower(child.tagName[:-4])
                slots[type] = self.makeSlots(type)
                if len(slots[type]) == 0:
                    slots.pop(type)
                slotnum = -1
                found = False
                for slot in child.childNodes:
                    if slot.nodeType == Node.TEXT_NODE: continue
                    slot_match = re.compile("SLOT(\d+)").match(slot.tagName)
                    if slot_match is None:
                        slotval = slot.getAttribute("Number")
                        if slotval == '' or slotval is None:
                            slotnum = slotnum + 1
                        else:
                            slotnum = int(slotval)
                    else:
                        slotnum = int(slot_match.group(1))
                    for attr in slot.childNodes:
                        if attr.nodeType == Node.TEXT_NODE: continue
                        val = XMLHelper.getText(attr.childNodes)
                        itemslot = slots[type][slotnum]
                        if itemslot.__dict__.has_key(attr.tagName):
                            itemslot.setAttr(attr.tagName, val)
                    if itemslot.type() != 'Unused':
                        found = True
                    itemslot.fixEffect()
                if not found:
                    slots.pop(type)
        if len(slots) > 0:
            if slots.has_key(self.ActiveState):
                self.itemslots = slots[self.ActiveState]
                self.itemslots = slots.pop(self.ActiveState)
            if len(slots) > 0:
                self.next = self.copy()
                type = slots.keys()[0]
                self.next.Equipped = '0'
                self.next.ActiveState = type
                self.next.itemslots = slots[type]
        item = self
        while item:
            if item.ActiveState == 'player':
                item.ItemName = 'Crafted Item' + namehint
            elif len(item.ItemName) == 0:
                item.ItemName = 'Drop Item' + namehint
            item = item.next

    def importLela(self, f):
        f.seek(0)
        lines = f.readlines()
        slots = []
        for l in range(0, len(lines)):
            line = string.strip(lines[l], " \n\r")
            if l == 1:
                self.Realm = line
            elif l == 5:
                self.ItemName = line
            elif l in range(6, 10):
                slots.append([])
                slots[l-6].append(TypeList[int(line)])  
            elif l in range(10, 14):
                slots[l-10].append(line)
            elif l in range(14, 18):
                if slots[l-14][0] == 'Unused':
                    slots[l-14].append('')
                else:
                    efflist = GemTables[self.Realm][slots[l-14][0]]
                    slots[l-14].append(efflist[int(line)])
            elif l in range(18, 22):
                if line == '0': line = '99'
                slots[l-18].append(line)
            elif l == 22:
                self.Level = line
            elif l == 23:
                self.ItemQuality = line
            elif l == 24:
                self.AF = line
            elif l == 25:
                self.Speed = line
            elif l == 26:
                self.Bonus = line
        s = 0
        self.ActiveState = 'drop'
        for type, amount, effect, qua in slots:
            self.slot(s).setAll(type, amount, effect, qua, self.Realm) 
            s += 1

    def loadLelaItemFromSCC(self, itemnum, scclines, realm, sepitem=False):
        slotattrs = []
        self.loadAttr('Realm', realm)
        itemquality = '0'
        for line in scclines:
            line = string.strip(line, " \n\r")
            if re.compile('^ITEM%02d' % itemnum).match(line) is not None\
                    or sepitem:
                itemname, value = string.split(line, '=', 1)
                if not sepitem:
                    i, attr = string.split(itemname, '_', 1)
                else:
                    attr = itemname
                gem_match = re.compile('^GEM(\d)').match(attr)
                if gem_match is not None:
                    slotnum = int(gem_match.group(1))
                    if len(slotattrs) < (slotnum + 1):
                        slotattrs.append({})
                    a, gem_attr = string.split(attr, '_', 1)
                    if gem_attr == 'QUALITY':
                        gemqual = QualityValues[int(value)]
                        slotattrs[slotnum]['Qual'] = gemqual
                    elif gem_attr == 'LEVEL':
                        slotattrs[slotnum]['Level'] = int(value)
                    elif gem_attr == 'GEM_ID':
                        value = re.sub('FOCUS_', '', value)
                        slotattrs[slotnum]['ID'] = value
                    elif gem_attr == 'REMAKES':
                        slotattrs[slotnum]['Remakes'] = value
                    elif gem_attr == 'MINUTES':
                        slotattrs[slotnum]['Time'] = value
                    elif gem_attr == 'DONE':
                        slotattrs[slotnum]['Done'] = value
                else:
                    if attr == 'QUALITY':
                        itemquality = value
                        #self.loadAttr('ItemQuality', QualityValues[int(value)])
                    elif attr == 'LEVEL':
                        self.loadAttr('Level', value)
                    elif attr == 'EQUIPPED':
                        self.loadAttr('Equipped', value)
                    elif attr == 'PLAYER_MADE':
                        if value == '1':
                            self.loadAttr('ActiveState', 'player')
                            self.loadAttr('ItemQuality', QualityValues[int(itemquality)])
                        else:   
                            self.loadAttr('ActiveState', 'drop')
                            self.loadAttr('ItemQuality', itemquality)
                    elif attr == 'DPS':
                        self.loadAttr('AFDPS', value)
                    elif attr == 'SPEED':
                        self.loadAttr('Speed', value)
                    elif attr == 'BONUS':
                        self.loadAttr('Bonus', value)
                    elif attr == 'NAME':
                        self.loadAttr('ItemName', value)
        slotindex = 0
        for slot in slotattrs:
            id = re.sub('_', ' ', slot['ID'])           
            if id == 'ASHEN CHAOS RUNE':
                id = 'ASHEN PRIMAL RUNE'
            if id == 'LIGHTNING WAR RUNE':
                id = 'LIGHTNING CHARGED WAR RUNE'
            if id == 'MYSTIC ESSENCE':
                id = 'MYSTICAL ESSENCE'
            if not id == '':
                for gem, subname in GemSubName.items():
                    namelist = GemTables[realm][gem]
                    gemamounts = ValuesLists[gem]
                    for effect in namelist.keys():
                        if re.compile('%s' % id, re.IGNORECASE)\
                                .search(string.strip(namelist[effect] + ' ' + subname))\
                                is not None:
                            if (self.getAttr('ActiveState') == 'player'):
                                self.slot(slotindex).setAll(gem, 
                                        gemamounts[slot['Level']], 
                                        string.strip(effect), slot['Qual'],
                                        self.Realm, slot['Time'],
                                        slot['Remakes'], slot['Done'])
                            else:
                                self.slot(slotindex).setAll(gem,  slot['Level'], 
                                        string.strip(effect), slot['Qual'],
                                        self.Realm, slot['Time'], 
                                        slot['Remakes'], slot['Done'])
                            break
            slotindex += 1
