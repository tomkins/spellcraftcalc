# Options.py: Dark Age of Camelot Spellcrafting Calculator
#
# See http://kscraft.sourceforge.net/ for updates
#
# See NOTICE.txt for copyrights and grant of license

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from B_Options import *
import re
import types
import XMLHelper
import sys
import os.path
import traceback
from xml.dom.minidom import *
from MyStringIO import UnicodeStringIO

from ScOptions import ScOptions

class Options(QDialog, Ui_B_Options):
    def __init__(self,parent = None,name = None,modal = False,fl = Qt.Widget):
        QDialog.__init__(self,parent,fl)
        Ui_B_Options.setupUi(self,self)
        if (name):
            self.setObjectName(name)
        if (modal):
            self.setModal(modal)

        self.connect(self.OK,SIGNAL("clicked()"),self.OK_pressed)
        self.connect(self.Cancel,SIGNAL("clicked()"),self.Cancel_pressed)
        self.connect(self.Tier,SIGNAL("activated(const QString&)"),self.TierMarkupChanged)
        self.connect(self.QualLevel,SIGNAL("activated(const QString&)"),self.QualMarkupChanged)
        self.connect(self.QualMarkup,SIGNAL("textChanged(const QString&)"),self.QualMarkupSet)
        self.connect(self.TierPrice,SIGNAL("textChanged(const QString&)"),self.TierMarkupSet)

#       self.Tab.setTabEnabled(self.Price, 0)
        self.parent = parent
        skilllist = range(1000, -1, -50)
        self.Skill.clear()
        self.Skill.addItems(map(lambda(x):str(x), skilllist))
        self.QualPricing = {}
        self.TierPricing = {}
        self.loadOptions()

    def loadOptions(self):
        li = self.Skill.findText(str(ScOptions.instance().getOption('CrafterSkill', 1000)))
        self.Skill.setCurrentIndex(li)
        self.NoteText.setHtml(self.parent.noteText)
        self.ShowDoneGems.setChecked(ScOptions.instance().getOption('DontShowDoneGems', False))
        self.loadPriceInfo(ScOptions.instance().getOption('Pricing', {}))
        self.Coop.setChecked(ScOptions.instance().getOption('Coop', False))
        self.IncludeRR.setChecked(ScOptions.instance().getOption('IncludeRRInTotals', False))
        self.CapDistance.setChecked(ScOptions.instance().getOption('DistanceToCap', False))
        self.HideNonClassSkills.setChecked(ScOptions.instance().getOption('HideNonClassSkills', False))

    def saveOptions(self):
        ScOptions.instance().setOption('CrafterSkill', int(str(self.Skill.currentText())))
        self.parent.noteText = str(self.NoteText.toPlainText())
        ScOptions.instance().setOption('DontShowDoneGems', self.ShowDoneGems.isChecked())
        ScOptions.instance().setOption('Pricing', self.getPriceInfo())
        ScOptions.instance().setOption('Coop', self.Coop.isChecked())
        ScOptions.instance().setOption('IncludeRRInTotals', self.IncludeRR.isChecked())
        ScOptions.instance().setOption('DistanceToCap', self.CapDistance.isChecked())
        ScOptions.instance().setOption('HideNonClassSkills', self.HideNonClassSkills.isChecked())

    def OK_pressed(self):
        self.saveOptions()
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

        # do some consistency checks
        if not self.pricingInfo.has_key('Qual') or\
                not isinstance(pinfo['Qual'], dict):
            pinfo['Qual'] = {}
        if not self.pricingInfo.has_key('Tier') or\
                not isinstance(pinfo['Tier'], dict):
            pinfo['Tier'] = {}

        self.PPGem.setText(str(pinfo['PPGem']))
        self.PPItem.setText(str(pinfo['PPItem']))
        self.PPOrder.setText(str(pinfo['PPOrder']))
        self.GenMarkup.setText(str(pinfo['General']))
        if pinfo['QualInclude']:
            self.QualInclude.setChecked(1)
        else:
            self.QualInclude.setChecked(0)
        self.QualPricing = pinfo['Qual']
        self.QualMarkupChanged(self.QualLevel.currentText())
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
        self.TierMarkupChanged(self.Tier.currentText())
        if pinfo['HourInclude']:
            self.HourInclude.setChecked(1)
        else:
            self.HourInclude.setChecked(0)
        self.HourPrice.setText(str(pinfo['Hour']))
        if pinfo['CostInPrice']:
            self.CostInPrice.setChecked(1)
        else:
            self.CostInPrice.setChecked(0)
