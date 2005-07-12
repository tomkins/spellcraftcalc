# MouseLabel.py: Dark Age of Camelot Spellcrafting Calculator
# See http://www.ugcs.caltech.edu/~jlamanna/daoc/sccalc/index.html for updates

# Copyright (C) 2003,  James Lamanna (jlamanna@ugcs.caltech.edu)

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

from qt import *
from constants import *
import DisplayWindow
import ReportWindow
import SC

class MouseLabel(QLabel):
    def __init__(self, effect, scwin, text='', parent=None, name='', f=0):
        QLabel.__init__(self, text, parent, name, f)
        self.effect = effect
        self.locs = []
        self.parent = scwin
    
    def mousePressEvent(self, e):
        if self.effect == '': return
        if e is None: return
        self.locs = []
        for key, item in self.parent.itemattrlist.items():
            activestate = item.getAttr('ActiveState')
            if activestate == 'drop':
                toprng = 10
            else:
                toprng = 4
            for slot in range(0, toprng):
                type = item.getSlotAttr(activestate, slot, 'Type')
                effect = item.getSlotAttr(activestate, slot, 'Effect')
                amount = item.getSlotAttr(activestate, slot, 'Amount')
                if self.effect == effect and type != 'Cap Increase'\
                        and type != 'Unused':
                    self.locs.append([key, amount])
                elif effect in AllBonusList[self.parent.realm][self.parent.charclass].keys():
                    if self.effect in AllBonusList[self.parent.realm][self.parent.charclass][effect]:
                        self.locs.append([key, amount])
        DW = DisplayWindow.DisplayWindow(self.parent, '', 1)
        DW.setCaption('Slots With %s' % self.effect)
        DW.loadLocations(self.locs)
        DW.exec_loop()

class GemLabel(QLabel):
    def __init__(self, item, slot, scwin, text='', parent=None, name='', f=0):
        QLabel.__init__(self, text, parent, name, f)
        self.item = item
        self.itemslot = slot
        self.parent = scwin
    
    def mousePressEvent(self, e):
        if self.item is None: return
        if e is None: return
        RW = ReportWindow.ReportWindow(self.parent, '', 1)
        RW.setCaption('Materials')
        mats = SC.getGemMaterials(self.item, self.itemslot, self.parent.realm)
        materialsstr = '<center><b>Materials List</b></center><dl>'
        for type, matlist in mats.items():
            materialsstr += '<dt><b>%s</b></dt>' % type
            for matl, val in matlist.items():
                materialsstr += '<dd>%d %s</dd>' % (val, matl)
        materialsstr += '</dl>'
        RW.ReportText.setText(materialsstr, "html")
        RW.exec_loop()
