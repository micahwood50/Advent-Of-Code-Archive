from collections import Counter


FILENAME = "input.txt"


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def part_1():
    repeating_messages = get_input()
    result = ""

    for i in range(len(repeating_messages[0])):
        result += Counter((message[i] for message in repeating_messages)).most_common(
            1
        )[0][0]

    print(f"Answer is {result}")


def part_2():
    repeating_messages = get_input()
    result = ""

    for i in range(len(repeating_messages[0])):
        result += Counter((message[i] for message in repeating_messages)).most_common()[
            -1
        ][0]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
