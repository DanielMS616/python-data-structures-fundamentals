class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find_middle(self):
        slow = self.head
        fast = self.head

        # slow moves one node, fast moves two nodes per iteration.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches the end, slow is at the middle.
        return slow.data if slow else None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def __str__(self):
        elements = []
        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        return "->".join(map(str, elements))


# Test
ll = LinkedList()

ll.append(5)
ll.append(6)

print(ll.find_middle())  # Expected: 6

ll.append(7)

print(ll.find_middle())  # Expected: 6