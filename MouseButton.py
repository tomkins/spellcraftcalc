# MouseButton.py: Dark Age of Camelot Spellcrafting Calculator
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
class MouseButton(QPushButton):
	def __init__(self, scwin, text='', parent=None, name=''):
		QPushButton.__init__(self, text, parent, name)
		self.reportFile = ''
		self.parent = scwin

	def setReportFile(self, file):
		self.reportFile = file
                self.parent.reportFile = file
	
	def getReportFile(self):
		return self.reportFile
	
	def mousePressEvent(self, e):
		if e.button() == Qt.RightButton:
			popup = QPopupMenu(self)
			popup.insertItem('Assign...', self.chooseReportFile)
			popup.exec_loop(e.globalPos())
		else:
			QPushButton.mousePressEvent(self, e)
			#self.emit(SIGNAL("clicked()"),())
	
	def chooseReportFile(self):
		filename = QFileDialog.getOpenFileName('./reports', "Reports (*.xml *.rpt)")
		if filename is not None and str(filename) != '':
			self.reportFile = str(filename)
                        self.parent.reportFile = str(filename)

