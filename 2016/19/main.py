FILENAME = "input.txt"


def get_input() -> int:
    with open(FILENAME) as file:
        return int(file.readline())


def part_1():
    size = get_input()
    result = int("0b" + bin(size)[3:] + "1", 2)

    print(f"Answer is {result}")


def part_2():
    size = get_input()
    i = 1

    while i * 3 < size:
        i *= 3

    result = size - i

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
