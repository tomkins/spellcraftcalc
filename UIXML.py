#!/usr/bin/env python
# UIXML.py: Dark Age of Camelot Spellcrafting Calculator
# See http://kscraft.sourceforge.net/ for updates

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
import sys
import re
import os.path
import string

import ReportWindow
import ReportParser

def uixml(scwin):
    pwd = os.path.dirname(os.path.abspath(sys.argv[0]))
    path = os.path.join(pwd, 'Reports')
    srcpath = os.path.join(path, 'windowgen.xml')

    filename = QFileDialog.getOpenFileName(srcpath, "Reports (*.xml)")
    if str(filename) == '':
        return
    filename = str(filename)
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
    savepath = os.path.join(path, 'custom1.xml')
    filename = QFileDialog.getSaveFileName(path, "WindowXML (*.xml)")
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

