def loneliest(n):
    arr = [*map(int, str(n))]
    mapped = sorted((sum(arr[max(i - c, 0): i] + arr[i + 1: i + 1 + c]), c) for i, c in enumerate(arr))
    min_val = min(i for i, _ in mapped)
    return any(i == 1 and v == min_val for v, i in mapped)