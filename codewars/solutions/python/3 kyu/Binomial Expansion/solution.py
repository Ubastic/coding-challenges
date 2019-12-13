import re
from math import factorial

TOKENS_REGEX = re.compile(r'(?P<sign>[+\-]?)(?P<number>\d*)(?P<var>\w?)')


def pascals_triangle(n) -> list:
    return [int((factorial(n)) / ((factorial(r)) * factorial(n - r))) for r in range(n + 1)]


def parse_num(n: str) -> tuple:
    r = TOKENS_REGEX.match(n).groupdict()
    return r['var'], int(f'{r["sign"]}{r["number"] if r["number"] != "" else 1}')


def format_part(n: int, var: str, power: int, first: bool = False) -> str:
    if abs(n) == 1 and power >= 1:
        r = f'{n:+}'[0] + var + (f'^{power}' * (power != 1))
    elif abs(n) != 1 and power == 1:
        r = f'{n:+}{var}'
    elif power == 0:
        r = f'{n:+}'
    else:
        r = f'{n:+}{var}^{power}'
    r = r[1:] if first and r[0] == '+' else r
    return (r + '1') if len(r) == 1 and r in '-+' else r


def expand(expr):
    a, b, power = filter(bool, map(''.join, TOKENS_REGEX.findall(expr)))
    b, power, (var, a) = int(b), int(power), parse_num(a)

    if power in (0, 1):
        return format_part(a, var, power, first=True) + (format_part(b, '', 1) if b else '') if power else '1'
    if b == 0:
        return format_part(a, var, power, first=True)
    return ''.join(
        format_part(n, var, power - i, i == 0) for i, n in
        ((j, int(p * a ** (power - j) * b ** j)) for j, p in zip(range(power + 1), pascals_triangle(power))) if n
    )