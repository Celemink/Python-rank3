def echo_validator(text: str) -> bool:

    clean = ""

    for c in text.lower():
        if c.isalpha():
            clean += c

    if clean == "":
        return False

    return clean == clean[::-1]


def main():
    print(echo_validator("racecar"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))


if __name__ == "__main__":
    main()
