def accum(sentence):
    return "-".join((s * i).title() for i, s in enumerate(sentence, 1))
