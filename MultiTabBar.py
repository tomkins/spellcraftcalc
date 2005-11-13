# MultiTabBar: a superclass of QTabBar for multiple rows of tabs
#
# See http://kscraft.sourceforge.net/python.html for details
#
# Copyright (C) 2005 Ehrayn <ehrayn@craftsage.com>.  All rights reserved.
#
# Portions copyright (C) 1992-2002 Trolltech AS.  All rights reserved.

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

# TODO:
#   * We draw the horizontal-bottom continuation bar for > 1 rows, but...
#     really should use the style itself to determine it's look (we use the
#     style''s color preference, but the width is wrong in the CDE skin.)
#   * Haven't even considered tab scrolling (that's the point of multiple
#     bars, isn't it?)
#   * Remove tabs/bars (we don't need no stinkin' remove - someone else might)
#   * Need to check the scope for identifiers v.s. indexes throughout the code,
#     especially before providing a remove feature which reorders indexes

import sys
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
        if QApplication.style().name() == "Macintosh (Aqua)" and \
           sys.platform == 'darwin':
            self.rowoverlap = 3
            self.cropheight = -1
        else:
            self.rowoverlap = 3
            self.cropheight = 2
        self.tabrows = []
        self.currows = []

    def insertTab(self, index = -1, row = 0):
        newindex = QTabBar.insertTab(self, index)
        while row >= len(self.tabrows):
            self.currows.insert(0, len(self.tabrows) - 1)
            self.tabrows.append([])
        self.tabrows[row].append(newindex)

    def setCurrentTab(self, tab):
        if self.count() == 0:
            return
        if isinstance(tab, int):
            tab = self.tab(tab)
        if tab == self.currentTab():
            return;
        index = self.indexOf(tab.identifier())
        if index in self.tabrows[self.currows[-1]]:
            QTabBar.setCurrentTab(self, tab)
        else:
            for row in range(0, len(self.tabrows)):
                if index in self.tabrows[self.currows[row]]:
                    saverow = self.currows[row]
                    self.currows[row] = self.currows[-1]
                    self.currows[-1] = saverow
                    QTabBar.setCurrentTab(self, tab)
                    self.layoutTabs()
                    self.repaint()
                    break

    def paintEvent(self, e):
        if e.rect().isNull():
	    return
        ct = self.tabAt(self.currentTab())
        painter = QPainter()
        painter.begin(self)
        cliprect = e.rect()
        if not e.erased():
             # self.erase(cliprect)
             painter.fillRect(cliprect, self.backgroundBrush())
        for row in range(0, len(self.tabrows)):
            telts = range(0, len(self.tabrows[self.currows[row]]))
            ft = self.tabAt(self.tabrows[self.currows[row]][0])
            lt = self.tabAt(self.tabrows[self.currows[row]][-1])
            rowrect = QRect(ft.rect().topLeft(), lt.rect().bottomRight())
            rowrect.setRight(self.rect().right())
            if not cliprect.intersects(rowrect):
                continue
            if self.cropheight > -1:
                if row < len(self.tabrows) - 1:
                    rowrect.setHeight(rowrect.height() - self.cropheight)
                rowrect = cliprect.intersect(rowrect)
                painter.setClipRect(rowrect, QPainter.CoordPainter)
            for telt in telts:
                t = self.tabAt(self.tabrows[self.currows[row]][telt])
                if t == ct: 
                    continue
                if t.rect().intersects(rowrect):
                    self.paint(painter, t, 0);
        if ct.rect().intersects(cliprect):
            self.paint(painter, ct, 1);
        if self.cropheight > -1:
            painter.setClipRect(cliprect, QPainter.CoordPainter)
        rowrect = QRect(lt.rect().right() + 1, lt.rect().bottom() - 1, 
                        self.rect().width() - lt.rect().right() - 1, 2)
        if rowrect.intersects(cliprect):
            rowrect.setHeight(1)
            painter.fillRect(rowrect, QBrush(self.colorGroup().light()));
            rowrect.moveTop(rowrect.top() + 1)
            painter.fillRect(rowrect, QBrush(self.colorGroup().midlight()));
        
        # rowrect = QRect(lt.rect().right() + 1, 0, 
        #               self.rect().width() - lt.rect().right() - 1,
        #               self.rect().height())
        # if rowrect.intersects(cliprect):
        #     flags = QStyle.Style_Default
        #     if self.shape() == QTabBar.RoundedAbove or \
        #        self.shape() == QTabBar.TriangularAbove:
        #         flags |= QStyle.Style_Top;
        #     elif self.shape() == QTabBar.RoundedBelow or \
        #          self.shape() == QTabBar.TriangularBelow:
        #         flags |= QStyle.Style_Bottom
        #     if self.isEnabled():
        #         flags |= QStyle.Style_Enabled
        #     sys.stdout.write("(%d, %d, %d, %d)\n" % (
        #                      rowrect.left(), rowrect.top(), 
        #                      rowrect.width(), rowrect.height()))
        #     self.style().drawPrimitive(QStyle.PE_TabBarBase, painter, 
        #                                rowrect, self.colorGroup(), flags)
        painter.end()

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
                t = self.tabAt(self.tabrows[self.currows[row]][telt])
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
            addx = maxx - self.tabAt(self.tabrows[self.currows[row]][-1]).rect().right()
            adjx = 0
            if addx <= 0: telts = []
            while len(telts) > 0:
                fixx = ((addx + len(telts) - 1) / len(telts))
                t = self.tabAt(self.tabrows[self.currows[row]][telts[0]])
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
                t = self.tabAt(self.tabrows[self.currows[row]][telt])
                t.rect().moveBy( offset, 0 )

        if self.sizeHint() != oldSh:
            self.updateGeometry()

        self.emit(PYSIGNAL("sigLayoutChanged"),(self,))

