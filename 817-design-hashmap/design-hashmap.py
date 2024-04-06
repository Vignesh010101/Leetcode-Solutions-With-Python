class MyHashMap:
    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        try:
            pos = self.keys.index(key)
            self.values[pos] = value
        except ValueError:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        try:
            pos = self.keys.index(key)
            return self.values[pos]
        except ValueError:
            return -1

    def remove(self, key: int) -> None:
        if key in self.keys:
            pos = self.keys.index(key)
            self.keys[pos] = None