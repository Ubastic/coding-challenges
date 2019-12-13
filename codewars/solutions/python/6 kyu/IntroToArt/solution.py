def get_w(height):
    if height <= 1:
        return []

    middle = height * 2 - 1
    arr = [[' '] * (height * 4 - 3) for _ in range(height)]
    for i, a in enumerate(arr):
        a[i] = a[-i - 1] = a[middle - i - 1] = a[middle - 1 + i] = '*'

    return [''.join(a) for a in arr]