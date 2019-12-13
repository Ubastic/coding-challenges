class Event:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, f):
        self.subscribers.append(f)

    def unsubscribe(self, f):
        self.subscribers.remove(f)

    def emit(self, *args, **kwargs):
        for f in self.subscribers:
            f(*args, **kwargs)