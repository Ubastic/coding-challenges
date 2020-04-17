def flatten(x, prefixes: tuple = (), store: dict = None) -> dict:
    store = store or {}

    for key, value in x.items():
        if isinstance(value, dict) and value:
            store = flatten(value, (*prefixes, key), store)
        elif isinstance(value, list) and value:
            for i, l in enumerate(value):
                store = flatten(l, (*prefixes, f"{key}[{i}]"), store)
        else:
            store[".".join(map(str, (*prefixes, key))) if prefixes else key] = value

    return store