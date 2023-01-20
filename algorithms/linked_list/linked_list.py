from algorithms.utils import default_equals
from algorithms.linked_list.models.linked_list_models import Node


class LinkedList:
    def __init__(self, equals=None):
        if equals is None:
            equals = default_equals

        self._count = 0
        self._head = None
        self._equals = equals

    def push(self, element):
        node = Node(element)
        if self._head is None:
            self._head = node
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = node
        self._count += 1

    def insert(self, element, index):
        if self._index_is_inside_range(index):
            node = Node(element)
            if index == 0:
                current = self._head
                node.next = current
                self._head = node
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                node.next = current
                previous.next = node
            self._count += 1
            return True
        return False

    def get_element_at(self, index):
        # TODO: make get_element_at return the element not a node instance
        if self._index_is_inside_range(index):
            node = self._head
            i = 0
            while i < index and node is not None:
                node = node.next
                i += 1
            return node
        return None

    def remove(self, element):
        index = self.index(element)
        return self.remove_at(index)

    def index(self, element):
        current = self._head
        i = 0
        # TODO: Transform while in for
        while i < self._count and current is not None:
            if self._equals(element, current.element):
                return i
            current = current.next
            i += 1
        return -1

    def remove_at(self, index):
        # TODO: rename to pop and remove last item when index is None
        if self._index_is_inside_range(index):
            current = self._head
            if index == 0:
                self._head = current.next
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                previous.next = current.next
            self._count -= 1
            return current.element
        return None

    def is_empty(self):
        return len(self) == 0

    @property
    def head(self):
        return self._head

    def _index_is_inside_range(self, index):
        return 0 <= index <= self._count

    def __getitem__(self, index):
        element = self.get_element_at(index)
        if element is None:
            raise IndexError
        return element.element

    def __len__(self):
        return self._count

    def __str__(self):
        if self._head is None:
            return ""

        obj_string = f"{self._head.element}"
        current = self._head.next
        i = 1
        while i < len(self) and current is not None:
            obj_string = f"{obj_string},{current.element}"
            current = current.next
            i += 1
        return obj_string

    def __bool__(self):
        return len(self) > 0
