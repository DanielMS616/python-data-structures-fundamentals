from pythonds3.basic import Stack


class ReversableQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            return None

        # Removing index 0 shifts all remaining elements -> O(n).
        return self.queue.pop(0)

    def reverse_first_k(self, k):
        if k < 0 or k > len(self.queue):
            raise ValueError("k must be between 0 and the queue length")

        stack = Stack()

        # Store the first k elements on the stack.
        for index in range(k):
            stack.push(self.queue[index])

        # LIFO writes the elements back in reverse order.
        for index in range(k):
            self.queue[index] = stack.pop()


if __name__ == "__main__":
    rq = ReversableQueue()

    rq.enqueue(1)
    rq.enqueue(2)
    rq.enqueue(3)

    rq.reverse_first_k(2)

    print(rq.dequeue())  # Expected: 2