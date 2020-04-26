def luck_check(s):
    return sum(map(int, s[:len(s) // 2])) == sum(map(int, s[len(s) // 2 + (len(s) % 2):]))