#!/usr/bin/python
#"""
#Minimal setup.py example, run with:
#% python setup.py py2app
#
#For the list of available commands, see:
#% python setup.py py2app --help
#"""

import glob
from distutils.core import setup
import py2app
import Ft.Lib.DistExt.Py2Exe
py2app_options = dict(
    iconfile='kscraft.icns',
    includes=['sip', 'cmd', 'Ft.Xml.XPath.ParsedPredicateList',
        'Ft.Xml.XPath.ParsedAbbreviatedAbsoluteLocationPath',
        'Ft.Xml.XPath.ParsedAbbreviatedRelativeLocationPath',
        'Ft.Xml.XInclude',
        'Ft.Xml.Xslt.XPatterns',
        ],
)
setup(
    app = ['Spellcraft.pyw'],
    data_files=[
        ('.', ['./LICENSE.txt']),
        ('.', ['./NOTICE.txt']),
        ('.', ['./CHANGES.txt']),
        ('.', ['./SC.rcc']),
        ('reports', ['reports/Reports.txt']), 
        ('reports', glob.glob("reports/*.xml")),
        ('reports', glob.glob("reports/*.xsl")),
    ],
    options=dict(
        py2app=py2app_options,
    )
)
