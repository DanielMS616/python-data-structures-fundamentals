class Node:
    def __init__(self, data: object) -> None:
        self.data: object = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    def append(self, data: object) -> None:
        new_node = Node(data)

        # An empty list gets its first and last node at the same time.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # A non-empty list always has a tail.
        assert self.tail is not None

        # tail gives direct access to the current last node -> O(1).
        self.tail.next = new_node
        self.tail = new_node

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
    ll.append(7)

    print(ll)