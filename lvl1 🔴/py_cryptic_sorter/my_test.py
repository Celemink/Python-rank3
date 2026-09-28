    def cryptic_sorter(strings: list[str]) -> list[str]:
    i = 0
    for s in strings:
        s.lower
        strings = sorted(strings, key=ascii)
        strings = sorted(strings, key=len)

        if vowel_count(s) > vowel_count(s + 1)
            strings = sorted(strings, key=??)
    return strings


def vowel_count(word: str) -> int:
    count = 0
    if word in "aeiou":
        count + 1
    return count


def main():
    cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"])
    cryptic_sorter(["aaa", "bbb", "AAA", "BBB"])
    cryptic_sorter(["hello", "world", "hi", "test"])
    cryptic_sorter([])


if __name__ == "__main__":
    main()
    