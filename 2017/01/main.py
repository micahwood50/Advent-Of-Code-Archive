FILENAME = "input.txt"


def get_input() -> str:
    with open(FILENAME) as file:
        return file.readline().strip()


def part_1():
    seq = get_input()
    result = 0

    if seq[0] == seq[-1]:
        result += int(seq[0])

    for i in range(len(seq) - 1):
        if seq[i] == seq[i + 1]:
            result += int(seq[i])

    print(f"Answer is {result}")


def part_2():
    seq = get_input()
    halfway_len = len(seq) // 2
    result = 0

    for i in range(len(seq)):
        if seq[i] == seq[i - halfway_len]:
            result += int(seq[i])

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
