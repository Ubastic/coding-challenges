VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        num, max_val = 0, "I"

        for c in reversed(s):
            if VALUES[c] >= VALUES[max_val]:
                max_val = c
                num += VALUES[c]
            else:
                num -= VALUES[c]

        return num