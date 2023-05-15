import math
import numpy as np
import matplotlib.pyplot as plt
from functionParser import *


class Main:
    def __init__(self, input: str):
        # ===== Pegando a função a partir da entrada =====
        self.functions = FunctionParser.getFunc(input)
        print(self.functions)
        self.max_ang_freq = max(self.functions, key=lambda item: item[3])[2]
        self.freq = self.max_ang_freq/(2*math.pi)

        # TODO:
        # Resolver o calculo do período da soma
        # self.periodo = 2*math.pi/np.gcd.reduce(
        #      [int(x[2]) for x in self.functions])
        self.periodo = 1/self.freq

        # ===== Calculando a quantidade de pontos =====
        # Se frequencia < 100kHz usa um valor fixo máximo
        if self.freq < 10000:
            if self.freq < 100:
                self.qtd_pontos = int(100*self.freq)
            else:
                self.qtd_pontos = int(10*self.freq)
        else:
            self.qtd_pontos = 100000

        self.evaluate()

        print(self.freq)
        print(self.qtd_pontos)
        print([round(elem)
              for elem in 4095*(self.F+max(self.F))/(2*max(self.F))])

        plt.plot(self.t*self.max_ang_freq, self.F)
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
