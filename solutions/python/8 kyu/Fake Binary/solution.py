def fake_bin(x):
    return ''.join(['0' if n < '5' else '1' for n in x])