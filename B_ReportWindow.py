# Form implementation generated from reading ui file 'ReportWindow.ui'
#
# Created: Sun Apr 4 17:55:22 2004
#      by: The Python User Interface Compiler (pyuic) 3.8
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_ReportWindow(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if name == None:
            self.setName('B_ReportWindow')

        self.resize(573,480)
        self.setCaption(self.tr("B_ReportWindow"))

        self.ReportText = QTextBrowser(self,'ReportText')
        self.ReportText.setGeometry(QRect(10,9,569,430))

        self.PushButton1 = QPushButton(self,'PushButton1')
        self.PushButton1.setGeometry(QRect(35,447,93,26))
        self.PushButton1.setText(self.tr("Save As HTML"))

        self.PushButton1_2 = QPushButton(self,'PushButton1_2')
        self.PushButton1_2.setGeometry(QRect(149,447,93,26))
        self.PushButton1_2.setText(self.tr("Save As Text"))

        self.PushButton2 = QPushButton(self,'PushButton2')
        self.PushButton2.setGeometry(QRect(446,448,93,26))
        self.PushButton2.setText(self.tr("Close"))

        self.MMLabel = QLabel(self,'MMLabel')
        self.MMLabel.setGeometry(QRect(298,451,91,16))
        self.MMLabel.setText(self.tr("Materials Multiplier"))

        self.MatMultiplier = QSpinBox(self,'MatMultiplier')
        self.MatMultiplier.setGeometry(QRect(256,449,37,21))
        self.MatMultiplier.setMinValue(1)
        self.MatMultiplier.setValue(1)

        self.connect(self.PushButton2,SIGNAL('clicked()'),self.closeWindow)
        self.connect(self.PushButton1,SIGNAL('clicked()'),self.saveToHTML)
        self.connect(self.PushButton1_2,SIGNAL('clicked()'),self.saveToText)
        self.connect(self.MatMultiplier,SIGNAL('valueChanged(int)'),self.matMultiplierUpdate)

    def closeWindow(self):
        print 'B_ReportWindow.closeWindow(): not implemented yet'

    def matMultiplierUpdate(self,a0):
        print 'B_ReportWindow.matMultiplierUpdate(int): not implemented yet'

    def saveToHTML(self):
        print 'B_ReportWindow.saveToHTML(): not implemented yet'

    def saveToText(self):
        print 'B_ReportWindow.saveToText(): not implemented yet'
