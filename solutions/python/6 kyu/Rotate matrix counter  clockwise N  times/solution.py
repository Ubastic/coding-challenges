def get_matrix(height, width):
    return [[0 for j in range(width)] for i in range(height)]


def rotate_against_clockwise(matrix, times):
    new_matrix = matrix

    for _ in range(times % 4):
        height, width = len(matrix), len(matrix[0])
        new_matrix = get_matrix(width, height)

        for i in range(height):
            for j in range(width):
                new_matrix[width - j - 1][i] = matrix[i][j]

        matrix = new_matrix

    return new_matrix