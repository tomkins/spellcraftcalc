import os
import sys

files = (
    ('ScWindow.ui4', 'B_ScWindow.py'),
    ('CraftWindow.ui4', 'B_CraftWindow.py'),
    ('DisplayWindow.ui4', 'B_DisplayWindow.py'),
    ('ReportWindow.ui4', 'B_ReportWindow.py'),
    ('ItemLevel.ui4', 'B_ItemLevel.py'),
    ('CraftBar.ui4', 'B_CraftBar.py'),
    ('Options.ui4', 'B_Options.py'),
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
    os.system('%s -d -o %s %s' % (
              os.path.join(os.path.dirname(sys.executable),'pyuic4'), py, ui))

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
