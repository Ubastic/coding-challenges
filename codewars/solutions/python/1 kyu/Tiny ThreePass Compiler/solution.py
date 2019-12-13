import re
import operator

OPS = {"+": 'AD', "-": 'SU', "*": 'MU', "/": 'DI'}

PRIORITY = {"+": 0, "-": 0, "*": 1, "/": 1}
HANDLERS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}


def create_polish_notation(tokens):
    out, stack = [], []
    for token in tokens:
        if token in OPS:
            while stack and stack[-1] in OPS:
                if not (PRIORITY[token] - PRIORITY[stack[-1]] <= 0):
                    break
                out.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()
        else:
            out.append(token)
    return out + stack[::-1]


def to_leaf(op, a=None, b=None, n=None):
    return dict(({'a': a, 'b': b} if op in OPS else {'n': n}), op=op)


def create_ast(tokens, args):
    stack = []
    for token in tokens:
        if token in OPS:
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.append(to_leaf(token, arg1, arg2))
        else:
            if isinstance(token, int):
                stack.append(to_leaf('imm', n=token))
            else:
                stack.append(to_leaf('arg', n=args.index(token)))

    return stack.pop()


def optimize_ast(root):
    if root['op'] in OPS:
        if root['a']['op'] == 'imm' and root['b']['op'] == 'imm':
            root['n'] = HANDLERS[root['op']](root['a']['n'], root['b']['n'])
            root['op'] = 'imm'
            del root['a']
            del root['b']
            return True
        else:
            return optimize_ast(root['a']) or optimize_ast(root['b'])
    return False


def generate_code(root, cmd):
    if root['op'] in OPS:
        generate_code(root['a'], cmd)
        generate_code(root['b'], cmd)

        cmd.extend(['PO', 'SW', 'PO', OPS[root['op']], 'PU'])
    else:
        cmd.extend(['{} {}'.format(root['op'][:2].upper(), root['n']), 'PU'])


class Compiler(object):
    def compile(self, program):
        return self.pass3(self.pass2(self.pass1(program)))

    def tokenize(self, program):
        """Turn a program string into an array of tokens.  Each token
           is either '[', ']', '(', ')', '+', '-', '*', '/', a variable
           name or a number (as a string)"""
        token_iter = (m.group(0) for m in re.finditer(r'[-+*/()[\]]|[A-Za-z]+|\d+', program))
        return [int(tok) if tok.isdigit() else tok for tok in token_iter]

    def pass1(self, program):
        """Returns an un-optimized AST"""
        tokens = self.tokenize(program)
        func_args = tokens[tokens.index('[') + 1: tokens.index(']')]
        func_body = tokens[tokens.index(']') + 1:]

        return create_ast(create_polish_notation(func_body), func_args)

    def pass2(self, ast):
        """Returns an AST with constant expressions reduced"""
        while optimize_ast(ast):
            pass
        return ast

    def pass3(self, ast):
        """Returns assembly instructions"""
        cmd = []
        generate_code(ast, cmd)
        return cmd