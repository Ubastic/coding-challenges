def get_money(s):
    return s.fives * 5 + s.tens * 10 + s.twenties * 20


def most_money(s):
    return (
        "all" if
        [*map(get_money, s)].count(get_money(s[0])) == len(s) != 1
        else max(s, key=get_money).name
    )
