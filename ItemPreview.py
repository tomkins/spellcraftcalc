from qt import *
from Item import *
from constants import *
from B_ItemPreview import *

class Preview(QFilePreview):
    def __init__(self, parent, scwin):
        QFilePreview.__init__(self)
        self.parent = parent
        self.item = Item()
        self.item.loadAttr('Realm', scwin.realm)
        self.scwin = scwin

    def previewUrl(self, url):
        charclass = unicode(self.scwin.CharClass.currentText())
        self.item.load(unicode(url.toString()), 1)  
        state = self.item.getAttr('ActiveState')
        utility = 0
        for i in range(0, 6):
            stattext = getattr(self.parent, 'Stat%d' % (i+1))
            stattext.setText('')
        if state == 'drop': toprng = 6
        else: toprng = 4
        for i in range(0, 6):
            stattext = getattr(self.parent, 'Stat%d' % (i+1))
            if i >= 4 and state == 'player':
                stattext.setText('')
                self.parent.ItemName.setText('')
                self.parent.ItemLevel.setText('')
                self.parent.ItemQua.setText('')
                self.parent.ItemAF.setText('')
                self.parent.ItemBonus.setText('')
                self.parent.ItemUtility.setText('')
                continue
            
            effect = self.item.getSlotAttr(state, i, 'Effect')
            gemtype = self.item.getSlotAttr(state, i, 'Type')
            if gemtype != 'Unused':
                amount = int(self.item.getSlotAttr(state, i, 'Amount'))
            statstr = self.item.getSlotAttr(state, i, 'Amount')
            statstr += ' ' + self.item.getSlotAttr(state, i, 'Effect')
            if self.item.getSlotAttr(state, i, 'Type') == 'Cap Increase':
                statstr += ' Cap Increase'
            stattext.setText(statstr)
            if gemtype == 'Skill':
                if effect == 'All Magic Skill Bonus'\
                    or effect == 'All Melee Skill Bonus'\
                    or effect == 'All Dual Wield Skill Bonus'\
                    or effect == 'Archery Skill Bonus':
                    for e in AllBonusList[charclass][effect]:
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
        self.parent.ItemName.setText(self.item.getAttr('ItemName'))
        self.parent.ItemLevel.setText(self.item.getAttr('Level'))
        self.parent.ItemQua.setText(self.item.getAttr('ItemQuality'))
        self.parent.ItemAF.setText(self.item.getAttr('AFDPS'))
        self.parent.ItemBonus.setText(self.item.getAttr('Bonus'))
        self.parent.ItemUtility.setText('%4.2f' % utility)
    
class ItemPreview(B_ItemPreview):
    def __init__(self,parent = None, scwin = None,fl = 0):
        print scwin
        B_ItemPreview.__init__(self,parent = None,name = None,fl = 0)
        self.pu = Preview(self, scwin)

