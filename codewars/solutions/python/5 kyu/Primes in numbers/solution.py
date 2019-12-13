def factors(n):
    d = 2
    while d * d <= n:
        while n > 1:
            c = 0
            while n % d == 0:
                c += 1
                n = n // d

            if c:
                yield d, c

            d += 1


def primeFactors(n):
    return ''.join(f'({i}{f"**{p}" * (p > 1)})' for i, p in factors(n))