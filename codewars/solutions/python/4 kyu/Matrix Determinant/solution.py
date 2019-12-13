def determinant(matrix, mul=1):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]

    sign = -1
    total = 0

    for i in range(width):
        m = [[matrix[j][k] for k in range(width) if k != i] for j in range(1, width)]

        sign *= -1
        total += mul * determinant(m, sign * matrix[0][i])
    return total