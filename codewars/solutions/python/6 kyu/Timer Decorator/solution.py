from time import time

def timer(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            s = time()
            func(*args, **kwargs)
            return time() - s <= limit
        return wrapper
    return decorator