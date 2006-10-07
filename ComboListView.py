from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ComboListView(QListView):
    def __init__(self, p, cb):
        QListView.__init__(self, p)
        self.combobox = cb

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Tab:
            backFocus = False
            if e.modifiers() == Qt.ShiftModifier:
                backFocus = True
            idxs = self.selectedIndexes()
            if len(idxs) > 0:
                self.combobox.setCurrentIndex(idxs[0].row())


            self.combobox.hidePopup()
            self.combobox.focusNextPrevChild(not backFocus)
            #self.focusNextPrevChild(not backFocus)
        else:
            QListView.keyPressEvent(self, e)

       
