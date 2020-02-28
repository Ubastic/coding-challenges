from operator import add, sub, floordiv, mul, mod
import re


def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


operations_executors = {'-': sub, '+': add, '*': mul, '/': floordiv, '%': mod}
priority = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1}


def to_rpn(tokens):
    out, stack = [], []
    for token in tokens:
        if token in priority.keys():
            while len(stack) != 0 and stack[-1] in priority.keys():
                if not (priority[token] - priority[stack[-1]] <= 0):
                    break
                out.append(stack.pop())
            stack.append(token)
        else:
            out.append(token)

    return out + stack[::-1]


class Calculator(object):
    def evaluate(self, string):
        print(string)
        return round(self._eval(to_rpn(tokenize(string))), 3)

    def _eval(self, operands):
        stack = []
        while operands:
            op = operands.pop(0)
            if op in operations_executors:
                b, a = stack.pop(), stack.pop()
                stack.append(operations_executors[op](float(a), float(b)))
            else:
                stack.append(float(op))

        return stack[0]