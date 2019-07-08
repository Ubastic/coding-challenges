def tower_builder(n):
    return [' ' * (n - j) + '*' * i + ' ' * (n - j) for j, i in enumerate(range(1, n * 2 + 1, 2), 1)]
