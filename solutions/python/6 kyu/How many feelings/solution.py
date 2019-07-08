def count_feelings(s, arr):
    count = 0

    for feeling in arr:
        if all(s.count(w) >= feeling.count(w) for w in set(feeling)):
            count += 1

    return "{} feeling{}.".format(count, "" if count == 1 else "s")