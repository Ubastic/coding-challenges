def maximum_product_of_parts(n):
    s = str(n)
    len_n = len(s)
    max_num = 0
    for i in range(1, len_n - 1):
        for j in range(i + 1, len_n):
            s1, s2, s3 = s[0:i], s[i:j], s[j:]
            max_num = max(int(s1) * int(s2) * int(s3), max_num)

    return max_num