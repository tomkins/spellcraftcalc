# Form implementation generated from reading ui file 'Craft.ui'
#
# Created: Sun Apr 4 17:55:22 2004
#      by: The Python User Interface Compiler (pyuic) 3.8
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_CraftWindow(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if name == None:
            self.setName('B_CraftWindow')

        self.resize(523,373)
        self.setCaption(self.tr("Working Item Detail"))

        self.TextLabel8 = QLabel(self,'TextLabel8')
        self.TextLabel8.setGeometry(QRect(365,338,57,16))
        self.TextLabel8.setText(self.tr("Total Cost:"))

        self.Close = QPushButton(self,'Close')
        self.Close.setGeometry(QRect(228,336,84,29))
        self.Close.setText(self.tr("Close"))

        self.TotalCost = QLabel(self,'TotalCost')
        self.TotalCost.setGeometry(QRect(421,338,103,16))
        self.TotalCost.setText(self.tr("0c"))

        self.GroupBox1 = QGroupBox(self,'GroupBox1')
        self.GroupBox1.setGeometry(QRect(9,7,523,324))
        self.GroupBox1.setTitle(self.tr("Gems"))

        self.TextLabel1 = QLabel(self.GroupBox1,'TextLabel1')
        self.TextLabel1.setGeometry(QRect(15,20,36,16))
        self.TextLabel1.setText(self.tr("Done:"))

        self.TextLabel5 = QLabel(self.GroupBox1,'TextLabel5')
        self.TextLabel5.setGeometry(QRect(323,20,50,16))
        self.TextLabel5.setText(self.tr("Remakes:"))

        self.TextLabel6 = QLabel(self.GroupBox1,'TextLabel6')
        self.TextLabel6.setGeometry(QRect(382,20,46,16))
        self.TextLabel6.setText(self.tr("Time (m):"))

        self.TextLabel7 = QLabel(self.GroupBox1,'TextLabel7')
        self.TextLabel7.setGeometry(QRect(438,20,30,16))
        self.TextLabel7.setText(self.tr("Cost:"))

        self.Gem1Cost = QLabel(self.GroupBox1,'Gem1Cost')
        self.Gem1Cost.setGeometry(QRect(442,41,73,21))
        self.Gem1Cost.setText(self.tr("0c"))
        self.Gem1Cost.setAlignment(QLabel.AlignVCenter | QLabel.AlignLeft)

        self.Gem3Cost = QLabel(self.GroupBox1,'Gem3Cost')
        self.Gem3Cost.setGeometry(QRect(442,88,73,21))
        self.Gem3Cost.setText(self.tr("0c"))
        self.Gem3Cost.setAlignment(QLabel.AlignVCenter | QLabel.AlignLeft)

        self.Gem3Name = QLabel(self.GroupBox1,'Gem3Name')
        self.Gem3Name.setGeometry(QRect(138,88,163,21))
        self.Gem3Name.setText(self.tr("None"))

        self.Gem4Name = QLabel(self.GroupBox1,'Gem4Name')
        self.Gem4Name.setGeometry(QRect(138,112,163,21))
        self.Gem4Name.setText(self.tr("None"))

        self.Gem3Time = QLineEdit(self.GroupBox1,'Gem3Time')
        self.Gem3Time.setGeometry(QRect(382,88,47,21))
        self.Gem3Time.setText(self.tr("0"))

        self.Gem4Time = QLineEdit(self.GroupBox1,'Gem4Time')
        self.Gem4Time.setGeometry(QRect(382,111,47,21))
        self.Gem4Time.setText(self.tr("0"))

        self.TextLabel2 = QLabel(self.GroupBox1,'TextLabel2')
        self.TextLabel2.setGeometry(QRect(108,20,36,16))
        self.TextLabel2.setText(self.tr("Name:"))

        self.Gem2Done = QCheckBox(self.GroupBox1,'Gem2Done')
        self.Gem2Done.setGeometry(QRect(15,64,59,21))
        self.Gem2Done.setText(self.tr("Gem 2:"))

        self.Gem3Done = QCheckBox(self.GroupBox1,'Gem3Done')
        self.Gem3Done.setGeometry(QRect(15,88,57,21))
        self.Gem3Done.setText(self.tr("Gem 3:"))

        self.Gem4Done = QCheckBox(self.GroupBox1,'Gem4Done')
        self.Gem4Done.setGeometry(QRect(15,112,57,21))
        self.Gem4Done.setText(self.tr("Gem 4:"))

        self.Gem1Qua = QLabel(self.GroupBox1,'Gem1Qua')
        self.Gem1Qua.setGeometry(QRect(103,41,28,21))
        self.Gem1Qua.setText(self.tr("99%"))
        self.Gem1Qua.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Gem3Remakes = QSpinBox(self.GroupBox1,'Gem3Remakes')
        self.Gem3Remakes.setGeometry(QRect(321,88,54,21))

        self.Gem4Remakes = QSpinBox(self.GroupBox1,'Gem4Remakes')
        self.Gem4Remakes.setGeometry(QRect(321,112,54,21))

        self.Gem2Qua = QLabel(self.GroupBox1,'Gem2Qua')
        self.Gem2Qua.setGeometry(QRect(103,64,28,21))
        self.Gem2Qua.setText(self.tr("99%"))
        self.Gem2Qua.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Gem3Qua = QLabel(self.GroupBox1,'Gem3Qua')
        self.Gem3Qua.setGeometry(QRect(103,88,28,21))
        self.Gem3Qua.setText(self.tr("99%"))
        self.Gem3Qua.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Gem4Qua = QLabel(self.GroupBox1,'Gem4Qua')
        self.Gem4Qua.setGeometry(QRect(103,112,28,21))
        self.Gem4Qua.setText(self.tr("99%"))
        self.Gem4Qua.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.Gem1Name = QLabel(self.GroupBox1,'Gem1Name')
        self.Gem1Name.setGeometry(QRect(138,41,163,21))
        self.Gem1Name.setText(self.tr("None"))

        self.Gem2Name = QLabel(self.GroupBox1,'Gem2Name')
        self.Gem2Name.setGeometry(QRect(138,64,163,21))
        self.Gem2Name.setText(self.tr("None"))

        self.Gem1Remakes = QSpinBox(self.GroupBox1,'Gem1Remakes')
        self.Gem1Remakes.setGeometry(QRect(321,41,54,21))

        self.Gem2Remakes = QSpinBox(self.GroupBox1,'Gem2Remakes')
        self.Gem2Remakes.setGeometry(QRect(321,64,54,21))

        self.Gem1Time = QLineEdit(self.GroupBox1,'Gem1Time')
        self.Gem1Time.setGeometry(QRect(382,41,47,21))
        self.Gem1Time.setText(self.tr("0"))

        self.Gem2Time = QLineEdit(self.GroupBox1,'Gem2Time')
        self.Gem2Time.setGeometry(QRect(382,64,47,21))
        self.Gem2Time.setText(self.tr("0"))

        self.Gem2Cost = QLabel(self.GroupBox1,'Gem2Cost')
        self.Gem2Cost.setGeometry(QRect(442,64,73,21))
        self.Gem2Cost.setText(self.tr("0c"))
        self.Gem2Cost.setAlignment(QLabel.AlignVCenter | QLabel.AlignLeft)

        self.Gem4Cost = QLabel(self.GroupBox1,'Gem4Cost')
        self.Gem4Cost.setGeometry(QRect(442,112,73,21))
        self.Gem4Cost.setText(self.tr("0c"))
        self.Gem4Cost.setAlignment(QLabel.AlignVCenter | QLabel.AlignLeft)

        self.Gem1Done = QCheckBox(self.GroupBox1,'Gem1Done')
        self.Gem1Done.setGeometry(QRect(15,41,59,21))
        self.Gem1Done.setText(self.tr("Gem 1:"))

        self.GroupBox2_2 = QGroupBox(self.GroupBox1,'GroupBox2_2')
        self.GroupBox2_2.setGeometry(QRect(266,142,240,175))
        self.GroupBox2_2.setTitle(self.tr("Materials (used)"))

        self.MatsUsed = QMultiLineEdit(self.GroupBox2_2,'MatsUsed')
        self.MatsUsed.setGeometry(QRect(8,16,225,153))

        self.GroupBox2_2_2 = QGroupBox(self.GroupBox1,'GroupBox2_2_2')
        self.GroupBox2_2_2.setGeometry(QRect(13,141,240,175))
        self.GroupBox2_2_2.setTitle(self.tr("Materials (expected)"))

        self.MatsExpected = QMultiLineEdit(self.GroupBox2_2_2,'MatsExpected')
        self.MatsExpected.setGeometry(QRect(8,16,225,153))

        self.TextLabel1_2 = QLabel(self,'TextLabel1_2')
        self.TextLabel1_2.setGeometry(QRect(35,341,94,16))
        self.TextLabel1_2.setText(self.tr("Expected Multiplier"))

        self.ExpMultiplier = QSpinBox(self,'ExpMultiplier')
        self.ExpMultiplier.setGeometry(QRect(130,339,54,21))

        self.connect(self.Gem2Remakes,SIGNAL('valueChanged(int)'),self.Remake2Changed)
        self.connect(self.Gem3Remakes,SIGNAL('valueChanged(int)'),self.Remake3Changed)
        self.connect(self.Gem4Remakes,SIGNAL('valueChanged(int)'),self.Remake4Changed)
        self.connect(self.Gem1Done,SIGNAL('clicked()'),self.Gem1Clicked)
        self.connect(self.Gem2Done,SIGNAL('clicked()'),self.Gem2Clicked)
        self.connect(self.Gem3Done,SIGNAL('clicked()'),self.Gem3Clicked)
        self.connect(self.Gem4Done,SIGNAL('clicked()'),self.Gem4Clicked)
        self.connect(self.Gem1Remakes,SIGNAL('valueChanged(int)'),self.Remake1Changed)
        self.connect(self.Close,SIGNAL('clicked()'),self.CloseWindow)
        self.connect(self.ExpMultiplier,SIGNAL('valueChanged(int)'),self.computeMaterials)
        self.connect(self.Gem1Time,SIGNAL('textChanged(const QString&)'),self.Time1Changed)
        self.connect(self.Gem2Time,SIGNAL('textChanged(const QString&)'),self.Time2Changed)
        self.connect(self.Gem3Time,SIGNAL('textChanged(const QString&)'),self.Time3Changed)
        self.connect(self.Gem4Time,SIGNAL('textChanged(const QString&)'),self.Time4Changed)

    def CloseWindow(self):
        print 'B_CraftWindow.CloseWindow(): not implemented yet'

    def Gem1Clicked(self):
        print 'B_CraftWindow.Gem1Clicked(): not implemented yet'

    def Gem2Clicked(self):
        print 'B_CraftWindow.Gem2Clicked(): not implemented yet'

    def Gem3Clicked(self):
        print 'B_CraftWindow.Gem3Clicked(): not implemented yet'

    def Gem4Clicked(self):
        print 'B_CraftWindow.Gem4Clicked(): not implemented yet'

    def Remake1Changed(self,a0):
        print 'B_CraftWindow.Remake1Changed(int): not implemented yet'

    def Remake2Changed(self,a0):
        print 'B_CraftWindow.Remake2Changed(int): not implemented yet'

    def Remake3Changed(self,a0):
        print 'B_CraftWindow.Remake3Changed(int): not implemented yet'

    def Remake4Changed(self,a0):
        print 'B_CraftWindow.Remake4Changed(int): not implemented yet'

    def Time1Changed(self,a0):
        print 'B_CraftWindow.Time1Changed(const QString&): not implemented yet'

    def Time2Changed(self,a0):
        print 'B_CraftWindow.Time2Changed(const QString&): not implemented yet'

    def Time3Changed(self,a0):
        print 'B_CraftWindow.Time3Changed(const QString&): not implemented yet'

    def computeMaterials(self):
        print 'B_CraftWindow.computeMaterials(): not implemented yet'

    def Time4Changed(self,a0):
        print 'B_CraftWindow.Time4Changed(const QString&): not implemented yet'
