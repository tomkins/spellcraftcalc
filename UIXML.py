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

def uixml(scwin):
    srcpath = os.path.join(scwin.ReportPath, 'windowgen.xsl')
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    xslt2 = os.path.join(path, 'reports', 'windowgen-post.xsl')

    uixslt = QFileDialog.getOpenFileName(scwin, "Choose a UI XSLT",
        srcpath, "UI XSLT (*.xsl);;All Files (*.*)")
    if str(uixslt) == '':
        return
    uixslt = str(uixslt)
    
    try:
        processor = Processor.Processor()
        source = InputSource.DefaultFactory.fromString(
            XMLHelper.writexml(scwin.asXML(True), UnicodeStringIO(), '', '\t', '\n'))

        xsltUri = OsPathToUri(uixslt)
        transform = InputSource.DefaultFactory.fromUri(xsltUri)

        xslt2Uri = OsPathToUri(xslt2)
        posttransform = InputSource.DefaultFactory.fromUri(xslt2Uri)

        processor.appendStylesheet(transform)
        step1 = processor.run(source)

        print step1

        processor = Processor.Processor()
        processor.appendStylesheet(posttransform)
        uixmlstr = processor.run(InputSource.DefaultFactory.fromString(step1))
    except:
        QMessageBox.critical(None, 'Error!', 
            'Error with XSLT transform!', 'OK')
        return
        

    """
    try:
        f = open(str(filename), 'r')
        uixmlin = f.read()
        f.close()
    except IOError:
        QMessageBox.critical(None, 'Error!', 
            'Error opening file: ' + filename, 'OK')
        return
    
    info = ReportWindow.ReportWindow(scwin).collectStats(scwin.itemattrlist)
    rp = ReportParser.ReportParser()
    uixmlheader_m = re.search('(.*)<windowgen>', uixmlin, re.DOTALL)
    uixmlheader = ''
    uixmlfooter = ''
    if uixmlheader_m is not None:
        uixmlheader = uixmlheader_m.group(1)
    uixmlfooter_m = re.search('</windowgen>(.*)', uixmlin, re.DOTALL)
    if uixmlfooter_m is not None:
        uixmlfooter = uixmlfooter_m.group(1)
    uixmlreport_m = re.search('<windowgen>(.*)</windowgen>', uixmlin, re.DOTALL)
    if uixmlreport_m is None:
        QMessageBox.critical(None, 'Error!', 
            'No report to parse!', 'OK')
        return
    uixmlreport = rp.parse(uixmlreport_m.group(1), info)
    uixmlreport = re.sub('<br>', '\n<br>\n', uixmlreport)
    # Wrap each line of uixmlreport in a labeldef
    reportlines = string.split(uixmlreport, '\n')
    labeledreportlines = []
    y = 5
    labeledstr = ''
    for line in reportlines:
        labeldeftemplate = '''
<LabelDef>
    <Color>
            <R>255</R>
            <G>255</G>
            <B>255</B>
            <A>255</A>
    </Color>
    <FontName>arial9</FontName>
    <Width>%d</Width>
    <Height>16</Height>
    <MaxCharacters>%d</MaxCharacters>
    <Position>
            <X>%d</X>
            <Y>%d</Y>
    </Position>
    <Data>%s</Data>
</LabelDef>
'''
        addcr = False
        if len(line) > 0 and not (len(line) == 1 and len[-1] == '\r'):
            if line[-1] == '\r':
                line = line[:-1]
                addcr = True
            if line != '<br>':
                x = 5
                columns = re.findall('<td (\d+)>([^<]*)', line)
                if len(columns) > 0:
                    for (width, text) in columns:
                        width = int(width)
                        labeledstr += labeldeftemplate % (width, len(text)+1, x, y, text)
                        x += width
                else:
                    width = len(line) * 15
                    labeledstr += labeldeftemplate % (width, len(line)+1, x, y, line)
                    x += width
                if addcr:
                    labeledstr += '\r'
                labeledstr += '\n'
            y += 17
    uixmlstr = uixmlheader + labeledstr + uixmlfooter
    """
    savepath = os.path.join(path, 'custom1.xml')
    filename = QFileDialog.getSaveFileName(scwin, "Save UI XML As:",
        savepath, "WindowXML (*.xml);;All Files (*.*)")
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

