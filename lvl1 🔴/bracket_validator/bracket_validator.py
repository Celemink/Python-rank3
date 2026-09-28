def bracket_validator(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in s:
        if character in "([{":
            stack.append(character)

        elif character in ")]}":
            if len(stack) == 0:
                return False

            if stack.pop() != pairs[character]:
                return False

    return len(stack) == 0
