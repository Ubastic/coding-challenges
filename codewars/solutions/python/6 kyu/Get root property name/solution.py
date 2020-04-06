def get_root_property(d, v):
    return v in d if isinstance(d, list) else next((k for k in d if get_root_property(d[k], v)), None)