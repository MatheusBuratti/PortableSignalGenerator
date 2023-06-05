# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import sys
import math
from functionGenerator import Waveform, functionGenerator as fg
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.generateSignalButton.clicked.connect(self.outputData)

    def outputData(self):
        print()
        self.printWaveform()
        frequency = self.printFrequencyData()
        amplitude = self.printAmplitudeData()
        offSet = self.printOffSetData()
        dutyCycle = self.printDutyCycleData()
        fg.generateSineWave(frequency, 0, amplitude)

    def printFrequencyData(self):
        text = self.ui.frequencyInput.text()
        number = float(text)
        result = 0
        if self.ui.radioMHz.isChecked():
            result = number * 1000000
            print("Frequency: " + str(number) + "MHz")

        elif self.ui.radioKHz.isChecked():
            result = number * 1000
            print("Frequency: " + str(number) + "KHz")

        else:
            result = number
            print("Frequency: " + str(number) + "Hz")
        return result

    def printAmplitudeData(self):
        text = self.ui.amplitudeInput.text()
        number = float(text)
        result = 0
        if self.ui.radiomV.isChecked():
            result = number/1000
            print("Amplitude: " + str(number) + "mV")

        else:
            result = number
            print("Amplitude: " + str(number) + "V")
        return result

    def printOffSetData(self):
        text = self.ui.offSetInput.text()
        number = float(text)

        if self.ui.radioomV.isChecked():
            result = number/1000
            print("Offset: " + str(number) + "mV")

        else:
            result = number
            print("Offset: " + str(number) + "V")
        return result

    def printDutyCycleData(self):
        text = self.ui.dutyInput.text()
        number = float(text)
        print("Duty Cycle: " + str(number) + "%")
        return number

    def printWaveform(self):
        if self.ui.radioPulse.isChecked():
            waveform = Waveform.PULSE
        elif self.ui.radioSaw.isChecked():
            waveform = Waveform.SAW
        elif self.ui.radioSine.isChecked():
            waveform = Waveform.SINE
        elif self.ui.radioSquare.isChecked():
            waveform = Waveform.SQUARE
        elif self.ui.radioTriangle.isChecked():
            waveform = Waveform.TRIANGLE
        print("Waveform: " + str(waveform))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
