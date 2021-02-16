import pytest

from algorithms.stacks.stack_list import StackList
from algorithms.stacks.stack import Stack


@pytest.fixture
def stack_list():
    return StackList()


@pytest.fixture
def stack():
    return Stack()
