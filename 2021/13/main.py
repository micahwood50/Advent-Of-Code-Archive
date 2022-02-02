from dataclasses import dataclass

FILENAME = "input.txt"


@dataclass
class FoldInstruction:
    direction: str
    line_val: int


def get_input() -> tuple[set[tuple[int, int]], list[FoldInstruction]]:
    dots_set = set()
    instruction_list = list()

    flag = True

    with open(FILENAME) as file:
        for line in file.readlines():
            if flag:
                if line.strip() == "":
                    flag = False
                    continue
                else:
                    dots_set.add(tuple(map(int, line.split(","))))
            else:
                eq = line.split()[2]
                direction, val = eq.split("=")
                val = int(val)
                instruction_list.append(FoldInstruction(direction, val))

    return dots_set, instruction_list


def fold(
    dots: set[tuple[int, int]], instruction: FoldInstruction
) -> set[tuple[int, int]]:
    result = set()
    line_val = instruction.line_val

    if instruction.direction == "x":
        for x, y in dots:
            if x < line_val:
                result.add((x, y))

            elif x > line_val:
                result.add((2 * line_val - x, y))

    else:
        for x, y in dots:
            if y < line_val:
                result.add((x, y))

            elif y > line_val:
                result.add((x, 2 * line_val - y))

    return result


def print_paper(dots: set[tuple[int, int]]):
    x_max, y_max = 0, 0

    for x, y in dots:
        x_max = max(x, x_max)
        y_max = max(y, y_max)

    grid = [[" " for __ in range(x_max + 1)] for __ in range(y_max + 1)]

    for x, y in dots:
        grid[y][x] = "#"

    for row in grid:
        print("".join(row))


def part_1():
    dots_set, instruction_list = get_input()

    dots_set = fold(dots_set, instruction_list[0])

    print(
        f"{len(dots_set)} dots are visible after completing just the first fold instruction"
    )


def part_2():
    dots_set, instruction_list = get_input()

    for instruction in instruction_list:
        dots_set = fold(dots_set, instruction)

    print("After finishing the instructions, the transparent paper looks like this:")
    print_paper(dots_set)


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
