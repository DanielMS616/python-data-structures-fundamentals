class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0

    def enqueue(self, item, priority):
        # The counter preserves FIFO order for equal priorities.
        self.queue.append((priority, self.counter, item))
        self.counter += 1

        # Keep the next item to remove at the end of the list.
        self.queue.sort(
            key=lambda element: (element[0], element[1]),
            reverse=True,
        )

    def dequeue(self):
        if not self.queue:
            return None

        # pop() at the end of a Python list is O(1).
        _, _, item = self.queue.pop()
        return item


if __name__ == "__main__":
    pq = PriorityQueue()

    pq.enqueue("A", 1)
    pq.enqueue("B", 3)
    pq.enqueue("C", 2)
    pq.enqueue("D", 2)

    print(pq.dequeue())  # Expected: A
    print(pq.dequeue())  # Expected: C
    print(pq.dequeue())  # Expected: D
    print(pq.dequeue())  # Expected: B