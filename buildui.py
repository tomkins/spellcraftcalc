import os
import re

files = [ ['ScWindow.ui', 'B_ScWindow.py'],
    ['Craft.ui', 'B_CraftWindow.py' ],
    ['DisplayWindow.ui', 'B_DisplayWindow.py'],
    ['ReportWindow.ui', 'B_ReportWindow.py'],
    ['ItemLevel.ui', 'B_ItemLevel.py'],
    ['CraftBar.ui', 'B_CraftBar.py'],
    ['ItemPreview.ui', 'B_ItemPreview.py'],
    ['Options.ui', 'B_Options.py'] ]

for ui, py in files:
    os.system('pyuic -o %s %s' % (py, ui))
    if ui == 'ScWindow.ui':
        f = open(py, 'r')
        scstr = f.read()
        f.close()
        scstr = re.sub('from qt import \*', 'from qt import *\nfrom SearchingCombo import *', scstr)
        scstr = re.sub('QDialog', 'QMainWindow', scstr)
        scstr = re.sub('QComboBox', 'SearchingCombo', scstr)
        scstr = re.sub('modal[^,]*,', '', scstr)
        f = open(py, 'w')
        f.write(scstr)
        f.close()

            
