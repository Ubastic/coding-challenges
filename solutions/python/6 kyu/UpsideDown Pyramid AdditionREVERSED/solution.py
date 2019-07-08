def reverse(right):
    arr = [[i] for i in right]

    for i, a in enumerate(arr[1:], 1):
        for j in range(i):
            a.insert(0, arr[i - 1][-j - 1] - a[0])

    return arr[-1]
