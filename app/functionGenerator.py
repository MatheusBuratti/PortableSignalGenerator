import math
import numpy as np
from enum import Enum
import re


class Waveform(Enum):
    SINESUM = 0
    SAWTOOTH = 1
    SINE = 2
    SQUARE = 3
    TRIANGLE = 4

    def __str__(self) -> str:
        return self.name


class Function:
    def __init__(self, waveform: Waveform, freq: int, phase: int, amplitude: int, dutyCycle: float, pontos: list, qtd_pontos: int) -> None:
        self.waveform = waveform
        self.freq = freq
        self.phase = phase
        self.amplitude = amplitude
        self.dutyCycle = dutyCycle
        self.pontos = pontos
        self.qtd_pontos = qtd_pontos
        self.__calc__()

    def __calc__(self):
        # Calcula o ARR e o Prescaler baseado na frequencia desejada, no MCLK e na quantidade de pontos
        MCLK = 168000000
        freq_timer = self.freq * self.qtd_pontos
        self.prescaler = 1
        self.arr = int(MCLK/(freq_timer*self.prescaler*2))


class cosSineSumParser:
    # separa uma entrada (somas) em tuplas
    def sep(string: str):
        return string.split('+')

    # retorna a função em uma tupla a partir de uma string
    def getFunc(string: str):
        all_results = re.findall(
            r"([-+]?[ ]*(?:\d*[\.]*\d+)?)[* \t]?((?:cos)|(?:sen|sin))[(](?:([-+]?[ ]*(?:\d*[\.]*\d+))([tx])[ ]*([-+]?[' ']*(?:\d*[\.]*\d+))?|([ ]*[-+]?[ ]*(?:\d*[\.]*\d+))[ ]*([-+]?[ ]*(?:\d*[\.]*\d+))([tx]))[)]", string)
        functions = []
        for result in all_results:
            # ===== Pega amplitude =====
            if result[0] != '':
                amp = result[0]
            else:
                amp = '1'

            # ===== Pega função =====
            if result[1] == "cos":
                func = "cos"
            elif result[1] == "sen" or result[1] == "sin":
                func = "sen"
            else:
                func = None

            # ===== Pega frequência e fase =====
            fase = ''
            if result[3] == 't':
                ang_freq = result[2] if result[2] != '' else '1'
                fase = result[4]
            elif result[7] == 't':
                ang_freq = result[6] if result[6] != '' else '1'
                fase = result[5]
            else:
                ang_freq = None
            if fase == '':
                fase = '0'

            # ===== Removendo whitespaces dos valores numéricos =====
            amp = amp.replace(' ', '')
            ang_freq = ang_freq.replace(' ', '')
            fase = fase.replace(' ', '')

            # ===== Resolve casos onde aparece apenas o sinal e nenhum número =====
            # Ex: - cos(t) --> amp = '-'
            if amp == '+' or amp == '-':
                amp += '1'
            if ang_freq == '+' or ang_freq == '-':
                ang_freq += '1'
            if fase == '+' or fase == '-':
                fase += '1'

            functions.append((float(amp),
                             func, float(ang_freq), float(fase)))
        return functions


class functionGenerator:
    def generateSineSumWave(input: str):
        # ===== Pegando a função a partir da entrada =====
        functions = cosSineSumParser.getFunc(input)
        max_ang_freq = max(
            functions, key=lambda item: item[3])[2]
        freq = max_ang_freq/(2*math.pi)
        periodo = 2*math.pi/np.gcd.reduce(
            [int(x[2]) for x in functions])
        # ===== Calculando a quantidade de pontos =====
        qtd_pontos = 128
        t = np.linspace(0, periodo, qtd_pontos)
        F = list()
        for function in functions:
            F.append(np.cos(function[2]*t + function[3])*function[0]
                     if function[1] == "cos"
                     else np.sin(function[2]*t + function[3])*function[0])
        F = np.sum(F, axis=0)
        pontos = [round(elem)
                  for elem in 4095*(F+max(F))/(2*max(F))]
        return Function(Waveform.SINESUM, freq, 0, 1, 1, pontos, qtd_pontos)

    def generateSawWave(freq: float, dutyCycle: float):
        qtd_pontos = 128
        pontos = np.zeros(qtd_pontos, dtype=int)
        slice = np.r_[0:int(dutyCycle*qtd_pontos)]
        pontos[slice] = np.poly1d([4095/(dutyCycle*qtd_pontos), 0])(slice)

        return Function(Waveform.SAWTOOTH, freq, 0, 1, dutyCycle, pontos, qtd_pontos)

    def generateSquareWave(freq: float, dutyCycle: float):
        # Duty cycle na forma 0.200 - 0.800
        qtd_pontos = 64
        pontos = np.zeros(qtd_pontos, dtype=int)
        slice = np.r_[0:int(dutyCycle*qtd_pontos)]
        pontos[slice] = 4095

        return Function(Waveform.SQUARE, freq, 0, 1, dutyCycle, pontos, qtd_pontos)

    def generateTriangleWave(freq: float):
        qtd_pontos = 64
        pontos = np.zeros(qtd_pontos, dtype=int)
        first_slice = np.r_[0:int(0.5*qtd_pontos)]
        second_slice = np.r_[int(0.5*qtd_pontos):qtd_pontos]
        pontos[first_slice] = np.poly1d([4095/(qtd_pontos), 0])(first_slice)
        pontos[second_slice] = np.poly1d(
            [-4095/(qtd_pontos), 4095])(second_slice)

        return Function(Waveform.TRIANGLE, freq, 0, 1, 1, pontos, qtd_pontos)

    def generateSineWave(freq: float, phase: float, amplitude: float):
        periodo = 1/freq
        # ===== Calculando a quantidade de pontos =====
        qtd_pontos = 128 if freq < 100000 else 64
        t = np.linspace(0, periodo, qtd_pontos)
        F = np.sin(2*math.pi*freq*t + phase)
        pontos = [round(elem)
                  for elem in 4095*(F+1)/2]
        return Function(Waveform.SINE, freq, phase, amplitude, 1, pontos, qtd_pontos)


# Testing and plotting output of the function generator
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    # Test 1: Sine wave
    plt.figure()
    plt.plot(functionGenerator.generateSineWave(
        1000, 0, 1).pontos, 'r', label='freq = 1000Hz')
    plt.plot(functionGenerator.generateSineWave(
        500, 0, 1).pontos, 'b', label='freq = 500Hz')
    plt.plot(functionGenerator.generateSineWave(
        2000, 0, 1).pontos, 'g', label='freq = 2000Hz')
    plt.show()

    # Test 2: Sawtooth wave
    plt.figure()
    plt.plot(functionGenerator.generateSawWave(2000, 0.5).pontos,
             'r', label='Duty cycle = 0.5 & freq = 2000Hz')
    plt.plot(functionGenerator.generateSawWave(1000, 0.25).pontos,
             'b', label='Duty cycle = 0.25 & freq = 1000Hz')
    plt.plot(functionGenerator.generateSawWave(500, 0.8).pontos,
             'g', label='Duty cycle = 0.8 & freq = 500Hz')
    plt.show()

    # Teste 3: Square wave
    plt.figure()
    plt.plot(functionGenerator.generateSquareWave(2000, 0.5).pontos,
             'r', label='Duty cycle = 0.5 & freq = 2000Hz')
    plt.plot(functionGenerator.generateSquareWave(1000, 0.2).pontos,
             'b', label='Duty cycle = 0.2 & freq = 1000Hz')
    plt.plot(functionGenerator.generateSquareWave(500, 0.8).pontos,
             'g', label='Duty cycle = 0.8 & freq = 500Hz')
    plt.show()

    # Teste 4: Triangle wave
    plt.figure()
    plt.plot(functionGenerator.generateTriangleWave(
        2000).pontos, 'r', label='freq = 2000Hz')
    plt.plot(functionGenerator.generateTriangleWave(
        1000).pontos, 'b', label='freq = 1000Hz')
    plt.plot(functionGenerator.generateTriangleWave(
        500).pontos, 'g', label='freq = 500Hz')
    plt.show()

    # Teste 5: Sine sum wave
    plt.figure()
    plt.plot(functionGenerator.generateSineSumWave(
        "2cos(1000t + 0) + 3sin(2000t + 0)").pontos, 'r', label='2cos(1000t + 0) + 3sin(2000t + 0)')
    plt.plot(functionGenerator.generateSineSumWave("2cos(1000t + 0) + 3sin(2000t + 0) + 4cos(3000t + 0)").pontos,
             'b', label='2cos(1000t + 0) + 3sin(2000t + 0) + 4cos(3000t + 0)')
    plt.plot(functionGenerator.generateSineSumWave("2cos(1000t + 0) + 3sin(2000t + 0) + 4cos(3000t + 0) + 5sin(4000t + 0)").pontos,
             'g', label='2cos(1000t + 0) + 3sin(2000t + 0) + 4cos(3000t + 0) + 5sin(4000t + 0)')
    plt.show()
