def pick_peaks(arr):
    picks, poss = [], []

    if not arr:
        return dict(peaks=picks, pos=poss)

    pos, value = 0, arr[0]
    arr_iter = iter(enumerate(arr[1:], 1))

    for i, a in arr_iter:
        if value < a:
            pos, value = i, a
            break
        else:
            pos, value = i, a

    for i, a in arr_iter:
        if a < value:
            picks.append(value)
            poss.append(pos)
            pos, value = i, a

            for i, a in arr_iter:
                if value < a:
                    pos, value = i, a
                    break
                else:
                    pos, value = i, a

        elif a > value:
            pos, value = i, a

    return dict(peaks=picks, pos=poss)