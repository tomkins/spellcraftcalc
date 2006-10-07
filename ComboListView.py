from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ComboListView(QListView):
    def __init__(self, p, cb):
        QListView.__init__(self, p)
        self.combobox = cb
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def showEvent(self, e):
        e.accept()
        model = self.model()
        rows = model.rowCount()
        fm = QFontMetrics(self.font())
        mx = 0

        for i in range(0, rows):
            idx = model.index(i, 0)
            data = model.data(idx)
            s = str(data.toString())
            print s
            print fm.size(Qt.TextSingleLine, s).width()
            mx = max(mx, fm.size(Qt.TextSingleLine, s).width())

        mx += 25

        self.setGeometry(self.pos().x(), self.pos().y(), mx, self.height())
        self.parent().setGeometry(self.parent().pos().x(),
            self.parent().pos().y(), mx, self.parent().height())
            


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

       
    def focusOutEvent(self, e):
        idxs = self.selectedIndexes()
        if len(idxs) > 0:
            self.combobox.setCurrentIndex(idxs[0].row())
            self.combobox.emit(SIGNAL("activated(int)"),self.combobox.currentIndex())
            self.combobox.emit(SIGNAL("activated(const QString &)"),self.combobox.currentText())

