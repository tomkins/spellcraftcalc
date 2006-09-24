# SearchingCombo.py
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

import sys
import string

from PyQt4.QtGui import QComboBox
from PyQt4.QtCore import SIGNAL, Qt

class SearchingCombo(QComboBox):
    def __init__(self, parent=None, name=None, editable=False):
        QComboBox.__init__(self, parent)
        self.setEditable(editable)

    def buildItemKeys(self):
        keys = []
        for i in range(0, self.count()):
            txt = str(self.itemText(i))
            keys.append(string.join(map(lambda s: s[0], txt.split()), "").upper())
        return keys

    def keyPressEvent(self, e):
        keycode = e.key()
        if keycode == Qt.Key_Up and \
                (not e.modifiers() or e.modifiers() == Qt.NoModifier or e.modifiers() == Qt.KeypadModifier) \
                and self.currentIndex() > 0:
            self.setCurrentIndex(self.currentIndex()-1)
            self.emit(SIGNAL("activated(const QString &)"),self.currentText())
            e.accept()
            return
        if keycode == Qt.Key_Down and \
                (not e.modifiers() or e.modifiers() == Qt.NoModifier or e.modifiers() == Qt.KeypadModifier) \
                and self.currentIndex() < self.count()-1:
            self.setCurrentIndex(self.currentIndex()+1)
            self.emit(SIGNAL("activated(const QString &)"),self.currentText())
            e.accept()
            return
        if not self.isEditable() and len(e.text()) > 0:
            key = str(e.text()).upper()
            indexlist = []
            if len(key) == 1:
                itemkeys = self.buildItemKeys()
                for i in range(0, len(itemkeys)):
                    if key in itemkeys[i]:
                        indexlist.append(i)
            if len(indexlist):
                if self.currentIndex() >= indexlist[-1]:
                    self.setCurrentIndex(indexlist[0])
                else:
                    i = filter(lambda x: x > self.currentIndex(), indexlist)[0]
                    self.setCurrentIndex(i)
                self.emit(SIGNAL("activated(const QString &)"),self.currentText())
            e.accept()
            return
        QComboBox.keyPressEvent(self, e)
