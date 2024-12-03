import re

FILENAME = "input.txt"


def get_input() -> str:
    string_list = list()

    with open(FILENAME) as file:
        return file.read().strip()

    return string_list


def part_1():
    memory = get_input()
    result = 0

    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    matches = re.findall(pattern, memory)

    for match in matches:
        n1, n2 = match.split(",")
        n1 = int(n1[4:])
        n2 = int(n2[:-1])

        result += n1 * n2

    print(f"Answer is {result}")


def part_2():
    memory = get_input()
    result = 0

    pattern = r"do\(\)|mul\(\d{1,3},\d{1,3}\)|don\'t\(\)"

    matches = re.findall(pattern, memory)
    do_mul = True

    for match in matches:
        if match == "do()":
            do_mul = True

        elif match == "don't()":
            do_mul = False

        else:
            if do_mul:
                n1, n2 = match.split(",")
                n1 = int(n1[4:])
                n2 = int(n2[:-1])

                result += n1 * n2

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
