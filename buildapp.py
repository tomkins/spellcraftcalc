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
import os
import os.path
py2app_options = dict(
    iconfile='images/ScWindow.icns',
    includes=['sip', 'cmd'],
    excludes=['_ssl',],
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

if os.path.exists('dist/Spellcraft.app'):
    os.system('hdiutil create -ov -imagekey zlib-level=9 -srcfolder dist/Spellcraft.app dist/Spellcraft.dmg')
