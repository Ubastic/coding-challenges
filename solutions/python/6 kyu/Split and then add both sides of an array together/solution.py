def split_and_add(a, n):
    for _ in range(n):
        if len(a) < 2: break
        a = [sum(a) for a in zip(([0] if len(a) % 2 else []) + a[:len(a) // 2], a[len(a) // 2:])]

    return a