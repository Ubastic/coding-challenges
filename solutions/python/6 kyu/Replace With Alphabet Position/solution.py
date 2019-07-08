def alphabet_position(text):
    return " ".join(str(ord(s) - ord('a') + 1) for s in text.lower() if s.isalpha())
