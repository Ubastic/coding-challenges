class DefaultList(list):
    def __init__(self, l, default):
        super().__init__(l)
        self.default = default

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return self.default