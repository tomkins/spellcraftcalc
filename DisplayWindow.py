# DisplayWindow.py: Dark Age of Camelot Spellcrafting Calculator 
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtGui import *
from B_DisplayWindow import *
from constants import *
import string

class DisplayWindow(QWidget, Ui_B_DisplayWindow):
	def __init__(self,parent = None,name = None,modal = 0,fl = 0):
                QWidget.__init__(self,parent,name,modal,fl)
                Ui_B_DisplayWindow.setupUi(self,self)
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
