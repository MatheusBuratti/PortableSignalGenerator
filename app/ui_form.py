# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(849, 648)
        icon = QIcon()
        icon.addFile(u"signal-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        Widget.setStyleSheet(u"font: 700 12pt \"Alef\";\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.Square = QWidget()
        self.Square.setObjectName(u"Square")
        self.label_5 = QLabel(self.Square)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 831, 67))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px;\n"
"height: 50px;")
        self.verticalLayoutWidget = QWidget(self.Square)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 80, 831, 471))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.line_6 = QFrame(self.verticalLayoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.frequencyInput_sq = QLineEdit(self.verticalLayoutWidget)
        self.frequencyInput_sq.setObjectName(u"frequencyInput_sq")

        self.horizontalLayout_2.addWidget(self.frequencyInput_sq)

        self.radioHz_sq = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_6 = QButtonGroup(Widget)
        self.buttonGroup_6.setObjectName(u"buttonGroup_6")
        self.buttonGroup_6.addButton(self.radioHz_sq)
        self.radioHz_sq.setObjectName(u"radioHz_sq")
        self.radioHz_sq.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioHz_sq)

        self.radioKHz_sq = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_6.addButton(self.radioKHz_sq)
        self.radioKHz_sq.setObjectName(u"radioKHz_sq")

        self.horizontalLayout_2.addWidget(self.radioKHz_sq)

        self.radioMHz_sq = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_6.addButton(self.radioMHz_sq)
        self.radioMHz_sq.setObjectName(u"radioMHz_sq")
        self.radioMHz_sq.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.radioMHz_sq)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.amplitudeInput_sq = QLineEdit(self.verticalLayoutWidget)
        self.amplitudeInput_sq.setObjectName(u"amplitudeInput_sq")

        self.horizontalLayout.addWidget(self.amplitudeInput_sq)

        self.radiomV_sq = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_8 = QButtonGroup(Widget)
        self.buttonGroup_8.setObjectName(u"buttonGroup_8")
        self.buttonGroup_8.addButton(self.radiomV_sq)
        self.radiomV_sq.setObjectName(u"radiomV_sq")
        self.radiomV_sq.setChecked(True)

        self.horizontalLayout.addWidget(self.radiomV_sq)

        self.radioV_sq = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_8.addButton(self.radioV_sq)
        self.radioV_sq.setObjectName(u"radioV_sq")

        self.horizontalLayout.addWidget(self.radioV_sq)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_3 = QFrame(self.verticalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.offSetInput_sq = QLineEdit(self.verticalLayoutWidget)
        self.offSetInput_sq.setObjectName(u"offSetInput_sq")

        self.horizontalLayout_4.addWidget(self.offSetInput_sq)

        self.offSetRadiomV_sq = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_7 = QButtonGroup(Widget)
        self.buttonGroup_7.setObjectName(u"buttonGroup_7")
        self.buttonGroup_7.addButton(self.offSetRadiomV_sq)
        self.offSetRadiomV_sq.setObjectName(u"offSetRadiomV_sq")
        self.offSetRadiomV_sq.setChecked(True)

        self.horizontalLayout_4.addWidget(self.offSetRadiomV_sq)

        self.offSetRadioV_sq = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_7.addButton(self.offSetRadioV_sq)
        self.offSetRadioV_sq.setObjectName(u"offSetRadioV_sq")

        self.horizontalLayout_4.addWidget(self.offSetRadioV_sq)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line_4 = QFrame(self.verticalLayoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.dutyInput_sq = QLineEdit(self.verticalLayoutWidget)
        self.dutyInput_sq.setObjectName(u"dutyInput_sq")

        self.horizontalLayout_5.addWidget(self.dutyInput_sq)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line_5 = QFrame(self.verticalLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.generateSignalButton_sq = QPushButton(self.verticalLayoutWidget)
        self.generateSignalButton_sq.setObjectName(u"generateSignalButton_sq")
        self.generateSignalButton_sq.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.verticalLayout.addWidget(self.generateSignalButton_sq)

        self.tabWidget.addTab(self.Square, "")
        self.Seno = QWidget()
        self.Seno.setObjectName(u"Seno")
        self.label_6 = QLabel(self.Seno)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 821, 67))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px;\n"
"height: 50px;")
        self.verticalLayoutWidget_2 = QWidget(self.Seno)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 80, 821, 471))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_7 = QFrame(self.verticalLayoutWidget_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_7)

        self.line_8 = QFrame(self.verticalLayoutWidget_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.frequencyInput = QLineEdit(self.verticalLayoutWidget_2)
        self.frequencyInput.setObjectName(u"frequencyInput")

        self.horizontalLayout_7.addWidget(self.frequencyInput)

        self.radioHz = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup_4 = QButtonGroup(Widget)
        self.buttonGroup_4.setObjectName(u"buttonGroup_4")
        self.buttonGroup_4.addButton(self.radioHz)
        self.radioHz.setObjectName(u"radioHz")
        self.radioHz.setChecked(True)

        self.horizontalLayout_7.addWidget(self.radioHz)

        self.radioKHz = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup_4.addButton(self.radioKHz)
        self.radioKHz.setObjectName(u"radioKHz")

        self.horizontalLayout_7.addWidget(self.radioKHz)

        self.radioMHz = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup_4.addButton(self.radioMHz)
        self.radioMHz.setObjectName(u"radioMHz")
        self.radioMHz.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.radioMHz)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.line_9 = QFrame(self.verticalLayoutWidget_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.amplitudeInput = QLineEdit(self.verticalLayoutWidget_2)
        self.amplitudeInput.setObjectName(u"amplitudeInput")

        self.horizontalLayout_8.addWidget(self.amplitudeInput)

        self.radiomV = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup = QButtonGroup(Widget)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radiomV)
        self.radiomV.setObjectName(u"radiomV")
        self.radiomV.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radiomV)

        self.radioV = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup.addButton(self.radioV)
        self.radioV.setObjectName(u"radioV")

        self.horizontalLayout_8.addWidget(self.radioV)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.line_10 = QFrame(self.verticalLayoutWidget_2)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.offSetInput = QLineEdit(self.verticalLayoutWidget_2)
        self.offSetInput.setObjectName(u"offSetInput")

        self.horizontalLayout_9.addWidget(self.offSetInput)

        self.offSetRadiomV = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup_5 = QButtonGroup(Widget)
        self.buttonGroup_5.setObjectName(u"buttonGroup_5")
        self.buttonGroup_5.addButton(self.offSetRadiomV)
        self.offSetRadiomV.setObjectName(u"offSetRadiomV")
        self.offSetRadiomV.setChecked(True)

        self.horizontalLayout_9.addWidget(self.offSetRadiomV)

        self.offSetRadioV = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup_5.addButton(self.offSetRadioV)
        self.offSetRadioV.setObjectName(u"offSetRadioV")

        self.horizontalLayout_9.addWidget(self.offSetRadioV)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.line_11 = QFrame(self.verticalLayoutWidget_2)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.phaseInput = QLineEdit(self.verticalLayoutWidget_2)
        self.phaseInput.setObjectName(u"phaseInput")

        self.horizontalLayout_10.addWidget(self.phaseInput)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.line_12 = QFrame(self.verticalLayoutWidget_2)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_12)

        self.generateSignalButton = QPushButton(self.verticalLayoutWidget_2)
        self.generateSignalButton.setObjectName(u"generateSignalButton")
        self.generateSignalButton.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.verticalLayout_2.addWidget(self.generateSignalButton)

        self.tabWidget.addTab(self.Seno, "")
        self.SomaSenos = QWidget()
        self.SomaSenos.setObjectName(u"SomaSenos")
        self.formLayout = QFormLayout(self.SomaSenos)
        self.formLayout.setObjectName(u"formLayout")
        self.inputSum = QLineEdit(self.SomaSenos)
        self.inputSum.setObjectName(u"inputSum")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.inputSum)

        self.generateSignalSum = QPushButton(self.SomaSenos)
        self.generateSignalSum.setObjectName(u"generateSignalSum")
        self.generateSignalSum.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.generateSignalSum)

        self.tabWidget.addTab(self.SomaSenos, "")
        self.Triangle = QWidget()
        self.Triangle.setObjectName(u"Triangle")
        self.label_51 = QLabel(self.Triangle)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(0, 0, 831, 67))
        self.label_51.setMaximumSize(QSize(16777215, 16777215))
        self.label_51.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px;\n"
"height: 50px;")
        self.verticalLayoutWidget_9 = QWidget(self.Triangle)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(0, 80, 831, 471))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.line_61 = QFrame(self.verticalLayoutWidget_9)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setFrameShape(QFrame.HLine)
        self.line_61.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_61)

        self.line_62 = QFrame(self.verticalLayoutWidget_9)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setFrameShape(QFrame.HLine)
        self.line_62.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_62)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_52 = QLabel(self.verticalLayoutWidget_9)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_42.addWidget(self.label_52)

        self.frequencyInput_tr = QLineEdit(self.verticalLayoutWidget_9)
        self.frequencyInput_tr.setObjectName(u"frequencyInput_tr")

        self.horizontalLayout_42.addWidget(self.frequencyInput_tr)

        self.radioHz_tr = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup_9 = QButtonGroup(Widget)
        self.buttonGroup_9.setObjectName(u"buttonGroup_9")
        self.buttonGroup_9.addButton(self.radioHz_tr)
        self.radioHz_tr.setObjectName(u"radioHz_tr")
        self.radioHz_tr.setChecked(True)

        self.horizontalLayout_42.addWidget(self.radioHz_tr)

        self.radioKHz_tr = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup_9.addButton(self.radioKHz_tr)
        self.radioKHz_tr.setObjectName(u"radioKHz_tr")

        self.horizontalLayout_42.addWidget(self.radioKHz_tr)

        self.radioMHz_tr = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup_9.addButton(self.radioMHz_tr)
        self.radioMHz_tr.setObjectName(u"radioMHz_tr")
        self.radioMHz_tr.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_42.addWidget(self.radioMHz_tr)


        self.verticalLayout_11.addLayout(self.horizontalLayout_42)

        self.line_63 = QFrame(self.verticalLayoutWidget_9)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setFrameShape(QFrame.HLine)
        self.line_63.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_63)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_53 = QLabel(self.verticalLayoutWidget_9)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_43.addWidget(self.label_53)

        self.amplitudeInput_tr = QLineEdit(self.verticalLayoutWidget_9)
        self.amplitudeInput_tr.setObjectName(u"amplitudeInput_tr")

        self.horizontalLayout_43.addWidget(self.amplitudeInput_tr)

        self.radiomV_tr = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup_10 = QButtonGroup(Widget)
        self.buttonGroup_10.setObjectName(u"buttonGroup_10")
        self.buttonGroup_10.addButton(self.radiomV_tr)
        self.radiomV_tr.setObjectName(u"radiomV_tr")
        self.radiomV_tr.setChecked(True)

        self.horizontalLayout_43.addWidget(self.radiomV_tr)

        self.radioV_tr = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup_10.addButton(self.radioV_tr)
        self.radioV_tr.setObjectName(u"radioV_tr")

        self.horizontalLayout_43.addWidget(self.radioV_tr)


        self.verticalLayout_11.addLayout(self.horizontalLayout_43)

        self.line_64 = QFrame(self.verticalLayoutWidget_9)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setFrameShape(QFrame.HLine)
        self.line_64.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_64)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_54 = QLabel(self.verticalLayoutWidget_9)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_44.addWidget(self.label_54)

        self.offSetInput_tr = QLineEdit(self.verticalLayoutWidget_9)
        self.offSetInput_tr.setObjectName(u"offSetInput_tr")

        self.horizontalLayout_44.addWidget(self.offSetInput_tr)

        self.offSetRadiomV_tr = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup_11 = QButtonGroup(Widget)
        self.buttonGroup_11.setObjectName(u"buttonGroup_11")
        self.buttonGroup_11.addButton(self.offSetRadiomV_tr)
        self.offSetRadiomV_tr.setObjectName(u"offSetRadiomV_tr")
        self.offSetRadiomV_tr.setChecked(True)

        self.horizontalLayout_44.addWidget(self.offSetRadiomV_tr)

        self.offSetRadioV_tr = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup_11.addButton(self.offSetRadioV_tr)
        self.offSetRadioV_tr.setObjectName(u"offSetRadioV_tr")

        self.horizontalLayout_44.addWidget(self.offSetRadioV_tr)


        self.verticalLayout_11.addLayout(self.horizontalLayout_44)

        self.line_65 = QFrame(self.verticalLayoutWidget_9)
        self.line_65.setObjectName(u"line_65")
        self.line_65.setFrameShape(QFrame.HLine)
        self.line_65.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_65)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_55 = QLabel(self.verticalLayoutWidget_9)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_45.addWidget(self.label_55)

        self.phaseInput_tr = QLineEdit(self.verticalLayoutWidget_9)
        self.phaseInput_tr.setObjectName(u"phaseInput_tr")

        self.horizontalLayout_45.addWidget(self.phaseInput_tr)


        self.verticalLayout_11.addLayout(self.horizontalLayout_45)

        self.line_66 = QFrame(self.verticalLayoutWidget_9)
        self.line_66.setObjectName(u"line_66")
        self.line_66.setFrameShape(QFrame.HLine)
        self.line_66.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_11.addWidget(self.line_66)

        self.generateSignalButton_tr = QPushButton(self.verticalLayoutWidget_9)
        self.generateSignalButton_tr.setObjectName(u"generateSignalButton_tr")
        self.generateSignalButton_tr.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.verticalLayout_11.addWidget(self.generateSignalButton_tr)

        self.tabWidget.addTab(self.Triangle, "")
        self.Sawtooth = QWidget()
        self.Sawtooth.setObjectName(u"Sawtooth")
        self.label_21 = QLabel(self.Sawtooth)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 0, 831, 67))
        self.label_21.setMaximumSize(QSize(16777215, 16777215))
        self.label_21.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px;\n"
"height: 50px;")
        self.verticalLayoutWidget_5 = QWidget(self.Sawtooth)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 80, 831, 471))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.line_25 = QFrame(self.verticalLayoutWidget_5)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_25)

        self.line_26 = QFrame(self.verticalLayoutWidget_5)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_26)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_22 = QLabel(self.verticalLayoutWidget_5)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_17.addWidget(self.label_22)

        self.frequencyInput_st = QLineEdit(self.verticalLayoutWidget_5)
        self.frequencyInput_st.setObjectName(u"frequencyInput_st")

        self.horizontalLayout_17.addWidget(self.frequencyInput_st)

        self.radioHz_st = QRadioButton(self.verticalLayoutWidget_5)
        self.radioHz_st.setObjectName(u"radioHz_st")
        self.radioHz_st.setChecked(True)

        self.horizontalLayout_17.addWidget(self.radioHz_st)

        self.radioKHz_st = QRadioButton(self.verticalLayoutWidget_5)
        self.radioKHz_st.setObjectName(u"radioKHz_st")

        self.horizontalLayout_17.addWidget(self.radioKHz_st)

        self.radioMHz_st = QRadioButton(self.verticalLayoutWidget_5)
        self.radioMHz_st.setObjectName(u"radioMHz_st")
        self.radioMHz_st.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.radioMHz_st)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.line_27 = QFrame(self.verticalLayoutWidget_5)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.HLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_27)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_23 = QLabel(self.verticalLayoutWidget_5)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_18.addWidget(self.label_23)

        self.amplitudeInput_st = QLineEdit(self.verticalLayoutWidget_5)
        self.amplitudeInput_st.setObjectName(u"amplitudeInput_st")

        self.horizontalLayout_18.addWidget(self.amplitudeInput_st)

        self.radiomV_st = QRadioButton(self.verticalLayoutWidget_5)
        self.buttonGroup_2 = QButtonGroup(Widget)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radiomV_st)
        self.radiomV_st.setObjectName(u"radiomV_st")
        self.radiomV_st.setChecked(True)

        self.horizontalLayout_18.addWidget(self.radiomV_st)

        self.radioV_st = QRadioButton(self.verticalLayoutWidget_5)
        self.buttonGroup_2.addButton(self.radioV_st)
        self.radioV_st.setObjectName(u"radioV_st")

        self.horizontalLayout_18.addWidget(self.radioV_st)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)

        self.line_28 = QFrame(self.verticalLayoutWidget_5)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_28)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_24 = QLabel(self.verticalLayoutWidget_5)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_19.addWidget(self.label_24)

        self.offSetInput_st = QLineEdit(self.verticalLayoutWidget_5)
        self.offSetInput_st.setObjectName(u"offSetInput_st")

        self.horizontalLayout_19.addWidget(self.offSetInput_st)

        self.offSetRadiomV_st = QRadioButton(self.verticalLayoutWidget_5)
        self.buttonGroup_3 = QButtonGroup(Widget)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.offSetRadiomV_st)
        self.offSetRadiomV_st.setObjectName(u"offSetRadiomV_st")
        self.offSetRadiomV_st.setChecked(True)

        self.horizontalLayout_19.addWidget(self.offSetRadiomV_st)

        self.offSetRadioV_st = QRadioButton(self.verticalLayoutWidget_5)
        self.buttonGroup_3.addButton(self.offSetRadioV_st)
        self.offSetRadioV_st.setObjectName(u"offSetRadioV_st")

        self.horizontalLayout_19.addWidget(self.offSetRadioV_st)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)

        self.line_29 = QFrame(self.verticalLayoutWidget_5)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_29)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_25 = QLabel(self.verticalLayoutWidget_5)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_20.addWidget(self.label_25)

        self.dutyInput_st = QLineEdit(self.verticalLayoutWidget_5)
        self.dutyInput_st.setObjectName(u"dutyInput_st")

        self.horizontalLayout_20.addWidget(self.dutyInput_st)


        self.verticalLayout_5.addLayout(self.horizontalLayout_20)

        self.line_30 = QFrame(self.verticalLayoutWidget_5)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_30)

        self.generateSignalButton_st = QPushButton(self.verticalLayoutWidget_5)
        self.generateSignalButton_st.setObjectName(u"generateSignalButton_st")
        self.generateSignalButton_st.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.verticalLayout_5.addWidget(self.generateSignalButton_st)

        self.tabWidget.addTab(self.Sawtooth, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Portable Signal Generator", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Square</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Frequency", None))
#if QT_CONFIG(tooltip)
        self.frequencyInput_sq.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.frequencyInput_sq.setText(QCoreApplication.translate("Widget", u"1000", None))
        self.radioHz_sq.setText(QCoreApplication.translate("Widget", u"Hz", None))
        self.radioKHz_sq.setText(QCoreApplication.translate("Widget", u"KHz", None))
        self.radioMHz_sq.setText(QCoreApplication.translate("Widget", u"MHz", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Amplitude", None))
        self.amplitudeInput_sq.setText(QCoreApplication.translate("Widget", u"15", None))
        self.radiomV_sq.setText(QCoreApplication.translate("Widget", u"mV", None))
        self.radioV_sq.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Offset", None))
        self.offSetInput_sq.setText(QCoreApplication.translate("Widget", u"0", None))
        self.offSetRadiomV_sq.setText(QCoreApplication.translate("Widget", u"mV", None))
        self.offSetRadioV_sq.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Duty Cycle (%)", None))
        self.dutyInput_sq.setText(QCoreApplication.translate("Widget", u"48.7", None))
        self.generateSignalButton_sq.setText(QCoreApplication.translate("Widget", u"Generate Signal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Square), QCoreApplication.translate("Widget", u"Square", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Sine</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Frequency", None))
#if QT_CONFIG(tooltip)
        self.frequencyInput.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.frequencyInput.setText(QCoreApplication.translate("Widget", u"1000", None))
        self.radioHz.setText(QCoreApplication.translate("Widget", u"Hz", None))
        self.radioKHz.setText(QCoreApplication.translate("Widget", u"KHz", None))
        self.radioMHz.setText(QCoreApplication.translate("Widget", u"MHz", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Amplitude", None))
        self.amplitudeInput.setText(QCoreApplication.translate("Widget", u"15", None))
        self.radiomV.setText(QCoreApplication.translate("Widget", u"mV", None))
        self.radioV.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Offset", None))
        self.offSetInput.setText(QCoreApplication.translate("Widget", u"0", None))
        self.offSetRadiomV.setText(QCoreApplication.translate("Widget", u"mV", None))
        self.offSetRadioV.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Phase", None))
        self.phaseInput.setText(QCoreApplication.translate("Widget", u"0", None))
        self.generateSignalButton.setText(QCoreApplication.translate("Widget", u"Generate Signal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Seno), QCoreApplication.translate("Widget", u"Sine", None))
        self.inputSum.setText(QCoreApplication.translate("Widget", u"2cos(1000t + 0) + 3sin(2000t + 0) + 4cos(3000t + 0) + 5sin(4000t + 0)", None))
        self.generateSignalSum.setText(QCoreApplication.translate("Widget", u"Generate Signal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SomaSenos), QCoreApplication.translate("Widget", u"Sum", None))
        self.label_51.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Triangle</p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("Widget", u"Frequency", None))
#if QT_CONFIG(tooltip)
        self.frequencyInput_tr.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.frequencyInput_tr.setText(QCoreApplication.translate("Widget", u"1000", None))
        self.radioHz_tr.setText(QCoreApplication.translate("Widget", u"Hz", None))
        self.radioKHz_tr.setText(QCoreApplication.translate("Widget", u"KHz", None))
        self.radioMHz_tr.setText(QCoreApplication.translate("Widget", u"MHz", None))
        self.label_53.setText(QCoreApplication.translate("Widget", u"Amplitude", None))
        self.amplitudeInput_tr.setText(QCoreApplication.translate("Widget", u"15", None))
        self.radiomV_tr.setText(QCoreApplication.translate("Widget", u"mV", None))
        self.radioV_tr.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_54.setText(QCoreApplication.translate("Widget", u"Offset", None))
        self.offSetInput_tr.setText(QCoreApplication.translate("Widget", u"0", None))
        self.offSetRadiomV_tr.setText(QCoreApplication.translate("Widget", u"mV", None))
        self.offSetRadioV_tr.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_55.setText(QCoreApplication.translate("Widget", u"Phase", None))
        self.phaseInput_tr.setText(QCoreApplication.translate("Widget", u"0", None))
        self.generateSignalButton_tr.setText(QCoreApplication.translate("Widget", u"Generate Signal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Triangle), QCoreApplication.translate("Widget", u"Triangle", None))
        self.label_21.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Sawtooth</p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Widget", u"Frequency", None))
#if QT_CONFIG(tooltip)
        self.frequencyInput_st.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.frequencyInput_st.setText(QCoreApplication.translate("Widget", u"1000", None))
        self.radioHz_st.setText(QCoreApplication.translate("Widget", u"Hz", None))
        self.radioKHz_st.setText(QCoreApplication.translate("Widget", u"KHz", None))
        self.radioMHz_st.setText(QCoreApplication.translate("Widget", u"MHz", None))
        self.label_23.setText(QCoreApplication.translate("Widget", u"Amplitude", None))
        self.amplitudeInput_st.setText(QCoreApplication.translate("Widget", u"15", None))
        self.radiomV_st.setText(QCoreApplication.translate("Widget", u"mV", None))
        self.radioV_st.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_24.setText(QCoreApplication.translate("Widget", u"Offset", None))
        self.offSetInput_st.setText(QCoreApplication.translate("Widget", u"0", None))
        self.offSetRadiomV_st.setText(QCoreApplication.translate("Widget", u"mV", None))
        self.offSetRadioV_st.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_25.setText(QCoreApplication.translate("Widget", u"Duty Cycle (%)", None))
        self.dutyInput_st.setText(QCoreApplication.translate("Widget", u"48.7", None))
        self.generateSignalButton_st.setText(QCoreApplication.translate("Widget", u"Generate Signal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sawtooth), QCoreApplication.translate("Widget", u"Sawtooth", None))
    # retranslateUi

