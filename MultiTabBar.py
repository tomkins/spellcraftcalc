# MultiTabBar.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

import sys
import math
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MultiTabFrame(QFrame):
    def paintEvent(self, e):

        painter = QPainter(self)
        tabframe = QStyleOptionTabWidgetFrame()
        tabframe.initFrom(self);
        self.style().drawPrimitive(QStyle.PE_FrameTabWidget, 
                                   tabframe, painter, self)

class MultiTab:
    def __init__(self):
        self.enabled = True
        self.text = None
        self.icon = QIcon()
        self.rect = QRect()
        self.textColor = QColor(0, 0, 0)
        self.data = None

class MultiTabBar(QWidget):
    def __init__(self, parent = None, name = None):
        self.__tabList = []
        self.__selectedIndex = (0, 0)
        self.__pressedIndex = (0, 0)
        self.__hoverRect = QRect()
        self.__layoutDirty = True

        QWidget.__init__(self, parent)
        if (name):
            self.setObjectName(name)

        self.setFocusPolicy(Qt.TabFocus)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)

    def dump(self):
        taboverlap = QStyleOptionTab()
        taboverlap.shape = QTabBar.RoundedNorth
        for var in (
            'PM_TabBarTabOverlap',
            'PM_TabBarTabHSpace',
            'PM_TabBarTabShiftHorizontal',
            'PM_TabBarTabVSpace',
            'PM_TabBarTabShiftVertical',
            'PM_TabBarBaseHeight',
            'PM_TabBarBaseOverlap',
        ):
            val = self.style().pixelMetric(getattr(QStyle, var), 
                                           taboverlap, self)
            sys.stdout.write("%s = %s\n" % (var, val))


    def baseOverlap(self):
        taboverlap = QStyleOptionTab()
        taboverlap.shape = QTabBar.RoundedNorth
        # The overlap doesn't work on mac - it makes things too tight
        #if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
        #    return 2
        #else:
        return self.style().pixelMetric(QStyle.PM_TabBarBaseOverlap,
                                        taboverlap, self)

    def addTab(self, row, text):
        self.insertTab(row, -1, text)

    def insertTab(self, row, col, text):
        while len(self.__tabList) <= row:
            self.__tabList.append([])

        tab = MultiTab()
        tab.text = text

        if col >= len(self.__tabList[row]) or col == -1:
            self.__tabList[row].append(tab)
        else:
            self.__tabList[row].insert(col, tab)

        self.refresh()

    def removeTab(self, text):
        for row in self.__tabList:
            for tab in row:
                if tab.text == text:
                    row.remove(tab)
                    self.__layoutTabs()
                    return

    def removeTab(self, row, col):
        if len(self.__tabList) <= row:
            return None
        if len(self.__tabList[row]) <= col:
            return None

        del self.__tabList[row][col]
    
    def tabRect(self, row, col):
        tab = self.__tabAt(row, col)
        if tab:
            return tab.rect
        return None

    def currentIndex(self):
        return self.__selectedIndex

    def setCurrentIndex(self, *args):
        if len(args) == 1:
            loctuple = args[0]
            if isinstance(loctuple, tuple) and len(loctuple) == 2:
                self.__setCurrentIndex(loctuple[0], loctuple[1])
            else:
                raise TypeError, 'Argument should be a row,col tuple! or row,col as separate arguments!'
        elif len(args) == 2:
            row = args[0]
            col = args[1]
            self.__setCurrentIndex(row, col)
        else:
            raise TypeError, 'Argument should be a row,col tuple! or row,col as separate arguments!'

    def __setCurrentIndex(self, row, col):
        self.__selectedIndex = (row, col)
        self.__layoutTabs()
        self.update()

        self.emit(SIGNAL('currentChanged'), row, col)

    def numTabsInRow(self, row):
        if len(self.__tabList) <= row: return 0
        return len(self.__tabList[row])

    def setTabText(self, row, col, text):
        tab = self.__tabAt(row, col)
        if tab: 
            tab.text = text

    def tabText(self, row, col):
        tab = self.__tabAt(row, col)
        if tab: return tab.text
        return None

    def setTabData(self, row, col, data):
        tab = self.__tabAt(row, col)
        if tab: 
            tab.data = data

    def tabData(self, row, col):
        tab = self.__tabAt(row, col)
        if tab: return tab.data
        return None

    def index(self, tabname):
        for i in range(len(self.__tabList)):
            for j in range(len(self.__tabList[i])):
                if tabname == self.__tabList[i][j].text:
                    return i,j

        return None
    
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

        # small padding so when the right-tab has the focus, it looks cleaner
        padwidth = self.style().pixelMetric(QStyle.PM_DefaultFrameWidth) * 2
        r = QRect()
        for i in range(len(self.__tabList)):
            for j in range(len(self.__tabList[i])):
                r = r.unite(self.__tabAt(i, j).rect)
        r.setRight(r.right() + padwidth)
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            r.setBottom(r.bottom() + padwidth)
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
        overlap = 0
        theParent = self.parentWidget()
        optTabBase = QStyleOptionTabBarBase()
        optTabBase.initFrom(self)
        optTabBase.shape = QTabBar.RoundedNorth
        optTabBase.tabBarRect = QRect()

        painter = QPainter(self)

        selected = (-1, -1)
        selected = (0, 0)
        cut = -1
        rtl = False
        verticalTabs = False
        cutTab = QStyleOptionTab()
        selectedTab = QStyleOptionTab()

        for i in range(len(self.__tabList)):
            for j in range(len(self.__tabList[i])):
                tab = self.__getStyleOption(i, j)
                if not (tab.state & QStyle.State_Enabled):
                    tab.palette.setCurrentColorGroup(QPalette.Disabled)

                optTabBase.tabBarRect |= tab.rect
                if (i, j) == self.__selectedIndex:
                    selected = (i, j)
                    selectedTab = tab
                    optTabBase.selectedTabRect = tab.rect
                    continue
                self.style().drawControl(QStyle.CE_TabBarTab, tab,
                                         painter, self)

        if selected != (-1, -1):
            for j in range(len(self.__tabList[selected[0]])):
                tab = self.__getStyleOption(selected[0], j)
                self.style().drawControl(QStyle.CE_TabBarTab, tab,
                                         painter, self)
            tab = self.__getStyleOption(selected[0], selected[1])
            painter.eraseRect(tab.rect)
            self.style().drawControl(QStyle.CE_TabBarTab, tab,
                                     painter, self)

        #optTabBase.rect = optTabBase.tabBarRect
        #optTabBase.rect.setHeight(400)
        #self.style().drawPrimitive(QStyle.PE_FrameTabBarBase, optTabBase,
        #    painter, self)

    def mousePressEvent(self, e):
        if e.button() != Qt.LeftButton:
            e.ignore()
            return

        self.__pressedIndex = self.__indexAtPos(e.pos())
        if self.__pressedIndex != (-1, -1):
            if e.type() == self.style().styleHint(QStyle.SH_TabBar_SelectMouseType, None, self):
                self.setCurrentIndex(self.__pressedIndex[0], self.__pressedIndex[1])
            else:
                self.repaint(self.tabRect(self.__pressedIndex[0], self.__pressedIndex[1]))


    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            e.ignore()
            return

        if self.style().styleHint(QStyle.SH_TabBar_SelectMouseType, None, self) \
                == QEvent.MouseButtonRelease:
            i = self.__indexAtPos(e.pos())
            if i != self.__pressedIndex:
                oldIndex = self.__pressedIndex
                self.__pressedIndex = (-1, -1)
                if oldIndex != (-1, -1):
                    self.repaint(self.tabRect(oldIndex[0], oldIndex[1]))
                if self.__pressedIndex != (-1, -1):
                    self.repaint(self.tabRect(self.__pressedIndex[0],
                        self.__pressedIndex[1]))

    def mouseReleaseEvent(self, e):
        if e.button() != Qt.LeftButton:
            e.ignore()

        if self.__indexAtPos(e.pos()) == self.__pressedIndex:
            i = self.__pressedIndex
        else:
            i = (-1, -1)
        self.__pressedIndex = (-1, -1)
        if e.type() == \
                self.style().styleHint(QStyle.SH_TabBar_SelectMouseType, None,
                self) and i != (-1, -1):
            self.setCurrentIndex(i[0], i[1])

    def keyPressEvent(self, e):
        if (e.key() != Qt.Key_Left and e.key() != Qt.Key_Right \
            and e.key() != Qt.Key_Up) or e.modifiers() != Qt.NoModifier:
            e.ignore()
            return

        if e.key() == Qt.Key_Left or e.key() == Qt.Key_Right:
            dx = -1
            if e.key() == Qt.Key_Right: dx = 1
            index = self.__selectedIndex[1] + dx
            while index < self.numTabsInRow(self.__selectedIndex[0]) and \
                index >= 0:
                if self.__tabAt(self.__selectedIndex[0], index).enabled:
                    self.setCurrentIndex(self.__selectedIndex[0], index)
                    break
                index += dx

        if e.key() == Qt.Key_Up:
            if self.__selectedIndex[0] == len(self.__tabList) - 1:
                index = self.__selectedIndex[0] - 1
            else:
                index = len(self.__tabList) - 1
            if index < 0:
                index = 0

            col = self.__selectedIndex[1]
            if col >= self.numTabsInRow(index):
                col = self.numTabsInRow(index) - 1
            
            self.setCurrentIndex(index, col)

    def changeEvent(self, e):
        self.refresh()
        QWidget.changeEvent(self, e)

    def showEvent(self, e):
        if self.__layoutDirty:
            self.__layoutTabs()
        if self.__selectedIndex == (-1, -1):
            self.setCurrentIndex(0, 0)

    def resizeEvent(self, e):
        self.__layoutTabs()

    def event(self, e):
        if e.type() == QEvent.HoverMove or e.type == QEvent.HoverEnter:
            if self.__hoverRect.contains(e.pos()):
                oldHoverRect = self.__hoverRect
                for i in range(len(self.__tabList)):
                    for j in range(len(self.__tabList[i])):
                        area = self.tabRect(i, j)
                        if area.contains(e.pos()):
                            self.__hoverRect = area
                            break
                if e.oldPos() != QPoint(-1, -1):
                    self.update(oldHoverRect)
                update(self.__hoverRect)
            return True
        elif e.type() == QEvent.HoverLeave:
            oldHoverRect = self.__hoverRect
            self.__hoverRect = QRect()
            self.update(oldHoverRect)
            return True

        return QWidget.event(self, e)

    def refresh(self):
        if not self.isVisible():
            self.__layoutDirty = True
        else:
            self.__layoutTabs()
            self.update()
            self.updateGeometry()
        
#### HELPERS (private) ####
    def __tabAt(self, row, col):
        if len(self.__tabList) <= row:
            return None
        if len(self.__tabList[row]) <= col:
            return None
        return self.__tabList[row][col]

    """
    def layoutTabs(self):
        if self.count() < 1:
            return

        r = self.tabList()[0].rect()
        for t in self.tabList()[1:]:
	    r = r.unite(t.rect())
	oldSh = r.size()

        ## btnWidth = self.style().pixelMetric(QStyle.PM_TabBarScrollButtonWidth, self)
        hframe  = self.style().pixelMetric(QStyle.PM_TabBarTabHSpace, self)
        vframe  = self.style().pixelMetric(QStyle.PM_TabBarTabVSpace, self)
        overlap = self.style().pixelMetric(QStyle.PM_TabBarTabOverlap, self)
        baseh = self.style().pixelMetric(QStyle.PM_TabBarBaseHeight, self)

        fm = self.fontMetrics()
        reverse = QApplication.reverseLayout()
        lastrow = len(self.tabrows) - 1
        y = 0
        maxx = 0
        for row in range(0, lastrow + 1):
            if reverse:
                telts = range(len(self.tabrows[self.currows[row]]) - 1, -1, -1)
            else:
                telts = range(0, len(self.tabrows[self.currows[row]]))
            x = 0
            offset = 0
            for telt in telts:
                t = self.tab(self.tabrows[self.currows[row]][telt])
                w = fm.width(noamptext(str(t.text())));
                h = max(fm.height(), QApplication.globalStrut().height() )
                if t.iconSet():
                    w += t.iconSet().pixmap(QIconSet.Small, QIconSet.Normal).width() + 4
                    h = max(h, t.iconSet().pixmap(QIconSet.Small, QIconSet.Normal).height())
                h = max(h + vframe, QApplication.globalStrut().height())
                w = max(w + hframe, QApplication.globalStrut().width())
                t.setRect(QRect(QPoint(x, y), 
                                self.style().sizeFromContents(
                                    QStyle.CT_TabBarTab, self, \
                                    QSize(w, h), QStyleOption(t))))
                x += t.rect().width() - overlap
                r = r.unite(t.rect())
            y += h - self.rowoverlap
            maxx = max(maxx, x + overlap - 1)
        y += self.rowoverlap;

        for row in range(0, lastrow + 1):
            if reverse:
                telts = range(len(self.tabrows[self.currows[row]]) - 1, -1, -1)
            else:
                telts = range(0, len(self.tabrows[self.currows[row]]))
            addx = maxx - self.tab(self.tabrows[self.currows[row]][-1]).rect().right()
            adjx = 0
            if addx <= 0: telts = []
            while len(telts) > 0:
                fixx = ((addx + len(telts) - 1) / len(telts))
                t = self.tab(self.tabrows[self.currows[row]][telts[0]])
                newrect = t.rect()
                newrect.moveLeft(newrect.left() + adjx)
                newrect.setWidth(newrect.width() + fixx)
                t.setRect(newrect)
                addx -= fixx
                adjx += fixx
                r = r.unite(t.rect())
                telts = telts[1:]

        w = self.width()
        if maxx < w:
            offset = w - maxx
        if offset > 0:
            offset = 0

        for row in range(0, len(self.tabrows)):
            telts = range(0, len(self.tabrows[self.currows[row]]))
            for telt in telts:
                t = self.tab(self.tabrows[self.currows[row]][telt])
                t.rect().moveBy( offset, 0 )

        if self.sizeHint() != oldSh:
            self.updateGeometry()

        self.emit(PYSIGNAL("sigLayoutChanged"),(self,))
    """

    def __layoutTabs(self):
        self.__layoutDirty = False

        numrows = len(self.__tabList)
        taboverlap = QStyleOptionTab()
        taboverlap.shape = QTabBar.RoundedNorth

        baseoverlap = self.baseOverlap()
        rowoverlap = self.style().pixelMetric(QStyle.PM_TabBarTabShiftVertical,
                                              taboverlap, self)
        if not str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            rowoverlap += baseoverlap

        # Horizontal tabs only for now
        mx = 0
        maxWidth = 0
        maxHeight = 0
        maxNumTabs = 0
        maxRowWidth = 0
        mx_row = -1
        x = 0
        rowpcts = []

        for i in range(numrows):
            maxNumTabs = max(self.numTabsInRow(i), maxNumTabs)
            mw = 0
            rowpcts.append([])
            for j in range(len(self.__tabList[i])):
                sz = self.tabSizeHint(i, j)
                mw += sz.width()
                maxWidth = max(sz.width(), maxWidth)
                maxHeight = max(maxHeight, sz.height())
                rowpcts[i].append(sz.width())
            rowpcts[i] = map(lambda x: float(x) / mw, rowpcts[i])
            maxRowWidth = max(mw, maxRowWidth)

        maxHeight -= rowoverlap
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh":
            centerOffset = (self.width() - maxRowWidth) / 2.0
        else:
            centerOffset = 0

        for i in range(numrows):
            x = 0
            if i == self.__selectedIndex[0]:
                y = (len(self.__tabList) - 1) * maxHeight
            elif i < self.__selectedIndex[0] or self.__selectedIndex[0] == -1:
                y = i * maxHeight
            else:
                y = (i - 1) * maxHeight
                
            for j in range(self.numTabsInRow(i)):
                w = rowpcts[i][j] * maxRowWidth
                # Just pad at the end because Im' lazy
                if j == self.numTabsInRow(i) - 1 and \
                        (x + int(w)) < maxRowWidth:
                    w = maxRowWidth - x
                self.__tabList[i][j].rect = QRect(x + centerOffset, y, int(w), maxHeight + rowoverlap)
                x += int(w)

        self.tabLayoutChange()

    def __getStyleOption(self, row, col):
        tab = self.__tabAt(row, col)
        if not tab: return None

        opt = QStyleOptionTabV2()
        opt.initFrom(self)
        opt.state &= ~(QStyle.State_HasFocus | QStyle.State_MouseOver)
        opt.rect = self.tabRect(row, col)

        isCurrent = (row, col) == self.__selectedIndex
        opt.row = 0

        if (row, col) == self.__pressedIndex:
            opt.state |= QStyle.State_Sunken
        if isCurrent:
            opt.state |= QStyle.State_Selected
        if isCurrent and self.hasFocus():
            opt.state |= QStyle.State_HasFocus
        if not tab.enabled:
            opt.state &= ~QStyle.State_Enabled
        if self.isActiveWindow():
            opt.state |= QStyle.State_Active
        if opt.rect == self.__hoverRect:
            opt.state |= QStyle.State_MouseOver
        opt.shape = QTabBar.RoundedNorth
        opt.text = tab.text

        if tab.textColor.isValid():
            opt.palette.setColor(self.foregroundRole(), tab.textColor)

        opt.icon = tab.icon
        opt.iconSize = self.iconSize()
        if row == self.__selectedIndex[0]:
            if col > 0 and col - 1 == self.__selectedIndex[1]:
                opt.selectedPosition = QStyleOptionTab.PreviousIsSelected
            elif col < self.numTabsInRow(row) - 1 and \
                    col + 1 == self.__selectedIndex[1]:
                opt.selectedPosition = QStyleOptionTab.NextIsSelected
            else:
                opt.selectedPosition = QStyleOptionTab.NotAdjacent
        else:
            opt.selectedPosition = QStyleOptionTab.NotAdjacent

        if col == 0:
            if self.numTabsInRow(row) > 1:
                opt.position = QStyleOptionTab.Beginning
            else:
                opt.position = QStyleOptionTab.OnlyOneTab
        elif col == self.numTabsInRow(row) - 1:
            opt.position = QStyleOptionTab.End
        else:
            opt.position = QStyleOptionTab.Middle

        return opt

    def __indexAtPos(self, p):
        if self.tabRect(self.__selectedIndex[0],
                self.__selectedIndex[1]).contains(p):
            return self.__selectedIndex

        for i in range(len(self.__tabList)):
            for j in range(len(self.__tabList[i])):
                if self.__tabAt(i, j).enabled and self.tabRect(i,
                        j).contains(p):
                    return (i, j)

        return (-1, -1)

if __name__ == '__main__':
    QApplication.setDesktopSettingsAware(0)
    app = QApplication(sys.argv)

    wind = QMainWindow()
    child = QWidget(wind)
    wind.setCentralWidget(child)

    bar = MultiTabBar(child)
    bar.addTab(0, 'One')
    bar.addTab(0, 'two')
    bar.addTab(0, 'three')
    bar.addTab(0, 'four')
    bar.addTab(0, 'five')
    bar.addTab(1, 'One1')
    bar.addTab(1, 'two1')
    bar.addTab(1, 'three1')
    bar.addTab(1, 'four1')
    bar.setGeometry(QRect(0, 0, bar.sizeHint().width(), 
                                bar.sizeHint().height()))
    bar.dump()

    frame = QFrame(child)
    frame.setFrameShape(QFrame.StyledPanel)
    frame.setFrameShadow(QFrame.Raised)
    frame.setGeometry(QRect(0, bar.sizeHint().height() - bar.baseOverlap(), 
                            bar.sizeHint().width(), 200))

    #w2 = QWidget(w)
    #w2.setGeometry(QRect(300, 300, 100, 100))
    #statlayout = QGridLayout(w2)
    #statlayout.setMargin(3)
    #statlayout.setSpacing(0)

    #w3 = QWidget(w2)
    #statlayout.addWidget(w3, 0, 0, 1, 1)

    #w.resize(600, 400)
    frame.stackUnder(bar)

    #layout = QVBoxLayout(child)
    #layout.setSpacing(0)
    #layout.setMargin(1)
    #layout.addWidget(bar, 0)
    #layout.addWidget(frame, 0)
    wind.resize(600, 400)

    bar.setCurrentIndex((0, 0))
    bar.setCurrentIndex(1,1)

    wind.show()

    app.exec_()

# vim: set ts=4 sw=4 et:
