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

int_number = re.compile(r'\d+')


class Base:
    def __init__(self, stack, variables, functions):
        self.functions, self.stack, self.vars = functions, stack, variables

    def __getitem__(self, operand=None):
        if isinstance(operand, int):
            return operand
        elif operand is None:
            return self.stack.pop()
        elif int_number.match(operand):
            return int(operand)
        elif operand in self.vars:
            return self.vars[operand]

        raise ValueError()

    def replace_functions_call(self, tokens):
        if not any(func in tokens for func in self.functions):
            return tokens

        for i, token in enumerate(tokens):
            if token in self.functions:
                func = self.functions[token]
                args_count, args = len(func), []

                i += 1

                for j, arg in enumerate(map(tokens.__getitem__, range(i, i + args_count)), i):
                    if arg in self.functions:
                        replaced = self.replace_functions_call(tokens[j:])
                        return self.replace_functions_call(tokens[:i] + replaced)
                    else:
                        args.append(arg)

                return self.replace_functions_call(tokens[:i - 1] + [func(args)] + tokens[i + args_count:])

    def replace_assigns(self, tokens):
        if '=' not in tokens:
            return tokens

        assign_index = tokens.index('=')

        destination, body = tokens[assign_index - 1], tokens[assign_index + 1:]

        if destination in self.functions:
            raise ValueError()

        if ')' in body and '(' not in body:
            body = body[:body.index(')')]

        value = self.eval(body)

        self.vars[destination] = value

        return tokens[:assign_index - 1:] + [value] + tokens[assign_index + len(body) + 1:]

    def to_rpn(self, tokens):
        tokens = self.replace_assigns(tokens)
        tokens = self.replace_functions_call(tokens)

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

    def eval(self, operands):
        operands = self.to_rpn(operands)

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


class Function(Base):
    def __init__(self, functions, args, body):
        super().__init__([], {}, functions)
        if any(arg not in body for arg in args) or len(args) != len(set(args)):
            raise ValueError()

        self.args, self.body = args, body

    def __len__(self):
        return len(self.args)

    def __call__(self, operands):
        if len(operands) != len(self.args):
            raise ValueError()

        self.vars = {arg: value for arg, value in zip(self.args, operands)}

        return self.eval(self.body)


class Interpreter(Base):
    def __init__(self):
        super().__init__([], {}, {})

    def input(self, expression):
        tokens = tokenize(expression)

        if len(tokens) < 1:
            return tokens[0] if tokens else ''

        self.stack = []

        if tokens[0] == 'fn':
            name, tokens = tokens[1], tokens[2:]

            if name in self.vars:
                raise ValueError()

            i = tokens.index('=>')

            self.functions[name] = Function(self.functions, tokens[:i], tokens[i + 1:])

            return ''

        return self.eval(tokens)


interpreter = Interpreter()
