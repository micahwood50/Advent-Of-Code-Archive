FILENAME = "input.txt"


def get_input() -> list[tuple[int, int]]:
    interval_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            interval_list.append(tuple(map(int, line.strip().split("-"))))

    return interval_list


def part_1():
    interval_list = get_input()
    result = 0

    while True:
        for lower, upper in interval_list:
            if lower <= result <= upper:
                result = upper + 1
                break

        else:
            print(f"Answer is {result}")
            return


def part_2():
    interval_list = get_input()
    result = 0
    IP_value = 0

    while IP_value <= 4294967295:
        for lower, upper in interval_list:
            if lower <= IP_value <= upper:
                IP_value = upper + 1
                break

        else:
            result += 1
            IP_value += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
