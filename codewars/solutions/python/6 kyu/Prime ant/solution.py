def is_prime(n):
    return next(iter(filter(lambda x: n % x == 0, xrange(2, n // 2 + 1))), -1)


def prime_ant(n):
    pos = 0
    arr = [2]

    for i in xrange(n):
        q = is_prime(arr[pos])

        if q == -1:
            pos += 1

            len_arr = len(arr)

            if len_arr <= pos:
                arr.append(len_arr + 2)

        else:
            arr[pos - 1] = arr[pos - 1] + q
            arr[pos] = arr[pos] / q

            pos -= 1

    return pos