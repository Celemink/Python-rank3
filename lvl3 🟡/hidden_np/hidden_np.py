def hiddenp(small: str, big: str) -> bool:
    i = 0
    j = 0

    while i < len(small) and j < len(big):
        if small[i] == big[j]:
            i += 1
        j += 1

    return i == len(small)


def main():
    print(hiddenp("abc", "a1b2c3"))
    print(hiddenp("aec", "abcde"))


if __name__ == "__main__":
    main()
