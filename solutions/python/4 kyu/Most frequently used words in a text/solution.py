from collections import Counter

def top_3_words(text):
    s = ''.join(t if t.isalnum() or t == "'" else ' ' for t in text.lower())
    return [i for i, _ in Counter(i for i in s.split() if len(i) != i.count("'")).most_common(3)]
