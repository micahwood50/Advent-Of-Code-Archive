FILENAME = "input.txt"


def get_input() -> list[int]:
    int_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            int_list.append(int(line))

    return int_list


def part_1():
    input = get_input()
    result = 0

    for n in input:
        result += n

    print(f"Answer is {result}")


def part_2():
    input = get_input()
    result = 0
    visited_set = set()

    while True:
        for n in input:
            result += n
            if result in visited_set:
                break

            visited_set.add(result)

        else:
            continue

        break

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
