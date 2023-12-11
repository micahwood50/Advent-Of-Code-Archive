FILENAME = "input.txt"

EMPTY_CHAR = "."
GALAXIES_CHAR = "#"

EXPAND_SIZE = 999_999


def get_input() -> list[list[str]]:
    grid = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            grid.append(list(line.strip()))

    return grid


def expand_grid(grid: list[list[str]]):
    i = len(grid) - 1

    while i >= 0:
        if GALAXIES_CHAR not in grid[i]:
            grid.insert(i, [EMPTY_CHAR for __ in grid[0]])

        i -= 1

    i = len(grid[0]) - 1

    while i >= 0:
        for j in range(len(grid)):
            if grid[j][i] == GALAXIES_CHAR:
                break

        else:
            for j in range(len(grid)):
                grid[j] = grid[j][:i] + [EMPTY_CHAR] + grid[j][i:]

        i -= 1


def get_empty_lists(grid: list[list[str]]) -> tuple[list[int], list[int]]:
    row_list = list()
    col_list = list()

    i = len(grid) - 1

    while i >= 0:
        if GALAXIES_CHAR not in grid[i]:
            row_list.append(i)

        i -= 1

    i = len(grid[0]) - 1

    while i >= 0:
        for j in range(len(grid)):
            if grid[j][i] == GALAXIES_CHAR:
                break

        else:
            col_list.append(i)

        i -= 1

    return row_list, col_list


def part_1():
    grid = get_input()
    expand_grid(grid)

    result = 0
    galaxies_coord_list = list()

    for ri, row in enumerate(grid):
        for ci, ch in enumerate(row):
            if ch == GALAXIES_CHAR:
                galaxies_coord_list.append((ri, ci))

    for gci in range(len(galaxies_coord_list) - 1):
        for gcj in range(gci + 1, len(galaxies_coord_list)):
            r1, c1 = galaxies_coord_list[gci]
            r2, c2 = galaxies_coord_list[gcj]

            result += abs(r1 - r2) + abs(c1 - c2)

    print(f"Answer is {result}")


def part_2():
    grid = get_input()
    expand_row, expand_col = get_empty_lists(grid)

    result = 0
    galaxies_coord_list = list()

    for ri, row in enumerate(grid):
        for ci, ch in enumerate(row):
            if ch == GALAXIES_CHAR:
                galaxies_coord_list.append((ri, ci))

    for gci in range(len(galaxies_coord_list) - 1):
        for gcj in range(gci + 1, len(galaxies_coord_list)):
            r1, c1 = galaxies_coord_list[gci]
            r2, c2 = galaxies_coord_list[gcj]

            r1, r2 = sorted([r1, r2])
            c1, c2 = sorted([c1, c2])

            count_expand_row = 0
            count_expand_col = 0

            for eri in expand_row:
                if r1 <= eri <= r2:
                    count_expand_row += 1

            for eci in expand_col:
                if c1 <= eci <= c2:
                    count_expand_col += 1

            result += (
                r2 - r1 + c2 - c1 + (count_expand_row + count_expand_col) * EXPAND_SIZE
            )

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
