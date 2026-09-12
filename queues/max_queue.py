from collections import deque


class MaxQueue:
    def __init__(self):
        self.queue = deque()
        self.max_queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

        # Remove values that can no longer become the maximum.
        while self.max_queue and self.max_queue[-1] < item:
            self.max_queue.pop()

        self.max_queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None

        item = self.queue.popleft()

        # Remove the maximum candidate as well if it leaves the main queue.
        if item == self.max_queue[0]:
            self.max_queue.popleft()

        return item

    def get_max(self):
        if not self.max_queue:
            return None

        # The current maximum is always at the front.
        return self.max_queue[0]


# Test
mq = MaxQueue()

mq.enqueue(3)
mq.enqueue(1)

print(mq.get_max())  # Expected: 3