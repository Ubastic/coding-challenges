from textwrap import wrap


def justify(text, width):
    lines = wrap(text, width)

    def justify_line(line):
        spaces = line.count(' ')

        if not spaces:
            return line

        n, r = divmod(width - sum(map(len, line)), spaces)
        subs = ' ' * (n + 1)
        return line.replace(' ', subs).replace(subs, subs + ' ', r)

    return '\n'.join([*map(justify_line, lines[:-1]), lines[-1]])