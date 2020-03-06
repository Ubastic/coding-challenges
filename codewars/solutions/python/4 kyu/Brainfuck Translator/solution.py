from itertools import groupby
from re import sub


def gen_code(source_code, ident=0):
    for c, group in groupby(source_code):
        if c in ('+', '-'):
            yield f'{"  " * ident}*p {c}= {len([*group])};'
        elif c == '<':
            yield f'{"  " * ident}p -= {len([*group])};'
        elif c == '>':
            yield f'{"  " * ident}p += {len([*group])};'
        elif c == '.':
            for _ in group:
                yield f'{"  " * ident}putchar(*p);'
        elif c == ',':
            for _ in group:
                yield f'{"  " * ident}*p = getchar();'
        elif c == '[':
            for _ in group:
                yield f'{"  " * ident}if (*p) do {{'
                ident += 1
        elif c == ']':
            for _ in group:
                assert ident > 0
                yield f'{"  " * (ident - 1)}}} while (*p);'
                ident -= 1

    assert ident == 0


USELESS = ('-+', '+-', '<>', '><', '[]')


def brainfuck_to_c(source_code):
    source_code = sub(r'[^+-<>,.\[\]]', '', source_code)

    while any(useless in source_code for useless in USELESS):
        for useless in USELESS:
            while useless in source_code:
                source_code = source_code.replace(useless, '')

    try:
        return ('\n'.join(gen_code(source_code)) + '\n').lstrip()
    except AssertionError:
        return 'Error!'