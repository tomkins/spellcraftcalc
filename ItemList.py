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
from ScOptions import ScOptions
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
        if item.load(unicode(filename), silent = 1) == -2:
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
            "Level: %s   Quality: %s" % (item.Level, item.ItemQuality),
            "AF/DPS: %s   Speed: %s" % (item.AFDPS, item.Speed),
            "Utility: %.1f   Bonus: %s" 
                    % (item.utility(classinfo), item.Bonus),
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
        self.connect(self,SIGNAL("finished(int)"),self.finish)

        self.loadOptions()

    def currentChanged(self, file):
        self.preview.preView(file)

    def finish(self, res):
        self.saveOptions()

    def saveOptions(self):
        ScOptions.instance().setOption('ItemListX', self.pos().x())
        ScOptions.instance().setOption('ItemListY', self.pos().y())
        ScOptions.instance().setOption('ItemListW', self.width())
        ScOptions.instance().setOption('ItemListH', self.height())

    def loadOptions(self):
        x = ScOptions.instance().getOption('ItemListX', self.pos().x())
        y = ScOptions.instance().getOption('ItemListY', self.pos().y())
        w = ScOptions.instance().getOption('ItemListW', self.width())
        h = ScOptions.instance().getOption('ItemListH', self.height())

        screenW = QApplication.desktop().width()
        screenH = QApplication.desktop().height()
        if w < 100:
            w = 781
        if h < 100:
            w = 589

        if w > screenW:
            w = 781
        if h > screenH:
            h = 589

        if x < 20 or x > (screenW - 20):
            x = 20
        if y < 20 or y > (screenH - 20):
            y = 20

        self.resize(w, h)
        self.move(x, y)
        self.updateGeometry()


