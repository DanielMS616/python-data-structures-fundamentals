from collections.abc import Hashable


class Node:
    def __init__(self, data: Hashable) -> None:
        self.data: Hashable = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def remove_duplicates(self) -> None:
        seen: set[Hashable] = set()
        current = self.head
        previous: Node | None = None

        while current:
            # Skip nodes whose value has already appeared.
            if current.data in seen:
                assert previous is not None
                previous.next = current.next

            else:
                seen.add(current.data)
                previous = current

            current = current.next

    def append(self, data: Hashable) -> None:
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
    ll.append(5)
    ll.append(6)
    ll.append(5)
    ll.append(7)
    ll.append(6)

    print(f"Before: {ll}")

    ll.remove_duplicates()

    print(f"After:  {ll}")