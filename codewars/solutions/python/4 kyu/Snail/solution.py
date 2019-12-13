def snail(matrix, j=0):
    if len(matrix) == 1: return matrix[0]
    s, res = len(matrix), []
    
    while j <= s:
        for i in range(j, s): res.append(matrix[j][i])
        for i in range(j + 1, s - 1): res.append(matrix[i][s - 1])
        for i in range(s, j, - 1) if s - j > 1 else []: res.append(matrix[s - 1][i - 1])
        for i in range(s - 2, j, -1): res.append(matrix[i][j])
        s, j = s - 1, j + 1

    return res