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

class Item:
    def __init__(self, loc=''):
        self.__dict__ = { 'ActiveState' : '',
            'Location': '', 'Realm' : '',
            'ItemName' : '', 'AFDPS' : '',
            'Speed' : '', 'Bonus' : '',
            'ItemQuality' : '',
            'Equipped' : '', 'Level' : ''}
        self.slots = { 'drop' : range(1, 11), 
            'player' : range(1, 6) }

        if loc == 'Neck' \
                or loc == 'Cloak' \
                or loc == 'Jewel' \
                or loc == 'Belt' \
                or loc == 'Left Ring' \
                or loc == 'Right Ring' \
                or loc == 'Left Wrist' \
                or loc == 'Right Wrist':
            self.ActiveState = 'drop'
        else:
            self.ActiveState = 'player'
        if loc == 'Right Hand' \
                or loc == 'Left Hand' \
                or loc == '2 Handed' \
                or loc == 'Ranged' \
                or loc == 'Spare':
            self.Equipped = '0'
        else:
            self.Equipped = '1'

        self.Location = loc
        self.Level = '51'
        self.Quality = '99'

        self.makeEmptyItem()
            
    def loadAttr(self, attrname, attrval):
        if self.__dict__.has_key(attrname):
            self.__dict__[attrname] = attrval
            #eval(self.attrs[attrname] + ' = ' + attrval)
            #if attrname == 'ItemName':
            #    print 'loadAttr ' + attrval
            #    print 'loadAttr direct ' + self.ItemName

    def fixslot(self, slot):
        if FixEffectsTable.has_key(slot['Effect']):
            slot['Effect'] = FixEffectsTable[slot['Effect']]
        if slot['Type'] == 'Focus' and len(slot['Effect']) > 6 and slot['Effect'][-6:] == ' Focus':
            slot['Effect'] = slot['Effect'][:-6]
        if slot['Type'] == 'Unused':
            slot['Qua'] = "94"

    def loadSlotAttrs(self, type, slotnum, stattype='Unused', amount='', effect='', qua='94', 
            time='0', remakes='0', done='0'):
        self.slots[type][slotnum] = { }
        attr = self.slots[type][slotnum]
        attr['Type'] = unicode(stattype)
        attr['Amount'] = unicode(amount)
        attr['Effect'] = unicode(effect)
        attr['Qua'] = unicode(qua)
        attr['Time'] = unicode(time)
        attr['Remakes'] = unicode(remakes)
        attr['Done'] = unicode(done)
        self.fixslot(attr)
    
    def getSlotAttr(self, type, slotnum, attr):
        return self.slots[type][slotnum][attr]

    def getAttr(self, attrname):
        if self.__dict__.has_key(attrname):
            return self.__dict__[attrname]
            #return eval(self.attrs[attrname])

    def makeEmptyItem(self):
        for i in range(0, 10):
            self.loadSlotAttrs('drop', i) 
        for i in range(0, 5):
            self.loadSlotAttrs('player', i)

    def loadSlotAttr(self, type, slotnum, attr, val):
        self.slots[type][slotnum][attr] = val

    def __repr__(self):
        return unicode(self.slots)
        
    def asXML(self):
        document = Document()
        rootnode = document.createElement(unicode('SCItem'))
        document.appendChild(rootnode)
        for key in ['ActiveState', 'Location', 'Realm',
            'ItemName', 'AFDPS',
            'Speed', 'Bonus',
            'ItemQuality',
            'Equipped', 'Level']:
            val = getattr(self, key)
            elem = document.createElement(key)
            elem.appendChild(document.createTextNode(val))
            rootnode.appendChild(elem)

        for (key, val) in self.slots.items():
            #if key != self.ActiveState: continue
            statenode = document.createElement(unicode(string.upper(key)+'ITEM'))
            rootnode.appendChild(statenode)
            for slot in range(0, len(val)):
                if val[slot]["Type"] == "Unused": continue
                slotnode = document.createElement(unicode('SLOT'))
                slotnode.setAttribute(unicode("Number"), unicode(slot))
                statenode.appendChild(slotnode)
                for (slotkey, slotval) in val[slot].items():
                    valnode = document.createElement(unicode(slotkey))
                    valtext = document.createTextNode(unicode(slotval))
                    valnode.appendChild(valtext)
                    slotnode.appendChild(valnode)

        return document
    
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

    def loadFromXML(self, itemnode):
        for child in itemnode.childNodes:
            if child.nodeType == Node.TEXT_NODE: continue
            if self.__dict__.has_key(child.tagName):
                #if child.tagName == 'ItemName':
                #    print 'ItemName'
                #print XMLHelper.getText(child.childNodes)
                setattr(self, child.tagName, XMLHelper.getText(child.childNodes))
                #exec('%s = "%s"' % (self.attrs[child.tagName],
                #    XMLHelper.getText(child.childNodes)))
            else: 
                item_match = re.compile("(\w+)ITEM").match(child.tagName)
                if item_match is not None:
                    type = string.lower(item_match.group(1))
                    type_node = child
                    for slot in type_node.childNodes:
                        if slot.nodeType == Node.TEXT_NODE: continue
                        slot_match = re.compile("SLOT(\d+)").match(slot.tagName)
                        if slot_match is None:
                            slotnum = slot.getAttribute("Number")
                            if slotnum == '' or slotnum is None:
                                continue
                            slotnum = int(slotnum)
                        else:
                            slotnum = int(slot_match.group(1))
                        for attr in slot.childNodes:
                            if attr.nodeType == Node.TEXT_NODE: continue
                            attrval = XMLHelper.getText(attr.childNodes)
                            self.slots[type][slotnum][attr.tagName] = attrval
                        self.fixslot(self.slots[type][slotnum])

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
                self.Quality = line
            elif l == 24:
                self.AF = line
            elif l == 25:
                self.Speed = line
            elif l == 26:
                self.Bonus = line
        s = 0
        self.ActiveState = 'drop'
        for type, amount, effect, qua in slots:
            self.loadSlotAttrs('drop', s, type, amount, effect, qua)    
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
            if id == '':
                self.loadSlotAttrs(self.getAttr('ActiveState'), slotindex,
                    'Unused', '0', '', '99')
            else:
                for gem, subname in GemSubName.items():
                    namelist = GemTables[realm][gem]
                    gemamounts = ValuesLists[gem]
                    for effect in namelist.keys():
                        if re.compile('%s' % id, re.IGNORECASE)\
                                .search(string.strip(namelist[effect] + ' ' + subname))\
                                is not None:
                            if (self.getAttr('ActiveState') == 'player'):
                                self.loadSlotAttrs(self.getAttr('ActiveState'), 
                                        slotindex,
                                        gem, gemamounts[slot['Level']], 
                                        string.strip(effect), slot['Qual'],
                                        slot['Time'], slot['Remakes'], 
                                        slot['Done'])
                            else:
                                self.loadSlotAttrs(self.getAttr('ActiveState'), 
                                        slotindex,
                                        gem, slot['Level'], 
                                        string.strip(effect), slot['Qual'],
                                        slot['Time'], slot['Remakes'], 
                                        slot['Done'])
                            break
            slotindex += 1
