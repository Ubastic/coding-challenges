def queue_time(customers, n):
    data = {i: 0 for i in range(n)}
    for c in customers:
        data[min(data, key=lambda key: data[key])] += c
    return max(data.values(), default=0)