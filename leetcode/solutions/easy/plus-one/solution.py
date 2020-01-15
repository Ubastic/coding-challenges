class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        reminder = 1
        for i, n in zip(*map(reversed, (range(len(digits)), digits))):
            reminder, digits[i] = divmod(n + reminder, 10)
        
        if reminder:
            digits.insert(0, reminder)
        
        return digits
