import pytest

from queues.max_queue import MaxQueue
from queues.priority_queue import PriorityQueue
from queues.reversable_queue import ReversableQueue


def test_priority_queue_respects_priority_and_fifo_order():
    queue = PriorityQueue()

    queue.enqueue("A", 1)
    queue.enqueue("B", 3)
    queue.enqueue("C", 2)
    queue.enqueue("D", 2)

    assert queue.dequeue() == "A"
    assert queue.dequeue() == "C"
    assert queue.dequeue() == "D"
    assert queue.dequeue() == "B"


def test_priority_queue_returns_none_when_empty():
    queue = PriorityQueue()

    assert queue.dequeue() is None


def test_max_queue_tracks_maximum_after_dequeues():
    queue = MaxQueue()

    queue.enqueue(3)
    queue.enqueue(1)
    queue.enqueue(5)
    queue.enqueue(2)

    assert queue.get_max() == 5

    assert queue.dequeue() == 3
    assert queue.get_max() == 5

    assert queue.dequeue() == 1
    assert queue.get_max() == 5

    assert queue.dequeue() == 5
    assert queue.get_max() == 2


def test_max_queue_preserves_duplicate_maximum_values():
    queue = MaxQueue()

    queue.enqueue(5)
    queue.enqueue(5)
    queue.enqueue(3)

    assert queue.get_max() == 5

    assert queue.dequeue() == 5
    assert queue.get_max() == 5


def test_max_queue_handles_empty_queue():
    queue = MaxQueue()

    assert queue.get_max() is None
    assert queue.dequeue() is None


def test_reversable_queue_reverses_first_k_elements():
    queue = ReversableQueue()

    for value in [1, 2, 3, 4]:
        queue.enqueue(value)

    queue.reverse_first_k(3)

    result = [queue.dequeue() for _ in range(4)]

    assert result == [3, 2, 1, 4]


def test_reversable_queue_handles_zero_k():
    queue = ReversableQueue()

    queue.enqueue(1)
    queue.enqueue(2)

    queue.reverse_first_k(0)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2


def test_reversable_queue_rejects_invalid_k():
    queue = ReversableQueue()

    queue.enqueue(1)
    queue.enqueue(2)

    with pytest.raises(ValueError):
        queue.reverse_first_k(-1)

    with pytest.raises(ValueError):
        queue.reverse_first_k(3)