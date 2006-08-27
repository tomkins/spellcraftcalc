# SearchingCombo.py
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from qt import *
import sys
import string

class SearchingCombo(QComboBox):
    def __init__(self, parent=None, name=None, editable=False):
        QComboBox.__init__(self, editable, parent, name)

    def buildItemKeys(self):
        keys = []
        for i in range(0, self.count()):
            txt = str(self.listBox().item(i).text())
            keys.append(string.join(map(lambda s: s[0], str(txt).split()), "").upper())
        return keys

    def keyPressEvent(self, e):
        keycode = e.key()
        if len(e.text()) > 0 and not self.editable():
            key = str(e.text()).upper()
            indexlist = []
            if len(key) == 1:
                itemkeys = self.buildItemKeys()
                for i in range(0, len(itemkeys)):
                    if key in itemkeys[i]:
                        indexlist.append(i)
            if len(indexlist):
                if self.currentItem() >= indexlist[-1]:
                    self.setCurrentItem(indexlist[0])
                else:
                    i = filter(lambda x: x > self.currentItem(), indexlist)[0]
                    self.setCurrentItem(i)
                self.emit(SIGNAL("activated(const QString&)"),(self.currentText(),))
            e.accept()
            return
        QComboBox.keyPressEvent(self, e)
        return
