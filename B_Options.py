# Form implementation generated from reading ui file 'Options.ui'
#
# Created: Tue Mar 8 21:25:43 2005
#      by: The Python User Interface Compiler (pyuic) 3.8
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_Options(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if name == None:
            self.setName('B_Options')

        self.resize(364,295)
        self.setCaption(self.tr("Options"))

        self.Cancel = QPushButton(self,'Cancel')
        self.Cancel.setGeometry(QRect(207,265,93,26))
        self.Cancel.setText(self.tr("Cancel"))

        self.OK = QPushButton(self,'OK')
        self.OK.setGeometry(QRect(52,265,93,26))
        self.OK.setText(self.tr("OK"))

        self.Tab = QTabWidget(self,'Tab')
        self.Tab.setEnabled(1)
        self.Tab.setGeometry(QRect(10,6,353,259))

        self.General = QWidget(self.Tab,'General')

        self.TextLabel1 = QLabel(self.General,'TextLabel1')
        self.TextLabel1.setGeometry(QRect(17,19,61,16))
        self.TextLabel1.setText(self.tr("Crafter Skill:"))

        self.TextLabel2 = QLabel(self.General,'TextLabel2')
        self.TextLabel2.setGeometry(QRect(36,56,36,16))
        self.TextLabel2.setText(self.tr("Realm:"))

        self.Skill = QComboBox(0,self.General,'Skill')
        self.Skill.setGeometry(QRect(83,17,81,22))

        self.Realm = QComboBox(0,self.General,'Realm')
        self.Realm.insertItem(self.tr("Albion"))
        self.Realm.insertItem(self.tr("Hibernia"))
        self.Realm.insertItem(self.tr("Midgard"))
        self.Realm.setGeometry(QRect(83,55,81,22))

        self.ShowDoneGems = QCheckBox(self.General,'ShowDoneGems')
        self.ShowDoneGems.setGeometry(QRect(18,100,250,17))
        self.ShowDoneGems.setText(self.tr("\"Done\" Gems do not show up in Materials List"))

        self.IncludeRR = QCheckBox(self.General,'IncludeRR')
        self.IncludeRR.setGeometry(QRect(18,125,250,17))
        self.IncludeRR.setText(self.tr("Include Racial Resists in Totals"))
        self.IncludeRR.setChecked(1)

        self.HideNonClassSkills = QCheckBox(self.General,'HideNonClassSkills')
        self.HideNonClassSkills.setGeometry(QRect(18,150,250,17))
        self.HideNonClassSkills.setText(self.tr("Hide Skills not usable by this Class"))
        self.HideNonClassSkills.setChecked(1)

        self.Coop = QCheckBox(self.General,'Coop')
        self.Coop.setGeometry(QRect(18,175,250,17))
        self.Coop.setText(self.tr("Co-op / PvP Server"))

        self.TextLabel2_5 = QLabel(self.General,'TextLabel2_5')
        self.TextLabel2_5.setGeometry(QRect(40,192,250,14))
        self.TextLabel2_5.setText(self.tr("(Lets you access items from all realms)"))
        self.Tab.insertTab(self.General,self.tr("General"))

        self.Notes = QWidget(self.Tab,'Notes')

        self.TextLabel2_2 = QLabel(self.Notes,'TextLabel2_2')
        self.TextLabel2_2.setGeometry(QRect(12,6,82,16))
        self.TextLabel2_2.setText(self.tr("Template Notes:"))

        self.NoteText = QMultiLineEdit(self.Notes,'NoteText')
        self.NoteText.setGeometry(QRect(13,26,321,154))
        self.Tab.insertTab(self.Notes,self.tr("Notes"))

        self.Price = QWidget(self.Tab,'Price')

        self.GroupBox1 = QGroupBox(self.Price,'GroupBox1')
        self.GroupBox1.setGeometry(QRect(4,1,95,115))
        self.GroupBox1.setTitle(self.tr("Price per"))

        self.TextLabel1_2 = QLabel(self.GroupBox1,'TextLabel1_2')
        self.TextLabel1_2.setGeometry(QRect(5,15,28,16))
        self.TextLabel1_2.setText(self.tr("Gem:"))
        self.TextLabel1_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel1_2_3 = QLabel(self.GroupBox1,'TextLabel1_2_3')
        self.TextLabel1_2_3.setGeometry(QRect(2,71,31,16))
        self.TextLabel1_2_3.setText(self.tr("Order:"))
        self.TextLabel1_2_3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel1_2_2 = QLabel(self.GroupBox1,'TextLabel1_2_2')
        self.TextLabel1_2_2.setGeometry(QRect(8,42,24,16))
        self.TextLabel1_2_2.setText(self.tr("Item:"))
        self.TextLabel1_2_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel2_3 = QLabel(self.GroupBox1,'TextLabel2_3')
        self.TextLabel2_3.setGeometry(QRect(26,94,43,16))
        self.TextLabel2_3.setText(self.tr("(cost+ X)"))

        self.PPGem = QLineEdit(self.GroupBox1,'PPGem')
        self.PPGem.setGeometry(QRect(37,14,52,22))
        self.PPGem.setText(self.tr("0"))

        self.PPItem = QLineEdit(self.GroupBox1,'PPItem')
        self.PPItem.setGeometry(QRect(37,41,52,22))
        self.PPItem.setText(self.tr("0"))

        self.PPOrder = QLineEdit(self.GroupBox1,'PPOrder')
        self.PPOrder.setGeometry(QRect(37,69,52,22))
        self.PPOrder.setText(self.tr("0"))

        self.GroupBox2 = QGroupBox(self.Price,'GroupBox2')
        self.GroupBox2.setGeometry(QRect(101,1,109,115))
        self.GroupBox2.setTitle(self.tr("Gem qual markup"))

        self.TextLabel3 = QLabel(self.GroupBox2,'TextLabel3')
        self.TextLabel3.setGeometry(QRect(4,17,41,13))
        self.TextLabel3.setText(self.tr("Markup:"))
        self.TextLabel3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel4 = QLabel(self.GroupBox2,'TextLabel4')
        self.TextLabel4.setGeometry(QRect(6,44,36,13))
        self.TextLabel4.setText(self.tr("Quality:"))
        self.TextLabel4.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel5 = QLabel(self.GroupBox2,'TextLabel5')
        self.TextLabel5.setGeometry(QRect(91,17,16,16))
        self.TextLabel5.setText(self.tr("%"))

        self.TextLabel6 = QLabel(self.GroupBox2,'TextLabel6')
        self.TextLabel6.setGeometry(QRect(9,94,92,16))
        self.TextLabel6.setText(self.tr("(cost + (cost * X%))"))

        self.QualLevel = QComboBox(0,self.GroupBox2,'QualLevel')
        self.QualLevel.insertItem(self.tr("94"))
        self.QualLevel.insertItem(self.tr("95"))
        self.QualLevel.insertItem(self.tr("96"))
        self.QualLevel.insertItem(self.tr("97"))
        self.QualLevel.insertItem(self.tr("98"))
        self.QualLevel.insertItem(self.tr("99"))
        self.QualLevel.insertItem(self.tr("100"))
        self.QualLevel.setGeometry(QRect(48,41,50,22))

        self.QualMarkup = QLineEdit(self.GroupBox2,'QualMarkup')
        self.QualMarkup.setGeometry(QRect(49,14,40,22))
        self.QualMarkup.setText(self.tr("0"))

        self.QualInclude = QCheckBox(self.GroupBox2,'QualInclude')
        self.QualInclude.setGeometry(QRect(8,72,59,17))
        self.QualInclude.setText(self.tr("Include"))

        self.GroupBox3 = QGroupBox(self.Price,'GroupBox3')
        self.GroupBox3.setGeometry(QRect(214,1,131,115))
        self.GroupBox3.setTitle(self.tr("Price per lvl/point"))

        self.TextLabel7 = QLabel(self.GroupBox3,'TextLabel7')
        self.TextLabel7.setGeometry(QRect(60,16,44,16))
        self.TextLabel7.setText(self.tr("per level"))

        self.TextLabel8 = QLabel(self.GroupBox3,'TextLabel8')
        self.TextLabel8.setGeometry(QRect(59,43,63,16))
        self.TextLabel8.setText(self.tr("per imbue pt."))

        self.TextLabel9 = QLabel(self.GroupBox3,'TextLabel9')
        self.TextLabel9.setGeometry(QRect(60,71,66,16))
        self.TextLabel9.setText(self.tr("per O/C pt."))

        self.TextLabel10 = QLabel(self.GroupBox3,'TextLabel10')
        self.TextLabel10.setGeometry(QRect(77,93,47,16))
        self.TextLabel10.setText(self.tr("(cost + X)"))

        self.PPImbue = QLineEdit(self.GroupBox3,'PPImbue')
        self.PPImbue.setGeometry(QRect(5,41,50,22))
        self.PPImbue.setText(self.tr("0"))

        self.PPInclude = QCheckBox(self.GroupBox3,'PPInclude')
        self.PPInclude.setGeometry(QRect(5,94,59,17))
        self.PPInclude.setText(self.tr("Include"))

        self.PPLevel = QLineEdit(self.GroupBox3,'PPLevel')
        self.PPLevel.setGeometry(QRect(5,14,50,22))
        self.PPLevel.setText(self.tr("0"))

        self.PPOC = QLineEdit(self.GroupBox3,'PPOC')
        self.PPOC.setGeometry(QRect(5,69,50,22))
        self.PPOC.setText(self.tr("0"))

        self.GroupBox4 = QGroupBox(self.Price,'GroupBox4')
        self.GroupBox4.setGeometry(QRect(4,119,98,65))
        self.GroupBox4.setTitle(self.tr("General Markup"))

        self.TextLabel11 = QLabel(self.GroupBox4,'TextLabel11')
        self.TextLabel11.setGeometry(QRect(59,19,16,16))
        self.TextLabel11.setText(self.tr("%"))

        self.TextLabel12 = QLabel(self.GroupBox4,'TextLabel12')
        self.TextLabel12.setGeometry(QRect(5,43,90,16))
        self.TextLabel12.setText(self.tr("(cost + (cost * X%))"))

        self.GenMarkup = QLineEdit(self.GroupBox4,'GenMarkup')
        self.GenMarkup.setGeometry(QRect(8,16,46,22))
        self.GenMarkup.setText(self.tr("50"))

        self.GroupBox5 = QGroupBox(self.Price,'GroupBox5')
        self.GroupBox5.setGeometry(QRect(106,120,166,64))
        self.GroupBox5.setTitle(self.tr("Price by gem tier"))

        self.TextLabel13 = QLabel(self.GroupBox5,'TextLabel13')
        self.TextLabel13.setGeometry(QRect(7,17,25,16))
        self.TextLabel13.setText(self.tr("Tier:"))

        self.TextLabel14 = QLabel(self.GroupBox5,'TextLabel14')
        self.TextLabel14.setGeometry(QRect(85,17,31,16))
        self.TextLabel14.setText(self.tr("Price:"))

        self.TextLabel15 = QLabel(self.GroupBox5,'TextLabel15')
        self.TextLabel15.setGeometry(QRect(99,42,51,16))
        self.TextLabel15.setText(self.tr("(cost + X)"))

        self.Tier = QComboBox(0,self.GroupBox5,'Tier')
        self.Tier.insertItem(self.tr("1"))
        self.Tier.insertItem(self.tr("2"))
        self.Tier.insertItem(self.tr("3"))
        self.Tier.insertItem(self.tr("4"))
        self.Tier.insertItem(self.tr("5"))
        self.Tier.insertItem(self.tr("6"))
        self.Tier.insertItem(self.tr("7"))
        self.Tier.insertItem(self.tr("8"))
        self.Tier.insertItem(self.tr("9"))
        self.Tier.insertItem(self.tr("10"))
        self.Tier.setGeometry(QRect(32,15,40,22))

        self.TierPrice = QLineEdit(self.GroupBox5,'TierPrice')
        self.TierPrice.setGeometry(QRect(118,15,42,22))
        self.TierPrice.setText(self.tr("0"))

        self.TierInclude = QCheckBox(self.GroupBox5,'TierInclude')
        self.TierInclude.setGeometry(QRect(6,42,59,17))
        self.TierInclude.setText(self.tr("Include"))

        self.GroupBox6 = QGroupBox(self.Price,'GroupBox6')
        self.GroupBox6.setGeometry(QRect(274,120,69,64))
        self.GroupBox6.setTitle(self.tr("Per hour"))

        self.HourInclude = QCheckBox(self.GroupBox6,'HourInclude')
        self.HourInclude.setGeometry(QRect(4,42,59,17))
        self.HourInclude.setText(self.tr("Include"))

        self.HourPrice = QLineEdit(self.GroupBox6,'HourPrice')
        self.HourPrice.setGeometry(QRect(4,15,58,22))
        self.HourPrice.setText(self.tr("0"))

        self.TextLabel2_4 = QLabel(self.Price,'TextLabel2_4')
        self.TextLabel2_4.setGeometry(QRect(44,209,276,16))
        self.TextLabel2_4.setText(self.tr("All numbers (except percentages) are in amounts of Gold."))

        self.CostInPrice = QCheckBox(self.Price,'CostInPrice')
        self.CostInPrice.setGeometry(QRect(112,189,119,17))
        self.CostInPrice.setText(self.tr("Include cost in price"))
        self.CostInPrice.setChecked(1)
        self.Tab.insertTab(self.Price,self.tr("Price"))

        self.connect(self.OK,SIGNAL('clicked()'),self.OK_pressed)
        self.connect(self.Cancel,SIGNAL('clicked()'),self.Cancel_pressed)
        self.connect(self.Tier,SIGNAL('activated(const QString&)'),self.TierMarkupChanged)
        self.connect(self.QualLevel,SIGNAL('activated(const QString&)'),self.QualMarkupChanged)
        self.connect(self.QualMarkup,SIGNAL('textChanged(const QString&)'),self.QualMarkupSet)
        self.connect(self.TierPrice,SIGNAL('textChanged(const QString&)'),self.TierMarkupSet)

    def Cancel_pressed(self):
        print 'B_Options.Cancel_pressed(): not implemented yet'

    def OK_pressed(self):
        print 'B_Options.OK_pressed(): not implemented yet'

    def QualMarkupChanged(self,a0):
        print 'B_Options.QualMarkupChanged(const QString&): not implemented yet'

    def QualMarkupSet(self,a0):
        print 'B_Options.QualMarkupSet(const QString&): not implemented yet'

    def TierMarkupChanged(self,a0):
        print 'B_Options.TierMarkupChanged(const QString&): not implemented yet'

    def TierMarkupSet(self,a0):
        print 'B_Options.TierMarkupSet(const QString&): not implemented yet'
