from itertools import product, chain
from functools import lru_cache


@lru_cache()
def balanced_parens(n):
    return ["()" * n] if n < 2 else [*set(chain.from_iterable(
        {a + b for a, b in product(balanced_parens(i), balanced_parens(n - i))} |
        {"(" * i + a + ")" * i for a in balanced_parens(n - i)} for i in range(1, n)
    ))]