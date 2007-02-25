from PyQt4.QtGui import QFrame, QPainter, QStyle, QPalette
from PyQt4.QtGui import QStyleOptionTabWidgetFrame, QStyleOptionFrameV2

class GroupFrame(QFrame):
    def __init__(self, parent = None):
        QFrame.__init__(self, parent)

    def paintEvent(self, pevent):
        painter = QPainter(self)
        if str(self.style().objectName()).lower() == "windowsxp":
          # it sucks, but windowsxp in classic view displays no groupframe
          styleoptions = QStyleOptionTabWidgetFrame()
          frame = QStyle.PE_FrameTabWidget
        else:
          styleoptions = QStyleOptionFrameV2()
          frame = QStyle.PE_FrameGroupBox
        styleoptions.initFrom(self);
        self.style().drawPrimitive(frame, styleoptions, painter, self)

