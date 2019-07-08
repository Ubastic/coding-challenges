from operator import add, sub, mul, floordiv

def factory(val):
    return lambda v=None: val if v is None else v(val)
def op_factory(op):
    return lambda val: lambda a: op(a, val)

for i, name in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
    globals()[name] = factory(i)
for name, op in zip(['plus', 'minus', 'times', 'divided_by'], [add, sub, mul, floordiv]):
    globals()[name] = op_factory(op)
