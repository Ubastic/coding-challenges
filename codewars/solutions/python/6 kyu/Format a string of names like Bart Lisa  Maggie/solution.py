def namelist(names):
    if not names:
        return ''

    names = [d['name'] for d in names]
    return names[0] if len(names) == 1 else f'{", ".join(names[:-1])} & {names[-1]}'

