def longest_consec(strarr, k):
    return max((''.join(strarr[i:i + k]) for i in range(len(strarr) - k + 1)), key=len) if 0 < k < len(strarr) else ''