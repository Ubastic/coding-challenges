def _next_permutation(array):
    i = max(i for i in xrange(1, len(array)) if array[i - 1] < array[i])
    j = max(j for j in xrange(i, len(array)) if array[j] > array[i - 1])
    array[j], array[i - 1] = array[i - 1], array[j]
    array[i:] = reversed(array[i:])


def next_bigger(n):
    if n // 10 == 0:
        return -1

    array = list(str(n))
    try:
        _next_permutation(array)
    except ValueError:
        return -1    

    res = int(''.join(array))

    return -1 if res == n else res