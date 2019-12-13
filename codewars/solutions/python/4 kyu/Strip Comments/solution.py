def solution(string, markers):
    lines = []
    for s in string.split('\n'):
        for m in markers:
            s = s.split(m)[0].strip()

        lines.append(s)

    return '\n'.join(lines)