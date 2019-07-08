from functools import partial

_class_private_attrs = ('_mro_', '_class_')


def _isinstance(x, A):
    return A in x._class_._mro_


def _type(x):
    return x._class_


def _class(*protos):
    def decorator(func):
        attributes = func()

        def cls(*args, **kwargs):
            def obj():
                pass

            _init_(obj, *args, **kwargs)

            for c in cls._mro_:
                for name, method in c._methods_.items():
                    setattr(obj, name, partial(method, obj))

            obj._mro_ = cls._mro_
            obj._class_ = cls._class_

            return obj

        cls._mro_ = (*protos, cls)
        cls._class_ = cls
        cls._methods_ = {**attributes}
        _init_ = next(c._methods_['_init_'] for c in reversed(cls._mro_) if '_init_' in c._methods_)

        return cls

    return decorator

__all__ = ['_class', '_isinstance', '_type']