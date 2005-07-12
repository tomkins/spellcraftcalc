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
    windows=[sc],
    #scripts=["ScWindow.pyw"],
    data_files=[
        ('.', ['./LICENSE.txt']),
        ('.', ['./CHANGES.txt']),
        ('reports', ['reports/Reports.txt']), 
        ('reports', glob.glob("reports/*"))],
    icon='ScWindow.ico',
    options = {'py2exe': {'includes': 'encodings, encodings.*', 
                          'packages' : ['encodings.*'],
                          'excludes' : ['_ssl', '_socket'], 
                          'dll_excludes' : ['ddraw.dll', 'opengl32.dll', 'glu32.dll']}
    },
)
