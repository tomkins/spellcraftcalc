from distutils.core import setup
import Ft.Lib.DistExt.Py2Exe
#import py2exe
import glob
import sys

if __name__ == "__main__":
    sys.argv.append('py2exe')

sc = {
    "script" : "Spellcraft.pyw",
    "icon_resources" : [(100, 'ScWindow.ico')],
    }

setup(name="kscraftsetup",
    zipfile=None,
    windows=[sc],
    data_files=[
        ('.', ['./LICENSE.txt']),
        ('.', ['./NOTICE.txt']),
        ('.', ['./CHANGES.txt']),
        ('.', ['./ScWindow.png']),
        ('.', ['./Spellcraft.png']),
        ('reports', ['reports/Reports.txt']), 
        ('reports', glob.glob("reports/*.xml")),
        ('reports', glob.glob("reports/*.xsl")),
    ],
    options = {'py2exe': {'excludes' : ['_ssl',], 
                          'includes' : ['sip',],
                          'bundle_files' : 3,
        }
    },
)
