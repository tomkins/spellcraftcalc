import sys
import math
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MultiTab:
    def __init__(self):
        self.enabled = True
        self.text = None
        self.icon = QIcon()
        self.rect = QRect()
        self.textColor = QColor(0, 0, 0)
        self.data = None

class MultiTabBar4(QWidget):
    def __init__(self, parent = None, name = None):
        QWidget.__init__(self, parent)
        if (name):
            self.setObjectName(name)

        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            self.rowoverlap = 3
            self.cropheight = -1
        else:
            self.rowoverlap = 3
            self.cropheight = 2

        self.tabList = []
        self.selectedIndex = (0, 0)
        self.pressedIndex = (-1, -1)
        self.hoverRect = QRect()
        self.__layoutDirty = False


    def addTab(self, text, row):
        while len(self.tabList) <= row:
            self.tabList.append([])

        tab = MultiTab()
        tab.text = text
        self.tabList[row].append(tab)

        self.__layoutTabs()

    def removeTab(self, text):
        for row in self.tabList:
            for tab in row:
                if tab.text == text:
                    row.remove(tab)
                    return

    def tabRect(self, row, col):
        if len(self.tabList) < row:
            return None
        if len(self.tabList[row]) < col:
            return None

        return self.tabList[row][col].rect

    def currentSelection(self):
        return self.selectedIndex

    def setCurrentSelection(self, row, col):
        self.selectedIndex = (row, col)

    def setCurrentIndex(self, row, col):
        self.setCurrentSelection(row, col)
        self.update()

    def tabsInRow(self, row):
        if len(self.tabList) < row: return 0
        return len(self.tabList[row])
        
    
#### HELPERS (private) ####
    def __tabAt(self, row, col):
        if len(self.tabList) < row:
            return None
        if len(self.tabList[row]) < col:
            return None
        return self.tabList[row][col]

    def __layoutTabs(self):
        self.__layoutDirty = False

        numrows = len(self.tabList)
        # Horizontal tabs only for now
        mx = 0
        mx_row = -1
        x = 0
        maxHeight = 0

        for i in range(numrows):
            if self.tabsInRow(i) > mx:
                mx_row = i
                mx = self.tabsInRow(i)
        
        for i in range(mx):
            sz = self.tabSizeHint(mx_row, i)
            self.tabList[mx_row][i].rect = QRect(x, 0, sz.width(),
                sz.height())
            maxHeight = max(maxHeight, sz.height())
            x += sz.width()
        maxWidth = x

        for r in range(numrows):
            if r == mx_row: continue
            num = self.tabsInRow(r)
            w = maxWidth / num
            x = 0

            for i in range(num):
                self.tabList[r][i].rect = QRect(x, r * maxHeight, w, maxHeight)
                x += w

        for j in range(len(self.tabList[mx_row])):
            self.tabList[mx_row][j].rect.setHeight(maxHeight)
            self.tabList[mx_row][j].rect.setY(mx_row * maxHeight)

        self.tabLayoutChange()

    def __getStyleOption(self, row, col):
        tab = self.__tabAt(row, col)
        if not tab: return None

        opt = QStyleOptionTabV2()
        opt.initFrom(self)
        opt.state &= ~(QStyle.State_HasFocus | QStyle.State_MouseOver)
        opt.rect = self.tabRect(row, col)

        isCurrent = (row, col) == self.currentSelection()
        opt.row = 0

        if (row, col) == self.pressedIndex:
            opt.state |= QStyle.State_Sunken
        if isCurrent:
            opt.state |= QStyle.State_Selected
        if isCurrent and self.hasFocus():
            opt.state |= QStyle.State_HasFocus
        if not tab.enabled:
            opt.state &= ~QStyle.State_Enabled
        if self.isActiveWindow():
            opt.state |= QStyle.State_Active
        if opt.rect == self.hoverRect:
            opt.state |= QStyle.State_MouseOver
        opt.shape = QTabBar.RoundedNorth
        opt.text = tab.text

        if tab.textColor.isValid():
            opt.palette.setColor(self.foregroundRole(), tab.textColor)

        opt.icon = tab.icon
        opt.iconSize = self.iconSize()
        if row == self.currentSelection()[0]:
            if col > 0 and col - 1 == self.currentSelection()[1]:
                opt.selectedPosition = QStyleOptionTab.PreviousIsSelected
            elif col < self.tabsInRow(row) - 1 and \
                    col + 1 == self.currentSelection()[1]:
                opt.selectedPosition = QStyleOptionTab.NextIsSelected
            else:
                opt.selectedPosition = QStyleOptionTab.NotAdjacent
        else:
            opt.selectedPosition = QStyleOptionTab.NotAdjacent

        if col == 0:
            if self.tabsInRow(row) > 1:
                opt.position = QStyleOptionTab.Beginning
            else:
                opt.position = QStyleOptionTab.OnlyOneTab
        elif col == self.tabsInRow(row) - 1:
            opt.position = QStyleOptionTab.End
        else:
            opt.position = QStyleOptionTab.Middle

        return opt

    def __indexAtPos(self, p):
        if self.tabRect(self.currentSelection()[0],
                self.currentSelection()[1]).contains(p):
            return self.currentSelection()

        for i in range(len(self.tabList)):
            for j in range(len(self.tabList[i])):
                if self.__tabAt(i, j).enabled and self.tabRect(i,
                        j).contains(p):
                    return (i, j)

        return (-1, -1)

    def tabSizeHint(self, row, col):
        tab = self.__tabAt(row, col)
        if (tab):
            opt = self.__getStyleOption(row, col)
            if tab.icon.isNull():
                iconSize = QSize()
            else:
                opt.iconSize
            hframe = self.style().pixelMetric(QStyle.PM_TabBarTabHSpace, opt,
                self)
            vframe = self.style().pixelMetric(QStyle.PM_TabBarTabVSpace, opt,
                self)
            fm = self.fontMetrics()

            csz = QSize(fm.size(Qt.TextShowMnemonic, tab.text).width() +
                iconSize.width() + hframe,
                max(fm.height(), iconSize.height()) + vframe)

            return self.style().sizeFromContents(QStyle.CT_TabBarTab, opt,
                csz, self)
            
        return QSize()

    def minimumSizeHint(self):
        return self.sizeHint()

    def sizeHint(self):
        if self.__layoutDirty:
            self.__layoutTabs()

        r = QRect()
        for i in range(self.tabsInRow(0)):
            r = r.unite(self.__tabAt(0, i).rect)
        sz = QApplication.globalStrut()
        return r.size().expandedTo(sz)

    def iconSize(self):
        iconExtent = self.style().pixelMetric(QStyle.PM_TabBarIconSize)
        return QSize(iconExtent, iconExtent)

    def tabLayoutChange(self):
        pass

    def paintEvent(self, e):
        tabOverlap = QStyleOptionTab()
        tabOverlap.shape = QTabBar.RoundedNorth
        overlap = self.style().pixelMetric(QStyle.PM_TabBarBaseOverlap,
            tabOverlap, self)
        overlap = 0
        theParent = self.parentWidget()
        optTabBase = QStyleOptionTabBarBase()
        optTabBase.initFrom(self)
        optTabBase.shape = QTabBar.RoundedNorth
        if theParent and overlap > 0:
            # FIXME
            QPainter.setRedirected(theParent, self, self.pos())
            rect = QRect()
            rect.setRect(0, self.height() - overlap, self.width(), overlap)

        #p = QStylePainter(self)
        selected = (-1, -1)
        cut = -1
        rtl = False
        verticalTabs = False
        cutTab = QStyleOptionTab()
        selectedTab = QStyleOptionTab()

        #for i in range(len(self.tabList)):
        for i in range(len(self.tabList)):
            for j in range(len(self.tabList[i])):
                tab = self.__getStyleOption(i, j)
                if not (tab.state & QStyle.State_Enabled):
                    tab.palette.setCurrentColorGroup(QPalette.Disabled)

                optTabBase.tabBarRect |= tab.rect
                if (i, j) == self.currentSelection():
                    selected = (i, j)
                    selectedTab = tab
                    optTabBase.selectedTabRect = tab.rect
                    continue
                self.style().drawControl(QStyle.CE_TabBarTab, tab,
                    QPainter(self), self)
                #p.drawControl(QStyle.CE_TabBarTab, tab)

        if selected != (-1, -1):
            tab = self.__getStyleOption(selected[0],
                selected[1])
            self.style().drawControl(QStyle.CE_TabBarTab, tab,
                QPainter(self), self)

    def mousePressEvent(self, e):
        if e.button() != Qt.LeftButton:
            e.ignore()
            return

        self.pressedIndex = self.__indexAtPos(e.pos())
        if self.pressedIndex != (-1, -1):
            if e.type() == self.style().styleHint(QStyle.SH_TabBar_SelectMouseType, None, self):
                self.setCurrentSelection(pressedIndex)
            else:
                self.repaint(self.tabRect(self.pressedIndex[0], self.pressedIndex[1]))

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            e.ignore()
            return

        if self.style().styleHint(QStyle.SH_TabBar_SelectMouseType, None, self) \
                == QEvent.MouseButtonRelease:
            i = self.__indexAtPos(e.pos())
            if i != self.pressedIndex:
                oldIndex = self.pressedIndex
                pressedIndex = (-1, -1)
                if oldIndex != (-1, -1):
                    self.repaint(self.tabRect(oldIndex[0], oldIndex[1]))
                if self.pressedIndex != (-1, -1):
                    self.repaint(self.tabRect(self.pressedIndex[0],
                        self.pressedIndex[1]))

    def mouseReleaseEvent(self, e):
        if e.button() != Qt.LeftButton:
            e.ignore()

        if self.__indexAtPos(e.pos()) == self.pressedIndex:
            i = self.pressedIndex
        else:
            i = (-1, -1)
        self.pressedIndex = (-1, -1)
        if e.type() == \
                self.style().styleHint(QStyle.SH_TabBar_SelectMouseType, None,
                self):
            self.setCurrentIndex(i[0], i[1])

    def changeEvent(self, e):
        self.refresh()
        QWidget.changeEvent(self, e)

    def showEvent(self, e):
        if self.__layoutDirty:
            self.__layoutTabs()
        if self.currentSelection() == (-1, -1):
            self.setCurrentIndex(0, 0)

    def refresh(self):
        if not self.isVisible():
            self.__layoutDirty = True
        else:
            self.__layoutTabs()
            self.update()
            self.updateGeometry()
        
            
if __name__ == '__main__':
    QApplication.setDesktopSettingsAware(0)
    app = QApplication(sys.argv)

    w = QMainWindow()
    bar = MultiTabBar4(w)
    bar.addTab('One', 0)
    bar.addTab('two', 0)
    bar.addTab('three', 0)
    bar.addTab('four', 0)
    bar.addTab('five', 0)
    bar.addTab('One1', 1)
    bar.addTab('two1', 1)
    bar.addTab('three1', 1)
    bar.addTab('four1', 1)
    bar.addTab('five1', 1)

    bar.setGeometry(QRect(10, 10, 300, 80))
    
    w.resize(600, 400)

    #bar.show()

#    w.addWidget(bar)
    w.show()

    app.exec_()
        





        


            







# vim: set ts=4 sw=4 et:
