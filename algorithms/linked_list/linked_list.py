from algorithms.utils import default_equals
from algorithms.linked_list.models.linked_list_models import Node


class LinkedList:
    def __init__(self, equals=None):
        if equals is None:
            equals = default_equals

        # TODO: add _ in the instance properties
        self.count = 0
        self.head = None
        self.equals = equals

    def push(self, element):
        node = Node(element)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.count += 1

    def insert(self, element, index):
        if index >= 0 and index <= self.count: # TODO: move it to a private method
            node = Node(element)
            if index == 0:
                current = self.head
                node.next = current
                self.head = node
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                node.next = current
                previous.next = node
            self.count += 1
            return True
        return False

    def get_element_at(self, index):
        # TODO: make get_element_at return the element not a node instance
        if index >= 0 and index <= self.count: # TODO: move it to a private method
            node = self.head
            i = 0
            while i < index and node is not None:
                node = node.next
                i += 1
            return node
        return None

    def remove(self, element):
        index = self.index_of(element)
        return self.remove_at(index)

    def index_of(self, element):
        current = self.head
        i = 0
        # TODO: Transform while in for
        while i < self.count and current is not None:
            if self.equals(element, current.element):
                return i
            current = current.next
            i += 1
        return -1

    def remove_at(self, index):
        if index >= 0 and index < self.count: # TODO: move it to a private method
            current = self.head
            if index == 0:
                self.head = current.next
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                previous.next = current.next
            self.count -= 1
            return current.element
        return None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        # TODO: Transform it in __len__
        return self.count

    def get_head(self):
        # TODO: Transform it in a property
        return self.head

    def to_string(self):
        # TODO: Transform it in __str__
        if self.head is None:
            return ""

        obj_string = f"{self.head.element}"
        current = self.head.next
        i = 1
        while i < self.size() and current is not None:
            obj_string = f"{obj_string},{current.element}"
            current = current.next
            i += 1
        return obj_string
