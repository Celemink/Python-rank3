def twist_sequence(arr: list[int], k: int) -> list[int]:
    if len(arr) == 0:
        return []

    k = k % len(arr)

    result = []

    for i in range(len(arr) - k, len(arr)):
        result.append(arr[i])

    for i in range(0, len(arr) - k):
        result.append(arr[i])

    return result


def main():
    print(twist_sequence([1, 2, 3, 4], 0))
    print(twist_sequence([1, 2, 3], 5))
    print(twist_sequence([], 3))


if __name__ == "__main__":
    main()
