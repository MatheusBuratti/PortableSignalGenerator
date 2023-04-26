import math
import numpy as np
import matplotlib.pyplot as plt
from functionParser import *


class Main:
    def __init__(self, input):
        # ===== Pegando a função a partir da entrada =====
        (self.amp, self.func, self.ang_freq,
         self.fase) = FunctionParser.getFunc(input)
        if self.func is None:
            raise Exception("Problema com a entrada!")
        self.freq = self.ang_freq/2*math.pi
        self.periodo = 2*math.pi/self.ang_freq

        # ===== Calculando a quantidade de pontos =====
        # Se frequencia < 100kHz usa um valor fixo máximo
        self.qtd_pontos = int(10*self.freq) \
            if self.freq < 100000  \
            else 1000000

        self.evaluate()

        plt.plot(self.wt, self.F)
        plt.show()

    # Calcula o valor da função para todos os pontos dentro de 1 período
    def evaluate(self):
        self.t = np.linspace(0, self.periodo, self.qtd_pontos)
        self.wt = self.t * self.ang_freq
        self.F = np.cos(self.wt + self.fase) \
            if self.func == "cos" \
            else np.sin(self.wt + self.fase)
        self.F *= self.amp


if __name__ == "__main__":
    input = "30 sin(31415t)"
    Main(input)
