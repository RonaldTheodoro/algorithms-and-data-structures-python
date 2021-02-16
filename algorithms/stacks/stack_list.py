class StackList:

    def __init__(self):
        self._items = []

    def push(self, element):
        self._items.append(element)

    def pop(self):
        if self.is_empty():
            return None

        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def clear(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return f'StackList({self._items})'

    def __bool__(self):
        return not self.is_empty()
