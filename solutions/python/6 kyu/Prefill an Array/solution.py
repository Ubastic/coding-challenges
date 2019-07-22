def prefill(n, v=0):
    if not ((isinstance(n, int) and n >= 0) or (isinstance(n, str) and n.isdigit() and int(n) >= 0)):
        raise TypeError(f"{n} is invalid")
    return [v] * int(n)
