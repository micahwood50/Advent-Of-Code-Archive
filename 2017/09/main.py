FILENAME = "input.txt"


def get_input() -> str:
    with open(FILENAME) as file:
        return file.readline().strip()


def part_1():
    str_input = get_input()

    cancel_removed_str_input = ""
    index = 0

    while index < len(str_input):
        if str_input[index] == "!":
            index += 2

        else:
            cancel_removed_str_input += str_input[index]
            index += 1

    clean_str_input = ""
    garbage_flag = False

    for ch in cancel_removed_str_input:
        if ch == "<":
            garbage_flag = True

        elif ch == ">":
            garbage_flag = False

        else:
            if not garbage_flag and ch in "{}":
                clean_str_input += ch

    acc_score_to_add = 0
    result = 0

    for ch in clean_str_input:
        if ch == "{":
            acc_score_to_add += 1

        else:
            result += acc_score_to_add
            acc_score_to_add -= 1

    print(f"Answer is {result}")


def part_2():
    str_input = get_input()
    result = 0

    cancel_removed_str_input = ""
    index = 0

    while index < len(str_input):
        if str_input[index] == "!":
            index += 2

        else:
            cancel_removed_str_input += str_input[index]
            index += 1

    garbage_flag = False

    for ch in cancel_removed_str_input:
        if ch == "<" and not garbage_flag:
            garbage_flag = True

        elif ch == ">":
            garbage_flag = False

        else:
            if garbage_flag:
                result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
