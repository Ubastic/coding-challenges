class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = []
        self.data = {}

    def mark_as_used(self, key):
        index = self.keys.index(key)
        if index != 0:
            self.keys.insert(0, self.keys.pop(index))

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1

        self.mark_as_used(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.data:
            if len(self.data) == self.capacity:
                del self.data[self.keys.pop(-1)]
            self.keys.insert(0, key)
        else:
            self.mark_as_used(key)

        self.data[key] = value