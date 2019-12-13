def solution(number):
    return sum(i for i in range(1, number) if not (i % 3 and i % 5))
  