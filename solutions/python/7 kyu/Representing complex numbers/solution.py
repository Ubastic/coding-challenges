class Complex:
    real = property(lambda self: self._value.real)
    imaginary = property(lambda self: self._value.imag)

    def __init__(self, real, compl):
        self._value = complex(real, compl)

    def __add__(self, other):
        new = self._value + other._value
        return Complex(new.real, new.imag)

    def __mul__(self, other):
        new = self._value * other._value
        return Complex(new.real, new.imag)