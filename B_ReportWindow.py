# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReportWindow.ui'
#
# Created: Tue Sep 27 10:37:00 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.15
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_ReportWindow(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("B_ReportWindow")



        self.ReportText = QTextBrowser(self,"ReportText")
        self.ReportText.setGeometry(QRect(10,9,569,430))

        self.PushButton1 = QPushButton(self,"PushButton1")
        self.PushButton1.setGeometry(QRect(35,447,93,26))

        self.PushButton1_2 = QPushButton(self,"PushButton1_2")
        self.PushButton1_2.setGeometry(QRect(149,447,93,26))

        self.PushButton2 = QPushButton(self,"PushButton2")
        self.PushButton2.setGeometry(QRect(446,448,93,26))

        self.MMLabel = QLabel(self,"MMLabel")
        self.MMLabel.setGeometry(QRect(298,451,91,16))

        self.MatMultiplier = QSpinBox(self,"MatMultiplier")
        self.MatMultiplier.setGeometry(QRect(256,449,37,21))
        self.MatMultiplier.setMinValue(1)
        self.MatMultiplier.setValue(1)

        self.languageChange()

        self.resize(QSize(573,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.PushButton2,SIGNAL("clicked()"),self.closeWindow)
        self.connect(self.PushButton1,SIGNAL("clicked()"),self.saveToHTML)
        self.connect(self.PushButton1_2,SIGNAL("clicked()"),self.saveToText)
        self.connect(self.MatMultiplier,SIGNAL("valueChanged(int)"),self.matMultiplierUpdate)


    def languageChange(self):
        self.setCaption(self.__tr("B_ReportWindow"))
        self.PushButton1.setText(self.__tr("Save As HTML"))
        self.PushButton1_2.setText(self.__tr("Save As Text"))
        self.PushButton2.setText(self.__tr("Close"))
        self.MMLabel.setText(self.__tr("Materials Multiplier"))


    def closeWindow(self):
        print "B_ReportWindow.closeWindow(): Not implemented yet"

    def matMultiplierUpdate(self,a0):
        print "B_ReportWindow.matMultiplierUpdate(int): Not implemented yet"

    def saveToHTML(self):
        print "B_ReportWindow.saveToHTML(): Not implemented yet"

    def saveToText(self):
        print "B_ReportWindow.saveToText(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("B_ReportWindow",s,c)
