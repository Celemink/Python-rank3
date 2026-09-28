def pattern_tracker(text: str) -> int:
    count = 0

    for i in range(len(text) - 1):
        first = text[i]
        second = text[i + 1]

        if first.isdigit() and second.isdigit():
            if int(second) == int(first) + 1:
                count += 1

    return count


def main():
    print(pattern_tracker("1a2b3c4"))
    print(pattern_tracker("123"))


if __name__ == "__main__":
    main()
