import math

class Vector:
    def __init__(self, vector):
        self.data = tuple(vector)
    
    def __str__(self):
        return '({})'.format(','.join(map(str, self.data)))
    
    def _map_vector(self, vector, operator):
        assert len(self.data) == len(vector.data)
        return Vector([operator(a, b) for a, b in zip(self.data, vector.data)])

    def add(self, vector):
        return self._map_vector(vector, lambda a, b: a + b)

    def subtract(self, vector):
        return self._map_vector(vector, lambda a, b: a - b)

    def dot(self, vector):
        return sum(self._map_vector(vector,  lambda a, b: a * b).data)

    def norm(self):
        return math.sqrt(sum(a ** 2 for a in self.data))
    
    def equals(self, vector):
        return self.data == vector.data