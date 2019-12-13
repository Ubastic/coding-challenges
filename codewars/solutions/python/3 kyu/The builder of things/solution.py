def name_func(name):
    return name[:-1] if name.endswith('s') else name


def make_callable(obj):
    if obj is None:
        return lambda item: item

    return obj if callable(obj) else lambda *args: obj


class Get(object):
    def __init__(self, parent, holder):
        self.parent = parent
        self.holder = holder

    def __getattr__(self, item):
        return getattr(self.holder, item) if hasattr(self.holder, item) else getattr(self.parent, item)


class Setter(object):
    def __init__(self, parent, value=None, name=None):
        self.names = make_callable(name)
        self.value = make_callable(value)
        self.parent = parent

    def __getattr__(self, item):
        value = self.value(item)
        setattr(self.parent, self.names(item), value)
        return Get(self.parent, value)


class Has(object):
    def __init__(self, parent):
        self.parent = parent

    def __call__(self, args):
        def one_object(item):
            return Thing(name_func(item), **{name_func(item): True})

        def many_objects(item):
            return ForEach(one_object(item) for _ in range(args))

        return Setter(self.parent, one_object if args == 1 else many_objects)

    def __getattr__(self, item):
        return Setter(self.parent, name=item)


class ForEach(tuple):
    @property
    def each(self):
        return Thing(__parent__=self)

    @property
    def and_the(self):
        return Thing(__parent__=self)

    def __getattr__(self, item):
        return getattr(Thing(__parent__=self), item)

    def __setattr__(self, key, value):
        for thing in self:
            setattr(thing, key, value)


class Callable(object):
    def __init__(self, parent, func_name=None):
        self.func_name = func_name
        self.parent = parent

    def __getattr__(self, item):
        return Callable(self.parent, item)

    def __call__(self, func, store_to=None):
        if store_to is not None:
            store_to_list = []
            setattr(self.parent, store_to, store_to_list)

        func.__globals__['name'] = self.parent.name

        def inner(*args, **kwargs):
            result = func(*args, **kwargs)

            if store_to is not None:
                store_to_list.append(result)

            return result

        setattr(self.parent, self.func_name, inner)


class Thing(object):
    def __init__(self, name='', **kwargs):
        parent = kwargs.pop('__parent__', self)
        self.name = name
        self.is_a = Setter(parent, True, "is_a_{}".format)
        self.is_not_a = Setter(parent, False, "is_a_{}".format)
        self.being_the = self.is_the = self.has = self.having = Has(parent)
        self.can = Callable(self)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __getattr__(self, item):
        return getattr(self.being_the, item)
