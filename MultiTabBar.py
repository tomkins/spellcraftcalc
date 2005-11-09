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
#   * New control fails to draw the horizontal-bottom continuation bar 
#     for > 1 rows.
#   * Initial selection is wrong, but it seems we need two arrays, one
#     for the original rows, one for the current row order.  Item 0 should
#     be on the row [-1]
#

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
        self.tabrows = []

    def insertTab(self, index = -1, row = 0):
        newindex = QTabBar.insertTab(self, index)
        while row >= len(self.tabrows):
            self.tabrows.append([])
        self.tabrows[row].append(newindex)

    def setCurrentTab(self, tab):
        if not tab or self.count() == 0:
            return
        if isinstance(tab, int):
            tab = self.tab(tab)
        if tab == self.currentTab():
            return;
        index = self.indexOf(tab.identifier())
        if index not in self.tabrows[-1]:
            for row in range(len(self.tabrows) - 2, -1, -1):
                if index in self.tabrows[row]:
                    saverow = self.tabrows[row]
                    self.tabrows[row] = self.tabrows[-1]
                    self.tabrows[-1] = saverow
                    self.layoutTabs()
                    self.repaint()
                    break
        QTabBar.setCurrentTab(self, tab)

    def newlayoutTabs(self):
        r = self.tabList()[0].rect()
        for t in self.tabList()[1:]:
	    r = r.unite(t.rect())
	oldSh = r.size()

        hframe  = self.style().pixelMetric(QStyle.PM_TabBarTabHSpace, self)
        vframe  = self.style().pixelMetric(QStyle.PM_TabBarTabVSpace, self)
        overlap = self.style().pixelMetric(QStyle.PM_TabBarTabOverlap, self)


        tabrect = self.PieceTab.tab(0).rect()
        taboverlap = tabrect.width() - self.PieceTab.tab(0).rect().left()
        tabrect.setWidth((self.PieceTab.rect().width() \
                        + taboverlap * (len(PieceTabList) - 1)) \
                       / len(PieceTabList))

        for tabid in range(0,len(PieceTabList)):
            self.PieceTab.tab(tabid).setRect(tabrect)
            tabrect.setLeft(tabrect.left() + taboverlap)

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
        ## if t and self.d.scrolls: t.r.x()
        lastrow = len(self.tabrows) - 1
        y = 0
        maxx = 0
        for row in range(0, lastrow + 1):
            if reverse:
                telts = range(len(self.tabrows[row]) - 1, -1, -1)
            else:
                telts = range(0, len(self.tabrows[row]))
            x = 0
            offset = 0
            for telt in telts:
                t = self.tabAt(self.tabrows[row][telt])
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
            y += h - 4
            maxx = max(maxx, x + overlap - 1)
        y += overlap;

        for row in range(0, lastrow + 1):
            if reverse:
                telts = range(len(self.tabrows[row]) - 1, -1, -1)
            else:
                telts = range(0, len(self.tabrows[row]))
            addx = maxx - self.tabAt(self.tabrows[row][-1]).rect().right()
            adjx = 0
            if addx <= 0: telts = []
            while len(telts) > 0:
                fixx = ((addx + len(telts) - 1) / len(telts))
                t = self.tabAt(self.tabrows[row][telts[0]])
                newrect = t.rect()
                newrect.moveLeft(newrect.left() + adjx)
                newrect.setWidth(newrect.width() + fixx)
                t.setRect(newrect)
                addx -= fixx
                adjx += fixx
                r = r.unite(t.rect())
                telts = telts[1:]

        ## if d.scrolls: w = d.leftB.x()
        ## else: 
        w = self.width()
        if maxx < w:
            offset = w - maxx
        if offset > 0:
            offset = 0

        for row in range(0, len(self.tabrows)):
            telts = range(0, len(self.tabrows[row]))
            for telt in telts:
                t = self.tabAt(self.tabrows[row][telt])
                t.rect().moveBy( offset, 0 )
#                sys.stdout.write(str(row) + ", " + str(telt) + ": " + str(self.tabrows[row][telt]) \
#                    + " (" + str(t.rect().top())    + ", " + str(t.rect().left()) \
#                    + "), (" + str(t.rect().bottom()) + ", " + str(t.rect().right()) + ")\r\n")

        if self.sizeHint() != oldSh:
            self.updateGeometry()

        sys.stdout.write("(" + str(self.rect().top())    + ", " + str(self.rect().left()) \
                    + "), (" + str(self.rect().bottom()) + ", " + str(self.rect().right()) + ")\r\n")

        self.emit(PYSIGNAL("sigLayoutChanged"),(self,))



