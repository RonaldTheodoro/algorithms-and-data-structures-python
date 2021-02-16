def test_stack_list_push(stack_list):
    assert stack_list.is_empty()
    stack_list.push(7)
    stack_list.push(8)
    stack_list.push(9)
    assert not stack_list.is_empty()
    assert len(stack_list) == 3


def test_stack_list_pop(stack_list):
    stack_list.push(7)
    stack_list.push(8)
    stack_list.push(9)
    assert stack_list.pop() == 9
    assert stack_list.pop() == 8
    assert stack_list.pop() == 7


def test_stack_list_pop_empty(stack_list):
    assert stack_list.pop() is None


def test_stack_list_peek(stack_list):
    stack_list.push(42)
    assert stack_list.peek() == 42


def test_stack_list_peek_empty(stack_list):
    assert stack_list.peek() is None


def test_stack_list_is_empty(stack_list):
    assert stack_list.is_empty()
    assert len(stack_list) == 0


def test_stack_list_is_not_empty(stack_list):
    stack_list.push(42)
    assert not stack_list.is_empty()
    assert len(stack_list) == 1


def test_stack_list_clear(stack_list):
    stack_list.push(42)
    stack_list.push(4)
    stack_list.push(2)
    assert len(stack_list) == 3
    stack_list.clear()
    assert stack_list.is_empty()


def test_stack_list_str(stack_list):
    stack_list.push(1)
    stack_list.push(2)
    stack_list.push(3)
    assert str(stack_list) == 'StackList([1, 2, 3])'


def test_stack_list_empty_str(stack_list):
    assert str(stack_list) == 'StackList([])'


def test_stack_list_true_value(stack_list):
    stack_list.push(42)
    assert bool(stack_list)


def test_stack_list_false_value(stack_list):
    assert not bool(stack_list)
