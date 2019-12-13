def count_smileys(arr):
    return sum(bool(__import__('re').match(r'[:;][-~]?[)D]', i)) for i in arr)
