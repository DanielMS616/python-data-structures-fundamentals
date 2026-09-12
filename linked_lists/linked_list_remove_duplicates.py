class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def remove_duplicates(self):
        seen = set()
        current = self.head
        previous = None

        while current:
            # Skip nodes whose value has already appeared.
            if current.data in seen:
                previous.next = current.next

            else:
                seen.add(current.data)
                previous = current

            current = current.next

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
    ll.append(5)
    ll.append(6)
    ll.append(5)
    ll.append(7)
    ll.append(6)

    print(f"Before: {ll}")

    ll.remove_duplicates()

    print(f"After:  {ll}")