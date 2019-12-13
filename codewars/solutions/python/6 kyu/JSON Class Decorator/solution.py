from json import load

def jsonattr(fp):
    def inner(cls):
        for name, attr in load(fp).items():
            setattr(cls, name, attr)
        return cls
    return inner
