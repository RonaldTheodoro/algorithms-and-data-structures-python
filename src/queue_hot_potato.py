from algorithms.queues.queue import Queue


def hot_potato(elements, num):
    queue = Queue()
    eliminated = []

    for element in elements:
        queue.enqueue(element)

    while len(queue) > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        eliminated.append(queue.dequeue())

    return {"eliminated": eliminated, "winner": queue.dequeue()}
