from collections import OrderedDict

ROMAN = OrderedDict(zip(
    [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
    ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
))
NUMBERS = {value: key for key, value in ROMAN.items()}


class RomanNumerals(object):
    @staticmethod
    def to_roman(n):
        def roman_num(num):
            for r in ROMAN.keys():
                x, y = divmod(num, r)
                yield ROMAN[r] * x
                num -= (r * x)
                if num > 0:
                    roman_num(num)
                else:
                    break

        return ''.join([a for a in roman_num(n)])

    @staticmethod
    def from_roman(n):
        value, max_val = 0, 1
        for i in map(lambda key: NUMBERS[key], reversed(str(n))):
            value += -i if i < max_val else i
            max_val = max((max_val, i))
        return value
