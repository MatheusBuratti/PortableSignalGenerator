import math
import re
import numpy as np
import matplotlib.pyplot as plt
from functionParser import *
from functools import reduce


class Main:
    def __init__(self, input: str):
        # ===== Pegando a função a partir da entrada =====
        self.functions = FunctionParser.getFunc(input)
        print(self.functions)

        self.max_ang_freq = max(self.functions, key=lambda item: item[3])[2]
        self.freq = self.max_ang_freq/2*math.pi

        # TODO:
        # Resolver o calculo do período da soma

        self.periodo = 48*math.pi/np.lcm.reduce(
            [int(x[2]) for x in self.functions])
        print(self.periodo)

        # ===== Calculando a quantidade de pontos =====
        # Se frequencia < 100kHz usa um valor fixo máximo
        self.qtd_pontos = int(100*self.freq) \
            if self.freq > 10000  \
            else 1000000

        self.evaluate()

        plt.plot(self.t, self.F)
        plt.show()

    # Calcula o valor das funções para todos os pontos dentro de 1 período da função de menor freq. ang.
    def evaluate(self):
        self.t = np.linspace(0, self.periodo, self.qtd_pontos)
        F = list()
        for function in self.functions:
            F.append(np.cos(function[2]*self.t + function[3])*function[0]
                     if function[1] == "cos"
                     else np.sin(function[2]*self.t + function[3])*function[0])
        self.F = np.sum(F, axis=0)


if __name__ == "__main__":
    input = input()
    Main(input)
