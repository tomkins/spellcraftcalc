# SearchingCombo.py
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

import sys
import string

from PyQt4.QtGui import QComboBox, QFontMetrics, QStyleOptionComboBox, QStyle
from PyQt4.QtCore import SIGNAL, Qt, QSize
from ComboListView import ComboListView

class SearchingCombo(QComboBox):
    def __init__(self, parent=None, name=None, editable=False):
        QComboBox.__init__(self, parent)
        self.setMaxVisibleItems(20)
        self.setEditable(editable)
        self.minText = ' '
        self.setView(ComboListView(self, self))

    def insertItems(self, idx, lst):
        len_ = 0
        for s in lst:
            if len(s) > len(self.minText):
                self.minText = s
        QComboBox.insertItems(self, idx, lst)

    def getMinimumWidth(self, items = None):
        if items:
            len_ = 0
            for s in items:
                if len(s) > len(self.minText):
                    self.minText = s
        fm = QFontMetrics(self.font())
        opt = QStyleOptionComboBox()
        opt.setCurrentText = self.minText
        sz = QSize(fm.width(self.minText), fm.height())
        return self.style().sizeFromContents(QStyle.CT_ComboBox, opt, sz, self).width()

    def buildItemKeys(self):
        keys = []
        for i in range(0, self.count()):
            txt = str(self.itemText(i))
            keys.append(string.join(map(lambda s: s[0], txt.split()), "").upper())
        return keys

    def keyPressEvent(self, e):
        keycode = e.key()
        if keycode == Qt.Key_Up and \
                (e.modifiers() == Qt.NoModifier or e.modifiers() == Qt.KeypadModifier) \
                and self.currentIndex() > 0:
            self.setCurrentIndex(self.currentIndex()-1)
            self.emit(SIGNAL("activated(int)"),self.currentIndex())
            self.emit(SIGNAL("activated(const QString &)"),self.currentText())
            e.accept()
            return
        if keycode == Qt.Key_Down and \
                (e.modifiers() == Qt.NoModifier or e.modifiers() == Qt.KeypadModifier) \
                and self.currentIndex() < self.count()-1:
            self.setCurrentIndex(self.currentIndex()+1)
            self.emit(SIGNAL("activated(int)"),self.currentIndex())
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
                self.emit(SIGNAL("activated(int)"),self.currentIndex())
                self.emit(SIGNAL("activated(const QString &)"),self.currentText())
            e.accept()
            return
        QComboBox.keyPressEvent(self, e)
