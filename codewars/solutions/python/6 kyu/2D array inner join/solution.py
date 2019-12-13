def inner_join(arrA, arrB, indA, indB):
    return [a + b for a in arrA for b in arrB if a[indA] is not None and b[indB] is not None and a[indA] == b[indB]]
