from collections import namedtuple


def create_namedtuple_cls(cls_name, fields):
    class Child(namedtuple(cls_name, fields)):
        def __getattr__(self, item):
            return eval(f'self.{item}')

    Child.__name__ = cls_name
    return Child