def recoverSecret(triplets):
    res = []

    while triplets:
        not_firsts = [i for a in triplets for i in a[1:]]
        firsts = [a for a, *_ in triplets]

        for i in firsts:
            if i not in not_firsts:
                res.append(i)

                for t in triplets:
                    if t[0] == i:
                        t.pop(0)

                break

        triplets = [i for i in triplets if i]

    return ''.join(res)