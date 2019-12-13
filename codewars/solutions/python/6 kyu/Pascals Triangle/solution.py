def pascals_triangle(n_rows):
    results = []
    for _ in range(n_rows):
        row = [1]
        if results:
            last_row = results[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        results.append(row)

    arr = []
    for a in results:
        arr.extend(a)

    return arr