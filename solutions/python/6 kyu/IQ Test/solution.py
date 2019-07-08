def iq_test(numbers):
    numbers, d = list(map(int, numbers.split())), {0: [], 1: []}
    for n in numbers:
        d[n % 2].append(n)
    return numbers.index(min(d.values(), key=len)[0]) + 1