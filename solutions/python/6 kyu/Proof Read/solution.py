from itertools import takewhile


def proofread(ss):
    return '.'.join(
        ''.join(takewhile(lambda c: c == ' ', s)) +
        s.lstrip().lower().replace('ie', 'ei').capitalize()

        for s in ss.split('.')
    )
