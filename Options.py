# Options.py: Dark Age of Camelot Spellcrafting Calculator
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
from B_Options import *
import re
import types
import XMLHelper
import sys
import os.path
import traceback
from xml.dom.minidom import *
from MyStringIO import UnicodeStringIO

class Options(B_Options):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        B_Options.__init__(self,parent,name,modal,fl)
#       self.Tab.setTabEnabled(self.Price, 0)
        self.parent = parent
        skilllist = range(1001, 51, -50)
        self.Skill.clear()
        self.Skill.insertStrList(map(lambda(x):str(x), skilllist))
        li = self.Skill.listBox().findItem(str(self.parent.crafterSkill))
        self.Skill.setCurrentItem(self.Skill.listBox().index(li))
        self.NoteText.setText(self.parent.noteText)
        self.ShowDoneGems.setChecked(self.parent.showDoneInMatsList)
        self.TierPricing = {}
        self.QualPricing = {}
        self.loadPriceInfo(self.parent.pricingInfo)
        self.QualMarkup.setText(
            str(self.QualPricing.get(str(self.QualLevel.currentText()), 0)))
        self.TierPrice.setText(
            str(self.TierPricing.get(str(self.Tier.currentText()), 0)))
        if self.parent.coop:
            self.Coop.setChecked(1)
        else:
            self.Coop.setChecked(0)

        if self.parent.includeRacials:
            self.IncludeRR.setChecked(1)
        else:
            self.IncludeRR.setChecked(0)

        if self.parent.capDistance:
            self.CapDistance.setChecked(1)
        else:
            self.CapDistance.setChecked(0)

        if self.parent.hideNonClassSkills:
            self.HideNonClassSkills.setChecked(1)
        else:
            self.HideNonClassSkills.setChecked(0)


    def asXML(self):
        document = Document()
        rootnode = document.createElement('DefaultOptions')
        document.appendChild(rootnode)
        realmnode = document.createElement('Realm')
        realmnode.appendChild(document.createTextNode(str(self.parent.Realm.currentText())))
        rootnode.appendChild(realmnode)
        showdone = document.createElement('DontShowDoneGems')
        showdone.appendChild(document.createTextNode(str(self.ShowDoneGems.isChecked())))
        rootnode.appendChild(showdone)
        includerr = document.createElement('IncludeRRInTotals')
        includerr.appendChild(document.createTextNode(str(self.IncludeRR.isChecked())))
        rootnode.appendChild(includerr)
        capnode = document.createElement('DistanceToCap')
        capnode.appendChild(document.createTextNode(str(self.CapDistance.isChecked())))
        rootnode.appendChild(capnode)
        hideskill = document.createElement('HideNonClassSkills')
        hideskill.appendChild(document.createTextNode(str(self.HideNonClassSkills.isChecked())))
        rootnode.appendChild(hideskill)
        coopnode = document.createElement('Coop')
        coopnode.appendChild(document.createTextNode(str(self.Coop.isChecked())))
        rootnode.appendChild(coopnode)
        cskill = document.createElement('CrafterSkill')
        cskill.appendChild(document.createTextNode(str(self.Skill.currentText())))
        rootnode.appendChild(cskill)
        pricenode = document.createElement('Pricing')
        pricing = self.getPriceInfo()

        locxnode = document.createElement('WindowX')
        locxnode.appendChild(document.createTextNode(str(self.parent.x())))
        rootnode.appendChild(locxnode)
        locynode = document.createElement('WindowY')
        locynode.appendChild(document.createTextNode(str(self.parent.y())))
        rootnode.appendChild(locynode)
        sizewnode = document.createElement('WindowW')
        sizewnode.appendChild(document.createTextNode(str(self.parent.width())))
        rootnode.appendChild(sizewnode)
        sizehnode = document.createElement('WindowH')
        sizehnode.appendChild(document.createTextNode(str(self.parent.height())))
        rootnode.appendChild(sizehnode)
        recentFiles = document.createElement('RecentFiles')
        for f in self.parent.recentFiles:
            fnode = document.createElement('File')
            fnode.appendChild(document.createTextNode(f))
            recentFiles.appendChild(fnode)
        rootnode.appendChild(recentFiles)
        camelotpath = document.createElement('DaocPath')
        camelotpath.appendChild(document.createTextNode(str(self.parent.DaocPath)))
        rootnode.appendChild(camelotpath)
        c_reportpath = document.createElement('ConfigReportFile')
        c_reportpath.appendChild(document.createTextNode(os.path.abspath(str(self.parent.reportFile))))
        rootnode.appendChild(c_reportpath)
        for key, val in pricing.items():
            node = document.createElement(key)
            if type(val) != types.DictType:
                node.appendChild(document.createTextNode(str(val)))
            else:
                for p, v in val.items():
                    # 'L' is needed since XML tags can't begin with Numbers!!
                    subnode = document.createElement('L'+p)
                    subnode.appendChild(document.createTextNode(str(v)))
                    node.appendChild(subnode)
            pricenode.appendChild(node)
        rootnode.appendChild(pricenode)
        return document

    def loadFromXML(self, xmldoc):
        pricing = {}
        x = 0
        y = 0
        w = 0
        h = 0
        for child in xmldoc.childNodes:
            if child.nodeType == Node.TEXT_NODE: continue
            if child.tagName == 'Realm':
                realm = XMLHelper.getText(child.childNodes)
                if realm == 'Albion':
                    self.parent.Realm.setCurrentItem(0)
                if realm == 'Hibernia':
                    self.parent.Realm.setCurrentItem(1)
                if realm == 'Midgard':
                    self.parent.Realm.setCurrentItem(2)
            elif child.tagName == 'DontShowDoneGems':
                if XMLHelper.getText(child.childNodes) == 'True':
                    self.ShowDoneGems.setChecked(1)
                else:
                    self.ShowDoneGems.setChecked(0)
            elif child.tagName == 'IncludeRRInTotals':
                if XMLHelper.getText(child.childNodes) == 'True':
                    self.IncludeRR.setChecked(1)
                else:
                    self.IncludeRR.setChecked(0)
            elif child.tagName == 'DistanceToCap':
                if XMLHelper.getText(child.childNodes) == 'True':
                    self.CapDistance.setChecked(1)
                else:
                    self.CapDistance.setChecked(0)
            elif child.tagName == 'HideNonClassSkills':
                if XMLHelper.getText(child.childNodes) == 'True':
                    self.HideNonClassSkills.setChecked(1)
                else:
                    self.HideNonClassSkills.setChecked(0)
            elif child.tagName == 'Coop':
                if XMLHelper.getText(child.childNodes) == 'True':
                    self.Coop.setChecked(1)
                else:
                    self.Coop.setChecked(0)
            elif child.tagName == 'CrafterSkill':
                li = self.Skill.listBox().findItem(XMLHelper.getText(child.childNodes))
                self.Skill.setCurrentItem(self.Skill.listBox().index(li))
            elif child.tagName == 'Pricing':
                for pchild in child.childNodes:
                    if pchild.nodeType == Node.TEXT_NODE: continue
                    if pchild.tagName == 'Qual' or pchild.tagName == 'Tier':
                        pricing[pchild.tagName] = {}
                        for dchild in pchild.childNodes:
                            if dchild.nodeType == Node.TEXT_NODE: continue
                            pricing[pchild.tagName][dchild.tagName[1:]] = \
                                    XMLHelper.getText(dchild.childNodes)
                    else:
                        pricing[pchild.tagName] = XMLHelper.getText(pchild.childNodes)
            elif child.tagName == 'WindowX':
                x = int(XMLHelper.getText(child.childNodes))
            elif child.tagName == 'WindowY':
                y = int(XMLHelper.getText(child.childNodes))
            elif child.tagName == 'WindowW':
                pass # was w = int(XMLHelper.getText(child.childNodes))
            elif child.tagName == 'WindowH':
                pass # was h = int(XMLHelper.getText(child.childNodes))
            elif child.tagName == 'RecentFiles':
                for pchild in child.childNodes:
                    if pchild.nodeType == Node.TEXT_NODE: continue
                    if pchild.tagName == 'File':
                        self.parent.recentFiles.append(XMLHelper.getText(pchild.childNodes))
            elif child.tagName == 'DaocPath':
                self.parent.DaocPath = XMLHelper.getText(child.childNodes)
            elif child.tagName == 'ConfigReportFile':
                self.parent.reportFile = XMLHelper.getText(child.childNodes)
                
        #if w == 0:
        #    w = 760
        #if h == 0:
        #    h = 517
        #self.parent.resize(w, h)
        self.parent.move(x, y)
        self.loadPriceInfo(pricing)
        self.OK_pressed()
            
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
                pass
                #traceback.print_exc()
        
    def OK_pressed(self):
        self.parent.crafterSkill = int(str(self.Skill.currentText()))
        self.parent.showDoneInMatsList = self.ShowDoneGems.isChecked()
        self.parent.includeRacials = self.IncludeRR.isChecked()
        self.parent.capDistance = self.CapDistance.isChecked()
        self.parent.hideNonClassSkills = self.HideNonClassSkills.isChecked()
        self.parent.noteText = str(self.NoteText.text())
        self.parent.pricingInfo = self.getPriceInfo()
        self.parent.coop = self.Coop.isChecked()
        scfile = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                              'Spellcraft.xml')
        if os.access(os.path.dirname(scfile), os.W_OK):
            try:
                f = open(scfile, 'w')
                f.write(XMLHelper.writexml(self.asXML(), UnicodeStringIO(), '', '\t', '\n'))
                f.close()
            except:
                pass
                #traceback.print_exc()
        self.done(1)

    def Cancel_pressed(self):
        self.done(-1)

    def QualMarkupSet(self, a0):
        st = re.sub('[^\d.]', '', str(a0))
        if st == '': st = '0'
        self.QualMarkup.setText(st)
        self.QualPricing[str(self.QualLevel.currentText())] = float(st)

    def TierMarkupSet(self, a0):
        st = re.sub('[^\d]', '', str(a0))
        if st == '': st = '0'
        self.TierPrice.setText(st)
        self.TierPricing[str(self.Tier.currentText())] = int(st)

    def QualMarkupChanged(self, a0):
        if self.QualPricing.has_key(str(a0)):
            self.QualMarkup.setText(str(self.QualPricing[str(a0)]))
        else:
            self.QualMarkup.setText('0')    

    def TierMarkupChanged(self, a0):
        if self.TierPricing.has_key(str(a0)):
            self.TierPrice.setText(str(self.TierPricing[str(a0)]))
        else:
            self.TierPrice.setText('0') 

    def getPriceInfo(self):
        pricing = { }
        pricing['CostInPrice'] = self.CostInPrice.isChecked()
        pricing['PPGem'] = int(str(self.PPGem.text()))
        pricing['PPItem'] = int(str(self.PPItem.text()))
        pricing['PPOrder'] = int(str(self.PPOrder.text()))
        pricing['QualInclude'] = self.QualInclude.isChecked()
        pricing['Qual'] = self.QualPricing
        pricing['PPInclude'] = self.PPInclude.isChecked()
        pricing['PPLevel'] = int(str(self.PPLevel.text()))
        pricing['PPImbue'] = int(str(self.PPImbue.text()))
        pricing['PPOC'] = int(str(self.PPOC.text()))
        pricing['General'] = float(str(self.GenMarkup.text()))
        pricing['TierInclude'] = self.TierInclude.isChecked()
        pricing['Tier'] = self.TierPricing
        pricing['HourInclude'] = self.HourInclude.isChecked()
        pricing['Hour'] = int(str(self.HourPrice.text()))

        return pricing

    def loadPriceInfo(self, pinfo):
        if not pinfo.has_key('PPGem'): return
        self.PPGem.setText(str(pinfo['PPGem']))
        self.PPItem.setText(str(pinfo['PPItem']))
        self.PPOrder.setText(str(pinfo['PPOrder']))
        self.GenMarkup.setText(str(pinfo['General']))
        if pinfo['QualInclude']:
            self.QualInclude.setChecked(1)
        else:
            self.QualInclude.setChecked(0)
        self.QualPricing = pinfo['Qual']
        if pinfo['PPInclude']:
            self.PPInclude.setChecked(1)
        else:
            self.PPInclude.setChecked(0)
        self.PPLevel.setText(str(pinfo['PPLevel']))
        self.PPImbue.setText(str(pinfo['PPImbue']))
        self.PPOC.setText(str(pinfo['PPOC']))
        if pinfo['TierInclude']:
            self.TierInclude.setChecked(1)
        else:
            self.TierInclude.setChecked(0)
        self.TierPricing = pinfo['Tier']
        if pinfo['HourInclude']:
            self.HourInclude.setChecked(1)
        else:
            self.HourInclude.setChecked(0)
        self.HourPrice.setText(str(pinfo['Hour']))
        if pinfo['CostInPrice']:
            self.CostInPrice.setChecked(1)
        else:
            self.CostInPrice.setChecked(0)
