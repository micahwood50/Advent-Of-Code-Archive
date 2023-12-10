FILENAME = "input.txt"


def get_input() -> list[list[int]]:
    row_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            row_list.append(list(map(int, line.split())))

    return row_list


def part_1():
    history_list = get_input()
    result = 0

    for history in history_list:
        patterns = [history]

        while set(patterns[-1]) != {0}:
            new_pattern = list()

            for i in range(len(patterns[-1]) - 1):
                new_pattern.append(patterns[-1][i + 1] - patterns[-1][i])

            patterns.append(new_pattern)

        for i in range(len(patterns) - 1, 0, -1):
            patterns[i - 1].append(patterns[i - 1][-1] + patterns[i][-1])

        result += patterns[0][-1]

    print(f"Answer is {result}")


def part_2():
    history_list = get_input()
    result = 0

    for history in history_list:
        patterns = [history]

        while set(patterns[-1]) != {0}:
            new_pattern = list()

            for i in range(len(patterns[-1]) - 1):
                new_pattern.append(patterns[-1][i + 1] - patterns[-1][i])

            patterns.append(new_pattern)

        for i in range(len(patterns) - 1, 0, -1):
            patterns[i - 1].insert(0, patterns[i - 1][0] - patterns[i][0])

        result += patterns[0][0]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
