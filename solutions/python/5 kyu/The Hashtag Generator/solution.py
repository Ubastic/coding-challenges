def generate_hashtag(s):
    s = f'#{s.title().replace(" ", "")}'
    return s if 1 < len(s) < 140 else False