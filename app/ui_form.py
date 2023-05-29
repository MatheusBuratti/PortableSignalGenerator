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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"signal-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        Widget.setStyleSheet(u"font: 700 12pt \"Alef\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 90, 731, 471))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.line_6 = QFrame(self.verticalLayoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.waveform = QLabel(self.verticalLayoutWidget)
        self.waveform.setObjectName(u"waveform")

        self.horizontalLayout_3.addWidget(self.waveform)

        self.radioSine = QRadioButton(self.verticalLayoutWidget)
        self.waveformButtons = QButtonGroup(Widget)
        self.waveformButtons.setObjectName(u"waveformButtons")
        self.waveformButtons.addButton(self.radioSine)
        self.radioSine.setObjectName(u"radioSine")
        self.radioSine.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radioSine)

        self.radioSquare = QRadioButton(self.verticalLayoutWidget)
        self.waveformButtons.addButton(self.radioSquare)
        self.radioSquare.setObjectName(u"radioSquare")

        self.horizontalLayout_3.addWidget(self.radioSquare)

        self.radioTriangle = QRadioButton(self.verticalLayoutWidget)
        self.waveformButtons.addButton(self.radioTriangle)
        self.radioTriangle.setObjectName(u"radioTriangle")

        self.horizontalLayout_3.addWidget(self.radioTriangle)

        self.radioSaw = QRadioButton(self.verticalLayoutWidget)
        self.waveformButtons.addButton(self.radioSaw)
        self.radioSaw.setObjectName(u"radioSaw")

        self.horizontalLayout_3.addWidget(self.radioSaw)

        self.radioPulse = QRadioButton(self.verticalLayoutWidget)
        self.waveformButtons.addButton(self.radioPulse)
        self.radioPulse.setObjectName(u"radioPulse")

        self.horizontalLayout_3.addWidget(self.radioPulse)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

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

        self.frequencyInput = QLineEdit(self.verticalLayoutWidget)
        self.frequencyInput.setObjectName(u"frequencyInput")

        self.horizontalLayout_2.addWidget(self.frequencyInput)

        self.radioHz = QRadioButton(self.verticalLayoutWidget)
        self.amplitudeButtons = QButtonGroup(Widget)
        self.amplitudeButtons.setObjectName(u"amplitudeButtons")
        self.amplitudeButtons.addButton(self.radioHz)
        self.radioHz.setObjectName(u"radioHz")
        self.radioHz.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioHz)

        self.radioKHz = QRadioButton(self.verticalLayoutWidget)
        self.amplitudeButtons.addButton(self.radioKHz)
        self.radioKHz.setObjectName(u"radioKHz")

        self.horizontalLayout_2.addWidget(self.radioKHz)

        self.radioMHz = QRadioButton(self.verticalLayoutWidget)
        self.amplitudeButtons.addButton(self.radioMHz)
        self.radioMHz.setObjectName(u"radioMHz")
        self.radioMHz.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.radioMHz)


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

        self.amplitudeInput = QLineEdit(self.verticalLayoutWidget)
        self.amplitudeInput.setObjectName(u"amplitudeInput")

        self.horizontalLayout.addWidget(self.amplitudeInput)

        self.radiomV = QRadioButton(self.verticalLayoutWidget)
        self.frequencyButtons = QButtonGroup(Widget)
        self.frequencyButtons.setObjectName(u"frequencyButtons")
        self.frequencyButtons.addButton(self.radiomV)
        self.radiomV.setObjectName(u"radiomV")
        self.radiomV.setChecked(True)

        self.horizontalLayout.addWidget(self.radiomV)

        self.radioV = QRadioButton(self.verticalLayoutWidget)
        self.frequencyButtons.addButton(self.radioV)
        self.radioV.setObjectName(u"radioV")

        self.horizontalLayout.addWidget(self.radioV)


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

        self.offSetInput = QLineEdit(self.verticalLayoutWidget)
        self.offSetInput.setObjectName(u"offSetInput")

        self.horizontalLayout_4.addWidget(self.offSetInput)

        self.radioomV = QRadioButton(self.verticalLayoutWidget)
        self.offSetButtons = QButtonGroup(Widget)
        self.offSetButtons.setObjectName(u"offSetButtons")
        self.offSetButtons.addButton(self.radioomV)
        self.radioomV.setObjectName(u"radioomV")
        self.radioomV.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioomV)

        self.radiooV = QRadioButton(self.verticalLayoutWidget)
        self.offSetButtons.addButton(self.radiooV)
        self.radiooV.setObjectName(u"radiooV")

        self.horizontalLayout_4.addWidget(self.radiooV)


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

        self.dutyInput = QLineEdit(self.verticalLayoutWidget)
        self.dutyInput.setObjectName(u"dutyInput")

        self.horizontalLayout_5.addWidget(self.dutyInput)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line_5 = QFrame(self.verticalLayoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_5)

        self.generateSignalButton = QPushButton(self.verticalLayoutWidget)
        self.generateSignalButton.setObjectName(u"generateSignalButton")
        self.generateSignalButton.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")

        self.verticalLayout.addWidget(self.generateSignalButton)

        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 10, 729, 67))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 181, 177, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px;\n"
"height: 50px;")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Portable Signal Generator", None))
        self.waveform.setText(QCoreApplication.translate("Widget", u"Waveform", None))
        self.radioSine.setText(QCoreApplication.translate("Widget", u"Sine", None))
        self.radioSquare.setText(QCoreApplication.translate("Widget", u"Square", None))
        self.radioTriangle.setText(QCoreApplication.translate("Widget", u"Triangle", None))
        self.radioSaw.setText(QCoreApplication.translate("Widget", u"Sawtooth", None))
        self.radioPulse.setText(QCoreApplication.translate("Widget", u"Pulse", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Frequency", None))
#if QT_CONFIG(tooltip)
        self.frequencyInput.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.frequencyInput.setText(QCoreApplication.translate("Widget", u"50", None))
        self.radioHz.setText(QCoreApplication.translate("Widget", u"Hz", None))
        self.radioKHz.setText(QCoreApplication.translate("Widget", u"KHz", None))
        self.radioMHz.setText(QCoreApplication.translate("Widget", u"MHz", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Amplitude", None))
        self.amplitudeInput.setText(QCoreApplication.translate("Widget", u"15", None))
        self.radiomV.setText(QCoreApplication.translate("Widget", u"mV", None))
        self.radioV.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Offset", None))
        self.offSetInput.setText(QCoreApplication.translate("Widget", u"5", None))
        self.radioomV.setText(QCoreApplication.translate("Widget", u"mV", None))
        self.radiooV.setText(QCoreApplication.translate("Widget", u"V", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Duty Cycle (%)", None))
        self.dutyInput.setText(QCoreApplication.translate("Widget", u"0", None))
        self.generateSignalButton.setText(QCoreApplication.translate("Widget", u"Generate Signal", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Portable Signal Generator</p></body></html>", None))
    # retranslateUi

