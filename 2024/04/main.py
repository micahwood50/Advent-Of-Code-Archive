FILENAME = "input.txt"
GOAL = "XMAS"
GOAL2 = "MAS"


def get_input() -> list[list[str]]:
    grid = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            grid.append(list(line.strip()))

    return grid


def part_1():
    grid = get_input()
    result = 0

    # Horizontal reading
    for ri in range(len(grid)):
        for ci in range(len(grid[0]) - len(GOAL) + 1):
            this_reading = "".join(grid[ri][ci : ci + len(GOAL)])

            if this_reading == GOAL or this_reading[::-1] == GOAL:
                result += 1

    # Vertical reading
    for ri in range(len(grid) - len(GOAL) + 1):
        for ci in range(len(grid[0])):
            this_reading = ""
            for i in range(len(GOAL)):
                this_reading += grid[ri + i][ci]

            if this_reading == GOAL or this_reading[::-1] == GOAL:
                result += 1

    # Diagonal reading
    for ri in range(len(grid) - len(GOAL) + 1):
        for ci in range(len(grid[0]) - len(GOAL) + 1):
            this_reading = ""
            for i in range(len(GOAL)):
                this_reading += grid[ri + i][ci + i]

            if this_reading == GOAL or this_reading[::-1] == GOAL:
                result += 1

            this_reading = ""
            for i in range(len(GOAL)):
                this_reading += grid[ri + i][ci + len(GOAL) - i - 1]

            if this_reading == GOAL or this_reading[::-1] == GOAL:
                result += 1

    print(f"Answer is {result}")


def part_2():
    grid = get_input()
    result = 0

    for ri in range(len(grid) - len(GOAL2) + 1):
        for ci in range(len(grid[0]) - len(GOAL2) + 1):
            this_reading = ""
            that_reading = ""

            for i in range(len(GOAL2)):
                this_reading += grid[ri + i][ci + i]
                that_reading += grid[ri + i][ci + len(GOAL2) - i - 1]

            if (this_reading == GOAL2 or this_reading[::-1] == GOAL2) and (
                that_reading == GOAL2 or that_reading[::-1] == GOAL2
            ):
                result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
