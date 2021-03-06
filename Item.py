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
import SC


class ItemSlot:
    def __init__(self, slottype='player', type='Unused', amount='0', effect='', requirement=''):
        self.__dict__ = {
            'SlotType': unicode(slottype),
            'Type': '',
            'Effect': '',
            'Amount': '',
            'Requirement': '',
        }
        self.setAll(type, amount, effect, requirement)

    def setAll(self, type='Unused', amount='0', effect='', requirement=''):
        self.Type = unicode(type)
        self.Amount = unicode(amount)
        self.Effect = unicode(effect)
        self.Requirement = unicode(requirement)
        self.fixEffect()
        self.CraftOk = False

    def getAttr(self, attrname):
        if self.__dict__.has_key(attrname):
            return self.__dict__[attrname]

    def setAttr(self, attrname, value):
        self.CraftOk = False
        if self.__dict__.has_key(attrname):
            self.__dict__[attrname] = unicode(value)

    def fixEffect(self):
        if FixTypeTable.has_key(self.Type):
            self.Type = FixTypeTable[self.Type]
        if self.Type == 'Focus' and len(self.Effect) > 6 and self.Effect[-6:] == ' Focus':
            self.Effect = self.Effect[:-6]
        if FixEffectsTable.has_key(self.Effect):
            self.Effect = FixEffectsTable[self.Effect]

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
        if self.Type == 'Unused':
            return ''
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

    def crafted(self):
        if self.CraftOk:
            return True
        if self.Type == '' or self.Type == 'Unused':
            return False
        if self.Effect == '':
            return False
        if not self.SlotType in ('player', 'effect',):
            return False
        if self.gemLevel() < 0:
            return False
        self.CraftOk = True
        return self.CraftOk

    def gemLevel(self):
        if ((self.SlotType != 'player' and self.SlotType != 'effect')
         or not ValuesLists.has_key(self.Type)):
            return -1
        amountlist = ValuesLists[self.Type]
        if not isinstance(amountlist, tuple):
            if amountlist.has_key(self.Effect):
                amountlist = amountlist[self.Effect]
                if isinstance(amountlist[0], tuple):
                    amountlist = amountlist[0]
            elif amountlist.has_key(None):
                amountlist = amountlist[None]
            else:
                return -1
        if not self.Amount in amountlist: return -1
        return amountlist.index(self.Amount) + 1

    def gemImbue(self):
        mval = 0
        if not self.crafted(): return 0.0
        if self.Type == 'Stat':
            if self.Effect == 'Hits':
                return int(self.Amount) / 4.0
            elif self.Effect == 'Power':
                mval = (int(self.Amount) - 1) * 2.0
            else:
                return ((int(self.Amount) - 1) / 3.0) * 2.0 + 1.0
        elif self.Type == 'Resist':
            mval = (int(self.Amount) - 1) * 2.0
        elif self.Type == 'Skill':
            mval = (int(self.Amount) - 1) * 5.0
        if (mval < 1): return 1.0
        return mval

    def gemUtility(self,skilltable={}):
        if self.Amount == '0' or self.Amount == '':
            return 0.0

        # Go lambda!
        try:
            return {
                'Stat': lambda x: (self.Effect == 'Hits' and [x / 4.0] or [x * 2.0 / 3.0])[0],
                'Resist': lambda x: x * 2,
                'Power': lambda x: x * 2,
                'Skill': lambda x: x * 5,
                'Focus': lambda x: 1.0,
            }[self.Type](float(self.Amount))
        except KeyError:
            return 0

    def gemName(self, realm, parts = 7):
        if self.SlotType == 'crafted':
            return '(Crafted Item Bonus)'
        if not GemTables.has_key(realm): return ''
        if not self.crafted():
            return ''
        amountindex = self.gemLevel() - 1
        if self.Type[-6:] == 'Effect':
            if not EffectTypeNames.has_key(self.Type): return ''
            if self.Type == 'Charged Effect':
                effectItemNames = StableItemNames
            else:
                effectItemNames = ProcItemNames
            if not effectItemNames.has_key(self.Effect): return ''
            if not (isinstance(ValuesLists[self.Type], dict)
                and ValuesLists[self.Type].has_key(self.Effect)
                and isinstance(ValuesLists[self.Type][self.Effect][0], tuple)):
                    return ''
            #requiredlevel = ValuesLists[self.Type][self.Effect][1][self.gemLevel()]
            amountindex += ValuesLists[self.Type][self.Effect][2]
            if (len(effectItemNames[self.Effect]) > 2
            and EffectMetal['All'][amountindex] == ""):
                # Different naming for the Drop tinctures
                return string.strip(
                    ' '.join([
                        EffectTypeNames[self.Type][0],
                        effectItemNames[self.Effect][2],
                        "Tincture (Drop)"
                    ]))
            else:
                return string.strip(
                    ' '.join([
                        effectItemNames[self.Effect][0],
                        EffectTypeNames[self.Type][0],
                        effectItemNames[self.Effect][1],
                        EffectMetal['All'][amountindex],
                        EffectTypeNames[self.Type][1]
                    ]))
        if not GemTables[realm].has_key(self.Type): return ''
        gemlist = GemTables[realm][self.Type]
        if not gemlist.has_key(self.Effect):
            gemlist = GemTables['All'][self.Type]
            if not gemlist.has_key(self.Effect): return ''
        if parts == 7:
            return string.strip(
                ' '.join([
                    GemNames[amountindex],
                    gemlist[self.Effect][0],
                    gemlist[self.Effect][1]
                ]))
        else:
            name = ""
            if parts & 4:
                name += GemNames[amountindex] + ' '
            if parts & 2:
                name += gemlist[self.Effect][0] + ' '
            if parts & 1:
                name += gemlist[self.Effect][1] + ' '
            return string.strip(name)

    def gemMaterials(self, realm):
        ret = { 'Gems' : { }, 'Dusts' : { }, 'Liquids' : { } }
        if not self.crafted() or not GemTables.has_key(realm):
            return ret
        gemindex = self.gemLevel() - 1
        gemlist = GemTables[realm][self.Type]
        if not gemlist.has_key(self.Effect):
            gemlist = GemTables['All'][self.Type]
            if not gemlist.has_key(self.Effect): return ret
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

    def gemCost(self, makes=1):
        if not self.crafted():
            return 0
        costindex = self.gemLevel() - 1
        cost = GemCosts[costindex]
        if self.Effect[0:4] == 'All ':
            if self.Type == 'Focus':
                cost = cost * 3 + 180 * costindex
            else:
                cost += 200 + 180 * costindex
        elif self.Type == 'Resist' or self.Type == 'Focus':
            cost += 60 * costindex
        cost = cost * makes
        return cost

    def asXML(self,slotnode,realm='',rich=False):
        document = Document()
        if self.Type == 'Unused' or self.Type == '':
            savexml = [(u'Type', u'Unused',),]
        else:
            savexml = [(u'Type', self.Type,),
                       (u'Effect', self.Effect,),
                       (u'Amount', self.Amount,)]
            if len(self.Requirement) > 0:
                savexml.append((u'Requirement', self.Requirement,))
            if rich:
                if self.Type[-6:] != "Effect":
                    savexml.append(
                       (u'Utility', u"%.1f" % self.gemUtility(),))
                name = self.gemName(realm)
                if len(name) > 0:
                    savexml.append(
                       (u'Name', name,))
                if self.crafted():
                    savexml.extend([
                       (u'Imbue', u"%.1f" % self.gemImbue(),),
                       (u'Level', unicode(self.gemLevel()),),
                       (u'Cost', unicode(self.gemCost()),)])
        for attrkey, attrval in savexml:
            if not rich and (attrval == '0' or attrval == ''):
                continue
            valnode = document.createElement(attrkey)
            valtext = document.createTextNode(attrval)
            valnode.appendChild(valtext)
            slotnode.appendChild(valnode)
        if rich and (self.SlotType == 'player') and self.crafted():
            matslist = self.gemMaterials(realm)
            #valnode = document.createElement(u'Materials')
            for mattype in (u'Gems', u'Dusts', u'Liquids',):
                matnames = matslist[mattype].keys()
                matnames.sort()
                for mat in matnames:
                    matsort = MaterialsOrder.index(mat)
                    matnode = document.createElement(u'Material')
                    matnode.setAttribute(u'Amount',
                                          unicode(matslist[mattype][mat]))
                    matnode.setAttribute(u'Type', mattype)
                    matnode.setAttribute(u'Name', unicode(mat))
                    matnode.setAttribute(u'Order', unicode(matsort))
                    slotnode.appendChild(matnode)
                    #valnode.appendChild(matnode)
            #slotnode.appendChild(valnode)

class Item:
    def __init__(self, state='', loc='', realm='All', idx = -1):
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
            'TYPE' : '',
            'SOURCE' : '',
            'OFFHAND' : '',
            'DAMAGETYPE' : '',
            'DBSOURCE' : 'kscraft',
            'CLASSRESTRICTIONS' : list(),
            'Notes' : '',
            'Requirement' : '',
            'TemplateIndex' : idx,
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

    def clearSlots(self):
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
            slots.append(ItemSlot('effect'))

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

    def itemImbue(self):
        if self.ActiveState != "player": return 0
        try: itemlevel = int(self.Level)
        except: itemlevel = 0
        if itemlevel < 1 or itemlevel > 51:
            return 0.0
        if (self.Level == self.AFDPS) and (itemlevel % 2 == 1) \
                and (itemlevel > 1) and (itemlevel != 51):
            # Cloth armor imbue points quirk
            itemlevel = itemlevel - 1
        itemimbue = ImbuePts[itemlevel - 1]
        return itemimbue

    def listGemImbue(self):
        if self.ActiveState != 'player': return (0.0, 0.0, 0.0, 0.0,)
        mvals = [self.slot(0).gemImbue(), self.slot(1).gemImbue(),
                 self.slot(2).gemImbue(), self.slot(3).gemImbue(),]
        maximbue = max(mvals)
        for j in range(0, len(mvals)):
            if j == mvals.index(maximbue): continue
            mvals[j] = mvals[j] / 2.0
        return mvals

    def totalImbue(self):
        if self.ActiveState != "player": return 0.0
        return sum(self.listGemImbue())

    def overchargeSuccess(self, crafterSkill=1000):
        itemimbue = self.itemImbue()
        gemimbue = self.listGemImbue()
        imbuepts = sum(gemimbue)
        if imbuepts == 0: return 0
        if (imbuepts - itemimbue) >= 6:
            return -100
        elif imbuepts < (itemimbue + 1.0):
            return 100
        success = 34 + ItemQualOCModifiers[self.ItemQuality]
        success -= OCStartPercentages[int(imbuepts-itemimbue)]
        skillbonus = int(crafterSkill / 10)
        if skillbonus > 100: skillbonus = 100
        success += skillbonus
        fudgefactor = int(100.0 * ((skillbonus / 100.0 - 1.0) \
                                 * (OCStartPercentages[int(imbuepts-itemimbue)] / 200.0)))
        success += fudgefactor
        if success > 100: success = 100
        return success

    def cost(self):
        cost = 0
        for slot in self.slots():
            cost += slot.gemCost()
        return cost

    def utility(self, skilltable={}):
        utility = 0.0
        for slot in self.slots():
            utility += slot.gemUtility(skilltable)
        return utility

    def isEmpty(self):
        for num in range(0,len(self.itemslots)):
            if self.itemslots[num].type() != "Unused": return False

        return True

    def asXML(self, pricingInfo=None, crafterSkill=1000,
                    realm=None, rich=False, writeIndex=False):
        if realm is None:
            realm = self.Realm
        document = Document()
        rootnode = document.createElement(u'SCItem')
        document.appendChild(rootnode)
        fields = [(u'ActiveState', self.ActiveState,),
                  (u'Location',self.Location,),
                  (u'Realm', self.Realm,),
                  (u'ItemName', self.ItemName,),
                  (u'AFDPS', self.AFDPS,),
                  (u'Speed', self.Speed,),
                  (u'Bonus', self.Bonus,),
                  (u'ItemQuality', self.ItemQuality,),
                  (u'Equipped', self.Equipped,),
                  (u'Level', self.Level,),
                  (u'Notes', self.Notes,),
                  (u'Requirement', self.Requirement,),
                  (u'TYPE', self.TYPE,),
                  (u'SOURCE', self.SOURCE,),
                  (u'OFFHAND', self.OFFHAND,),
                  (u'DAMAGETYPE', self.DAMAGETYPE,),
                  (u'DBSOURCE', self.DBSOURCE,),]
        if writeIndex:
            fields.extend([
                  (u'TemplateIndex', unicode(self.TemplateIndex),),])
        if rich:
            imbuevals = self.listGemImbue()
            fields.extend([
                  (u'Utility', u"%.1f" % self.utility(),),
                  (u'Cost', unicode(self.cost()),),
                  (u'Imbue', u"%.1f" % sum(imbuevals),),
                  (u'ItemImbue', unicode(self.itemImbue()),),
                  (u'Success',
                       unicode(self.overchargeSuccess(crafterSkill)),),])

        for key, val in fields:
            if not rich and val == '': continue
            if not isinstance(val, basestring):
                sys.stderr.write("%s value %s is not a string\n" % (key, str(val)))
            elem = document.createElement(key)
            elem.appendChild(document.createTextNode(unicode(val)))
            rootnode.appendChild(elem)
        if (len(self.CLASSRESTRICTIONS) > 0):
            elem = document.createElement(u'CLASSRESTRICTIONS')
            rootnode.appendChild(elem)
            for val in self.CLASSRESTRICTIONS:
                if not isinstance(val, basestring):
                    sys.stderr.write("CLASSRESTRICTION %s is not a string\n" % str(val))
                classnode = document.createElement(u'CLASS')
                classnode.appendChild(document.createTextNode(unicode(val)))
                elem.appendChild(classnode)
        slotnode = None
        for num in range(0,len(self.itemslots)):
            if self.itemslots[num].type() == "Unused":
                continue
            slotnode = document.createElement(u'SLOT')
            slotnode.setAttribute(u'Number', unicode(num))
            if rich or self.itemslots[num].slotType() != self.ActiveState:
                slotnode.setAttribute(u'Type', unicode(self.itemslots[num].slotType()))
            self.itemslots[num].asXML(slotnode,realm,rich)
            if rich and num < len(imbuevals) and imbuevals[num] > 0:
                imbuenode = slotnode.getElementsByTagName('Imbue')[0]
                elem = document.createTextNode(u"%.1f" % imbuevals[num])
                imbuenode.replaceChild(elem, imbuenode.childNodes[0])
            rootnode.appendChild(slotnode)
        return document

    def save(self, filename):
        itemxml = self.asXML()
        if itemxml is None:
            QMessageBox.critical(None, 'Error!',
                'There was no item to save!', 'OK')
            return
        try:
            f = file(filename, 'w')
        except IOError:
            QMessageBox.critical(None, 'Error!',
                'Error opening file: ' + filename, 'OK')
            return
        f.write(XMLHelper.writexml(itemxml, UnicodeStringIO(), '', '\t', '\n'))
        f.close()

    def load(self, filename, namehint = '', silent = 0):
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
                self.loadFromXML(items[0], namehint)
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

    def loadFromXML(self, itemnode, namehint = '', convert = False):
        slots = {}
        for child in itemnode.childNodes:
            if child.nodeType == Node.TEXT_NODE: continue
            if child.tagName == 'SLOT':
                slotval = child.getAttribute("Number")
                itemslot = self.itemslots[int(slotval)]
                slottype = child.getAttribute("Type")
                if slottype is not None and slottype != '':
                    itemslot.setSlotType(slottype)
                for attr in child.childNodes:
                    if attr.nodeType == Node.TEXT_NODE: continue
                    val = XMLHelper.getText(attr.childNodes)
                    if itemslot.__dict__.has_key(attr.tagName):
                        itemslot.setAttr(attr.tagName, val)
                    itemslot.fixEffect()
            elif child.tagName == 'CLASSRESTRICTIONS':
                for classnode in child.childNodes:
                    if classnode.nodeType == Node.TEXT_NODE: continue
                    val = XMLHelper.getText(classnode.childNodes)
                    val = val.strip()
                    if len(val) > 0:
                        self.CLASSRESTRICTIONS.append(val)
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
                        if slotval is None or slotval == '':
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
                if not (convert or found):
                    slots.pop(type)
            elif self.__dict__.has_key(child.tagName):
                #if child.tagName == 'ItemName':
                #    print 'ItemName'
                #print XMLHelper.getText(child.childNodes)
                setattr(self, child.tagName, XMLHelper.getText(child.childNodes))
                #exec('%s = "%s"' % (self.attrs[child.tagName],
                #    XMLHelper.getText(child.childNodes)))
                if child.tagName == 'ActiveState':
                    self.itemslots = self.makeSlots()
                elif child.tagName == 'TemplateIndex':
                    self.TemplateIndex = int(self.TemplateIndex)
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
                if self.ActiveState == 'player': self.ItemName = ''
                if self.next.ActiveState == 'player': self.next.ItemName = ''
        item = self
        while item:
            if item.ActiveState == 'player' and len(item.ItemName) == 0:
                item.ItemName = 'Crafted Item' + namehint
            elif len(item.ItemName) == 0:
                item.ItemName = 'Drop Item' + namehint
            item = item.next
