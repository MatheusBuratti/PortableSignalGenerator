import serial
import time
from functionGenerator import *

# O que mandar?
# 1. Vetor de pontos
# 2. Tamanho do vetor de pontos
# 3. CCR0 e Prescaler TIM2


class USBHandler:
    def __init__(self):
        self.baudrate = 115200
        self.serial = None
        while (self.serial is None):
            try:
                self.serial = serial.Serial("/dev/ttyACM0", 115200)
                print(self.serial)
            except:
                print("USB not connected")
                time.sleep(5)

    def send(self, data: Function):
        message = b'!Start!'
        message += int.to_bytes(data.arr, 4, 'little')
        message += int.to_bytes(data.prescaler-1, 2, 'little')
        message += int.to_bytes(data.qtd_pontos, 2, 'little')
        self.serial.write(message)
        message = b''
        for ponto in data.pontos:
            message += int.to_bytes(int(ponto), 2, 'little')
        self.serial.write(message)


if __name__ == "__main__":
    # Teste enviando uma senoide de 500Hz para o microcontrolador
    usb = USBHandler()
    func = functionGenerator.generateSineSumWave(
        "2cos(1000t + 0) + 3sin(2000t + 0) + 4cos(3000t + 0) + 5sin(4000t + 0)")
    usb.send(func)
