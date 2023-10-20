FILENAME = "input.txt"


def get_input() -> tuple[int, int]:
    with open(FILENAME) as file:
        return tuple(map(int, file.readline().split("-")))


def part_1():
    low_bound, high_bound = get_input()
    result = 0

    for n in range(low_bound, high_bound + 1):
        str_n = str(n)
        double_flag = False

        for i in range(len(str_n) - 1):
            if str_n[i] > str_n[i + 1]:
                break

            if str_n[i] == str_n[i + 1]:
                double_flag = True

        else:
            if double_flag:
                result += 1

    print(f"Answer is {result}")


def part_2():
    low_bound, high_bound = get_input()
    result = 0

    for n in range(low_bound, high_bound + 1):
        str_n = str(n)
        double_flag = False
        is_repeating = False
        double_only_flag = False

        for i in range(len(str_n) - 1):
            if str_n[i] > str_n[i + 1]:
                break

            if str_n[i] == str_n[i + 1]:
                if double_flag:
                    is_repeating = True

                double_flag = True

            else:
                if double_flag and not is_repeating:
                    double_only_flag = True

                double_flag = False
                is_repeating = False

        else:
            if double_only_flag or (double_flag and not is_repeating):
                result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
