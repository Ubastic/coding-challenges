class B:
    def __str__(self):
        raise

class D(B):
    def __str__(self):
        pass

x = D()