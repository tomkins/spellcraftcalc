# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Options.ui'
#
# Created: Wed Sep 28 18:57:26 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.15
#
# WARNING! All changes made in this file will be lost!


from qt import *


class B_Options(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("B_Options")



        self.OK = QPushButton(self,"OK")
        self.OK.setGeometry(QRect(52,265,93,26))

        self.Cancel = QPushButton(self,"Cancel")
        self.Cancel.setGeometry(QRect(207,265,93,26))

        self.Tab = QTabWidget(self,"Tab")
        self.Tab.setEnabled(1)
        self.Tab.setGeometry(QRect(10,6,353,259))

        self.General = QWidget(self.Tab,"General")

        self.TextLabel2 = QLabel(self.General,"TextLabel2")
        self.TextLabel2.setGeometry(QRect(19,17,36,22))

        self.Realm = QComboBox(0,self.General,"Realm")
        self.Realm.setGeometry(QRect(65,17,81,22))

        self.TextLabel1 = QLabel(self.General,"TextLabel1")
        self.TextLabel1.setGeometry(QRect(185,17,61,22))

        self.Skill = QComboBox(0,self.General,"Skill")
        self.Skill.setGeometry(QRect(256,17,81,22))

        self.ShowDoneGems = QCheckBox(self.General,"ShowDoneGems")
        self.ShowDoneGems.setGeometry(QRect(18,100,250,17))

        self.IncludeRR = QCheckBox(self.General,"IncludeRR")
        self.IncludeRR.setGeometry(QRect(18,125,250,17))
        self.IncludeRR.setChecked(1)

        self.HideNonClassSkills = QCheckBox(self.General,"HideNonClassSkills")
        self.HideNonClassSkills.setGeometry(QRect(18,150,250,17))
        self.HideNonClassSkills.setChecked(1)

        self.Coop = QCheckBox(self.General,"Coop")
        self.Coop.setGeometry(QRect(18,175,250,17))

        self.TextLabel2_5 = QLabel(self.General,"TextLabel2_5")
        self.TextLabel2_5.setGeometry(QRect(40,192,250,14))
        self.Tab.insertTab(self.General,QString.fromLatin1(""))

        self.Notes = QWidget(self.Tab,"Notes")

        self.TextLabel2_2 = QLabel(self.Notes,"TextLabel2_2")
        self.TextLabel2_2.setGeometry(QRect(12,6,82,16))

        self.NoteText = QMultiLineEdit(self.Notes,"NoteText")
        self.NoteText.setGeometry(QRect(13,26,321,154))
        self.Tab.insertTab(self.Notes,QString.fromLatin1(""))

        self.Price = QWidget(self.Tab,"Price")

        self.GroupBox1 = QGroupBox(self.Price,"GroupBox1")
        self.GroupBox1.setGeometry(QRect(4,1,95,115))

        self.TextLabel1_2 = QLabel(self.GroupBox1,"TextLabel1_2")
        self.TextLabel1_2.setGeometry(QRect(5,15,28,16))
        self.TextLabel1_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel1_2_3 = QLabel(self.GroupBox1,"TextLabel1_2_3")
        self.TextLabel1_2_3.setGeometry(QRect(2,71,31,16))
        self.TextLabel1_2_3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel1_2_2 = QLabel(self.GroupBox1,"TextLabel1_2_2")
        self.TextLabel1_2_2.setGeometry(QRect(8,42,24,16))
        self.TextLabel1_2_2.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel2_3 = QLabel(self.GroupBox1,"TextLabel2_3")
        self.TextLabel2_3.setGeometry(QRect(26,94,43,16))

        self.PPGem = QLineEdit(self.GroupBox1,"PPGem")
        self.PPGem.setGeometry(QRect(37,14,52,22))

        self.PPItem = QLineEdit(self.GroupBox1,"PPItem")
        self.PPItem.setGeometry(QRect(37,41,52,22))

        self.PPOrder = QLineEdit(self.GroupBox1,"PPOrder")
        self.PPOrder.setGeometry(QRect(37,69,52,22))

        self.GroupBox2 = QGroupBox(self.Price,"GroupBox2")
        self.GroupBox2.setGeometry(QRect(101,1,109,115))

        self.TextLabel3 = QLabel(self.GroupBox2,"TextLabel3")
        self.TextLabel3.setGeometry(QRect(4,17,41,13))
        self.TextLabel3.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel4 = QLabel(self.GroupBox2,"TextLabel4")
        self.TextLabel4.setGeometry(QRect(6,44,36,13))
        self.TextLabel4.setAlignment(QLabel.AlignVCenter | QLabel.AlignRight)

        self.TextLabel5 = QLabel(self.GroupBox2,"TextLabel5")
        self.TextLabel5.setGeometry(QRect(91,17,16,16))

        self.TextLabel6 = QLabel(self.GroupBox2,"TextLabel6")
        self.TextLabel6.setGeometry(QRect(9,94,92,16))

        self.QualLevel = QComboBox(0,self.GroupBox2,"QualLevel")
        self.QualLevel.setGeometry(QRect(48,41,50,22))

        self.QualMarkup = QLineEdit(self.GroupBox2,"QualMarkup")
        self.QualMarkup.setGeometry(QRect(49,14,40,22))

        self.QualInclude = QCheckBox(self.GroupBox2,"QualInclude")
        self.QualInclude.setGeometry(QRect(8,72,59,17))

        self.GroupBox3 = QGroupBox(self.Price,"GroupBox3")
        self.GroupBox3.setGeometry(QRect(214,1,131,115))

        self.TextLabel7 = QLabel(self.GroupBox3,"TextLabel7")
        self.TextLabel7.setGeometry(QRect(60,16,44,16))

        self.TextLabel8 = QLabel(self.GroupBox3,"TextLabel8")
        self.TextLabel8.setGeometry(QRect(59,43,63,16))

        self.TextLabel9 = QLabel(self.GroupBox3,"TextLabel9")
        self.TextLabel9.setGeometry(QRect(60,71,66,16))

        self.TextLabel10 = QLabel(self.GroupBox3,"TextLabel10")
        self.TextLabel10.setGeometry(QRect(77,93,47,16))

        self.PPImbue = QLineEdit(self.GroupBox3,"PPImbue")
        self.PPImbue.setGeometry(QRect(5,41,50,22))

        self.PPInclude = QCheckBox(self.GroupBox3,"PPInclude")
        self.PPInclude.setGeometry(QRect(5,94,59,17))

        self.PPLevel = QLineEdit(self.GroupBox3,"PPLevel")
        self.PPLevel.setGeometry(QRect(5,14,50,22))

        self.PPOC = QLineEdit(self.GroupBox3,"PPOC")
        self.PPOC.setGeometry(QRect(5,69,50,22))

        self.GroupBox4 = QGroupBox(self.Price,"GroupBox4")
        self.GroupBox4.setGeometry(QRect(4,119,98,65))

        self.TextLabel11 = QLabel(self.GroupBox4,"TextLabel11")
        self.TextLabel11.setGeometry(QRect(59,19,16,16))

        self.TextLabel12 = QLabel(self.GroupBox4,"TextLabel12")
        self.TextLabel12.setGeometry(QRect(5,43,90,16))

        self.GenMarkup = QLineEdit(self.GroupBox4,"GenMarkup")
        self.GenMarkup.setGeometry(QRect(8,16,46,22))

        self.GroupBox5 = QGroupBox(self.Price,"GroupBox5")
        self.GroupBox5.setGeometry(QRect(106,120,166,64))

        self.TextLabel13 = QLabel(self.GroupBox5,"TextLabel13")
        self.TextLabel13.setGeometry(QRect(7,17,25,16))

        self.TextLabel14 = QLabel(self.GroupBox5,"TextLabel14")
        self.TextLabel14.setGeometry(QRect(85,17,31,16))

        self.TextLabel15 = QLabel(self.GroupBox5,"TextLabel15")
        self.TextLabel15.setGeometry(QRect(99,42,51,16))

        self.Tier = QComboBox(0,self.GroupBox5,"Tier")
        self.Tier.setGeometry(QRect(32,15,40,22))

        self.TierPrice = QLineEdit(self.GroupBox5,"TierPrice")
        self.TierPrice.setGeometry(QRect(118,15,42,22))

        self.TierInclude = QCheckBox(self.GroupBox5,"TierInclude")
        self.TierInclude.setGeometry(QRect(6,42,59,17))

        self.GroupBox6 = QGroupBox(self.Price,"GroupBox6")
        self.GroupBox6.setGeometry(QRect(274,120,69,64))

        self.HourInclude = QCheckBox(self.GroupBox6,"HourInclude")
        self.HourInclude.setGeometry(QRect(4,42,59,17))

        self.HourPrice = QLineEdit(self.GroupBox6,"HourPrice")
        self.HourPrice.setGeometry(QRect(4,15,58,22))

        self.TextLabel2_4 = QLabel(self.Price,"TextLabel2_4")
        self.TextLabel2_4.setGeometry(QRect(44,209,276,16))

        self.CostInPrice = QCheckBox(self.Price,"CostInPrice")
        self.CostInPrice.setGeometry(QRect(112,189,119,17))
        self.CostInPrice.setChecked(1)
        self.Tab.insertTab(self.Price,QString.fromLatin1(""))

        self.languageChange()

        self.resize(QSize(364,295).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.OK,SIGNAL("clicked()"),self.OK_pressed)
        self.connect(self.Cancel,SIGNAL("clicked()"),self.Cancel_pressed)
        self.connect(self.Tier,SIGNAL("activated(const QString&)"),self.TierMarkupChanged)
        self.connect(self.QualLevel,SIGNAL("activated(const QString&)"),self.QualMarkupChanged)
        self.connect(self.QualMarkup,SIGNAL("textChanged(const QString&)"),self.QualMarkupSet)
        self.connect(self.TierPrice,SIGNAL("textChanged(const QString&)"),self.TierMarkupSet)


    def languageChange(self):
        self.setCaption(self.__tr("Options"))
        self.OK.setText(self.__tr("OK"))
        self.Cancel.setText(self.__tr("Cancel"))
        self.TextLabel2.setText(self.__tr("Realm:"))
        self.Realm.clear()
        self.Realm.insertItem(self.__tr("Albion"))
        self.Realm.insertItem(self.__tr("Hibernia"))
        self.Realm.insertItem(self.__tr("Midgard"))
        self.TextLabel1.setText(self.__tr("Crafter Skill:"))
        self.ShowDoneGems.setText(self.__tr("\"Done\" Gems do not show up in Materials List"))
        self.IncludeRR.setText(self.__tr("Include Racial Resists in Totals"))
        self.HideNonClassSkills.setText(self.__tr("Hide Skills not usable by this Class"))
        self.Coop.setText(self.__tr("Co-op / PvP Server"))
        self.TextLabel2_5.setText(self.__tr("(Lets you access items from all realms)"))
        self.Tab.changeTab(self.General,self.__tr("General"))
        self.TextLabel2_2.setText(self.__tr("Template Notes:"))
        self.Tab.changeTab(self.Notes,self.__tr("Notes"))
        self.GroupBox1.setTitle(self.__tr("Price per"))
        self.TextLabel1_2.setText(self.__tr("Gem:"))
        self.TextLabel1_2_3.setText(self.__tr("Order:"))
        self.TextLabel1_2_2.setText(self.__tr("Item:"))
        self.TextLabel2_3.setText(self.__tr("(cost+ X)"))
        self.PPGem.setText(self.__tr("0"))
        self.PPItem.setText(self.__tr("0"))
        self.PPOrder.setText(self.__tr("0"))
        self.GroupBox2.setTitle(self.__tr("Gem qual markup"))
        self.TextLabel3.setText(self.__tr("Markup:"))
        self.TextLabel4.setText(self.__tr("Quality:"))
        self.TextLabel5.setText(self.__tr("%"))
        self.TextLabel6.setText(self.__tr("(cost + (cost * X%))"))
        self.QualLevel.clear()
        self.QualLevel.insertItem(self.__tr("94"))
        self.QualLevel.insertItem(self.__tr("95"))
        self.QualLevel.insertItem(self.__tr("96"))
        self.QualLevel.insertItem(self.__tr("97"))
        self.QualLevel.insertItem(self.__tr("98"))
        self.QualLevel.insertItem(self.__tr("99"))
        self.QualLevel.insertItem(self.__tr("100"))
        self.QualMarkup.setText(self.__tr("0"))
        self.QualInclude.setText(self.__tr("Include"))
        self.GroupBox3.setTitle(self.__tr("Price per lvl/point"))
        self.TextLabel7.setText(self.__tr("per level"))
        self.TextLabel8.setText(self.__tr("per imbue pt."))
        self.TextLabel9.setText(self.__tr("per O/C pt."))
        self.TextLabel10.setText(self.__tr("(cost + X)"))
        self.PPImbue.setText(self.__tr("0"))
        self.PPInclude.setText(self.__tr("Include"))
        self.PPLevel.setText(self.__tr("0"))
        self.PPOC.setText(self.__tr("0"))
        self.GroupBox4.setTitle(self.__tr("General Markup"))
        self.TextLabel11.setText(self.__tr("%"))
        self.TextLabel12.setText(self.__tr("(cost + (cost * X%))"))
        self.GenMarkup.setText(self.__tr("50"))
        self.GroupBox5.setTitle(self.__tr("Price by gem tier"))
        self.TextLabel13.setText(self.__tr("Tier:"))
        self.TextLabel14.setText(self.__tr("Price:"))
        self.TextLabel15.setText(self.__tr("(cost + X)"))
        self.Tier.clear()
        self.Tier.insertItem(self.__tr("1"))
        self.Tier.insertItem(self.__tr("2"))
        self.Tier.insertItem(self.__tr("3"))
        self.Tier.insertItem(self.__tr("4"))
        self.Tier.insertItem(self.__tr("5"))
        self.Tier.insertItem(self.__tr("6"))
        self.Tier.insertItem(self.__tr("7"))
        self.Tier.insertItem(self.__tr("8"))
        self.Tier.insertItem(self.__tr("9"))
        self.Tier.insertItem(self.__tr("10"))
        self.TierPrice.setText(self.__tr("0"))
        self.TierInclude.setText(self.__tr("Include"))
        self.GroupBox6.setTitle(self.__tr("Per hour"))
        self.HourInclude.setText(self.__tr("Include"))
        self.HourPrice.setText(self.__tr("0"))
        self.TextLabel2_4.setText(self.__tr("All numbers (except percentages) are in amounts of Gold."))
        self.CostInPrice.setText(self.__tr("Include cost in price"))
        self.Tab.changeTab(self.Price,self.__tr("Price"))


    def Cancel_pressed(self):
        print "B_Options.Cancel_pressed(): Not implemented yet"

    def OK_pressed(self):
        print "B_Options.OK_pressed(): Not implemented yet"

    def QualMarkupChanged(self,a0):
        print "B_Options.QualMarkupChanged(const QString&): Not implemented yet"

    def QualMarkupSet(self,a0):
        print "B_Options.QualMarkupSet(const QString&): Not implemented yet"

    def TierMarkupChanged(self,a0):
        print "B_Options.TierMarkupChanged(const QString&): Not implemented yet"

    def TierMarkupSet(self,a0):
        print "B_Options.TierMarkupSet(const QString&): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("B_Options",s,c)
