class UnexpectedTypeException(Exception):
    pass

def expected_type(return_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            if not isinstance(ret, return_types):
                raise UnexpectedTypeException
            return ret
        return wrapper
    return decorator