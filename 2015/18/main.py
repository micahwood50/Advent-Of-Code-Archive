FILENAME = "input.txt"

LIGHT_ON = "#"
LIGHT_OFF = "."

STEPS = 100


def get_input() -> list[list[str]]:
    grid = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            grid.append([ch for ch in line.strip()])

    return grid


def get_next_configuration(grid: list[list[str]]) -> list[list[str]]:
    new_grid = list()

    for i, row in enumerate(grid):
        new_grid.append(list())

        for j, ch in enumerate(row):
            count_on_neighbor = 0

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue

                    try:
                        if (
                            0 <= i + di
                            and 0 <= j + dj
                            and grid[i + di][j + dj] == LIGHT_ON
                        ):
                            count_on_neighbor += 1

                    except IndexError:
                        continue

            if ch == LIGHT_ON:
                if 2 <= count_on_neighbor <= 3:
                    new_ch = LIGHT_ON
                else:
                    new_ch = LIGHT_OFF

            else:
                if count_on_neighbor == 3:
                    new_ch = LIGHT_ON
                else:
                    new_ch = LIGHT_OFF

            new_grid[-1].append(new_ch)

    return new_grid


def part_1():
    grid = get_input()

    for __ in range(STEPS):
        grid = get_next_configuration(grid)

    result = 0

    for row in grid:
        for ch in row:
            if ch == LIGHT_ON:
                result += 1

    print(f"Answer is {result}")


def part_2():
    grid = get_input()

    for __ in range(STEPS):
        grid = get_next_configuration(grid)

        grid[0][0] = LIGHT_ON
        grid[-1][0] = LIGHT_ON
        grid[0][-1] = LIGHT_ON
        grid[-1][-1] = LIGHT_ON

    result = 0

    for row in grid:
        for ch in row:
            if ch == LIGHT_ON:
                result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
