import httplib, urllib
import HTMLParser
import re
import sys
import time

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Item import *
from xml.dom.minidom import *
from B_Ethinarg import *
from B_QueryBox import *

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

    def handle_data(self, data):
        if self.inSelect and self.currentValue:
            v = data.strip()
            if len(v) > 0:
                self.formTags[self.tagName].append((v, self.currentValue))

    def handle_endtag(self, tag):
        if tag == 'select' and self.inSelect:
            self.inSelect = False
            self.currentValue = None

    def getFormData(self):
        return self.formTags

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
        elif self.inTable and tag == 'tr' and self.tableLevel == self.saveTableLevel:
            self.columnCount = 0
            self.rowCount += 1
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
            self.htmlList.append(data.strip())

        #if self.inTable: print data

    def handle_endtag(self, tag):
        if tag == 'table':
            if self.tableLevel == self.saveTableLevel:
                self.inTable = False
                self.done = True
            self.tableLevel -= 1
        if self.inTable or self.testTable:
            if tag == 'tr' and self.tableLevel == self.saveTableLevel and \
                    self.rowCount > 1:
                self.htmlList.append('<td><a href="%d">Add Item To Template</a></td>' % (self.rowCount - 2))
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
        return '&'.join(['%s=%s' % (k, v) for k,v in self.queryparams.items()])

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
        return p.getFormData()

    def makeQuery(self, username = None, password = None):
        if username:
            self.username = username
        if password:
            self.password = password
            
        curtime = time.time()

        if not self.sid or (curtime - self.lastLogin) > 60 * 20:
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

    def setPageNumber(self, num):
        self.queryparams['curr_page'] = str(num)

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
        self.currentPage = 1
        self.pageStatus.setText('')
        #self.processBox = QueryProgress(self)

        self.show()

        self.processBox = QProgressDialog('Querying the database', 'Cancel',
            0, 0, self)
        self.processBox.setCancelButton(None)

        self.slotCombo.setCurrentIndex(0)

        self.processBox.setLabelText('Initializing...')
        InitializeThread(self).start()
        self.processBox.setWindowModality(Qt.WindowModal)
        self.processBox.show()

    def initialize(self):
        self.query = EthinargQuery()
        QApplication.postEvent(self, QEvent(InitializedEvent))

    def runQuery(self):
        uname = str(self.usernameBox.text())
        pwd = str(self.passwordBox.text())

        if len(uname) == 0 or len(pwd) == 0:
            QMessageBox.critical(self, "Login Error!",
                "You must enter a username and password for Ethinarg's database!")
            return

        self.currentPage = 1
        self.query.setItemName(str(self.itemNameBox.text()))
        idx = str(self.slotCombo.itemData(self.slotCombo.currentIndex()).toString())
        self.query.setItemSlot(idx)
        self.query.setPageNumber(self.currentPage)

        self.doQuery(uname, pwd)

    def doQuery(self, uname = None, pwd = None):
        self.processBox.reset()
        self.processBox.setLabelText('Querying the database...')
        self.processBox.show()
        #self.processBox.start()
        QueryRunner(self, uname, pwd).start()

    def _doQuery(self, uname = None, pwd = None):
        if not self.query.makeQuery(uname, pwd):
            QApplication.postEvent(self, QEvent(LoginFailedEvent))
            #QMessageBox.critical(self, "Login Error!",
            #    "Could not login, please check username and password")
            return

        QApplication.postEvent(self, QEvent(PostResultsEvent))
        #self.browser.setHtml(self.query.htmlText)
        #self.updatePageStatus()
        
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
        self.pageStatus.setText('%d/%d' % (self.currentPage, numpages))

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

    def event(self, e):
        if e.type() == LoginFailedEvent:
            #self.processbox.stop()
            self.processBox.cancel()
            QMessageBox.critical(self, "Login Error!",
                "Could not login, please check username and password")
            return True
        elif e.type() == PostResultsEvent:
            #self.processBox.stop()
            self.processBox.cancel()
            self.browser.setHtml(self.query.htmlText)
            self.updatePageStatus()
            return True
        elif e.type() == InitializedEvent:
            self.slotCombo.clear()
            for k,v in self.query.formValues['itemtype']:
                self.slotCombo.addItem(k, QVariant(v))
            self.processBox.cancel()
            return True
        else:
            return QDialog.event(self, e)

b = None

def anchorClicked(link):
    global b

    print link.path()
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

