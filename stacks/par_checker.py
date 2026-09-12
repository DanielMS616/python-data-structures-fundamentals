from pythonds3.basic import Stack


def par_checker(symbol_string: str) -> bool:
    stack = Stack()

    # Opening parentheses wait for a matching closing parenthesis.
    for symbol in symbol_string:
        if symbol == "(":
            stack.push(symbol)

        elif symbol == ")":
            # A closing parenthesis without an opener makes the string invalid.
            if stack.is_empty():
                return False

            stack.pop()

    # Balanced only if no unmatched opening parentheses remain.
    return stack.is_empty()


if __name__ == "__main__":
    print("The code should pass the following tests:")
    print(f"((())): {par_checker('((()))')}")
    print(f"((()())): {par_checker('((()()))')}")
    print(f"((): {par_checker('(()')}")
    print(f")(: {par_checker(')(')}")