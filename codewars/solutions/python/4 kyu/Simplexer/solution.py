import re

TOKEN_TYPES = 'identifier string integer boolean keyword operator whitespace'.split()
KEYWORDS = 'if else for while return func break'.split()
OPERATORS = '+ - * / % ( ) ='.split()
BOOLEAN = 'true false'.split()


class Simplexer:
    __iter__ = lambda self: self
    __next__ = lambda self: next(self.iter)

    def __init__(self, expression):
        def g():
            for c in re.findall(r'\d+|\w+|\".*\"|[+\-*/%()=]|[$_\w]+[$_\w\d]+|\s+', expression):
                if c.isdigit():
                    yield Token(c, 'integer')
                elif c.isspace():
                    yield Token(c, 'whitespace')
                elif c in KEYWORDS:
                    yield Token(c, 'keyword')
                elif c in OPERATORS:
                    yield Token(c, 'operator')
                elif c in BOOLEAN:
                    yield Token(c, 'boolean')
                elif c.startswith('"') and c.endswith('"'):
                    yield Token(c, 'string')
                else:
                    yield Token(c, 'identifier')

        self.iter = iter(g())