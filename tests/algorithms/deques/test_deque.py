def test_deque_add_front(deque):
    assert deque.is_empty()
    deque.add_front(1)
    deque.add_front(2)
    deque.add_front(3)
    assert not deque.is_empty()
    assert len(deque) == 3


def test_deque_add_back(deque):
    assert deque.is_empty()
    deque.add_back(1)
    deque.add_back(2)
    deque.add_back(3)
    assert not deque.is_empty()
    assert len(deque) == 3


def test_deque_remove_front(deque):
    deque.add_front(1)
    deque.add_front(2)
    deque.add_front(3)
    assert deque.remove_front() == 3
    assert deque.remove_front() == 2
    assert deque.remove_front() == 1


def test_deque_remove_back(deque):
    deque.add_back(1)
    deque.add_back(2)
    deque.add_back(3)
    assert deque.remove_back() == 3
    assert deque.remove_back() == 2
    assert deque.remove_back() == 1


def test_deque_remove_front_empty(deque):
    assert deque.remove_front() is None


def test_deque_remove_back_empty(deque):
    assert deque.remove_back() is None


def test_deque_peek_front(deque):
    deque.add_front(1)
    deque.add_front(2)
    deque.add_front(3)
    deque.add_front(42)
    assert deque.peek_front() == 42


def test_deque_peek_back(deque):
    deque.add_back(1)
    deque.add_back(2)
    deque.add_back(3)
    deque.add_back(42)
    assert deque.peek_back() == 42


def test_deque_peek_empty(deque):
    assert deque.peek_front() is None
    assert deque.peek_back() is None


def test_deque_is_empty(deque):
    assert deque.is_empty()
    assert len(deque) == 0


def test_deque_is_not_empty(deque):
    deque.add_front(42)
    assert not deque.is_empty()
    assert len(deque) == 1


def test_deque_clear(deque):
    deque.add_front(1)
    deque.add_back(2)
    deque.add_front(3)
    deque.add_back(4)
    assert len(deque) == 4
    deque.clear()
    assert deque.is_empty()


def test_deque_str(deque):
    deque.add_front(1)
    deque.add_back(2)
    deque.add_front(3)
    deque.add_back(4)
    assert str(deque) == 'Deque([3, 1, 2, 4])'


def test_deque_empty_str(deque):
    assert str(deque) == 'Deque([])'


def test_deque_true_value(deque):
    deque.add_front(42)
    assert bool(deque)


def test_deque_false_value(deque):
    assert not bool(deque)
