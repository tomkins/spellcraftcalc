# CraftBar.py: Dark Age of Camelot Spellcrafting Calculator 
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
from B_CraftBar import *
from constants import *
import os
import os.path
import glob
import re
import dempak
import string
import SC
import ConfigParser

servercodes = {
    '100' : 'Bors', '85' : 'Bedevere',
    '55' : 'Galahad', '135' : 'Gaheris',
    '105' : 'Iseult', '130' : 'Igraine',
    '60' : 'Lancelot', '120' : 'Kay',
    '95' : 'Gawaine', '155' : 'Mordred',
    '115' : 'Nimue', '50' : 'Pendragon',
    '70' : 'Palomides', '65' : 'Percival',
    '110' : 'Pellinor', '90' : 'Morgan Le Fey',
    '75' : 'Merlin', '80' : 'Gwenivere',
    '150' : 'Pendragon',
    '125' : 'Tristan',
    '33' : 'Excalibur', '177' : 'Prydwen',
    '45' : 'Avalon', '11' : 'Lyonesse',
    '14' : 'Stonehenge', '134' : 'Logres',
    '153' : 'Dartmoor', '147' : 'Camlann',
    '34' : 'Broceliande', '12' : 'Ys',
    '139' : 'Orcanie', '171' : 'Carnac',
    '148' : 'Gorr'}

euroservers = ['Excalibur', 'Prydwen',
     'Avalon',  'Lyonesse',
     'Stonehenge',  'Logres',
     'Dartmoor',  'Camlann',
     'Broceliande',  'Ys',
     'Orcanie',  'Carnac',
     'Gorr']

class CharItem(QListViewItem):
    def __init__(self, parent = None, charname = '', server = '', filename = ''):
        QListViewItem.__init__(self, parent, charname, server)
        self.charname = charname
        self.server = server
        self.filename = filename

class CraftBar(B_CraftBar):
    def __init__(self,path = '', parent = None,name = None,modal = 0,fl = 0):
        B_CraftBar.__init__(self, parent, name, modal, fl)
        self.scwin = parent
        self.gemcount = 0
        self.piecelist = { }
        self.HotbarNum.setValue(1)
        self.HotbarPos.setValue(1)
        self.CharList.setAllColumnsShowFocus(1)
        self.DaocPath.setText(path)
        self.computeGemCount()
        self.computeBarEnd()
        self.mythicdir = path

    def loadGems(self):
        slotcounter = (self.HotbarNum.value() - 1) * 10 + self.HotbarPos.value() - 1
        char = self.CharList.selectedItem()
        if char is None: return
        self.LoadGemsButton.setEnabled(0)
        self.LoadGemsButton.repaint(self.LoadGemsButton.visibleRect())
        filename = char.filename
        server = char.server
        f = open(filename, 'r')
        g = open(re.sub(r'(\w+)-(\d+)\.ini$', r'\1_bak-\2.ini', filename), 'w')
        g.write(f.read())
        f.close()
        g.close()
        CP = ConfigParser.SafeConfigParser()
        CP.read([filename])
        try:
            mpak = dempak.MPAKFile(str(self.DaocPath.text())+'/data/ifd.mpk')
        except:
            QMessageBox.critical(None, 'Error!', 
                'Error opening data Daoc file. Check your Daoc path.', 'OK')
            self.LoadGemsButton.setEnabled(1)
            self.LoadGemsButton.repaint(self.LoadGemsButton.visibleRect())
            return

        for e in mpak.entries:
            mpaklist = mpak.open(e).readlines()
        mpak.close()
        itemlist = {}
        for line in mpaklist:
            try:
                n, key, num, realm, p, q, lvl, name, rest = string.split(line, ',', 8)
                itemlist[name+str(realm)] = [key, num, realm]
            except: pass
        
        for loc in TabList:
            item = self.piecelist.get(loc, None)
            if item is None: continue
            if item.getAttr('ActiveState') == 'player':
                for slot in range(0, 4):
                    if item.getSlotAttr('player', slot, 'Type') != 'Unused':
                        gemlvl, gemname = string.split(SC.getGemName(item, slot), ' ', 1)
                        for name in itemlist.keys():
                            m = re.compile(re.escape(gemname), re.IGNORECASE).search(name)
                            if m is not None:
                                if self.scwin.realm == 'Albion' and name[-1] != '1': continue
                                if self.scwin.realm == 'Hibernia' and name[-1] != '3': continue
                                if self.scwin.realm == 'Midgard' and name[-1] != '2': continue
                                vals = itemlist[name]   
                                #if server in euroservers:
                                #    buttonstr = '45,%s%02d%02d' % (vals[0], (int(vals[1]) - 1), GemNames.index(gemlvl))
                                #else:
                                buttonstr = '45,%s%03d%02d' % (vals[0], (int(vals[1]) - 1) * 2, GemNames.index(gemlvl))
                                CP.set('Quickbar', 'Hotkey_%d' % slotcounter, buttonstr)
                                slotcounter += 1
        f = open(filename, 'w')
        CP.write(f)
        f.close()
        self.LoadGemsButton.setEnabled(1)
        self.LoadGemsButton.repaint(self.LoadGemsButton.visibleRect())

    def findPath(self,a0):
        if os.path.isdir(str(a0)):
            self.mythicdir = str(a0)
            self.CharList.clear()
            filelist = glob.glob(str(a0)+'/*-*.ini')
            for file in filelist: 
                m = re.compile("(\w+)-(\d+)\.ini$").search(file)
                if m is not None:
                    server = servercodes[m.group(2)]
                    self.CharList.insertItem(CharItem(self.CharList, m.group(1),
                        server, file))
            self.CharList.setColumnWidthMode(0, QListView.Maximum)
            self.CharList.setColumnWidthMode(1, QListView.Maximum)

    def openFileDialog(self):
        daocdir = QFileDialog.getExistingDirectory(None, self, '', 'Select DAoC Directory')
        self.DaocPath.setText(daocdir)

    def computeBarEnd(self):
        eb = int((self.HotbarNum.value() * 10 + self.HotbarPos.value() + self.gemcount - 1) / 10)
        ep = int((self.HotbarNum.value() * 10 + self.HotbarPos.value() + self.gemcount - 1) % 10)
        if ep == 0: 
            ep = 10
            eb -= 1
        if eb > 10 or self.gemcount == 0:
            self.LoadGemsButton.setEnabled(0)
            self.EndBar.setText('-')
            self.EndPos.setText('-')
        else:
            self.LoadGemsButton.setEnabled(1)
            self.EndBar.setText(str(eb))
            self.EndPos.setText(str(ep))

    def hotbarNumChanged(self,a0):
        self.computeBarEnd()

    def hotbarPosChanged(self,a0):
        self.computeBarEnd()

    def computeGemCount(self):
        self.gemcount = 0
        for loc, item in self.piecelist.items():
            if item.getAttr('ActiveState') == 'player':
                for slot in range(0, 4):
                    if item.getSlotAttr('player', slot, 'Type') != 'Unused':
                        self.gemcount += 1
        self.NumGems.setText(str(self.gemcount))

    def PieceBoxChanged(self):
        self.piecelist = {}
        if self.ChestSelect.isChecked():
            self.piecelist['Chest'] = self.scwin.itemattrlist['Chest']
        if self.ArmsSelect.isChecked():
            self.piecelist['Arms'] = self.scwin.itemattrlist['Arms']
        if self.HeadSelect.isChecked():
            self.piecelist['Head'] = self.scwin.itemattrlist['Head']
        if self.LegsSelect.isChecked():
            self.piecelist['Legs'] = self.scwin.itemattrlist['Legs']
        if self.FeetSelect.isChecked():
            self.piecelist['Feet'] = self.scwin.itemattrlist['Feet']
        if self.HandsSelect.isChecked():
            self.piecelist['Hands'] = self.scwin.itemattrlist['Hands']
        if self.RHSelect.isChecked():
            self.piecelist['Right Hand'] = self.scwin.itemattrlist['Right Hand']
        if self.LHSelect.isChecked():
            self.piecelist['Left Hand'] = self.scwin.itemattrlist['Left Hand']
        if self.THSelect.isChecked():
            self.piecelist['2 Handed'] = self.scwin.itemattrlist['2 Handed']
        if self.RangedSelect.isChecked():
            self.piecelist['Ranged'] = self.scwin.itemattrlist['Ranged']
        self.computeGemCount()
        self.computeBarEnd()
