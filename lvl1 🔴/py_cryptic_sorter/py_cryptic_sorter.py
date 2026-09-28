def vowel_count(word):
    count = 0

    for c in word.lower():
        if c in "aeiou":
            count += 1

    return count


def cryptic_sorter(strings):
    strings = sorted(strings, key=vowel_count)
    strings = sorted(strings, key=str.lower)
    strings = sorted(strings, key=len)
    return strings


def main():
    print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
    print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
    print(cryptic_sorter(["hello", "world", "hi", "test"]))
    print(cryptic_sorter([]))
    print(cryptic_sorter([""]))


if __name__ == "__main__":
    main()
