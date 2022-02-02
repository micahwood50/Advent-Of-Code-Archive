FILENAME = "input.txt"


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip().lower())

    return string_list


def is_nice_1(string: str) -> bool:
    vowel_set = {"a", "e", "i", "o", "u"}
    banned_substr_set = {"ab", "cd", "pq", "xy"}

    double_letter_flag = False
    vowel_counter = 1 if string[-1] in vowel_set else 0

    for index in range(len(string) - 1):
        if string[index] in vowel_set:
            vowel_counter += 1

        if string[index] == string[index + 1]:
            double_letter_flag = True

        if string[index : index + 2] in banned_substr_set:
            return False

    return vowel_counter > 2 and double_letter_flag


def is_nice_2(string: str) -> bool:
    repeat_flag = False
    double_flag = False

    double_dict = dict()

    for index in range(len(string) - 2):
        if string[index] == string[index + 2]:
            repeat_flag = True

        if string[index : index + 2] in double_dict:
            if double_dict[string[index : index + 2]] == index - 1:
                continue

            double_flag = True

        else:
            double_dict[string[index : index + 2]] = index

    if not double_flag:
        double_flag = (
            string[-2:] in double_dict and double_dict[string[-2:]] != len(string) - 3
        )

    return repeat_flag and double_flag


def part_1():
    string_list = get_input()
    result = 0

    for string in string_list:
        if is_nice_1(string):
            result += 1

    print(f"There are {result} nice strings")


def part_2():
    string_list = get_input()
    result = 0

    for string in string_list:
        if is_nice_2(string):
            result += 1

    print(f"There are {result} nice strings")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
