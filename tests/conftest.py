import pytest

from algorithms.deques.deque import Deque
from algorithms.linked_list.linked_list import LinkedList
from algorithms.queues.queue import Queue
from algorithms.stacks.stack import Stack
from algorithms.stacks.stack_list import StackList


@pytest.fixture
def stack_list():
    return StackList()


@pytest.fixture
def stack():
    return Stack()


@pytest.fixture
def queue():
    return Queue()


@pytest.fixture
def deque():
    return Deque()


@pytest.fixture
def linked_list():
    return LinkedList()
