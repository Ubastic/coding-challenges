from collections import Counter

def permute_a_palindrome (s): 
  return sum(i % 2 for i in Counter(s).values()) <= 1
