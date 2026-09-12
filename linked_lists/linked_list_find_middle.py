class Node:
    def __init__(self, data: object) -> None:
        self.data: object = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def find_middle(self) -> object | None:
        slow = self.head
        fast = self.head

        # slow moves one node, fast moves two nodes per iteration.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # When fast reaches the end, slow is at the middle.
        return slow.data if slow else None

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

    print(ll.find_middle())  # Expected: 6

    ll.append(7)

    print(ll.find_middle())  # Expected: 6