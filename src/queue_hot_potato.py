from algorithms.queues.queue import Queue


def hot_potato(elements, num):
    queue = Queue()
    elimitated = []

    for element in elements:
        queue.enqueue(element)

    while len(queue) > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        elimitated.append(queue.dequeue())

    return { 'elimitated': elimitated, 'winner': queue.dequeue() }
