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
from qt import *

QApplication.setDesktopSettingsAware(0)
locale.setlocale(locale.LC_ALL, '')

class ScApplication(QApplication):
    def __init__(self):
        args = sys.argv
        self.curPath = QDir.cleanDirPath(QDir.currentDirPath())
        if args[0]:
             args[0] = unicode(QDir(self.curPath).absFilePath(args[0], True))
        else:
             args[0] = unicode(QDir(self.curPath).absFilePath(__file__, True))
        self.appPath = unicode(QDir.cleanDirPath(QDir(args[0]).absFilePath("..")))

        self.splashFile = unicode(QDir(self.appPath).absFilePath("Spellcraft.png"))
 
        if len(args) > 1:
           args[1] = unicode(QDir.cleanDirPath(QDir(self.curPath).absFilePath(args[1], True)))

        QApplication.__init__(self, args)

    def start(self):
        splash = QSplashScreen(QPixmap(self.splashFile))
        splash.show()

        # Font sizes are strange things on Mac, while our favorite
        # medeval font, Trebuchet MS, can only be counted on for
        # Mac and Windows NT+ (on Windows 98 it just blows up)
        #
        font = QFont(self.font())
        if QApplication.style().name()[0:9] == "Macintosh" and \
           sys.platform == "darwin":
            font.setFamily("Trebuchet MS")
            #font.setFamily("Lucida Grande")
            font.setPointSize(11)
        elif sys.platform == "win32":
            if sys.getwindowsversion()[3] < 2:
                font.setFamily("Arial")
            else:
                font.setFamily("Trebuchet MS")
            font.setPointSize(8)
        self.setFont(font)

        import ScWindow
        scw = ScWindow.ScWindow()
        scw.splashFile = self.splashFile
        app.setMainWidget(scw)
        scw.setIcon(QPixmap("ScWindow.png"));
        if len(app.argv()) > 1:
            scw.openFile(app.argv()[1], True)
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

