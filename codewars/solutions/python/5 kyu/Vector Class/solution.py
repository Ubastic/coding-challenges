import math
import operator


class Vector:
    def __init__(self, *args):
        self.x, self.y, self.z = self.args = tuple(args[0] if len(args) == 1 else args)
        self.magnitude = math.sqrt(sum(i ** 2 for i in self.args))

    def __str__(self):
        return '<{}>'.format(', '.join(map(str, self.args)))

    def __eq__(self, other):
        return self.args == other.args

    def __add__(self, other):
        return Vector(*map(operator.add, self.args, other.args))

    def __sub__(self, other):
        return Vector(*map(operator.sub, self.args, other.args))

    def dot(self, other):
        return sum(map(operator.mul, self.args, other.args))

    def to_tuple(self):
        return self.args

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )