from functionParser import *


class Main:
    def __init__(self, inputs):
        print(FunctionParser.getFunc(inputs[4]))


if __name__ == "__main__":
    inputs = ["cos(2t)",
              "23sen(8 + 3t)",
              "1cos(2t)",
              "2*cos(2t)",
              "20 cos(87t + 32)"]
    Main(inputs)
