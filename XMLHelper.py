# XMLHelper.py: Dark Age of Camelot Spellcrafting Calculator
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

from xml.dom.minidom import *
import string
import binascii
from MyStringIO import UnicodeStringIO

# I didn't like how the default writer wrote to files, so I wrote my own
def writexml(self, writer, indent="", addindent="", newl=""):
    if self.nodeType == Node.DOCUMENT_NODE:
        writer.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    #    writer.write('''
#<!DOCTYPE doc [
#  <!ENTITY % html2utf8 SYSTEM "html2utf8.ent">
# %html2utf8;
# ]>
# ''')
        if self.childNodes:
            for node in self.childNodes:
                writexml(node, writer, indent, addindent, newl)
        return writer.getvalue()
    elif self.nodeType == Node.TEXT_NODE:
        writer.write(self.data, True)
        return
    writer.write(indent+"<" + self.tagName)

    attrs = self._get_attributes()
    a_names = attrs.keys()
    a_names.sort()

    for a_name in a_names:
        writer.write(" %s=\"" % a_name)
        _write_data(writer, attrs[a_name].value)
        writer.write("\"")
    if self.childNodes:
        writer.write(">")
        textonly = 0
        for node in self.childNodes:
            if node.nodeType != node.TEXT_NODE:
                writer.write(newl)
                textonly = 0
            else:
                textonly = 1
            writexml(node, writer,indent+addindent,addindent,newl)
        if textonly:
            writer.write("</%s>" % (self.tagName))
        else:
            writer.write("%s%s</%s>" % (newl,indent,self.tagName))
    else:
        writer.write("/>%s"%(newl))

def getText(nodelist):
    rc = ''
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            try:
                rc = rc + unicode(node.data, 'UTF-8')
            except:
                rc = rc + node.data
    return rc

def _write_data(writer, data):
    "Writes datachars to writer."
    #data = data.replace("&", "&amp;").replace("<", "&lt;")
    #data = data.replace("\"", "&quot;").replace(">", "&gt;")
    writer.write(data, True)    

