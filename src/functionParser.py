import re


class FunctionParser:
    def getFunc(string: str):
        result = re.search(
            r"(?:([0-9]*)[* \t]?)(?:(?:(cos))|(?:(sen|sin)))(?:[(](([0-9]*)[* ]*([t]?)[ +]*([0-9]*)|([0-9]*)[+ ]*([0-9]*)[ *]*([t]?))[)])", string)

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
            ang_freq = result.group(5) if result.group(5) is not None else 1
            fase = result.group(7)
        elif result.group(10) == 't':
            ang_freq = result.group(9) if result.group(9) is not None else 1
            fase = result.group(8)
        else:
            ang_freq = None

        if fase == '':
            fase = 0

        return (float(amp), func, float(ang_freq), float(fase))
