from collections import defaultdict
from itertools import permutations

FILENAME = "input.txt"


def get_input() -> dict[str, dict[str, int]]:
    happiness_dict = defaultdict(dict)

    with open(FILENAME) as file:
        for line in file.readlines():
            line_list = line.strip().split()

            name, direction, point, neighbor_name = (
                line_list[0],
                line_list[2],
                int(line_list[3]),
                line_list[-1][:-1],
            )

            happiness_dict[name][neighbor_name] = (
                point if direction == "gain" else -point
            )

    return happiness_dict


def calculate_max_happiness(happiness_dict: dict[str, dict[str, int]]) -> int:
    result = float("-inf")

    for p in permutations(happiness_dict.keys()):
        this_result = 0
        for i in range(len(p) - 1):
            name1, name2 = p[i], p[i + 1]
            this_result += happiness_dict[name1][name2] + happiness_dict[name2][name1]

        name1, name2 = p[0], p[-1]
        this_result += happiness_dict[name1][name2] + happiness_dict[name2][name1]

        result = max(result, this_result)

    return result


def part_1():
    happiness_dict = get_input()

    print(
        f"The max total change in happiness is {calculate_max_happiness(happiness_dict)}"
    )


def part_2():
    happiness_dict = get_input()

    my_name = "Me"
    names = list(happiness_dict.keys())

    for name in names:
        happiness_dict[my_name][name] = 0
        happiness_dict[name][my_name] = 0

    print(
        f"The max total change in happiness is {calculate_max_happiness(happiness_dict)}"
    )


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
