from functools import reduce


class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr):
        return reduce(lambda a, b: cls(b, a), reversed(arr), None) if arr else None

    def filter(self, fn):
        return self.from_array([*filter(fn, self.to_array())])

    def map(self, fn):
        return self.from_array([*map(fn, self.to_array())])