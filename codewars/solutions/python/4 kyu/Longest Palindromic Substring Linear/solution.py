SEN, START, END = SPECIAL = "@!#"


def longest_palindrome(s):
    arr = f"{START}{SEN.join('_' + s + '_')[1:-1]}{END}"
    length = [0] * len(arr)

    center = right = max_len = index = 0
    for i in range(1, len(arr) - 1):
        mirror = 2 * center - i
        if i < right:
            length[i] = min(right - i, length[mirror])

        while arr[i + length[i] + 1] == arr[i - (length[i] + 1)]:
            length[i] += 1

        if i + length[i] > right:
            center, right = i, i + length[i]

        if length[i] > max_len:
            index, max_len = i, length[i]

    res = arr[index - max_len: index + max_len + 1]
    return "".join(c for c in res if c not in SPECIAL)