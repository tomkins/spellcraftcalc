# CraftBar.py: Dark Age of Camelot Spellcrafting Calculator 
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qt3Support import *
from B_CraftBar import *
from Character import *
from constants import *
import os
import os.path
import glob
import re
import string
import SC
import ConfigParser
import sys

class CharItem(Q3ListViewItem):
    def __init__(self, parent = None, charname = '', server = '', filename = ''):
        Q3ListViewItem.__init__(self, parent, charname, server)
        self.charname = charname
        self.server = server
        self.filename = filename

class CraftBar(QDialog, Ui_B_CraftBar):
    def __init__(self,path = '',parent = None,name = None,modal = False,fl = Qt.Widget):
        QDialog.__init__(self, parent, fl)
        Ui_B_CraftBar.setupUi(self,self)
        self.CharList.addColumn("Server")
        self.CharList.addColumn("Char Name")
        if (name):
            self.setObjectName(name)
        if (modal):
            self.setModal(modal)

        self.connect(self.PathSelectButton,SIGNAL("clicked()"),self.openFileDialog)
        self.connect(self.PushButton19,SIGNAL("clicked()"),self.accept)
        self.connect(self.LoadGemsButton,SIGNAL("clicked()"),self.loadGems)
        self.connect(self.DaocPath,SIGNAL("textChanged(const QString&)"),self.findPath)
        self.connect(self.HotbarNum,SIGNAL("valueChanged(int)"),self.hotbarNumChanged)
        self.connect(self.HotbarPos,SIGNAL("valueChanged(int)"),self.hotbarPosChanged)
        self.connect(self.ChestSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.ArmsSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.HeadSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.LegsSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.HandsSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.FeetSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.RangedSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.RHSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.LHSelect,SIGNAL("clicked()"),self.PieceBoxChanged)
        self.connect(self.THSelect,SIGNAL("clicked()"),self.PieceBoxChanged)

        self.scwin = parent
        self.gemcount = 0
        self.piecelist = { }
        self.HotbarNum.setValue(1)
        self.HotbarPos.setValue(1)
        #self.CharList.setAllColumnsShowFocus(1)
        self.DaocPath.setText(path)
        self.computeGemCount()
        self.computeBarEnd()
        self.mythicdir = path

    def loadGems(self):
        char = self.CharList.selectedItem()
        if char is None: return
        self.LoadGemsButton.setEnabled(0)
        self.LoadGemsButton.repaint(self.LoadGemsButton.visibleRect())
        filename = char.filename
        server = char.server
        f = open(filename, 'r')
        g = open(re.sub(r'(\w+)-(\d+)\.ini$', r'\1-\2.ini.bak', filename), 'w')
        g.write(f.read())
        f.close()
        g.close()
        CP = ConfigParser.SafeConfigParser()
        CP.read([filename])
        buttons = [-1, -1, -1]
        newbuttons = []
        slotcounter = 0
        while slotcounter <= 99:
            try:
                buttonstr=CP.get('Macros', 'Macro_%d' % slotcounter)
            except:
                if len(newbuttons) < 3:
                    newbuttons.append(slotcounter)
            else:
                buttonval = string.split(buttonstr, ',', 1)
                if len(buttonval) > 1 and buttonval[1][:7].lower() == '/craft ':
                    if buttonval[1][7].lower() in "ahm":
                        buttons['ahm'.index(buttonval[1][7].lower())] = slotcounter
            slotcounter += 1
        for i in (0, 1, 2):
            if buttons[i] < 0 and len(newbuttons) > 0:
                buttons[i] = newbuttons.pop(0)
                CP.set('Macros', 'Macro_%d' % buttons[i],
                       "%s,/craft %s" % (Realms[i][0:3], Realms[i]))
        
        realm = self.scwin.realm
        slotcounter = (self.HotbarNum.value() - 1) * 10 + self.HotbarPos.value() - 1
        for loc in TabList:
            item = self.piecelist.get(loc, None)
            if item is None: continue
            if item.getAttr('ActiveState') == 'player':
                for slot in range(0, 4):
                    if item.getSlotAttr('player', slot, 'Type') != 'Unused':
                        gemlvl, gemname = string.split(SC.getGemName(item, slot), ' ', 1)
                        if slotcounter >= 300:
                            sys.stdout.write("Out of slots!\n")
                            continue
                        if not HotkeyGems[realm].has_key(gemname):
                            for i in (0, 1, 2):
                                if realm == Realms[i]:
                                    continue
                                if HotkeyGems[Realms[i]].has_key(gemname):
                                    realm = Realms[i]
                                    buttonstr = 'Hotkey_%d' % buttons[i]
                                    if slotcounter >= 200:
                                        CP.set('Quickbar3', 'Hotkey_%d' % slotcounter - 200, buttonstr)
                                    elif slotcounter >= 100:
                                        CP.set('Quickbar2', 'Hotkey_%d' % slotcounter - 100, buttonstr)
                                    else:
                                        CP.set('Quickbar', 'Hotkey_%d' % slotcounter, buttonstr)
                                    slotcounter += 1
                                    break
                        if HotkeyGems[realm].has_key(gemname):
                            val = HotkeyGems[realm][gemname]
                            buttonstr = '45,13%03d%02d' % (val, GemNames.index(gemlvl))
                            if slotcounter >= 200: 
                                CP.set('Quickbar3', 'Hotkey_%d' % (slotcounter - 200), buttonstr)
                            elif slotcounter >= 100:
                                CP.set('Quickbar2', 'Hotkey_%d' % (slotcounter - 100), buttonstr)
                            else:
                                CP.set('Quickbar', 'Hotkey_%d' % slotcounter, buttonstr)
                            slotcounter += 1
                        else:
                            sys.stdout.write(realm + " has no '" + gemname + "' gem\n")
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
                    server = ServerCodes[m.group(2)]
                    self.CharList.insertItem(CharItem(self.CharList, m.group(1),
                        server, file))
            self.CharList.setColumnWidthMode(0, Q3ListView.Maximum)
            self.CharList.setColumnWidthMode(1, Q3ListView.Maximum)

    def openFileDialog(self):
        daocdir = QFileDialog.getExistingDirectory(self, 'Select DAoC Directory', self.DaocPath.text())
        if (daocdir):
            self.DaocPath.setText(daocdir)

    def computeBarEnd(self):
        eb = int((self.HotbarNum.value() * 10 + self.HotbarPos.value() + self.gemcount - 1) / 10)
        ep = int((self.HotbarNum.value() * 10 + self.HotbarPos.value() + self.gemcount - 1) % 10)
        if ep == 0: 
            ep = 10
            eb -= 1
        if eb > 30 or self.gemcount == 0:
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
