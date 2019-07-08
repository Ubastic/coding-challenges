def scale(strng, k, n):
    return "\n".join("\n".join(["".join(s * k for s in ss)] * n) for ss in strng.split())