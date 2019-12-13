def first_n_smallest(arr, n):
    original = sorted(arr)[:n]
    return [original.pop(original.index(a)) for a in arr if a in original]
