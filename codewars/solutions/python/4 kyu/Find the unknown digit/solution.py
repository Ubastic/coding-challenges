import re
REGEX = re.compile(r'[+\-*=]')

def solve_runes(runes: str):
    return next((
        i for i in range(1 if any(s.startswith('?') or len(s) == s.count('?') for s in REGEX.split(runes) if len(s) > 1) else 0, 10)
        if str(i) not in runes and eval(runes.replace('=', '==').replace('?', f'{i}'))
    ), -1)
