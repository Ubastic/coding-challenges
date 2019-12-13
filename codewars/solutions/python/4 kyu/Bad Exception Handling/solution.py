class Handler:
    def __init__(self, func, on_fail, *excs):
        self.func = func
        self.on_fail = on_fail
        self.exsc = excs

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, self.exsc):
            self.on_fail(self.func, exc_val)
            return True


def handle(func, success, failure, *excs):
    with Handler(func, failure, *excs):
        return success(func, func())
