# ItemList.py: Dark Age of Camelot Spellcrafting Calculator 
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from qt import *
from Item import *
from constants import *

class Preview(QFilePreview):
    def __init__(self, itemlist, scwin):
        QFilePreview.__init__(self)
        self.itemlist = itemlist
        self.item = Item()
        self.item.loadAttr('Realm', scwin.realm)
        self.scwin = scwin

    def previewUrl(self, url):
        self.itemlist.clear()
        if self.item.load(unicode(url.toString()), 1) == -2:
            return

        state = self.item.getAttr('ActiveState')
        if state == 'drop': 
            toprng = 10
        else:
            toprng = 4
        utility = 0
        stattext = []

        for i in range(0, toprng):
            effect = self.item.getSlotAttr(state, i, 'Effect')
            gemtype = self.item.getSlotAttr(state, i, 'Type')
            if gemtype != 'Unused':
                amount = int(self.item.getSlotAttr(state, i, 'Amount'))
            statstr = self.item.getSlotAttr(state, i, 'Amount')
            statstr += ' ' + self.item.getSlotAttr(state, i, 'Effect')
            if self.item.getSlotAttr(state, i, 'Type') == 'Cap Increase':
                statstr += ' Cap Increase'
            stattext.append(statstr)
            ## This code must GO AWAY to Item.py:
            if gemtype == 'Skill':
                if effect == 'All Magic Skills'\
                    or effect == 'All Melee Weapon Skills'\
                    or effect == 'All Dual Wield Skills'\
                    or effect == 'All Archery Skills':
                    for e in AllBonusList[self.scwin.realm][self.scwin.charclass][effect]:
                        utility += amount * 5
                else:
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

        listtext = [
            "Name:   %s" % self.item.getAttr('ItemName'),
            "Level:  %s  Quality: %s" % (self.item.getAttr('Level'),
                                         self.item.getAttr('ItemQuality')),
            "AF/DPS: %s  Speed:   %s" % (self.item.getAttr('AFDPS'),
                                         self.item.getAttr('Speed')),
            "Bonus:  %s  Utility: %4.2f" % (self.item.getAttr('Bonus'), utility),
        ]
        listtext.extend(stattext)
        self.itemlist.insertStrList(listtext)

    
class ItemList(QListBox):
    def __init__(self, parent = None, scwin = None, fl = 0):
        QListBox.__init__(self, parent)
        self.preview = Preview(self, scwin)
