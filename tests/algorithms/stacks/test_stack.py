def test_stack_push(stack):
    assert stack.is_empty()
    stack.push(7)
    stack.push(8)
    stack.push(9)
    assert not stack.is_empty()
    assert len(stack) == 3


def test_stack_pop(stack):
    stack.push(7)
    stack.push(8)
    stack.push(9)
    assert stack.pop() == 9
    assert stack.pop() == 8
    assert stack.pop() == 7


def test_stack_pop_empty(stack):
    assert stack.pop() is None


def test_stack_peek(stack):
    stack.push(42)
    assert stack.peek() == 42


def test_stack_peek_empty(stack):
    assert stack.peek() is None


def test_stack_is_empty(stack):
    assert stack.is_empty()
    assert len(stack) == 0


def test_stack_is_not_empty(stack):
    stack.push(42)
    assert not stack.is_empty()
    assert len(stack) == 1


def test_stack_clear(stack):
    stack.push(42)
    stack.push(4)
    stack.push(2)
    assert len(stack) == 3
    stack.clear()
    assert stack.is_empty()


def test_stack_str(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert str(stack) == 'Stack([1, 2, 3])'


def test_stack_empty_str(stack):
    assert str(stack) == 'Stack([])'