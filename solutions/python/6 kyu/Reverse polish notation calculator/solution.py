from operator import add, sub, floordiv, mul, mod
import re


def calc(expr):
    if not expr:
        return 0

    operations = {'-': sub, '+': add, '*': mul, '/': floordiv, '%': mod}
    operands = [s for s in re.findall("[-+*/]|[0-9]*\.?[0-9]+", expr) if not s.isspace()]

    if not any(op in operands for op in operations):
        return float(operands[-1])

    stack = []
    while operands:
        op = operands.pop(0)
        if op in operations:
            b, a = stack.pop(), stack.pop()
            stack.append(operations[op](float(a), float(b)))
        else:
            stack.append(float(op))

    return stack[0]
