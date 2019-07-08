class ContextManager(object):
    def __init__(self, gen):
        self.gen = gen
    
    def __enter__(self):
        return next(self.gen)
    
    def __exit__(self, *args):
        return self.gen.throw(*args)

def contextmanager(func):
    def wrapper(*args, **kwargs):
        return ContextManager(func(*args, **kwargs))
    return wrapper