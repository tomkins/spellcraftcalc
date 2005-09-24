# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DisplayWindow.ui'
#
# Created: Sat Sep 24 00:50:58 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.15
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_DisplayWindow(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("B_DisplayWindow")



        self.PushButton1 = QPushButton(self,"PushButton1")
        self.PushButton1.setGeometry(QRect(69,270,93,26))

        self.DisplayText = QListBox(self,"DisplayText")
        self.DisplayText.setGeometry(QRect(8,4,221,256))

        self.languageChange()

        self.resize(QSize(238,310).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.PushButton1,SIGNAL("clicked()"),self.CloseWindow)
        self.connect(self.DisplayText,SIGNAL("clicked(QListBoxItem*)"),self.LocationClicked)


    def languageChange(self):
        self.setCaption(QString.null)
        self.PushButton1.setText(self.__tr("Close"))


    def CloseWindow(self):
        print "B_DisplayWindow.CloseWindow(): Not implemented yet"

    def LocationClicked(self,a0):
        print "B_DisplayWindow.LocationClicked(QListBoxItem*): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("B_DisplayWindow",s,c)
