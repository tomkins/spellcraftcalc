from distutils.core import setup
import py2exe
import glob
import sys

if __name__ == "__main__":
    sys.argv.append('py2exe')
    ##sys.argv.append('-w')
    #sys.argv.append('-p encodings')
    #sys.argv.append('-i encodings.*')
    #sys.argv.append('--force-imports encodings')
    #sys.argv.append('-icon py.ico')

sc = dict(
        script="ScWindow.py",
        icon_resources=[(100, 'py.ico')],)
setup(name="testsetup", 
    windows=[sc],
   ##scripts=["ScWindow.py"],
    data_files=[('.', ['./LICENSE.txt']),
        ('reports', ['reports/Reports.txt']), 
        ('reports', glob.glob("reports/*"))],
    #icon='py.ico',
    options = {'py2exe': {'includes': 'encodings, encodings.*', 
                          'packages' : ['encodings.*'],
                          'dll_excludes' : ['ddraw.dll', 'opengl32.dll', 'glu32.dll']}},
    )

