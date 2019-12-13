class add(int):
    def __call__(self, number):
        return add(self + number)