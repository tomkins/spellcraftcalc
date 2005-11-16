from qt import *
import sys
import string
class SearchingCombo(QComboBox):
    def __init__(self, parent=None, name=None):
        QComboBox.__init__(self, 0, parent, name)
        
    def buildItemList(self):
        lst = []
        for i in range(0, self.count()):
            li = self.listBox().item(i)
            lst.append(str(li.text()))  
        return lst

    def keyPressEvent(self, e):
        keycode = e.key()
        if keycode == Qt.Key_Up:
            ci = self.currentItem()
            if ci > 0: ci -= 1
            self.setCurrentItem(ci)
            self.emit(SIGNAL("activated(const QString&)"),(self.currentText(),))
        elif keycode == Qt.Key_Down:
            ci = self.currentItem()
            if ci != (self.count() - 1): ci += 1
            self.setCurrentItem(ci)
            self.emit(SIGNAL("activated(const QString&)"),(self.currentText(),))
        else:
            key = str(e.text())
            itemlist = self.buildItemList()
            indexlist = []
            for i in range(0, len(itemlist)):
                if string.lower(itemlist[i][0]) == string.lower(key):
                    indexlist.append(i)
            if len(indexlist) == 0:
                QComboBox.keyPressEvent(self, e)
                return
            if self.currentItem() >= indexlist[-1]:
                self.setCurrentItem(indexlist[0])
            else:
                i = filter(lambda x: x > self.currentItem(), indexlist)[0]
                self.setCurrentItem(i)
            self.emit(SIGNAL("activated(const QString&)"),(self.currentText(),))
