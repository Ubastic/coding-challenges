import re
import contextlib
import typing


def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile(r"\s*(->|[-+*/%=(){},]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+|.+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


SELF = object()


def to_iterable(obj):
    return obj if isinstance(obj, typing.Iterable) and not isinstance(obj, str) else [obj]


class Rule:
    def __init__(self, *args, cls=None):
        self.rules = args
        self.cls = cls

    def __repr__(self):
        return f"{type(self).__name__}({self.rules!r})"

    def __or__(self, other):
        return OrRule(self, other)

    def create(self, obj):
        return obj if not self.cls else self.cls.func(*to_iterable(obj))

    def parse(self, tokens):
        results = []
        for r in self.rules:
            res = r.parse(tokens)

            if res:
                res, tokens = res
                results.append(res)
            else:
                return
        else:
            return self.create(results), tokens


class OptionalRule(Rule):
    def parse(self, tokens):
        res = super().parse(tokens)

        if res:
            res, tokens = res
            return self.create(res), tokens

        return None, tokens


class StrRule(Rule):
    def parse(self, tokens):
        if tokens and self.rules[0] == tokens[0]:
            return self.create(tokens[0]), tokens[1:]


class ReRule(Rule):
    def parse(self, tokens):
        if tokens and self.rules[0].match(tokens[0]):
            return self.create(tokens[0]), tokens[1:]


class OrRule(OptionalRule):
    def parse(self, tokens):
        for r in self.rules:
            res = r.parse(tokens)

            if res:
                res, tokens = res
                return self.create(res), tokens


class T:
    def __init__(self):
        self.stack = []

    def __getitem__(self, item):
        if not isinstance(item, tuple):
            if hasattr(item, '__node__'):
                return self[item.__node__]
            elif isinstance(item, NodeMeta):
                r = item.rule
                return type(r)(*r.rules, cls=r.cls)
            elif isinstance(item, list):
                return OptionalRule(*(self[i] for i in item))
            elif isinstance(item, str):
                return StrRule(item)
            elif item is SELF:
                return self.stack[0]
            else:
                return ReRule(item)

        rule = Rule()
        self.stack.append(rule)
        rule.rules = [t[i] for i in item]
        self.stack.pop()

        return rule


t = T()


class NodeMeta(type):
    def __new__(mcs, *args, **kwargs):
        cls = super().__new__(mcs, *args, **kwargs)
        with contextlib.suppress(AttributeError):
            cls.rule.cls = cls

        return cls


class Node(metaclass=NodeMeta):
    rule: Rule = None
    func = None

    @classmethod
    def parse(cls, tokens):
        if cls.rule:
            return cls.rule.parse(tokens)


class Grammar:
    def __init__(self):
        self.nodes = []

    def parse(self, tokens):
        for node in reversed(self.nodes):
            with contextlib.suppress():
                res = node.parse(tokens)

                if res and not res[-1]:
                    return res

    def rule(self, _rule):
        def decorator(_func):
            temp = type(f'{_func.__name__.title()}Node', (Node,), {'rule': _rule, 'func': _func})
            self.nodes.append(temp)
            _func.__node__ = temp
            _func.parse = temp.parse

            return _func

        return decorator


grammar = Grammar()


def _to_target(obj):
    try:
        return str(obj.to_target())
    except AttributeError:
        return str(obj)


class Parameters:
    def __init__(self, *args, separator=','):
        self.separator = separator
        self.values = [*args]

    def __repr__(self):
        return f'{self.values!r}'

    def add(self, *args):
        self.values = [*args] + self.values
        return self

    def to_target(self):
        return self.separator.join(_to_target(e) for e in self.values)


class Lambda:
    def __init__(self, params, stmts):
        self.stmts = stmts
        self.params = params

    def to_target(self):
        params = _to_target(self.params) if self.params else ""
        stmt = _to_target(self.stmts) if self.stmts else ""
        return f'({params}){{{stmt}{";" if self.stmts else ""}}}'


class Function:
    def __init__(self, expression, parameters):
        self.expression = expression
        self.parameters = parameters

    def to_target(self):
        return f'{_to_target(self.expression)}({_to_target(self.parameters)})'


def create_params(first, others, separator=","):
    return others[-1].add(first) if others else Parameters(first, separator=separator)


@grammar.rule(t[re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)$')])
def name(first):
    return first


@grammar.rule(t[re.compile(r'^([A-Za-z_][A-Za-z0-9_]*|[0-9]*)$')])
def name_or_number(first):
    return first


@grammar.rule(t[name_or_number, [",", SELF]])
def lambda_param(first, others):
    return create_params(first, others)


@grammar.rule(t[name_or_number, [SELF]])
def lambda_stmt(first, others):
    return create_params(first, others, separator=';')


@grammar.rule(t["{", [lambda_param, "->"], [lambda_stmt], "}"])
def lambda_(_, lambda_param_, lambda_stmt_, __):
    return Lambda(lambda_param_[0] if lambda_param_ else None, lambda_stmt_[0] if lambda_stmt_ else None)


@grammar.rule(t[name_or_number] | t[lambda_])
def expression(first):
    return first


@grammar.rule(t[expression, [",", SELF]])
def parameters(first, others=None):
    return create_params(first, others)


@grammar.rule(t[expression, "(", [parameters], ")", [lambda_]] | t[expression, lambda_])
def function_(expression_, *args):
    try:
        _, parameters_, _, lambda_ = args
        parameters_ = Parameters(*(parameters_ or []), *([lambda_[0]] if lambda_ else []))
    except ValueError:
        parameters_ = args[0]

    return Function(expression_, parameters_)


def transpile(source):
    res = function_.parse(tokenize(source))
    return res[0].to_target() if res and not res[-1] else ''
