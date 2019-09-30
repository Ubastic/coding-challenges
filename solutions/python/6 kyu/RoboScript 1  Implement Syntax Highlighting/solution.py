import re

REGEX = re.compile(r'\d+|F+|R+|L+|\(|\)')

COLORS = {
    'F': 'pink',
    'R': 'green',
    'L': 'red',
}


def highlight(code):
    return ''.join(
        c if c in '()' else f'<span style="color: {COLORS.get(c[0], "orange")}">{c}</span>'
        for c in REGEX.findall(code)
    )