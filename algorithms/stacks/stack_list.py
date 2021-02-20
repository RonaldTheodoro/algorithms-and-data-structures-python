class StackList:

    def __init__(self):
        self._itens = []

    def push(self, element):
        self._itens.append(element)

    def pop(self):
        if self.is_empty():
            return None

        return self._itens.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self._itens[-1]

    def is_empty(self):
        return len(self._itens) == 0

    def clear(self):
        self._itens = []

    def __len__(self):
        return len(self._itens)

    def __str__(self):
        return f'StackList({self._itens})'

    def __bool__(self):
        return not self.is_empty()
