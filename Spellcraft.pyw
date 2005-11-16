#!/usr/local/bin/pythonw
# ScWindow.py: Dark Age of Camelot Spellcrafting Calculator (main Window)
# See http://sc.aod.net for updates

# Copyright (C) 2003, 2004  James Lamanna (jlamanna@ugcs.caltech.edu)

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

import psyco

if __name__ == '__main__':
    psyco.full()

import os
import sys
import locale
from qt import *

QApplication.setDesktopSettingsAware(0)
locale.setlocale(locale.LC_ALL, '')

class ScApplication(QApplication):
    def __init__(self):
        args = sys.argv
        if not os.path.isabs(args[0]):
             args[0] = os.path.abspath(args[0])

        QApplication.__init__(self, args)
        # QObject.connect(self, SIGNAL('lastWindowClosed()'), 
        #                 self, SLOT('quit()'))

    def start(self):
        splash = QSplashScreen(QPixmap("Spellcraft.png"));
        splash.show()

        font = QFont(self.font())
        if QApplication.style().name()[0:9] == "Macintosh" and \
           sys.platform == "darwin":
            font.setFamily("Lucida Grande")
            font.setPointSize(11)
        elif sys.platform == "win32":
            font.setFamily("Trebuchet MS")
            font.setPointSize(8)
        self.setFont(font)

        import ScWindow
        scw = ScWindow.ScWindow()
        app.setMainWidget(scw)
        scw.setCaption("Kort's Spellcrafting Calculator")
        scw.setIcon(QPixmap("ScWindow.png"));
        scw.show()

        splash.finish(scw);

    def polish(self, widget):
        # Fix Mac bits of uglyness, not all of which can be fixed.
        QApplication.polish(self, widget)
        if self.style().name()[0:9] != "Macintosh": return
        if sys.platform != "darwin": return
        if widget.className() == 'QGroupBox':
            crect = widget.geometry()
            crect.setHeight(crect.height() + 3)
            widget.setGeometry(crect)
        if widget.className() == 'QPushButton':
            crect = widget.geometry()
            crect.moveBy(-3, -3)
            crect.setHeight(crect.height() + 6)
            crect.setWidth(crect.width() + 6)
            widget.setGeometry(crect)

if __name__ == '__main__':
    app=ScApplication()
    app.start()
    sys.exit(app.exec_loop())

