from collections import defaultdict

FILENAME = "input.txt"


def get_input() -> list[tuple[int, int]]:
    tuple_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            tuple_list.append(tuple(map(int, line.split())))

    return tuple_list


def part_1():
    lists_input = get_input()

    left_list = list()
    right_list = list()

    for left_val, right_val in lists_input:
        left_list.append(left_val)
        right_list.append(right_val)

    left_list.sort()
    right_list.sort()

    result = 0

    for ld, rd in zip(left_list, right_list):
        result += abs(ld - rd)

    print(f"Answer is {result}")


def part_2():
    lists_input = get_input()

    similarity_dict = defaultdict(int)

    for __, right_val in lists_input:
        similarity_dict[right_val] += 1

    result = 0

    for left_val, __ in lists_input:
        result += left_val * similarity_dict[left_val]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
