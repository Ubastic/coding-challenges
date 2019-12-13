def dashatize(num):
    return ''.join(f'-{c}-' if int(c) % 2 else c for c in str(abs(num))).replace('--', '-').strip('-') if num is not None else "None"
