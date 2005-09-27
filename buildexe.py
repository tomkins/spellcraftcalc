from distutils.core import setup
import py2exe
import glob
import sys

if __name__ == "__main__":
    sys.argv.append('py2exe')

sc = dict(
    script="ScWindow.pyw",
    icon_resources=[(100, 'ScWindow.ico')],)

setup(name="testsetup", 
    zipfile=None,
    windows=[sc],
    data_files=[
        ('.', ['./LICENSE.txt']),
        ('.', ['./CHANGES.txt']),
        ('reports', ['reports/Reports.txt']), 
        ('reports', glob.glob("reports/*.xml"))],
    options = {'py2exe': {'excludes' : ['_ssl', '_socket'], 
                          'includes' : ['sip'],
                          'bundle_files' : 3,
                          #'dll_excludes' : ['ddraw.dll', 'opengl32.dll', 'glu32.dll']
        }
    },
)
