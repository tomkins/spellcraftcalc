# ItemList.py: Dark Age of Camelot Spellcrafting Calculator 
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtGui import *
from PyQt4.Qt3Support import Q3FilePreview
from Item import *
from Character import *
from constants import *

class Preview(Q3FilePreview):
    def __init__(self, itemlist, scwin):
        Q3FilePreview.__init__(self)
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
            gemtype = self.item.getSlotAttr(state, i, 'Type')
            if not gemtype or gemtype == 'Unused':
                continue
            effect = self.item.getSlotAttr(state, i, 'Effect')
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
            str(self.item.getAttr('ItemName')),
            "Level: %s   Quality: %s   Utility: %.1f" % (self.item.getAttr('Level'),
                                         self.item.getAttr('ItemQuality'), utility),
            "AF/DPS: %s   Speed: %s   Bonus:  %s" % (self.item.getAttr('AFDPS'),
                                         self.item.getAttr('Speed'),
                                         self.item.getAttr('Bonus')),
        ]
        listtext.extend(stattext)
        self.itemlist.insertItems(0, listtext)

    
class ItemList(QListWidget):
    def __init__(self, parent = None, scwin = None, fl = 0):
        QListWidget.__init__(self, parent)
        self.preview = Preview(self, scwin)
