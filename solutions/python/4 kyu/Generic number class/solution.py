def create_number_class(alphabet):
    class Number(object):
        base = alphabet

        def __init__(self, value):
            if isinstance(value, int):
                self.value = value
            else:
                base, alph = len(self.base), self.base
                self.value = sum(alph.index(s) * base ** i for i, s in enumerate(value[::-1]))

        def __str__(self):
            base_len, value, result = len(self.base), self.value, ''
            while value:
                result += self.base[value % base_len]
                value //= base_len

            return result[::-1] if result else self.base[0]

        def __add__(self, other):
            return Number(self.value + other.value)

        def __sub__(self, other):
            return Number(self.value - other.value)

        def __mul__(self, other):
            return Number(self.value * other.value)

        def __floordiv__(self, other):
            return Number(self.value // other.value)

        def convert_to(self, other):
            return other(self.value)

    return Number