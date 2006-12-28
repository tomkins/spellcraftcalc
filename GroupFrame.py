from PyQt4.QtGui import QFrame, QPainter, QStyle, QStyleOptionFrame

class GroupFrame(QFrame):
    def __init__(self, parent = None):
        QFrame.__init__(self, parent)

    def paintEvent(self, pevent):
        painter = QPainter(self)
        groupframe = QStyleOptionFrame()
        groupframe.init(self);
        self.style().drawPrimitive(QStyle.PE_FrameGroupBox,
                                   groupframe, painter, self)

