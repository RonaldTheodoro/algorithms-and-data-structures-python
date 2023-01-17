class Stack:
    def __init__(self):
        self._count = 0
        self._itens = {}

    def push(self, element):
        self._itens[self._count] = element
        self._count += 1

    def pop(self):
        if self.is_empty():
            return None

        self._count -= 1
        return self._itens.pop(self._count)

    def peek(self):
        if self.is_empty():
            return None

        return self._itens[self._count - 1]

    def is_empty(self):
        return self._count == 0

    def clear(self):
        self._itens = {}
        self._count = 0

    def __len__(self):
        return self._count

    def __str__(self):
        return f"Stack({[self._itens[i] for i in range(self._count)]})"

    def __bool__(self):
        return not self.is_empty()
