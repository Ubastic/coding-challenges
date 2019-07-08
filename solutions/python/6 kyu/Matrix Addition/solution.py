from numpy import matrix

def matrix_addition(a, b):
    return (matrix(a) + matrix(b)).tolist()