def simplify(number): 
    n = str(number)
    return "+".join(
        "{}{}".format(c, "" if i == len(n) - 1 else "*1" + "0" * (len(n) - i - 1))
        for i, c in enumerate(n) if c != "0"
    )