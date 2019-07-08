def chunks(lst, chunk_size):
    len_s, arr = len(lst), []
    is_max = False
    i = 0

    while i < len_s:
        if is_max:
            chunk_size += 1

        value = lst[i:i + chunk_size]
        value_next = lst[i + chunk_size:i + 2 * chunk_size]

        l = len(value)

        is_max = value == '9' * l or (value == '9' * (l - 1) + '8' and value_next != '9' * l)

        arr.append(int(value))
        i += chunk_size

    return arr


def missing(s):
    len_s = len(s)

    for i in range(1, len_s // 2):
        arr = chunks(s, i)
        max_num, min_num = max(arr), min(arr)

        if max_num - min_num != len(arr):
            continue

        for j in range(min_num + 1, max_num):
            if j not in arr:
                return j

    return -1
