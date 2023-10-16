class CircularDict(dict):

    def __init__(self, size):
        super().__init__()
        self._size = size
        self._keys = []

    def __setitem__(self, key, value):
        if key not in self:
            self._keys.append(key)
        super().__setitem__(key, value)
        self._enforce_size_limit()

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __delitem__(self, key):
        super().__delitem__(key)
        self._keys.remove(key)

    def _enforce_size_limit(self):
        while len(self._keys) > self._size:
            oldest_key = self._keys.pop(0)
            super().__delitem__(oldest_key)
