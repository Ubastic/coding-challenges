def maxSequence(arr):
    if not arr:
        return 0

    m = arr[0]
    for i in range(len(arr) + 1):
        m = max((m, max((sum(arr[i:j]) for j in range(i + 1, len(arr) + 1)), default=m)))

    return m if m > 0 else 0
