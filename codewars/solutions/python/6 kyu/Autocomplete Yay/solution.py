def autocomplete(input_, dictionary):
    input_ = ''.join(c for c in input_ if c.isalpha()).lower()
    return [i for i in dictionary if i.lower().startswith(input_)][:5]

