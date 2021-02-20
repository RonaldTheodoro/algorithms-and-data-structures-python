class Queue:

    def __init__(self):
        self._count = 0
        self._lowest_count = 0
        self._itens = {}

    def enqueue(self, element):
        self._itens[self._count] = element
        self._count += 1

    def dequeue(self):
        if self.is_empty():
            return None

        result = self._itens[self._lowest_count]
        del self._itens[self._lowest_count]
        self._lowest_count += 1
        return result

    def peek(self):
        if self.is_empty():
            return None

        return self._itens[self._lowest_count]

    def is_empty(self):
        return self._count - self._lowest_count == 0

    def clear(self):
        self._itens = {}
        self._count = 0
        self._lowest_count = 0

    def __len__(self):
        return self._count - self._lowest_count

    def __str__(self):
        return f'Queue({[self._itens[i] for i in range(self._count)]})'

    def __bool__(self):
        return not self.is_empty()
