# Form implementation generated from reading ui file 'DisplayWindow.ui'
#
# Created: Sun Apr 4 17:55:22 2004
#      by: The Python User Interface Compiler (pyuic) 3.8
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_DisplayWindow(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if name == None:
            self.setName('B_DisplayWindow')

        self.resize(238,310)
        self.setCaption(self.tr(""))

        self.PushButton1 = QPushButton(self,'PushButton1')
        self.PushButton1.setGeometry(QRect(69,270,93,26))
        self.PushButton1.setText(self.tr("Close"))

        self.DisplayText = QListBox(self,'DisplayText')
        self.DisplayText.setGeometry(QRect(8,4,221,256))

        self.connect(self.PushButton1,SIGNAL('clicked()'),self.CloseWindow)
        self.connect(self.DisplayText,SIGNAL('clicked(QListBoxItem*)'),self.LocationClicked)

    def CloseWindow(self):
        print 'B_DisplayWindow.CloseWindow(): not implemented yet'

    def LocationClicked(self,a0):
        print 'B_DisplayWindow.LocationClicked(QListBoxItem*): not implemented yet'
