class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        previous = None
        current = self.head

        while current:
            # Save the next node before reversing the current link.
            next_node = current.next

            current.next = previous

            # Move both references one node forward.
            previous = current
            current = next_node

        # The old last node is now the first node.
        self.head = previous

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


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(5)
    ll.append(6)

    ll.reverse()

    print(ll)