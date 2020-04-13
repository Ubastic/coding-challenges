import operator


def create_op(op):
    def first(self, other):
        return op(self.value, other) if self else None

    def second(self, other):
        return op(other, self.value) if self else None

    return first, second


class State:
    def __init__(self, value, get_change, parent):
        self.parent = parent
        self.value = value
        self.get_change = get_change

    def __call__(self, *args, **kwargs):
        return self.value(self.parent, *args, **kwargs)

    def __bool__(self):
        return self.value is not None

    def __eq__(self, other):
        return self.value == other

    def __getattr__(self, item):
        return getattr(self.value, item, None)

    def __setattr__(self, key, value):
        try:
            val = super().__getattribute__('value')
            if val is not None and key in val.__dict__:
                setattr(self.value, key, value)
                return
        except:
            pass

        super().__setattr__(key, value)

    __add__, __radd__ = create_op(operator.add)
    __mul__, __rmul__ = create_op(operator.mul)
    __sub__, __rsub__ = create_op(operator.sub)


def change_detection(cls):
    cache = {}

    class WithChangeDetection(cls):
        def __init__(self, *args, **kwargs):
            cache.update({key: (value, 'INIT', self) for key, value in cls.__dict__.items()})
            super(WithChangeDetection, self).__init__(*args, **kwargs)

        def __getattribute__(self, item):
            return State(*cache.get(item, (None, '', self)))

        def __setattr__(self, key, value):
            if key not in cache:
                cache[key] = (value, 'INIT', self)
            elif cache[key][0] is not value:
                cache[key] = (value, 'MOD', self)

        def __delattr__(self, item):
            cache[item] = (None, 'DEL', self)

    return WithChangeDetection