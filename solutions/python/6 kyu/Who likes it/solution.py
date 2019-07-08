def likes(names):
    return {0: 'no one likes this', 1: '{} likes this', 2: '{} and {} like this', 3: '{}, {} and {} like this', }.get(
        len(names)).format(*names) if len(names) < 4 else '{}, {} and {} others like this'.format(names[0], names[1], len(names) - 2)
