def limiter(limit: int, unique: str, lookup: str):
    def decorator(cls):
        cache, recent = {}, None

        def wrapper(*args, **kwargs):
            nonlocal recent
            obj = cls(*args, **kwargs)
            key = getattr(obj, unique)

            if key in cache:
                recent = cache[key]
            elif limit > len(cache):
                recent = cache[key] = obj
            elif lookup != "RECENT":
                recent = [*cache.values()][0 if lookup == 'FIRST' else -1]

            return recent

        return wrapper

    return decorator
