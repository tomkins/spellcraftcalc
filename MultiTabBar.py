# MultiTabBar: a superclass of QTabBar for multiple rows of tabs
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

# TODO:
#   * We draw the horizontal-bottom continuation bar for > 1 rows, but...
#     really should use the style itself to determine it's look (we use the
#     style''s color preference, but in Mac skins should use gradient tone.)

# [Won't consider tab scrolling - that's the point of multiple bars]

import sys
import string
from qt import *

def noamptext(text):
    start = str.find(text, '&')
    while start >= 0:
        if start >= len(text):
            text = text[0:start - 1]
            break
        else:
            text = text[0:start - 1] + text[start + 1:]
            start += 1
        start = str.find(text, '&', start)
    return text                


class MultiTabBar(QTabBar):
    def __init__(self, parent, name):
        QTabBar.__init__(self, parent, name)
        if QApplication.style().name()[0:9] == "Macintosh":
            self.rowoverlap = 3
            self.cropheight = -1
        else:
            self.rowoverlap = 3
            self.cropheight = 2
        self.tabrows = []
        self.currows = []

    def insertTab(self, tab, index = -1, row = -1):
        if index >= 0:
            row = 0
            rowindex = index
            for tabrow in self.tabrows:
                if rowindex < len(tabrow):
                    break
                row += 1
                rowindex -= len(tabrow)
            else:
                index = -1
        newid = QTabBar.insertTab(self, tab, index)
        if index >= 0:
            self.tabrows[row].insert(rowindex, newid)
        else:
            row = min(row, len(self.tabrows))
            if row < 0: row = max(0, len(self.tabrows))
            if row == len(self.tabrows):
                self.currows.insert(0, len(self.tabrows) - 1)
                self.tabrows.append([])
            self.tabrows[row].append(newid)
        return newid

    def addTab(self, tab, row = -1):
        return insertTab(self, tab, -1, row)

    def removeTab(self, tab):
        oldindex = self.indexOf(tab.identifier())
        if oldindex < 0: return
        row = 0
        rowindex = index
        for row in self.tabrows:
            if rowindex < len(tabrow):
                break
            row += 1
            rowindex -= len(tabrow)
        else:
            oldindex = -1 # Well that's wacked
        if oldindex >= 0:
            del self.tabrows[row][rowindex]
            if len(self.tabrows[row]) == 0:
                self.currows.remove(row)
                del self.tabrows[row]
        QTabBar.removeTab(self, tab)

    def setCurrentTab(self, tab):
        if self.count() == 0:
            return
        if isinstance(tab, int):
            tab = self.tab(tab)
        id = tab.identifier()
        if id in self.tabrows[self.currows[-1]]:
            QTabBar.setCurrentTab(self, tab)
        else:
            for row in range(0, len(self.tabrows)):
                if id in self.tabrows[self.currows[row]]:
                    saverow = self.currows[row]
                    self.currows[row] = self.currows[-1]
                    self.currows[-1] = saverow
                    self.layoutTabs()
                    if QApplication.style().name()[0:9] == "Macintosh":
                        QTabBar.setCurrentTab(self, tab)
                        self.repaint()
                    else:
                        self.repaint()
                        QTabBar.setCurrentTab(self, tab)
                    break

    def buildTabKeys(self):
        keys = []
        for i in range(0, self.count()):
            txt = str(self.tabAt(i).text())
            keys.append(string.join(map(lambda s: s[0], str(txt).split()), "").upper())
        return keys

    def keyPressEvent(self, e):
        if (e.key() == Qt.Key_Up or e.key() == Qt.Key_Down) and not e.state():
            if len(self.currows) <= 1: return
            if e.key() == Qt.Key_Up:
                newrow = self.tabrows[self.currows[-2]]
            else:
                newrow = self.tabrows[self.currows[0]]
            fr = self.tab(self.currentTab()).rect()
            fr.setLeft(fr.left() + fr.width() / 2)
            fr.setTop(0)
            for id in newrow:
                tab = self.tab(id)
                if tab.rect().intersects(fr):
                    self.setCurrentTab(tab)
                    return
        else:
            key = str(e.text()).upper()
            indexlist = []
            if len(key) == 1:
                tabkeys = self.buildTabKeys()
                for i in range(0, len(tabkeys)):
                    if key in tabkeys[i]:
                        indexlist.append(i)
            if len(indexlist) > 0:
                if self.currentTab() >= indexlist[-1]:
                    self.setCurrentTab(indexlist[0])
                else:
                    i = filter(lambda x: x > self.currentTab(), indexlist)[0]
                    self.setCurrentTab(i)
                return
        QTabBar.keyPressEvent(self, e)
        return

    def paintEvent(self, e):
        if e.rect().isNull():
	    return
        ct = self.tab(self.currentTab())
        painter = QPainter(self)
        cliprect = e.rect()
        if not e.erased():
             self.erase(cliprect)
             #painter.fillRect(cliprect, self.backgroundBrush())
        for row in range(0, len(self.tabrows)):
            telts = range(0, len(self.tabrows[self.currows[row]]))
            ft = self.tab(self.tabrows[self.currows[row]][0])
            lt = self.tab(self.tabrows[self.currows[row]][-1])
            rowrect = ft.rect()
            rowrect.setRight(self.rect().right())
            if not cliprect.intersects(rowrect):
                continue
            if self.cropheight > -1:
                if row < len(self.tabrows) - 1:
                    rowrect.setHeight(rowrect.height() - self.cropheight)
                    rowrect = cliprect.intersect(rowrect)
                    painter.setClipRect(rowrect, QPainter.CoordPainter)
                else:
                    painter.setClipping(0)
            for telt in telts:
                t = self.tab(self.tabrows[self.currows[row]][telt])
                if t == ct: 
                    continue
                if t.rect().intersects(rowrect):
                    self.paint(painter, t, 0);
        if ct.rect().intersects(cliprect):
            self.paint(painter, ct, 1);
        rowrect = QRect(lt.rect().right() + 1, lt.rect().bottom(), 
                        self.rect().width() - lt.rect().right() - 1, 1)
        if rowrect.intersects(cliprect):
            if not QApplication.style().name() == "CDE":
                painter.fillRect(rowrect, QBrush(self.colorGroup().midlight()));
                rowrect.moveTop(rowrect.top() - 1)
                rowrect.setRight(rowrect.right() - 1)
            painter.fillRect(rowrect, QBrush(self.colorGroup().light()));

    def sizeHint(self):
        size = QTabBar.sizeHint(self)
        size.setHeight(size.height() \
                     + self.style().pixelMetric(QStyle.PM_TabBarBaseHeight, self))
        return size

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

