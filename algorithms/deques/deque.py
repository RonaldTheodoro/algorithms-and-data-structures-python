class Deque:
    def __init__(self):
        self._count = 0
        self._lowest_count = 0
        self._itens = {}

    def add_front(self, element):
        if self.is_empty():
            self.add_back(element)
        elif self._lowest_count > 0:
            self._lowest_count -= 1
            self._itens[self._lowest_count] = element
        else:
            for i in range(self._count, 0, -1):
                self._itens[i] = self._itens[i - 1]
            self._count += 1
            self._lowest_count = 0
            self._itens[0] = element

    def add_back(self, element):
        self._itens[self._count] = element
        self._count += 1

    def remove_front(self):
        if self.is_empty():
            return None

        result = self._itens[self._lowest_count]
        del self._itens[self._lowest_count]
        self._lowest_count += 1
        return result

    def remove_back(self):
        if self.is_empty():
            return None

        self._count -= 1
        return self._itens.pop(self._count)

    def peek_front(self):
        if self.is_empty():
            return None

        return self._itens[self._lowest_count]

    def peek_back(self):
        if self.is_empty():
            return None

        return self._itens[self._count - 1]

    def is_empty(self):
        return self._count - self._lowest_count == 0

    def clear(self):
        self._itens = {}
        self._count = 0
        self._lowest_count = 0

    def __len__(self):
        return self._count - self._lowest_count

    def __str__(self):
        return f"Deque({[self._itens[i] for i in range(self._count)]})"

    def __bool__(self):
        return not self.is_empty()
