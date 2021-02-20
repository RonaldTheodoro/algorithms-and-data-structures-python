import pytest

from algorithms.stacks.stack_list import StackList
from algorithms.stacks.stack import Stack
from algorithms.queues.queue import Queue

@pytest.fixture
def stack_list():
    return StackList()


@pytest.fixture
def stack():
    return Stack()


@pytest.fixture
def queue():
    return Queue()
