from collections import defaultdict


FILENAME = "input.txt"
NON_SYMBOL = "."
GEAR_SYMBOL = "*"


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def part_1():
    grid = get_input()
    result = 0

    digit_set = set(str(n) for n in range(10))

    for i in range(len(grid)):
        grid[i] = NON_SYMBOL + grid[i] + NON_SYMBOL

    grid.insert(0, NON_SYMBOL * len(grid[0]))
    grid.append(NON_SYMBOL * len(grid[0]))

    for line_index, line in enumerate(grid):
        ch_index = 0

        while ch_index < len(line):
            if line[ch_index].isdigit():
                this_num = ""
                this_start_index = ch_index - 1

                while line[ch_index].isdigit():
                    this_num += line[ch_index]
                    ch_index += 1

                this_num = int(this_num)

                if (
                    set(grid[line_index - 1][this_start_index : ch_index + 1])
                    - digit_set
                    != {NON_SYMBOL}
                    or set(grid[line_index + 1][this_start_index : ch_index + 1])
                    - digit_set
                    != {NON_SYMBOL}
                    or line[this_start_index] != NON_SYMBOL
                    or line[ch_index] != NON_SYMBOL
                ):
                    result += this_num

            else:
                ch_index += 1

    print(f"Answer is {result}")


def part_2():
    grid = get_input()
    result = 0

    for i in range(len(grid)):
        grid[i] = NON_SYMBOL + grid[i] + NON_SYMBOL

    grid.insert(0, NON_SYMBOL * len(grid[0]))
    grid.append(NON_SYMBOL * len(grid[0]))

    gear_dict = defaultdict(list)

    for line_index, line in enumerate(grid):
        ch_index = 0

        while ch_index < len(line):
            if line[ch_index].isdigit():
                this_num = ""
                this_start_index = ch_index - 1

                while line[ch_index].isdigit():
                    this_num += line[ch_index]
                    ch_index += 1

                this_num = int(this_num)

                for i in range(this_start_index, ch_index + 1):
                    if grid[line_index - 1][i] == GEAR_SYMBOL:
                        gear_dict[(line_index - 1, i)].append(this_num)

                    if grid[line_index + 1][i] == GEAR_SYMBOL:
                        gear_dict[(line_index + 1, i)].append(this_num)

                if line[this_start_index] == GEAR_SYMBOL:
                    gear_dict[(line_index, this_start_index)].append(this_num)

                if line[ch_index] == GEAR_SYMBOL:
                    gear_dict[(line_index, ch_index)].append(this_num)

            else:
                ch_index += 1

    for v in gear_dict.values():
        if len(v) == 2:
            result += v[0] * v[1]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
