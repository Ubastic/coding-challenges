import re
import contextlib
import typing


def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile(r"\s*(->|<|>|\.|[-+*/%=(){},]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+|.+)\s*")
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


class RefRule:
    def __init__(self, name):
        self.__wrapper = None
        self.name = name

    @property
    def _wrapper(self):
        if self.__wrapper is None:
            self.__wrapper = globals()[self.name]
        return self.__wrapper

    def __getattr__(self, item):
        return getattr(self._wrapper, item)


def ref(s):
    return RefRule(s)


class T:
    def __init__(self):
        self.stack = []

    def __getitem__(self, item):
        if not isinstance(item, tuple):
            if isinstance(item, RefRule):
                return item
            elif hasattr(item, '__node__'):
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

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return iter(self.values)

    def add(self, *args):
        self.values = [*args] + self.values
        return self

    def to_target(self):
        return self.separator.join(_to_target(e) for e in self.values)


class Function:
    def __init__(self, params, return_type):
        self.params = params
        self.return_type = return_type

    def to_target(self):
        result = [*self.params, self.return_type]
        return f'Function{len(self.params)}<{",".join(r.to_target() for r in result)}>'


def create_params(first, others, separator=","):
    try:
        return others[-1].add(first) if others else Parameters(first, separator=separator)
    except:
        return Parameters(first, others[-1], separator=separator)


class TypeParamAny:
    def to_target(self):
        return '?'


class TypeParamType:
    def __init__(self, tp):
        self.tp = tp

    def to_target(self):
        return self.tp.to_target()


class TypeParamWithLimitation:
    def __init__(self, limitation, tp):
        self.limitation = limitation
        self.tp = tp

    def to_target(self):
        if self.limitation == "in":
            return "? super " + self.tp.to_target()
        else:
            return "? extends " + self.tp.to_target()


class SimpleUserType:
    def __init__(self, name, type_params):
        self.type_params = type_params
        self.name = name

    def to_target(self):
        return self.name.to_target() + ("<" + self.type_params.to_target() + ">" if self.type_params else "")


class UserType:
    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail

    def to_target(self):
        if self.tail:
            return self.head.to_target() + "." + self.tail.to_target()

        return self.head.to_target()


class Identifier:
    def __init__(self, value):
        self.value = value

    def to_target(self):
        return self.value


NAME_MAPPING = {
    'Int': 'Integer',
    'Unit': 'Void',
}


@grammar.rule(t[re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)$')])
def name(first):
    return Identifier(NAME_MAPPING.get(first, first))


@grammar.rule(t['*'] |
              t['in', ref('type_')] |
              t['out', ref('type_')] |
              t[ref('type_')])
def typeParam(first, other=None):
    if other is None:
        if first == "*":
            return TypeParamAny()
        else:
            return TypeParamType(first)

    return TypeParamWithLimitation(first, other)


@grammar.rule(t[typeParam, [',', SELF]])
def typeParams(first, others=None):
    return create_params(first, others)


@grammar.rule(t[name, ['<', typeParams, '>']])
def simpleUserType(*args):
    return SimpleUserType(args[0], args[1][1] if args[1] else Parameters())


@grammar.rule(t[simpleUserType, ['.', SELF]])
def userType(first, other=None):
    return UserType(first, (other or (None, None))[1])


@grammar.rule(t[ref('type_'), [',', SELF]])
def parameters(first, others=None):
    return create_params(first, others)


@grammar.rule(t['(', [parameters], ')', '->', ref('type_')])
def functionType(*args):
    return Function(args[1][0] if args[1] else Parameters(), args[-1])


@grammar.rule(t[userType] |
              t[functionType] |
              t[name])
def type_(first):
    return first


def transpile(source):
    res = type_.parse(tokenize(source))
    return res[0].to_target() if res and not res[-1] else None
