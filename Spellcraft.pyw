#!/usr/bin/pythonw
# CraftBar.py: Dark Age of Camelot Spellcrafting Calculator 
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

try:
    import psyco

    if __name__ == '__main__':
        psyco.full()
except:
    pass

import os
import sys
import locale
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#QApplication.setApplicationName("Kscalc")
if sys.platform == "darwin":
    QApplication.setDesktopSettingsAware(False)
else:
    QApplication.setDesktopSettingsAware(True)
locale.setlocale(locale.LC_ALL, '')

class ScApplication(QApplication):
    def __init__(self):
        args = sys.argv
        self.curPath = QDir.cleanPath(QDir.currentPath())
        if args[0]:
             args[0] = unicode(QDir(self.curPath).absoluteFilePath(args[0]))
        else:
             args[0] = unicode(QDir(self.curPath).absoluteFilePath(__file__, True))
        self.appPath = unicode(QDir.cleanPath(QDir(args[0]).absoluteFilePath("..")))

        self.splashFile = unicode(QDir(self.appPath).absoluteFilePath("Spellcraft.png"))
 
        if len(args) > 1:
           args[1] = unicode(QDir.cleanPath(QDir(self.curPath).absoluteFilePath(args[1], True)))

        QApplication.__init__(self, args)

    def start(self):
        splash = QSplashScreen(QPixmap(self.splashFile),
                               Qt.SplashScreen|Qt.MSWindowsFixedSizeDialogHint)
        splash.show()

        # Font sizes are strange things on Mac, while our favorite
        # medeval font, Trebuchet MS, can only be counted on for
        # Mac and Windows NT+ (on Windows 98 it just blows up)
        #
        font = QFont(self.font())
        if str(QApplication.style().objectName()[0:9]).lower() == "macintosh" and \
           sys.platform == "darwin":
            font.setFamily("Trebuchet MS")
            #font.setFamily("Lucida Grande")
            font.setPointSize(12)
            font.setWeight(QFont.Light)
        elif sys.platform == "win32":
            if sys.getwindowsversion()[0] < 4:
                font.setFamily("Arial")
            else:
                font.setFamily("Trebuchet MS")
            font.setPointSize(8)
        else:
            font.setFamily("Trebuchet MS")
            font.setPointSize(8)
        self.setFont(font)

        import ScWindow
        scw = ScWindow.ScWindow()
        scw.splashFile = self.splashFile
        app.setActiveWindow(scw)
        scw.setWindowIcon(QIcon(QPixmap("ScWindow.png")));
        if len(app.argv()) > 1:
            scw.openFile(app.argv()[1], True)
        scw.show()
        splash.finish(scw);


if __name__ == '__main__':
    app=ScApplication()
    app.start()
    sys.exit(app.exec_())

