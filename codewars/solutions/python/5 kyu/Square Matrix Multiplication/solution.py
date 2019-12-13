from numpy import array

def matrix_mult(a, b):
  return (array(a).dot(array(b))).tolist()