from distutils.core import setup
import py2exe
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
        ('.', ['./CHANGES.txt']),
        ('.', ['./ScWindow.png']),
        ('.', ['./Spellcraft.png']),
        ('reports', ['reports/Reports.txt']), 
        ('reports', glob.glob("reports/*.xml"))],
    options = {'py2exe': {'excludes' : ['_ssl', '_socket'], 
                          'includes' : ['sip'],
                          'bundle_files' : 3,
                          #'dll_excludes' : ['ddraw.dll', 'opengl32.dll', 'glu32.dll']
        }
    },
)
