import httplib, urllib
import HTMLParser
import re
import urllib
import sys
import time
import traceback
from ScOptions import ScOptions

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Item import *
from xml.dom.minidom import *
from B_Ethinarg import *

LoginFailedEvent = QEvent.Type(QEvent.User + 1)
PostResultsEvent = QEvent.Type(QEvent.User + 2)
InitializedEvent = QEvent.Type(QEvent.User + 3)

class EthinargFormParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.inSelect = False
        self.formTags = {}
        self.currentValue = None
        self.tagName = ''
        self.tableNumber = 0
        self.statRow = 0
        self.inStatTable = False
        self.inStatColumn = False
        self.statTable = []
        self.itemCounts = None

    def handle_starttag(self, tag, attrs):
        if tag == 'select':
            self.inSelect = True
            for k, v in attrs:
                if k == 'name':
                    self.tagName = v
                    self.formTags[self.tagName] = []
        elif tag == 'option' and self.inSelect:
            for k, v in attrs:
                if k == 'value':
                    self.currentValue = v
        elif tag == 'table':
            self.tableNumber += 1
            if self.tableNumber == 2:
                self.inStatTable = True
            else:
                self.inStatTable = False
        elif self.inStatTable and tag == 'tr':
            self.statRow += 1
        elif self.inStatTable and self.statRow > 1 and tag == 'td':
            self.inStatColumn = True
            

    def handle_data(self, data):
        if self.inSelect and self.currentValue:
            v = data.strip()
            if len(v) > 0:
                self.formTags[self.tagName].append((v, self.currentValue))
        elif self.inStatColumn:
            self.statTable.append(data.strip())
            self.inStatColumn = False

    def handle_endtag(self, tag):
        if tag == 'select' and self.inSelect:
            self.inSelect = False
            self.currentValue = None

    def getFormData(self):
        return self.formTags

    def getItemCounts(self):
        if self.itemCounts: return self.itemCounts
        self.itemCounts = {}
        self.itemCounts['Hibernia'] = {}
        self.itemCounts['Midgard'] = {}
        self.itemCounts['Albion'] = {}
        self.itemCounts['All'] = {}
        self.itemCounts['Total'] = {}

        self.itemCounts['Hibernia']['Verified'] = int(self.statTable[1])
        self.itemCounts['Midgard']['Verified'] = int(self.statTable[2])
        self.itemCounts['Albion']['Verified'] = int(self.statTable[3])
        self.itemCounts['All']['Verified'] = int(self.statTable[4])
        self.itemCounts['Total']['Verified'] = int(self.statTable[5])

        self.itemCounts['Hibernia']['Non-Verified'] = int(self.statTable[7])
        self.itemCounts['Midgard']['Non-Verified'] = int(self.statTable[8])
        self.itemCounts['Albion']['Non-Verified'] = int(self.statTable[9])
        self.itemCounts['All']['Non-Verified'] = int(self.statTable[10])
        self.itemCounts['Total']['Non-Verified'] = int(self.statTable[11])

        self.itemCounts['Hibernia']['Total'] = int(self.statTable[13])
        self.itemCounts['Midgard']['Total'] = int(self.statTable[14])
        self.itemCounts['Albion']['Total'] = int(self.statTable[15])
        self.itemCounts['All']['Total'] = int(self.statTable[16])

        return self.itemCounts

class EthinargItemParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.tableLevel = 0
        self.saveTableLevel = 0
        self.rowCount = 0
        self.columnCount = 0
        self.inTable = False
        self.onItemName = False
        self.testTable = False
        self.testColumn = False
        self.linkCount = 0
        self.items = []
        self.htmlList = []
        self.done = False
        self.numPages = 0
        self.pageRE = re.compile(r'curr_page=(\d+)')
        self.linkSet = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for k,v in attrs:
                if k == 'href':
                    m = self.pageRE.search(v)
                    if m:
                        self.numPages = max(self.numPages, int(m.group(1)))
                    break
        if self.done:
            return
        if tag == 'table':
            self.tableLevel += 1
        if not self.inTable and tag == 'table':
            for k, v in attrs:
                if k == 'class' and v == 'forumline':
                    self.testTable = True
                    self.rowCount = 0
        elif self.testTable and tag == 'tr':
            self.columnCount = 0
            self.rowCount += 1
            self.linkSet = False
        elif self.inTable and tag == 'tr' and self.tableLevel == self.saveTableLevel:
            self.columnCount = 0
            self.rowCount += 1
            self.linkSet = False
        elif self.testTable and self.rowCount == 1 and tag == 'td':
            self.testColumn = True
        elif self.inTable and self.rowCount > 1 and tag == 'td':
            self.columnCount += 1
            self.linkCount = 0
        elif self.inTable and self.rowCount > 1 and self.columnCount == 2 and tag == 'a':
            #print attrs
            if self.linkCount == 0:
                self.onItemName = True
            elif self.linkCount == 1:
                name, e = self.items[-1]
                for k, v in attrs:
                    if k == 'href':
                        self.items[-1] = (name, v)
            self.linkCount += 1

        if self.inTable or self.testTable:
            if tag != 'a':
                h = '<%s ' % tag
                for k, v in attrs:
                    h += '%s="%s" ' % (k, v)
                h += '>'
                self.htmlList.append(h)

    def handle_data(self, data):
        if self.onItemName:
            self.items.append((data.strip(), None))
            self.onItemName = False
        elif self.testColumn:
            if data.strip().lower() == 'name':
                self.inTable = True
                self.saveTableLevel = self.tableLevel
                self.testColumn = False
                self.testTable = False
            else:
                self.testColumn = False
                self.testTable = False
                self.htmlList = []
        if self.inTable or self.testTable:
            txt = data.strip()
            if txt == 'Utility Value':
                txt = 'Utility<br />Value'
            elif txt == 'Magical Ability':
                txt = 'Magical<br />Ability'
            if self.rowCount > 1 and self.columnCount == 2 and \
                    not self.linkSet and len(txt) > 0:
                txt = '<a href="%d">%s</a>' % (self.rowCount - 2, txt)
                self.linkSet = True
                
            self.htmlList.append(txt)

        #if self.inTable: print data

    def handle_endtag(self, tag):
        if tag == 'table':
            if self.tableLevel == self.saveTableLevel:
                self.inTable = False
                self.done = True
            self.tableLevel -= 1
        if self.inTable or self.testTable:
            #if tag == 'tr' and self.tableLevel == self.saveTableLevel and \
            #        self.rowCount > 1:
            #    self.htmlList.append('<td><a href="%d">Add Item To Template</a></td>' % (self.rowCount - 2))
            if tag != 'a':
                self.htmlList.append('</' + tag + '>')

    def getItemNames(self):
        return self.items

class EthinargQuery:
    def __init__(self):
        self.htmlText = ''
        self.sid = None
        self.username = None
        self.password = None
        self.lastLogin = -1
        self.numPages = 0
        self.itemCounts = None

        self.queryparams = {
            'dmgType' : '1',
            'ma' : '9999',
            'realm' : '0',
            'class' : '14',
            'min_level' : '1',
            'max_level' : '51',
            'location' : '9999',
            'location2' : '0',
            'itemtype' : '9999',
            'stat1' : '9999',
            'stat2' : '9999',
            'stat3' : '9999',
            'min_uv' : '0',
            'max_uv' : '10',
            'ipp' : '2',
            'itemName' : '',
            'order_by' : '',
            'curr_page' : '1',
        }

        self.formValues = self.makeInitialQuery()

    def makeQueryString(self):
        return urllib.urlencode(self.queryparams)

    def makeInitialQuery(self):
        self.conn = httplib.HTTPConnection("www.ethinarg.com")
        self.conn.request("GET",
            "http://www.ethinarg.com/itemdb/main.php?" +
            self.makeQueryString())
        resp = self.conn.getresponse()

        html = resp.read()
        self.conn.close()

        p = EthinargFormParser()
        p.feed(html)
        self.itemCounts = p.getItemCounts()
        return p.getFormData()

    def makeQuery(self, username = None, password = None):
        if username:
            self.username = username
        if password:
            self.password = password
            
        curtime = time.time()

        if not self.sid or (curtime - self.lastLogin) > 60 * 60 * 24:
            if not self.login(self.username, self.password):
                return False

        self.conn = httplib.HTTPConnection("www.ethinarg.com")
        self.conn.request("GET",
            "http://www.ethinarg.com/itemdb/main.php?" +
            self.makeQueryString()
            + "&sid=" + self.sid)
        resp = self.conn.getresponse()

        html = resp.read()
        self.conn.close()
        p2 = EthinargItemParser()
        p2.feed(html)

        self.htmlText = ''.join(p2.htmlList).replace("(xml)", "")
        self.htmlText = self.htmlText.replace("(Save)", "")
        self.htmlText = re.compile(r'\(#\d+\)').sub("", self.htmlText)
        self.htmlText = '<html><body>%s</body></html>' % self.htmlText
        self.itemData = p2.getItemNames()
        self.numPages = p2.numPages

        return True

    def getXML(self, path):
        self.conn = httplib.HTTPConnection("www.ethinarg.com")
        self.conn.request("GET", '/itemdb/' + path)

        return self.conn.getresponse().read()

    def login(self, username, password):
        conn = httplib.HTTPConnection('www.ethinarg.com')
        conn.request('GET', '/phpbb2/login.php')
        resp = conn.getresponse()
        resp.read()
        cookie = resp.getheader('Set-Cookie')
        params = urllib.urlencode({'username' : username, 
            'password' : password, 'autologin' : 'on',
            'login' : 'Log in', 'redirect' : ''})
        headers = {"Content-Type": "application/x-www-form-urlencoded", 
            "Accept": "text/xml,text/html,application/xml,text/plain", 'Cookie' : cookie,
            "Referrer" : 'http://www.ethinarg.com/phpbb2/login.php' }

        conn.request('POST', '/phpbb2/login.php', params, headers)

        resp = conn.getresponse()
        cookie = resp.getheader('Location')
        if not cookie or len(cookie) == 0:
            self.sid = None
            return False
        m = re.compile(r'sid=([a-zA-Z0-9]*)').search(cookie)
        sid = m.group(1)
        resp.read()

        conn.close()

        self.sid = sid
        self.lastLogin = time.time()

        return True

    def setItemName(self, name):
        self.queryparams['itemName'] = name

    def setItemSlot(self, slot):
        self.queryparams['itemtype'] = slot

    def setRealm(self, realm):
        self.queryparams['realm'] = realm

    def setClass(self, cls):
        self.queryparams['class'] = cls

    def setMinLevel(self, lvl):
        self.queryparams['min_level'] = lvl

    def setMaxLevel(self, lvl):
        self.queryparams['max_level'] = lvl

    def setBonus1(self, stat):
        self.queryparams['stat1'] = stat

    def setBonus2(self, stat):
        self.queryparams['stat2'] = stat

    def setBonus3(self, stat):
        self.queryparams['stat3'] = stat

    def setMagicalAbility(self, ma):
        self.queryparams['ma'] = ma

    def setPageNumber(self, num):
        self.queryparams['curr_page'] = str(num)

    def setLocation(self, loc):
        self.queryparams['location'] = loc

class QueryRunner(QThread):
    def __init__(self, parent, uname, pwd):
        QThread.__init__(self, parent)
        self.qb = parent
        self.uname = uname
        self.pwd = pwd

    def run(self):
        self.qb._doQuery(self.uname, self.pwd)

class InitializeThread(QThread):
    def __init__(self, parent):
        QThread.__init__(self, parent)
        self.qb = parent

    def run(self):
        self.qb.initialize()

class EthinargTestWindow(QDialog, Ui_B_Ethinarg):
    def __init__(self,scwin,parent = None,name = None,modal = False,fl = Qt.Widget):
        QDialog.__init__(self, parent, fl)
        Ui_B_Ethinarg.setupUi(self,self)

        self.scwin = scwin
        self.connect(self.browser, SIGNAL('anchorClicked(const QUrl&)'), self.anchorClicked)
        self.connect(self.queryButton, SIGNAL('clicked()'), self.runQuery)
        self.connect(self.nextButton, SIGNAL('clicked()'), self.nextPage)
        self.connect(self.prevButton, SIGNAL('clicked()'), self.prevPage)
        self.connect(self.goButton, SIGNAL('clicked()'), self.goPage)
        self.connect(self.closeButton, SIGNAL('clicked()'), self.close)
        #self.connect(self.collapseButton, SIGNAL('clicked()'),
        #    self.collapsePane)
        #self.connect(self.openSearchButton, SIGNAL('clicked()'),
        #    self.openSearch)
        self.connect(self.openSearchButton, SIGNAL('toggled(bool)'),
            self.openSearch)
        self.connect(self.minLevelCombo, SIGNAL('currentIndexChanged(int)'),
            self.minLevelChanged)
        self.connect(self.maxLevelCombo, SIGNAL('currentIndexChanged(int)'),
            self.maxLevelChanged)
        self.currentPage = 1
        self.pageStatus.setText('')
        self.openSearchButton.setChecked(True)
        self.slotCombo.setCurrentIndex(0)
        self.usernameBox.setText(ScOptions.instance().getOption(
            'Ethinarg_username', ''))
        self.passwordBox.setText(ScOptions.instance().getOption(
            'Ethinarg_password', ''))
        self.show()

        self.processBox = QProgressDialog('Querying the database', 'Cancel',
            0, 0, self)
        self.processBox.setCancelButton(None)
        self.processBox.setLabelText('Initializing...')
        self.processBox.setWindowModality(Qt.WindowModal)
        InitializeThread(self).start()
        self.processBox.show()

    def initialize(self):
        self.query = EthinargQuery()
        self.queryBoxes = [
            (self.slotCombo, 'itemtype', self.query.setItemSlot),
            (self.realmCombo, 'realm', self.query.setRealm),
            (self.classCombo, 'class', self.query.setClass),
            (self.minLevelCombo, 'min_level', self.query.setMinLevel),
            (self.maxLevelCombo, 'max_level', self.query.setMaxLevel),
            (self.bonus1Combo, 'stat1', self.query.setBonus1),
            (self.bonus2Combo, 'stat2', self.query.setBonus2),
            (self.bonus3Combo, 'stat3', self.query.setBonus3),
            (self.magicalCombo, 'ma', self.query.setMagicalAbility),
            (self.locationCombo, 'location', self.query.setLocation),
        ]
        QApplication.postEvent(self, QEvent(InitializedEvent))

    def loadCombos(self):
        for ctrl, key, func in self.queryBoxes:
            ctrl.clear()
            for k, v in self.query.formValues[key]:
                ctrl.addItem(k, QVariant(v))

    def loadSavedOptions(self):
        options_dict = ScOptions.instance().getOption('EthinargValues', {})
        for ctrl, key, func in self.queryBoxes:
            if options_dict.has_key(key):
                ctrl.setCurrentIndex(ctrl.findText(str(options_dict[key])))
        if options_dict.has_key('item_name'):
            self.itemNameBox.setText(options_dict['item_name'])

    def setQueryParams(self):
        options_dict = {}
        self.query.setItemName(str(self.itemNameBox.text()))
        options_dict['item_name'] = str(self.itemNameBox.text())
        for ctrl, key, func in self.queryBoxes:
            idx = str(ctrl.itemData(ctrl.currentIndex()).toString())
            func(idx)
            options_dict[key] = str(ctrl.currentText())
        self.query.setPageNumber(self.currentPage)
        ScOptions.instance().setOption('EthinargValues', options_dict)

    def runQuery(self):
        uname = str(self.usernameBox.text())
        pwd = str(self.passwordBox.text())

        if len(uname) == 0 or len(pwd) == 0:
            QMessageBox.critical(self, "Login Error!",
                "You must enter a username and password for Ethinarg's database!")
            return

        self.currentPage = 1
        self.setQueryParams()
        #self.query.setItemName(str(self.itemNameBox.text()))
        #idx = str(self.slotCombo.itemData(self.slotCombo.currentIndex()).toString())
        #self.query.setItemSlot(idx)
        #self.query.setPageNumber(self.currentPage)

        ScOptions.instance().setOption('Ethinarg_username', 
            str(self.usernameBox.text()))
        ScOptions.instance().setOption('Ethinarg_password', 
            str(self.passwordBox.text()))

        self.doQuery(uname, pwd)

    def doQuery(self, uname = None, pwd = None):
        self.processBox.reset()
        self.processBox.setLabelText('Querying the database...')
        self.processBox.show()
        QueryRunner(self, uname, pwd).start()

    def _doQuery(self, uname = None, pwd = None):
        if not self.query.makeQuery(uname, pwd):
            QApplication.postEvent(self, QEvent(LoginFailedEvent))
            #QMessageBox.critical(self, "Login Error!",
            #    "Could not login, please check username and password")
            return

        try:
            QApplication.postEvent(self, QEvent(PostResultsEvent))
        except:
            pass
        
    def updatePageStatus(self):
        numpages = self.query.numPages
        if numpages == 1:
            self.nextButton.setEnabled(False)
            self.goButton.setEnabled(False)
            self.prevButton.setEnabled(False)
        else:
            self.goButton.setEnabled(True)
            self.nextButton.setEnabled(self.currentPage < numpages)
            self.prevButton.setEnabled(self.currentPage > 1)

        self.pageNum.setText(str(self.currentPage))
        self.pageStatus.setText('Page: %d/%d' % (self.currentPage, numpages))

    def nextPage(self):
        self.currentPage += 1
        self.query.setPageNumber(self.currentPage)
        self.doQuery()

    def prevPage(self):
        self.currentPage -= 1
        self.query.setPageNumber(self.currentPage)
        self.doQuery()

    def goPage(self):
        try:
            num = int(str(self.pageNum.text()))
            if num > self.query.numPages:
                self.pageNum.setText(str(self.currentPage))
            else:
                self.currentPage = num
                self.query.setPageNumber(self.currentPage)
                self.doQuery()
        except:
            self.pageNum.setText(str(self.currentPage))

    def collapsePane(self):
        self.splitter.setSizes([self.width(), 0])

    def openSearch(self, toggle):
        if toggle:
            self.openSearchButton.setText("<<< Collapse")
            self.splitter.setSizes([self.width(),
                self.splitter.widget(1).minimumSizeHint().width()])
        else:
            self.openSearchButton.setText("Open Search >>>")
            self.splitter.setSizes([self.width(), 0])

    def displayItemCounts(self):
        cnts = self.query.itemCounts
        html = """<html><center><h3>Current Item Counts</h3><table border=0
        width="75%%" cellspacing=10 cellpadding=0>
        <tr><td></td><td>Hibernia</td><td>Midgard</td><td>Albion</td><td>All</td><td>Total</td></tr>
        <tr><td>Verified Items</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td></tr>
        <tr><td>Non Verified Items</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td></tr>
        <tr><td>Total</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td><td></td></tr>
        </table></html>""" % (
            cnts['Hibernia']['Verified'],
            cnts['Midgard']['Verified'],
            cnts['Albion']['Verified'],
            cnts['All']['Verified'],
            cnts['Total']['Verified'],
            cnts['Hibernia']['Non-Verified'],
            cnts['Midgard']['Non-Verified'],
            cnts['Albion']['Non-Verified'],
            cnts['All']['Non-Verified'],
            cnts['Total']['Non-Verified'],
            cnts['Hibernia']['Total'],
            cnts['Midgard']['Total'],
            cnts['Albion']['Total'],
            cnts['All']['Total'])

        self.browser.setHtml(html)

    def minLevelChanged(self, idx):
        if str(self.minLevelCombo.currentText()) == '' or \
                str(self.maxLevelCombo.currentText()) == '':
            return

        lvl = int(str(self.minLevelCombo.currentText()))
        max_level = int(str(self.maxLevelCombo.currentText()))

        if lvl > max_level:
            self.maxLevelCombo.setCurrentIndex(
                self.maxLevelCombo.findText(str(lvl)))

    def maxLevelChanged(self, idx):
        if str(self.minLevelCombo.currentText()) == '' or \
                str(self.maxLevelCombo.currentText()) == '':
            return

        min_level = int(str(self.minLevelCombo.currentText()))
        lvl = int(str(self.maxLevelCombo.currentText()))

        if lvl < min_level:
            self.minLevelCombo.setCurrentIndex(
                self.minLevelCombo.findText(str(lvl)))
            
    def anchorClicked(self, link):
        self.browser.setSource(QUrl()) # don't navigate

        idx = int(str(link.path()))

        name, xml_url = self.query.itemData[idx]

        xmlstring = self.query.getXML(xml_url)

        item = Item()

        xmldoc = parseString(xmlstring)
        items = xmldoc.getElementsByTagName('SCItem')
        item.loadFromXML(items[0])

        self.scwin.addItem(item)

        QMessageBox.information(self, "Item Added!",
            "'%s' added to the '%s' slot" % (item.ItemName, item.Location,))

    def event(self, e):
        if e.type() == LoginFailedEvent:
            self.processBox.cancel()
            QMessageBox.critical(self, "Login Error!",
                "Could not login, please check username and password")
            return True
        elif e.type() == PostResultsEvent:
            self.processBox.cancel()
            self.browser.setHtml(self.query.htmlText)
            self.updatePageStatus()
            self.openSearchButton.setChecked(False)
            return True
        elif e.type() == InitializedEvent:
            self.loadCombos()
            self.loadSavedOptions()
            self.displayItemCounts()
            self.maxLevelCombo.setCurrentIndex(
                self.maxLevelCombo.findText('51'))
            self.processBox.cancel()
            return True
        else:
            return QDialog.event(self, e)

b = None

def anchorClicked(link):
    global b

    b.setSource(QUrl())

if __name__ == '__main__':
    e = EthinargQuery()

    app=QApplication(sys.argv)
    b = QTextBrowser()
    b.connect(b, SIGNAL('anchorClicked(const QUrl&)'), anchorClicked)
    b.setHtml(e.htmlText)
    b.show()
    app.setActiveWindow(b)
 
    sys.exit(app.exec_())

# vim: set ts=4 sw=4 et:
