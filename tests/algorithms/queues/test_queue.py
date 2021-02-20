def test_queue_enqueue(queue):
    assert queue.is_empty()
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    assert not queue.is_empty()
    assert len(queue) == 3


def test_queue_dequeue(queue):
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    assert queue.dequeue() == 7
    assert queue.dequeue() == 8
    assert queue.dequeue() == 9


def test_queue_dequeue_empty(queue):
    assert queue.dequeue() is None


def test_queue_peek(queue):
    queue.enqueue(42)
    assert queue.peek() == 42


def test_queue_peek_empty(queue):
    assert queue.peek() is None


def test_queue_is_empty(queue):
    assert queue.is_empty()
    assert len(queue) == 0


def test_queue_is_not_empty(queue):
    queue.enqueue(42)
    assert not queue.is_empty()
    assert len(queue) == 1


def test_queue_clear(queue):
    queue.enqueue(42)
    queue.enqueue(4)
    queue.enqueue(2)
    assert len(queue) == 3
    queue.clear()
    assert queue.is_empty()


def test_queue_str(queue):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert str(queue) == 'Queue([1, 2, 3])'


def test_queue_empty_str(queue):
    assert str(queue) == 'Queue([])'


def test_queue_true_value(queue):
    queue.enqueue(42)
    assert bool(queue)


def test_queue_false_value(queue):
    assert not bool(queue)
