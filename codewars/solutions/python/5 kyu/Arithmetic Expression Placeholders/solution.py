def unwrap(obj, x):
    return obj.do(x) if hasattr(obj, "do") else obj


class Placeholder:
    def __init__(self, action=lambda x: next(x)):
        self.do = action

    def __call__(self, *args):
        return self.do(iter(args))

    def __add__(self, other):
        return Placeholder(lambda x: self.do(x) + unwrap(other, x))

    def __sub__(self, other):
        return Placeholder(lambda x: self.do(x) - unwrap(other, x))

    def __mul__(self, other):
        return Placeholder(lambda x: self.do(x) * unwrap(other, x))

    def __floordiv__(self, other):
        return Placeholder(lambda x: self.do(x) // unwrap(other, x))

    def __radd__(self, other):
        return Placeholder(lambda x: unwrap(other, x) + self.do(x))

    def __rsub__(self, other):
        return Placeholder(lambda x: unwrap(other, x) - self.do(x))

    def __rmul__(self, other):
        return Placeholder(lambda x: unwrap(other, x) * self.do(x))

    def __rfloordiv__(self, other):
        return Placeholder(lambda x: unwrap(other, x) // self.do(x))

x = Placeholder()