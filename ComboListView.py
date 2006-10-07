from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ComboListView(QListView):
    def __init__(self, p, cb):
        QListView.__init__(self, p)
        self.combobox = cb

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Tab or e.key() == Qt.Key_Backtab:
            backFocus = e.key() == Qt.Key_Backtab
            idxs = self.selectedIndexes()
            if len(idxs) > 0:
                self.combobox.setCurrentIndex(idxs[0].row())
                self.combobox.emit(SIGNAL("activated(int)"),self.combobox.currentIndex())
                self.combobox.emit(SIGNAL("activated(const QString &)"),self.combobox.currentText())

            self.combobox.hidePopup()
            self.combobox.focusNextPrevChild(not backFocus)
            #self.focusNextPrevChild(not backFocus)
        else:
            QListView.keyPressEvent(self, e)

       
