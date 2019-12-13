import operator
from functools import reduce

ARITHMETIC = ['add', 'sub', 'mul', 'div', 'and', 'or', 'xor']
REGS = 'abcd'


def arithmetic_op(op):
    def inner(self: 'Machine', val: str, dest: str = 'a', push: str = None):
        if push is not None:
            self.cpu.write_stack(self.cpu.read_reg(push))

        self.cpu.write_reg(dest, reduce(op, self.stack(self.value_of(val))))

    return inner


def stack_op(op, regs):
    def inner(self: 'Machine'):
        for reg in regs:
            op(self, reg)

    return inner


class Machine(object):

    def __init__(self, cpu: 'CPU'):
        self.cpu = cpu

    def execute(self, instr: str):
        kwargs = {}
        name, *args = map(str.strip, instr.replace(',', ' ').strip().split())

        if any(name.startswith(s) and name != s for s in ARITHMETIC):
            reg, name = name[-1], name[:-1]
            kwargs = {'push': reg}

        return getattr(self, name)(*args, **kwargs)

    def value_of(self, var: str):
        return int(var) if var.isdigit() else self.cpu.read_reg(var)

    def stack(self, size: int):
        yield from (self.cpu.pop_stack() for _ in range(size))

    # Stack operations
    def push(self, val: str):
        self.cpu.write_stack(self.value_of(val))

    def pop(self, val=None):
        if val is None:
            self.cpu.pop_stack()
        else:
            self.cpu.write_reg(val, self.cpu.pop_stack())

    locals().update({
        'pushr': stack_op(push, REGS),
        'pushrr': stack_op(push, REGS[::-1]),
        'popr': stack_op(pop, REGS[::-1]),
        'poprr': stack_op(pop, REGS),
    })

    # Misc operations
    def mov(self, src: str, dest: str):
        self.cpu.write_reg(dest, self.value_of(src))

    # Arithmetic operations
    locals().update({
        'add': arithmetic_op(operator.add),
        'sub': arithmetic_op(operator.sub),
        'mul': arithmetic_op(operator.mul),
        'div': arithmetic_op(operator.floordiv),
        'and': arithmetic_op(operator.and_),
        'or': arithmetic_op(operator.or_),
        'xor': arithmetic_op(operator.xor),
    })