class Node:
    def __init__(self, data: object) -> None:
        self.data: object = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def reverse(self) -> None:
        previous: Node | None = None
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

    def append(self, data: object) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def __str__(self) -> str:
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