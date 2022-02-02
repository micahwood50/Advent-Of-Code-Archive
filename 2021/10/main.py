from statistics import median

FILENAME = "input.txt"

OPEN_CHARS = {"(", "[", "{", "<"}
CLOSE_CHARS = {")", "]", "}", ">"}

MATCH_DICT = {"(": ")", "[": "]", "{": "}", "<": ">"}


def is_match(open_ch: str, close_ch: str) -> bool:
    return MATCH_DICT[open_ch] == close_ch


def get_match(open_ch: str) -> str:
    return MATCH_DICT[open_ch]


def get_input() -> list[str]:
    line_list = list()

    with open(FILENAME) as file:
        for file_line in file.readlines():
            line_list.append(file_line.strip())

    return line_list


def part_1():
    line_list = get_input()
    result = 0

    point_table = {")": 3, "]": 57, "}": 1197, ">": 25137}

    for line in line_list:
        stack = list()

        for ch in line:
            if ch in OPEN_CHARS:
                stack.append(ch)

            else:
                if stack:
                    open_ch = stack.pop()
                    if not is_match(open_ch, ch):
                        result += point_table[ch]
                        break
                else:
                    break

    print(f"The total syntax error score for those errors is {result}")


def part_2():
    line_list = get_input()
    score_list = list()

    point_table = {")": 1, "]": 2, "}": 3, ">": 4}

    for line in line_list:
        stack = list()

        for ch in line:
            if ch in OPEN_CHARS:
                stack.append(ch)

            else:
                if stack:
                    open_ch = stack.pop()
                    if not is_match(open_ch, ch):
                        break
                else:
                    break

        else:
            if stack:
                closing_str = "".join(get_match(open_ch) for open_ch in reversed(stack))

                score = 0
                for ch in closing_str:
                    score = 5 * score + point_table[ch]

                score_list.append(score)

    print(f"The middle score is {median(score_list)}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
