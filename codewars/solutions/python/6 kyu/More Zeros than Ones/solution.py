def more_zeros(s):
    def gen():
        print(s)
        consumed = set()
        for c in s:
            b = bin(ord(c))[2:]
            print(f"{c} -> {b}")
            if c not in consumed and b.count("0") > b.count("1"):
                consumed.add(c)
                yield c

    return [*gen()]