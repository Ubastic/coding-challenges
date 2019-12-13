def wave(s: str):
    return [s[0:i] + c.upper() + s[i + 1:] for i, c in enumerate(s) if c.isalnum()]
