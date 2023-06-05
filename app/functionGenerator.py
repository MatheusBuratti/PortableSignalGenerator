import math
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum
import re


class Waveform(Enum):
    SINESUM = 0
    SAW = 1
    SINE = 2
    SQUARE = 3
    TRIANGLE = 4

    def __str__(self) -> str:
        return self.name


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
        print(functions)
        max_ang_freq = max(
            functions, key=lambda item: item[3])[2]
        freq = max_ang_freq/(2*math.pi)
        periodo = 4*math.pi/np.gcd.reduce(
            [int(x[2]) for x in functions])
        # ===== Calculando a quantidade de pontos =====
        # Se frequencia < 100kHz usa um valor fixo máximo
        if freq < 10000:
            if freq < 100:
                qtd_pontos = int(100*freq)
            else:
                qtd_pontos = int(10*freq)
        else:
            qtd_pontos = 100000
        t = np.linspace(0, periodo, qtd_pontos)
        F = list()
        for function in functions:
            F.append(np.cos(function[2]*t + function[3])*function[0]
                     if function[1] == "cos"
                     else np.sin(function[2]*t + function[3])*function[0])
        F = np.sum(F, axis=0)
        pontos = [round(elem)
                  for elem in 4095*(F+max(F))/(2*max(F))]
        plt.plot(t*max_ang_freq, F)
        plt.show()

    def generateSawWave(freq: float, dutyCycle: float):
        pass

    def generateSquareWave(freq: float, dutyCycle: float):
        # Duty cycle na forma 0.200 - 0.800
        qtd_pontos = 1000
        pontos = np.zeros(qtd_pontos)
        slice = np.r_[0:dutyCycle*qtd_pontos]
        pontos[slice] = 4095
        plt.plot(pontos)
        plt.show()

    def generateTriangleWave(freq: float, dutyCycle: float):
        pass

    def generateSineWave(freq: float, phase: float, amplitude: float):
        periodo = 1/freq
        # ===== Calculando a quantidade de pontos =====
        # Se frequencia < 100kHz usa um valor fixo máximo
        if freq < 10000:
            if freq < 100:
                qtd_pontos = int(100*freq)
            else:
                qtd_pontos = int(10*freq)
        else:
            qtd_pontos = 100000
        t = np.linspace(0, periodo, qtd_pontos)
        F = np.sin(2*math.pi*freq*t + phase)
        pontos = [round(elem)
                  for elem in 4095*(F+1)/2]
        plt.plot(t*2*math.pi*freq, F)
        plt.show()
