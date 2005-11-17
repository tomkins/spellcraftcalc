# DisplayWindow.py: Dark Age of Camelot Spellcrafting Calculator 
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
from B_DisplayWindow import *
from constants import *
import string

class DisplayWindow(B_DisplayWindow):
	def __init__(self,parent = None,name = None,modal = 0,fl = 0):
		B_DisplayWindow.__init__(self,parent,name,modal,fl)
                #self.font().setPointSize(8)
		self.scwindow = parent

	def loadLocations(self, locs):
		strlist = map(lambda(x): '%s: %s' % (x[0], x[1]), locs)
		self.DisplayText.clear()
		self.DisplayText.insertStrList(strlist)

	def CloseWindow(self):
		self.done(1)

	def LocationClicked(self,a0):
		if a0 is None: return
		tabname, rest = string.split(str(a0.text()), ':', 1)
		tabindex = TabList.index(tabname)
		self.scwindow.PieceTab.setCurrentTab(tabindex)
		self.done(1)
