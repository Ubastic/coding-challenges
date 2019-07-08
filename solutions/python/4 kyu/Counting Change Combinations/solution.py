def count_change(money, coins):
    if money < 0 or (money > 0 and not coins):
        return 0
    elif money == 0:
        return 1
    return count_change(money-coins[-1], coins) + count_change(money, coins[:-1])