import re

from collections import ChainMap
from functools import reduce
from itertools import chain


class Num:
    def __init__(self, name, cof=1):
        self.name = name
        self.cof = cof

    def __iter__(self):
        yield self

    def __add__(self, other):
        if isinstance(other, Nums):
            return other + self
        if self.name != other.name:
            return Nums(self, other)

        return Num(self.name, self.cof + other.cof)

    def __mul__(self, other):
        return Num(self.name, self.cof * other)

    def __rmul__(self, other):
        return self * other


class Nums(Num):
    def __init__(self, *nums):
        self.nums = nums

    def __iter__(self):
        yield from self.nums

    def __add__(self, other):
        nums = {}
        for n in chain(self, other):
            nums[n.name] = nums[n.name] + n if n.name in nums else n

        return Nums(*nums.values())

    def __mul__(self, other):
        return Nums(*(num * other for num in self.nums))


def parse(example):
    valid = re.sub(r'(\d+)(\s*[^+\-*/])', lambda m: '*'.join(m.groups()), example)
    without_sub = valid.replace('-', '+ -1 *')

    formula = [m.group() for m in re.finditer(r'(-?\d)+|[a-zA-Z]+|[+\-*/()=]', without_sub)]
    namespace = {n: Num(n) for n in filter(str.isalpha, formula)}

    if '=' in formula:
        left, right = ''.join(formula).split('=')
        return {right: eval(left, namespace)}
    else:
        return eval(''.join(formula), namespace)


def transform(formulas, a, b):
    return a if a.name == b else reduce(
        lambda a, b: a + b, a.cof * Nums(*(transform(formulas, f, b) for f in formulas[a.name]))
    )


def simplify(examples, formula):
    formulas = {**ChainMap(*(parse(e) for e in examples))}
    missed, = {r.name for n in formulas.values() for r in n} - {*formulas}
    answer = reduce(lambda a, b: a + b, (transform(formulas, n, missed) for n in parse(formula)))

    return f'{answer.cof}{answer.name}'