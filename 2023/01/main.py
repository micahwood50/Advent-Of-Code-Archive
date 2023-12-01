FILENAME = "input.txt"

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def part_1():
    calibration_document = get_input()
    result = 0

    for line in calibration_document:
        digits_in_line = list()

        for index, ch in enumerate(line):
            if ch.isdigit():
                digits_in_line.append((index, int(ch)))

        digits_in_line.sort(key=lambda t: t[0])

        result += 10 * digits_in_line[0][1] + digits_in_line[-1][1]

    print(f"Answer is {result}")


def part_2():
    calibration_document = get_input()
    result = 0

    for line in calibration_document:
        digits_in_line = list()

        for index, ch in enumerate(line):
            if ch.isdigit():
                digits_in_line.append((index, int(ch)))

            else:
                for digit_name in DIGITS.keys():
                    if line[index:].startswith(digit_name):
                        digits_in_line.append((index, DIGITS[digit_name]))

        digits_in_line.sort(key=lambda t: t[0])

        result += 10 * digits_in_line[0][1] + digits_in_line[-1][1]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
