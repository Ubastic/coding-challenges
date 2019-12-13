def seq_to_one(n):
    return list(range(n, 0 if n > 1 else 2, -1 if n > 1 else 1))
