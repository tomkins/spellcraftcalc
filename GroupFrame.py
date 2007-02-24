from PyQt4.QtGui import QFrame, QPainter, QStyle
from PyQt4.QtGui import QStyleOptionFrame, QStyleOptionFrameV2

class GroupFrame(QFrame):
    def __init__(self, parent = None):
        QFrame.__init__(self, parent)

    def paintEvent(self, pevent):
        painter = QPainter(self)
        styleoptions = QStyleOptionFrameV2()
        styleoptions.init(self);
        #styleoptions.FrameFeatures = QStyleOptionFrameV2.None
        if str(self.style().objectName()).lower() == "windowsxp":
          # it sucks, but windowsxp in classic view displays no groupframe
          frame = QStyle.PE_FrameTabWidget
        else:
          frame = QStyle.PE_FrameGroupBox
        self.style().drawPrimitive(frame, styleoptions, painter, self)

