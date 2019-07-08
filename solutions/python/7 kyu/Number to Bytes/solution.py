def to_bytes(n):
    result = [] if n else ["0" * 8]
    while n:
        s, n = bin(n & 0xFF)[2:], n >> 8
        result.append("0" * (8 - len(s)) + s)

    return result[::-1]