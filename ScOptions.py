# ScOptions.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

import XMLHelper
import sys
import os.path
import traceback
from xml.dom.minidom import *
from MyStringIO import UnicodeStringIO
from Singleton import Singleton

class ScOptions(Singleton):
    def __init__(self):
        Singleton.__init__(self)
        self.__options = {}

    def getOption(self, name, defaultValue):
        if self.__options.has_key(name):
            return self.__options[name]

        return defaultValue

    def setOption(self, name, val):
        self.__options[name] = val

    def asXML(self):
        document = Document()
        rootnode = document.createElement('DefaultOptions')
        document.appendChild(rootnode)
        for key, val in self.__options.items():
            rootnode.appendChild(self.writeOption(document, key, val))
        return document

    def writeOption(self, doc, key, val):
        if key[0].isdigit():
            key = 'N__' + key
        elem = doc.createElement(key)
        if isinstance(val, dict):
            for subkey, subval in val.items():
                elem.appendChild(self.writeOption(doc, subkey, subval))
            return elem
        elif isinstance(val, list):
            for v in val:
                elem.appendChild(doc, key + 'Item', v)
        else:
            elem.appendChild(doc.createTextNode(unicode(val)))

        return elem
            
    def parseOption(self, node):
        hasElements = False
        sameElements = True
        ptag = None

        for child in node.childNodes:
            if child.nodeType == Node.ELEMENT_NODE:
                hasElements = True
                if ptag and ptag != child.nodeName:
                    sameElements = False
                ptag = child.nodeName

        if not hasElements:
            val = XMLHelper.getText(node.childNodes)
            if val.lower() == 'true' or val.lower() == 'false':
                return bool(val)
            else:
                try:
                    return int(val)
                except ValueError:
                    pass
                try:
                    return float(val)
                except ValueError:
                    pass
                return val
        else:
            if not sameElements:
                vals = {}
                for child in node.childNodes:
                    if child.nodeType == Node.TEXT_NODE: continue
                    nodeName = child.nodeName
                    if len(nodeName) > 3 and nodeName[:3] == 'N__': 
                        nodeName = nodeName[3:]
                    elif len(nodeName) >= 2 and nodeName[0] == 'L' and nodeName[1].isdigit():  # old style
                            nodeName = nodeName[1:]
                    vals[nodeName] = self.parseOption(child)

                return vals
            else:
                vals = []
                for child in node.childNodes:
                    if child.nodeType == Node.TEXT_NODE: continue
                    vals.append(self.parseOption(child))

                return vals

    def loadFromXML(self, xmldoc):
        self.__options.clear()
        for child in xmldoc.childNodes:
            if child.nodeType == Node.TEXT_NODE: continue
            nodeName = child.nodeName
            if len(nodeName) > 3 and nodeName[:3] == 'N__':
                nodeName = nodeName[3:]
            self.__options[nodeName] = self.parseOption(child)
            
    def load(self):
        scfile = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                              'Spellcraft.xml')
        if os.path.exists(scfile):
            try:
                f = open(scfile, 'r')
                xmldoc = parseString(f.read())
                template = xmldoc.getElementsByTagName('DefaultOptions')
                self.loadFromXML(template[0])
                f.close()
            except: 
                traceback.print_exc()
                pass

        print self.__options

    def save(self):        
        scfile = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                              'Spellcraft.xml')
        if os.access(os.path.dirname(scfile), os.W_OK):
            try:
                f = open(scfile, 'w')
                f.write(XMLHelper.writexml(self.asXML(), UnicodeStringIO(), '', '\t', '\n'))
                f.close()
            except:
                traceback.print_exc()
                pass
