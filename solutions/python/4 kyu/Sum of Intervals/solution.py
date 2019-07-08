def sum_of_intervals(intervals):
    current, *intervals = map(list, sorted(intervals, key=lambda i: i[0]))
    res = [current]

    for start, end in filter(lambda a: res[-1][0] > a[0] or res[-1][1] < a[1], intervals):
        if start <= res[-1][1] <= end:
            res[-1][1] = end
        else:
            res.append([start, end])

    return sum(b - a for a, b in res)