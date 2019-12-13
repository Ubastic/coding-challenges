import re

NUMBER_REGEX = re.compile(r'([+\-])?(\d+)?(x)(\^\d+)?')


def differentiate(equation, point):
    def diff_part(sign, coff, _, power, point):
        power = int(power[1:]) - 1 if power else 0
        return int(f'{sign}1') * int(coff or 1) * (point ** power) * (power + 1)

    return sum(diff_part(*n, point) for n in NUMBER_REGEX.findall(equation))