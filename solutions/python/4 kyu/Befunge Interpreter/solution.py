from enum import Enum
from random import choice


class Direction(Enum):
    UP = -1, 0
    DOWN = 1, 0
    LEFT = 0, -1
    RIGHT = 0, 1

    def next(self, x, y, area):
        add_x, add_y = self.value
        x, y = x + add_x, y + add_y

        try:
            _ = area[x][y]
        except IndexError:
            if self == Direction.UP:
                x = len(area)
            elif self == Direction.DOWN:
                x = 0
            elif self == Direction.RIGHT:
                y = len(area[0])
            elif self == Direction.LEFT:
                y = 0

        return x, y


SIMPLE = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: b - a,
    '*': lambda a, b: a * b,
    '/': lambda a, b: b // a,
    '%': lambda a, b: (b % a) if a else 0,
    '!': lambda a: a == 0,
    '`': lambda a, b: int(bool(b > a)),
}
DIRECTIONS = {
    '>': Direction.RIGHT,
    '<': Direction.LEFT,
    '^': Direction.UP,
    'v': Direction.DOWN,
}


def interpret(code):
    area = [[*a] for a in code.splitlines()]
    x, y = 0, 0
    output = []
    stack = []
    direction = Direction.RIGHT

    while True:
        c: str = area[x][y]

        if c == '@':
            break
        elif c.isdigit():
            stack.append(int(c))
        elif c in SIMPLE:
            res = SIMPLE[c](*(stack.pop() for _ in range(SIMPLE[c].__code__.co_argcount)))
            stack.append(res)
        elif c in DIRECTIONS:
            direction = DIRECTIONS[c]
        elif c == '_':
            direction = Direction.RIGHT if stack.pop() == 0 else Direction.LEFT
        elif c == '|':
            direction = Direction.DOWN if stack.pop() == 0 else Direction.UP
        elif c == '"':
            while True:
                x, y = direction.next(x, y, area)
                c = area[x][y]
                if c == '"':
                    break
                stack.append(ord(c))
        elif c == ':':
            stack.append(stack[-1] if stack else 0)
        elif c == '\\':
            if len(stack) == 1:
                stack.append(0)
            else:
                stack[-1], stack[-2] = stack[-2], stack[-1]
        elif c == '$':
            stack.pop()
        elif c == '.':
            output.append(int(stack.pop()))
        elif c == ',':
            output.append(chr(stack.pop()))
        elif c == '#':
            x, y = direction.next(x, y, area)
        elif c == 'p':
            xx, yy, v = stack.pop(), stack.pop(), stack.pop()
            area[xx][yy] = chr(v)
        elif c == 'g':
            xx, yy = stack.pop(), stack.pop()
            stack.append(ord(area[xx][yy]))
        elif c == '?':
            direction = choice([*DIRECTIONS.values()])

        x, y = direction.next(x, y, area)

    return ''.join(map(str, output))