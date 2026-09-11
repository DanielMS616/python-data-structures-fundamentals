from pythonds3.basic import Stack


def rev_string(my_str):
    stack = Stack()

    # Store all characters on the stack.
    for character in my_str:
        stack.push(character)

    reversed_characters = []

    # LIFO returns the characters in reverse order.
    while not stack.is_empty():
        reversed_characters.append(stack.pop())

    return "".join(reversed_characters)


# Test
print("Test with 'apple', 'x', and '1234567890'")
print(f"apple: {rev_string('apple')}")
print(f"x: {rev_string('x')}")
print(f"1234567890: {rev_string('1234567890')}")