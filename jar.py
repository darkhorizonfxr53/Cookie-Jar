class Jar:
    def __init__(self, capacity=12):
        # We check the capacity immediately
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Returns n cookies (🍪)
        return "🍪" * self._size

    def deposit(self, n):
        # Check if adding n exceeds capacity
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies for this jar!")
        self._size += n

    def withdraw(self, n):
        # Check if we have enough cookies to remove n
        if n > self._size:
            raise ValueError("Not enough cookies in the jar!")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
