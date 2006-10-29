# ReportWindow.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from B_ReportWindow import *
from Character import *
from constants import *
from htmlplus import *
from SC import *
from MyStringIO import UnicodeStringIO
import XMLHelper
import Item
import string
import re
import sys
import os.path

from Ft.Xml.Xslt import Processor
from Ft.Xml import InputSource
from Ft.Lib.Uri import OsPathToUri

#import libxsltmod

class ReportWindow(QDialog, Ui_B_ReportWindow):
    def __init__(self,parent = None,name = None,modal = False,fl = Qt.Widget):
        QDialog.__init__(self,parent,fl)
        Ui_B_ReportWindow.setupUi(self,self)
        if (name):
            self.setObjectName(name)
        if (modal):
            self.setModal(modal)

        self.connect(self.PushButton2,SIGNAL("clicked()"),self.closeWindow)
        self.connect(self.PushButton1,SIGNAL("clicked()"),self.saveToHTML)
        self.connect(self.PushButton1_2,SIGNAL("clicked()"),self.saveToText)
        self.connect(self.MatMultiplier,SIGNAL("valueChanged(int)"),self.matMultiplierUpdate)

        #self.font().setPointSize(8)
        #self.ReportText.setTextFormat(Qt.RichText)
        self.parent = parent
        self.gemnames = None
        self.materials = None
        self.prevMultiplier = 1
        self.totalcost = 0
        
    def materialsReport(self, itemlist, showslot = 0):
        self.MMLabel.show()
        self.MatMultiplier.show()
        self.setWindowTitle('Materials Report')
        self.materials = { 'Gems' : { }, 'Liquids' : {}, 'Dusts': {} }
        self.gemnames = { }
        self.totalcost = 0
        if showslot == 0:
            lastslot = 6
        else:
            lastslot = showslot
        for loc, item in itemlist.items():
            if item.ActiveState != 'player':
                continue
            for slot in range(max(showslot - 1,0), lastslot):
                if item.slot(slot).done() == '1' \
                        and showslot == 0 \
                        and self.parent.showDoneInMatsList:
                    continue
                gemtype = item.slot(slot).type()
                effect = item.slot(slot).effect()
                amount = item.slot(slot).amount()
                for mattype, matl in item.slot(slot).gemMaterials(self.parent.realm).items():
                    for mat, val in matl.items():
                        if self.materials[mattype].has_key(mat):
                            self.materials[mattype][mat] += val
                        else:
                            self.materials[mattype][mat] = val
        
                if gemtype == 'Unused':
                    continue
                gemname = item.slot(slot).gemName(self.parent.realm)
                if self.gemnames.has_key(gemname):
                    self.gemnames[gemname] += 1
                else:
                    self.gemnames[gemname] = 1

                cost = item.slot(slot).gemCost()
                self.totalcost += cost
        keys = self.gemnames.keys()
        keys.sort(gemNameSort)
        self.gemnames = map(lambda(x): [x, self.gemnames.get(x)], keys)
        for type, matlist in self.materials.items():
            if type == 'Gems':
                keys = matlist.keys()
                keys.sort(gemTypeSort)
                matlist = map(lambda(x): [x, matlist.get(x)], keys)
            elif type == 'Liquids':
                keys = matlist.keys()
                keys.sort()
                matlist = map(lambda(x): [x, matlist.get(x)], keys)
            elif type == 'Dusts':
                keys = matlist.keys()
                keys.sort()
                matlist = map(lambda(x): [x, matlist.get(x)], keys)
            self.materials[type] = matlist
        self.printMaterials()

    def printMaterials(self):
        materialsstr = '<b>Total Cost:</b> <font color="#FF0000">%s</font>\n' % formatCost(self.totalcost)
        materialsstr += '<hr><center><b>Gem Names</b></center><ul>\n'
        for name, amount in self.gemnames:
            materialsstr += '<li>%d %s</li>\n' % (amount, name)
        materialsstr += '</ul><hr><center><b>Materials List</b></center><dl>\n'
        for type in ['Gems', 'Liquids', 'Dusts']:
            matlist = self.materials[type]
            materialsstr += '<dt><b>%s</b></dt>\n' % type
            for matl, val in matlist:
                materialsstr += '<dd>%d %s</dd>\n' % (val, matl)
        materialsstr += '</dl>\n'
        self.reportHtml = materialsstr
        self.ReportText.setHtml(self.reportHtml)

    def matMultiplierUpdate(self, multiplier):
        for i in range(0, len(self.gemnames)):
            name, amount = self.gemnames[i]
            self.gemnames[i] = [name, amount * multiplier / self.prevMultiplier]
        for type, matlist in self.materials.items():
            for i in range(0, len(matlist)):
                matl, val = matlist[i]
                self.materials[type][i] = [matl, val * multiplier / self.prevMultiplier]
        self.totalcost = self.totalcost * multiplier / self.prevMultiplier
        self.prevMultiplier = multiplier
        self.printMaterials()

    def parseConfigReport(self, filename, scxmldoc):
        processor = Processor.Processor()
        source = InputSource.DefaultFactory.fromString(
            XMLHelper.writexml(scxmldoc, UnicodeStringIO(), '', '\t', '\n'),
            "uri:sctemplate")

        try:
            xsltUri = OsPathToUri(filename)
            transform = InputSource.DefaultFactory.fromUri(xsltUri)

            processor.appendStylesheet(transform)
            self.reportHtml = processor.run(source)
        except Exception, e:
            QMessageBox.critical(None, 'Error!', 
                'Error composing report ' + filename + "\n\n" + str(e), 'OK')
            return

        self.MMLabel.hide()
        self.MatMultiplier.hide()
        self.setWindowTitle('Config Report')
        self.ReportText.setHtml(self.reportHtml)

    def saveToHTML(self):
        filename = QFileDialog.getSaveFileName(self, "Save HTML Report", "", "HTML (*.html);;All Files (*.*)")
        if filename is not None and str(filename) != '':
            try:
                if re.compile('\.html$').search(str(filename)) is None:
                    filename = str(filename)
                    filename += '.html'
                f = open(str(filename), 'w')
                f.write('<HTML>'+self.reportHtml+'</HTML>')
                f.close()
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + filename, 'OK')

    def saveToText(self):
        filename = QFileDialog.getSaveFileName(self, "Save Text Report", "", "Text (*.txt);;All Files (*.*)")
        if filename is not None and str(filename) != '':
            try:
                if re.compile('\.txt$').search(str(filename)) is None:
                    filename = str(filename)
                    filename += '.txt'
                f = open(str(filename), 'w')
                w = DimWriter(f)
                s = ObtuseFormatter(w)
                p = HTMLPlusParser(s)
                p.feed(self.reportHtml)
                p.close()
                w.flush()
                f.close()
            except IOError:
                QMessageBox.critical(None, 'Error!', 
                    'Error writing to file: ' + filename, 'OK')
        
    def closeWindow(self):
        self.done(1)                        

class XSLTMessageHandler:
    def __init__(self):
        self.content = ''
    def write(self, msg):
        self.content = self.content + msg
    def getContent(self):
        return self.content

