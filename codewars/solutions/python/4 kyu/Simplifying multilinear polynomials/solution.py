import re
import collections
import functools

PART_REGEX = re.compile(r'([+-])?(\d+)?(\w+)')


class Poly:
    def __init__(self, sign, cof, polys):
        self.cof = int(f'{sign}1') * (int(cof or 1) if isinstance(cof, str) else cof)
        self.polys = ''.join(sorted(polys))

    def __add__(self, other):
        return Poly('', self.cof + other.cof, self.polys)

    def __lt__(self, other):
        return self.polys < other.polys if len(self.polys) == len(other.polys) else len(self.polys) < len(other.polys)

    def to_str(self, pos=0):
        if self.cof == 0:
            return ''

        prefix = f'{"+" if self.cof > 0 and pos != 0 else ""}{"-" if self.cof == -1 else ""}' \
            f'{self.cof if abs(self.cof) != 1 else ""}'
        return f'{prefix}{self.polys}'


def simplify(poly):
    all_polys = collections.defaultdict(list)
    for sign, cof, polys in PART_REGEX.findall(poly):
        p = Poly(sign, cof, polys)
        all_polys[p.polys] = [functools.reduce(lambda a, b: a + b, all_polys[p.polys], p)]

    return ''.join(p.to_str(i) for i, (p, *_) in enumerate(sorted(all_polys.values())))
