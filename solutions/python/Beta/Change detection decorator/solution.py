import operator


def create_op(op):
    def first(self, other):
        return op(self.value, other) if self.value is not None else None

    def second(self, other):
        return op(other, self.value) if self.value is not None else None

    return first, second


class State(object):
    def __init__(self, value=None, get_change='', parent=None):
        self.parent = parent
        self.value = value
        self.get_change = get_change

    def __call__(self, *args, **kwargs):
        return self.value(self.parent, *args, **kwargs)

    def __nonzero__(self):
        return self.value is not None

    def __eq__(self, other):
        return self.value == other

    def __getattr__(self, item):
        return getattr(self.value, item, None)

    def __setattr__(self, key, value):
        try:
            val = super(State, self).__getattribute__('value')
            if val is not None and key in val.__dict__:
                setattr(self.value, key, value)
                return
        except:
            pass

        super(State, self).__setattr__(key, value)

    __add__, __radd__ = create_op(operator.add)
    __mul__, __rmul__ = create_op(operator.mul)
    __sub__, __rsub__ = create_op(operator.sub)


def change_detection(cls):
    class WithChangeDetection(cls):

        def __init__(self, *args, **kwargs):
            WithChangeDetection.__cache__ = {
                key: (value, 'INIT', self) for key, value in dict(cls.__dict__).items()
            }
            super(WithChangeDetection, self).__init__(*args, **kwargs)

        def __getattribute__(self, item):
            if item not in WithChangeDetection.__cache__:
                return State()

            return State(*WithChangeDetection.__cache__[item])

        def __setattr__(self, key, value):
            if key not in WithChangeDetection.__cache__:
                WithChangeDetection.__cache__[key] = (value, 'INIT', self)
            elif WithChangeDetection.__cache__[key][0] != value:
                WithChangeDetection.__cache__[key] = (value, 'MOD', self)

        def __delattr__(self, item):
            WithChangeDetection.__cache__[item] = (None, 'DEL', self)

    return WithChangeDetection