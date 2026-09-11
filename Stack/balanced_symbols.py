from pythonds3.basic import Stack


def balanced_symbols(symbol_string):
    stack = Stack()

    # Map each closing symbol to its matching opening symbol.
    matching_symbols = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for symbol in symbol_string:
        if symbol in "([{":
            stack.push(symbol)

        elif symbol in ")]}":
            # A closing symbol without an opener is always invalid.
            if stack.is_empty():
                return False

            # The most recently opened symbol must match this closer.
            if stack.pop() != matching_symbols[symbol]:
                return False

    # Balanced only if no unmatched opening symbols remain.
    return stack.is_empty()


# Test
print("The code should pass the following tests:")
print(balanced_symbols(""))
print(balanced_symbols("[[()]]"))
print(balanced_symbols("[][][]()"))
print(balanced_symbols("([)]"))
print(balanced_symbols("((()])"))
print(balanced_symbols("[{(]"))