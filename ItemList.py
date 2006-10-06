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
        self.realm = realm
        self.charclass = charclass

    def preView(self, filename):
        self.clear()
        item = Item(realm=self.realm)
        if item.load(unicode(filename), 1) == -2:
            return
        stattext = []
        for slot in item.slots():
            gemtype = slot.type()
            if not gemtype or gemtype == 'Unused':
                continue
            statstr = slot.effect() + ' ' + slot.amount()
            if slot.type() == 'Resist' or slot.type() == 'Focus' or \
               slot.type() == 'Cap Increase':
                statstr += ' '+ slot.type()
            stattext.append(statstr)
        classinfo = AllBonusList[self.realm][self.charclass]
        listtext = [
            str(item.ItemName),
            "Level: %s   Quality: %s   Utility: %.1f" % (item.Level,
                                         item.ItemQuality, 
                                         item.utility(classinfo)),
            "AF/DPS: %s   Speed: %s   Bonus:  %s" % (item.AFDPS,
                                         item.Speed,
                                         item.Bonus),
        ]
        self.addItems(listtext)
        self.addItems(stattext)

    
class ItemListDialog(QFileDialog):
    def __init__(self, parent = None, caption = None, itemdir = None, filter = None, realm = None, charclass = None):
        QFileDialog.__init__(self, parent, caption, itemdir, filter)
        self.setAcceptMode(QFileDialog.AcceptOpen)
        self.setFileMode(QFileDialog.ExistingFile)
        self.setViewMode(QFileDialog.List)
        self.preview = ItemPreview(self, realm, charclass)
        self.connect(self,SIGNAL("currentChanged(const QString&)"),self.currentChanged)

    def currentChanged(self, file):
        self.preview.preView(file)
