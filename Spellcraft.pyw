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
    locale.setlocale(locale.LC_ALL, '')

    args = sys.argv
    if not os.path.isabs(args[0]):
        args[0] = os.path.abspath(args[0])

    from qt import *
    app = QApplication(args)
    QObject.connect(app,SIGNAL('lastWindowClosed()'),app,SLOT('quit()'))
    if QApplication.style().name() == "Macintosh (Aqua)" and \
       sys.platform == "darwin":
        f = QFont(self.font())
        f.setPointSize(11)
        self.setFont(f)

    splash = QSplashScreen(QPixmap("Spellcraft.png"));
    splash.show()

    import ScWindow
    scw = ScWindow.SCApp()
    app.setMainWidget(scw)
    scw.setCaption("Kort's Spellcrafting Calculator")
    scw.setIcon(QPixmap("ScWindow.png"));
    scw.show()

    splash.finish(scw);
    del splash

    sys.exit(app.exec_loop())
