from functools import wraps
from types import FunctionType


class Debugger(object):
    attribute_accesses = []
    method_calls = []

    @classmethod
    def method(cls, func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            cls.method_calls.append({
                'class': type(self), 'method': func.__name__, 'args': (self,) + args, 'kwargs': kwargs
            })
            return func(self, *args, **kwargs)

        return inner

    @classmethod
    def attr(cls, func_type):
        def func(self, name, value=None):
            if func_type == 'set':
                super(type(self), self).__setattr__(name, value)
            else:
                value = super(type(self), self).__getattribute__(name)

            cls.attribute_accesses.append({
                'action': func_type, 'class': type(self), 'attribute': name, 'value': value
            })
            return value

        return func


class Meta(type):
    def __new__(mcs, name, bases=None, namespace=None):
        for key, value in filter(lambda (key, value): isinstance(value, FunctionType), namespace.items()):
            namespace[key] = Debugger.method(value)

        namespace.update(__setattr__=Debugger.attr('set'), __getattribute__=Debugger.attr('get'))

        return super(Meta, mcs).__new__(mcs, name, bases, namespace)
