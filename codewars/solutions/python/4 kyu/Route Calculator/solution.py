import operator
import re

PRIORITY = {"+": 0, "-": 0, "*": 1, "$": 1}
HANDLERS = {"+": operator.add, "-": operator.sub, "*": operator.mul, '$': operator.truediv}


def create_polish_notation(tokens):
    out, stack = [], []
    for token in tokens:
        if token in HANDLERS:
            while stack and stack[-1] in HANDLERS:
                if not (PRIORITY[token] - PRIORITY[stack[-1]] <= 0):
                    break
                out.append(stack.pop())
            stack.append(token)
        else:
            out.append(token)
    return out + stack[::-1]


def calculate_polish_notation(tokens):
    stack = []

    for token in tokens:
        if token in HANDLERS:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = HANDLERS[token](arg1, arg2)
            stack.append(result)
        else:
            stack.append(token)

    return stack.pop()


def tokenize(expression):
    token_iter = (m.group(0) for m in re.finditer(r"[-+*$]|(\d+\.?\d*)", expression))
    return [int(tok) if tok.isdigit() else tok for tok in token_iter]


def calculate(expression):
    if any(s not in '.0123456789+-*$' for s in expression):
        return "400: Bad request"

    return float(calculate_polish_notation(create_polish_notation(tokenize(expression))))
