def spiralize(s, j=0):
    matrix = [[int(s == 1) for _ in range(s)] for _ in range(s)]
    while j <= s:
        for i in range(j, s): matrix[j][i] = 1
        for i in range(j, s - 1): matrix[i][s - 1] = matrix[s - 1][i + 1] = 1
        for i in range(j + 2, s): matrix[i][j] = 1
        s, j = s - 2, j + 2
        if j < s: matrix[j][j - 1] = 1
        
    return matrix