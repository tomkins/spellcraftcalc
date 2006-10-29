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
import traceback
from MyStringIO import UnicodeStringIO
import XMLHelper

from Ft.Xml.Xslt import Processor
from Ft.Xml.InputSource import DefaultFactory
from Ft.Lib.Uri import OsPathToUri

def uixml(scwin, uixslt):
    extidx = uixslt.rindex('.')
    xslt2 = uixslt[:extidx] + "Post" + uixslt[extidx:]
    if not os.path.exists(xslt2):
        xslt2 = os.path.combine(os.path.abspath(os.path.dirname(sys.argv[0])),
            'reports', 'DefaultUiXmlWindowPost.xsl')
    sctemplate = XMLHelper.writexml(scwin.asXML(True), UnicodeStringIO(), '', '\t', '\n')

    try:
        source = DefaultFactory.fromString(sctemplate, "urn:pass1")
        xsltUri = OsPathToUri(uixslt)
        transform = DefaultFactory.fromUri(xsltUri)

        processor = Processor.Processor()
        processor.appendStylesheet(transform)
        uixmlstr = processor.run(source)

        if os.path.exists(xslt2):
            source = DefaultFactory.fromString(uixmlstr, "urn:pass2")
            xsltUri = OsPathToUri(xslt2)
            transform = DefaultFactory.fromUri(xsltUri)

            processor = Processor.Processor()
            processor.appendStylesheet(transform)
            uixmlstr = processor.run(source)
    except Exception, e:
        QMessageBox.critical(None, 'Error!', 
            'Error with XSLT transform!\n\n'+str(e), 'OK')
        return
        
    path = os.path.join(scwin.ReportPath, 'custom1_window.xml')
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

