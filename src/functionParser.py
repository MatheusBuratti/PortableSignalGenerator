import re


class FunctionParser:
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
