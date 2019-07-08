def remember(origin_cls):
    cache = {}

    class CacheMeta(type):
        def __call__(cls, *args):
            if args not in cache:
                cache[args] = origin_cls(*args)
            return cache[args]

        def __iter__(self):
            return (i[0] if len(i) == 1 else i for i in cache)

        def __getitem__(self, item):
            return cache[(item,) if not isinstance(item, tuple) else item]

    return CacheMeta(origin_cls.__name__, (origin_cls,), {})
