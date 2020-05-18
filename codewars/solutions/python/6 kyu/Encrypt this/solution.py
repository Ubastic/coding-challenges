def encrypt_this(text):
    return " ".join(
        str(ord(s[0])) + (s[1] if len(s) == 2 else s[-1] + s[2:-1] + s[1] if len(s) > 2 else "")
        for s in text.split()
    )