from operator import add, sub, floordiv, mul, mod
import re


def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


int_number, float_number = re.compile(r'\d+'), re.compile(r'\d+\.\d+')

operations_executors = {'-': sub, '+': add, '*': mul, '/': floordiv, '%': mod}
priority = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1}


def reverse_polish_notation(tokens):
    out, stack = [], []
    for token in tokens:
        if token in priority.keys():
            while len(stack) != 0 and stack[-1] in priority.keys():
                if not (priority[token] - priority[stack[-1]] <= 0):
                    break
                out.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while len(stack) != 0 and stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()
        else:
            out.append(token)
    while len(stack) != 0:
        out.append(stack.pop())
    return out


class Interpreter:
    def __init__(self):
        self.vars, self.stack = {}, []

    def __getitem__(self, operand=None):
        if isinstance(operand, (int, float)):
            return operand
        elif operand is None:
            return self.stack.pop()
        elif int_number.match(operand):
            return int(operand)
        elif float_number.match(operand):
            return float(operand)
        elif operand in self.vars:
            return self.vars[operand]
        
        raise ValueError()
        
    def polish_eval(self, operands):
        stack = []
        while operands:
            op = operands.pop(0)

            if op in operations_executors:
                b, a = stack.pop(), stack.pop()
                stack.append(operations_executors[op](self[a], self[b]))
            else:
                stack.append(self[op])

        if len(stack) > 1:
            raise ValueError()

        return stack[0]

    def input(self, expression):
        tokens = tokenize(expression)

        if len(tokens) < 1:
            return tokens[0] if tokens else ''

        self.stack, dest = [], None

        if '=' in tokens:
            dest = tokens[0]
            tokens = tokens[2:]

        value = self.polish_eval(reverse_polish_notation(tokens))

        if dest is not None:
            self.vars[dest] = value

        return value


interpreter = Interpreter()
