def longest_slide_down(p):
    for i in xrange(len(p) - 2, -1, -1):
        for j in xrange(len(p[i])):
            p[i][j] += max(p[i + 1][j], p[i + 1][j + 1])

    return p[0][0]