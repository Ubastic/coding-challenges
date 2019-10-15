def is_interesting(number, awesome_phrases, forward=False):
    s = str(number)
    if number > 99 and (
            s[1:].count('0') == len(s) - 1 or  # Any digit followed by all zeros
            s.count(s[0]) == len(s) or  # Every digit is the same number
            all(ord(s[i + 1]) - ord(s[i]) + 10 * (s[i + 1] == '0') == 1 for i in range(len(s) - 1)) or  # The digits are sequential, incementing
            all(ord(s[i]) - ord(s[i + 1]) == 1 for i in range(len(s) - 1)) or  # The digits are sequential, decrementing
            s == s[::-1] or  # The digits are a palindrome
            number in awesome_phrases  # The digits match one of the values in the awesome_phrases array
    ):
        return 2
    elif not forward and (
            is_interesting(number + 1, awesome_phrases, True) or
            is_interesting(number + 2, awesome_phrases, True)
    ):
        return 1
    return 0
