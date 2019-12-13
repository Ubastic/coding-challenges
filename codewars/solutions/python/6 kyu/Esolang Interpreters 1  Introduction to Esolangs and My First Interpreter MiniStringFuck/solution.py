def my_first_interpreter(code):
    i, s = 0, ''
    for c in code:
        if c == '+':
            i = i + 1 if i != 255 else 0
        elif c == '.':
            s += chr(i)
    return s