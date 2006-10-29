# UIXML.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtGui import *
import sys
import re
import os.path
import string
from MyStringIO import UnicodeStringIO
import XMLHelper

from Ft.Xml.Xslt import Processor
from Ft.Xml import InputSource
from Ft.Lib.Uri import OsPathToUri

def uixml(scwin, uixslt):
    extidx = uixslt.rindex('.')
    xslt2 = uixslt[:extidx] + "Post" + uixslt[extidx:]

    try:
        sctemplate = XMLHelper.writexml(scwin.asXML(True), UnicodeStringIO(), '', '\t', '\n')
        source = InputSource.DefaultFactory.fromString(sctemplate)
        xsltUri = OsPathToUri(uixslt)
        transform = InputSource.DefaultFactory.fromUri(xsltUri)

        processor = Processor.Processor()
        processor.appendStylesheet(transform)
        uixmlstr = processor.run(source)

        if os.path.exists(xslt2):
            source = InputSource.DefaultFactory.fromString(uixmlstr)
            xsltUri = OsPathToUri(xslt2)
            transform = InputSource.DefaultFactory.fromUri(xsltUri)

            processor = Processor.Processor()
            processor.appendStylesheet(posttransform)
            uixmlstr = processor.run(source)
    except:
        QMessageBox.critical(None, 'Error!', 
            'Error with XSLT transform!', 'OK')
        return
        
    path = os.path.join(self.parent.ReportPath, 'custom1_window.xml')
    filename = QFileDialog.getSaveFileName(scwin, "Save UI Window as",
                   path, "UI Window XML (*_window.xml);;All Files (*.*)")
    if str(filename) == '':
        return
    try:
        f = open(str(filename), 'w')
        f.write(uixmlstr)
        f.close()
    except IOError:
        QMessageBox.critical(None, 'Error!', 
            'Error opening file: ' + filename, 'OK')
        return

