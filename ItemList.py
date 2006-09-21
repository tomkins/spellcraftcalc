# ItemList.py: Dark Age of Camelot Spellcrafting Calculator 
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Item import *
from Character import *
from constants import *
import sys

def fixlayout(parent):
    index = 0
    while (index < parent.count()):
        (row, col, rowSpan, colSpan) = parent.getItemPosition(index)
        if (colSpan == parent.columnCount()):
            # Take the List/Tree controls and squish them down...
            alignment = parent.itemAt(index).alignment()
            moveItem = parent.takeAt(index)
            parent.addItem(moveItem, row, col, rowSpan, colSpan - 2, alignment)
        else:
            # Fix the buttons' location, column 5 just grew wider...
            if (col == parent.columnCount() - 1):
                parent.itemAt(index).setAlignment(Qt.AlignRight)
            index += 1
        

class ItemPreview(QListWidget):
    def __init__(self, parent, realm, charclass):
        fixlayout(parent.layout())
        QListWidget.__init__(self, None)
        parent.layout().addWidget(self, 1, 4, 1, 2)
        self.item = Item()
        self.item.loadAttr('Realm', realm)
        self.realm = realm
        self.charclass = charclass

    def preView(self, filename):
        self.clear()
        if self.item.load(unicode(filename), 1) == -2:
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
                    for e in AllBonusList[self.realm][self.charclass][effect]:
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

    
class ItemListDialog(QFileDialog):
    def __init__(self, parent = None, caption = None, itemdir = None, filter = None, realm = None, charclass = None):
        QFileDialog.__init__(self, parent, caption, itemdir, filter)
        self.setAcceptMode(QFileDialog.AcceptOpen)
        self.setFileMode(QFileDialog.ExistingFile)
        self.setViewMode(QFileDialog.List)
        self.preview = ItemPreview(self, realm, charclass)
        self.connect(self,SIGNAL("currentChanged(const QString&)"),self.currentChanged)
        self.connect(self,SIGNAL("filesSelected(const QStringList &)"),self.filesSelected)

    def currentChanged(self, file):
        self.preview.preView(file)

    def filesSelected(self, files):
        if files.count() == 1:
            self.preview.preView(files[0])

if __name__ == "__main__":
    QApplication.setDesktopSettingsAware(0)
    mine = QApplication(sys.argv)
    extstr = 'XML Files (*.xml)'
    itemdir = ''
    Qfd = ItemListDialog(None, "Open Item", itemdir, extstr, "Albion", "Armsman")
    if Qfd.exec_():
        filename = Qfd.selectedFile()
