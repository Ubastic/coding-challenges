def solution(s):
    s = s + '_' if len(s) % 2 else s
    return [s[i * 2:i * 2 + 2] for i in range(len(s) // 2)]
