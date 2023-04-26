import re


class FunctionParser:
    def getFunc(string: str):
        result = re.search(
            r"(?:([0-9]*)[* \t]?)(?:(?:(cos))|(?:(sen)))(?:[(](([0-9]*)[* ]*([t]?)[ +]*([0-9]*)|([0-9]*)[+ ]*([0-9]*)[ *]*([t]?))[)])", string)

        # ===== Pega amplitude =====
        if result.group(1) != '':
            amp = result.group(1)
        else:
            amp = 1

        # ===== Pega função =====
        if result.group(2) is not None:
            func = "cos"
        elif result.group(3) is not None:
            func = "sen"
        else:
            func = None

        # ===== Pega frequência e fase =====
        if result.group(6) == 't':
            freq = result.group(5)
            fase = result.group(7)
            if freq is None:
                freq = 1
        elif result.group(10) == 't':
            freq = result.group(9)
            fase = result.group(8)
            if freq is None:
                freq = 1
        else:
            freq = None

        if fase is None:
            fase = 0

        return (amp, func, freq, fase)
