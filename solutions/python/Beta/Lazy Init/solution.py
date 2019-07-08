class LazyInit(type):
    def __new__(mcs, name, bases, namespace):
        init_args = namespace['__init__'].__code__.co_varnames[1:]

        def __init__(self, *args):
            self.__dict__.update(dict(zip(init_args, args)))

        namespace['__init__'] = __init__
        return super().__new__(mcs, name, bases, namespace)
