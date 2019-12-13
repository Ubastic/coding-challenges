def fusc(n):
    if n <= 1:
        return n
    if n % 2:
        n //= 2
        return fusc(n) + fusc(n + 1)
    else:
        return fusc(n // 2)

