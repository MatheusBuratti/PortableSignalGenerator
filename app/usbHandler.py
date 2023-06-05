import serial
import time

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
                Exception("Não foi possível conectar ao dispositivo USB")
                time.sleep(2)

    def send(self, data):
        self.serial.write(data)

    def recieve(self):
        print(self.serial.read(20))


if __name__ == "__main__":
    USB = USBHandler()
    i = 0
    while (True):
        USB.send(f'Hello World!{i}'.encode())
        i += 1
        USB.recieve()
