import os
import sys

files = (
    ('ScWindow.ui', 'B_ScWindow.py'),
    ('CraftWindow.ui', 'B_CraftWindow.py'),
    ('DisplayWindow.ui', 'B_DisplayWindow.py'),
    ('ReportWindow.ui', 'B_ReportWindow.py'),
    ('ItemLevel.ui', 'B_ItemLevel.py'),
    ('CraftBar.ui', 'B_CraftBar.py'),
    ('Options.ui', 'B_Options.py'),
)

for ui, py in files:
    try:
        if os.stat(ui).st_mtime < os.stat(py).st_mtime:
            continue
    except:
        # We are happy to continue if a file is not found,
        # as we will error on a missing input file, and go
        # quietly on if the output file was missing
        pass
    os.system('%s -o %s %s' % (
              os.path.join(os.path.dirname(sys.executable),'pyuic'), py, ui))

    # Make this Win32 text
    if os.name == 'nt':
        f = open(py, 'r')
        scstr = f.read()
        f.close()
        f = open(py, 'w')
        f.write(scstr)
        f.close()
        del scstr

    sys.stdout.write("Generated %s from %s\n" % (py, ui))
