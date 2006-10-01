# CraftBar.py: Dark Age of Camelot Spellcrafting Calculator 
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtCore import *
from PyQt4.QtGui import *
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

class CraftBar(QDialog, Ui_B_CraftBar):
    def __init__(self,parent = None,name = None,modal = False,fl = Qt.Widget):
        QDialog.__init__(self, parent, fl)
        Ui_B_CraftBar.setupUi(self,self)

        self.model = QStandardItemModel(0, 3)
        self.model.setHeaderData(0, Qt.Horizontal, QVariant('Server'), Qt.DisplayRole)
        self.model.setHeaderData(1, Qt.Horizontal, QVariant('Char Name'), Qt.DisplayRole)
        self.CharList.setModel(self.model)
        self.CharList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.CharList.setShowGrid(False)
        self.CharList.verticalHeader().hide()
        self.CharList.horizontalHeader().setResizeMode(QHeaderView.Stretch)
        self.CharList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.CharList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.CharList.setColumnHidden(2, True)

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

        self.parent = parent
        self.gemcount = 0
        self.piecelist = { }
        self.HotbarNum.setValue(1)
        self.HotbarPos.setValue(1)
        self.DaocPath.setText(self.parent.DaocPath)
        self.computeGemCount()
        self.computeBarEnd()

    def loadGems(self):
        indexList = self.CharList.selectedIndexes()
        if len(indexList) == 0: return
        for idx in indexList:
            if idx.column() == 0: server = str(idx.data().toString())

        # file column is hidden so we have to fetch it
        row = indexList[0].row()
        fileIndex = self.model.index(row, 2)
        filename = str(self.model.data(fileIndex).toString())
        
        self.LoadGemsButton.setEnabled(0)
        self.LoadGemsButton.update()

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
        
        realm = self.parent.realm
        slotcounter = (self.HotbarNum.value() - 1) * 10 + self.HotbarPos.value() - 1
        for loc in TabList:
            item = self.piecelist.get(loc, None)
            if item is None: continue
            if item.getAttr('ActiveState') == 'player':
                for slot in range(0, 4):
                    if item.slot(slot).crafted():
                        gemname = item.slot(slot).gemName()
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
                            buttonstr = '45,13%03d%02d' % (val, item.slot(slot).gemLevel() - 1)
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
        a0 = unicode(a0)
        if os.path.isdir(a0):
            self.model.removeRows(0, self.model.rowCount())
            filelist = glob.glob(a0+'/*-*.ini')
            for file in filelist:
                m = re.compile("(\w+)-(\d+)\.ini$").search(file)
                if m is not None:
                    server = ServerCodes[m.group(2)]
                    self.model.insertRows(self.model.rowCount(), 1)
                    index = self.model.index(self.model.rowCount()-1, 0, QModelIndex())
                    self.model.setData(index, QVariant(server), Qt.DisplayRole)
                    index = self.model.index(self.model.rowCount()-1, 1, QModelIndex())
                    self.model.setData(index, QVariant(m.group(1)), Qt.DisplayRole)
                    index = self.model.index(self.model.rowCount()-1, 2, QModelIndex())
                    self.model.setData(index, QVariant(file), Qt.DisplayRole)
            if len(filelist) > 0:
                self.parent.DaocPath = a0
        self.CharList.resizeRowsToContents()

    def openFileDialog(self):
        daocdir = QFileDialog.getExistingDirectory(self, 'Select DAoC Directory', self.DaocPath.text())
        if (daocdir):
            self.DaocPath.setText(os.path.abspath(daocdir))

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
                    if item.slot(slot).type() != 'Unused':
                        self.gemcount += 1
        self.NumGems.setText(str(self.gemcount))

    def PieceBoxChanged(self):
        self.piecelist = {}
        if self.ChestSelect.isChecked():
            self.piecelist['Chest'] = self.parent.itemattrlist['Chest']
        if self.ArmsSelect.isChecked():
            self.piecelist['Arms'] = self.parent.itemattrlist['Arms']
        if self.HeadSelect.isChecked():
            self.piecelist['Head'] = self.parent.itemattrlist['Head']
        if self.LegsSelect.isChecked():
            self.piecelist['Legs'] = self.parent.itemattrlist['Legs']
        if self.FeetSelect.isChecked():
            self.piecelist['Feet'] = self.parent.itemattrlist['Feet']
        if self.HandsSelect.isChecked():
            self.piecelist['Hands'] = self.parent.itemattrlist['Hands']
        if self.RHSelect.isChecked():
            self.piecelist['Right Hand'] = self.parent.itemattrlist['Right Hand']
        if self.LHSelect.isChecked():
            self.piecelist['Left Hand'] = self.parent.itemattrlist['Left Hand']
        if self.THSelect.isChecked():
            self.piecelist['2 Handed'] = self.parent.itemattrlist['2 Handed']
        if self.RangedSelect.isChecked():
            self.piecelist['Ranged'] = self.parent.itemattrlist['Ranged']
        self.computeGemCount()
        self.computeBarEnd()
