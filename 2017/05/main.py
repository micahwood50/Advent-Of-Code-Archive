FILENAME = "input.txt"


def get_input() -> list[int]:
    with open(FILENAME) as file:
        return list(map(int, file.readlines()))


def part_1():
    jumps = get_input()
    index = 0
    steps = 0

    while 0 <= index < len(jumps):
        jumps[index] += 1
        index += jumps[index] - 1
        steps += 1

    print(f"Answer is {steps}")


def part_2():
    jumps = get_input()
    index = 0
    steps = 0

    while 0 <= index < len(jumps):
        if jumps[index] >= 3:
            jumps[index] -= 1
            index += jumps[index] + 1

        else:
            jumps[index] += 1
            index += jumps[index] - 1

        steps += 1

    print(f"Answer is {steps}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
