def square_digits_sequence(n):
    values = {n}

    while True:
        n = sum(int(i) ** 2 for i in str(n))

        if n in values:
            return len(values) + 1

        values.add(n)