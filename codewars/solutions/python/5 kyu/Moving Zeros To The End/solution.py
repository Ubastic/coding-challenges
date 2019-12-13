def move_zeros(array):
    a = [i for i in array if not (i == 0 and type(i) in (int, float))]
    return a + [0] * (len(array) - len(a))
