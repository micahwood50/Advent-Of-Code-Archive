FILENAME = "input.txt"


def get_input() -> list[list[list[str]]]:
    grid_list = list()

    with open(FILENAME) as file:
        this_grid = list()

        for line in file.readlines():
            line = line.strip()

            if line:
                this_grid.append(list(line))

            else:
                grid_list.append(this_grid)
                this_grid = list()

        if this_grid:
            grid_list.append(this_grid)

    return grid_list


def mirrored_row_score(row_index: int, grid: list[list[str]]) -> int:
    result = 0

    upper_index = row_index - 1
    lower_index = row_index

    while 0 <= upper_index and lower_index < len(grid):
        for ci in range(len(grid[0])):
            if grid[upper_index][ci] != grid[lower_index][ci]:
                result += 1

        upper_index -= 1
        lower_index += 1

    return result


def mirrored_col_score(col_index: int, grid: list[list[str]]) -> int:
    result = 0

    left_index = col_index - 1
    right_index = col_index

    while 0 <= left_index and right_index < len(grid[0]):
        for ri in range(len(grid)):
            if grid[ri][left_index] != grid[ri][right_index]:
                result += 1

        left_index -= 1
        right_index += 1

    return result


def part_1():
    grid_list = get_input()
    row_result = 0
    col_result = 0

    for grid in grid_list:
        for row_index in range(1, len(grid)):
            if mirrored_row_score(row_index, grid) == 0:
                row_result += row_index

        for col_index in range(1, len(grid[0])):
            if mirrored_col_score(col_index, grid) == 0:
                col_result += col_index

    result = 100 * row_result + col_result

    print(f"Answer is {result}")


def part_2():
    grid_list = get_input()
    row_result = 0
    col_result = 0

    for grid in grid_list:
        for row_index in range(1, len(grid)):
            if mirrored_row_score(row_index, grid) == 1:
                row_result += row_index

        for col_index in range(1, len(grid[0])):
            if mirrored_col_score(col_index, grid) == 1:
                col_result += col_index

    result = 100 * row_result + col_result

    print(f"Answer is {result}")


if __name__ == "__main__":
    part_1()
    part_2()
    pass
