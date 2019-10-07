def two_sum(numbers, target):
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers[i+1:], i + 1):
            if a + b == target:
                return i,j