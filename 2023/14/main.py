FILENAME = "input.txt"

ROUND_ROCK_CHAR = "O"
CUBE_ROCK_CHAR = "#"
EMPTY_CHAR = "."

TARGET_CYCLE_NUM = 1_000_000_000


def get_input() -> list[list[str]]:
    grid = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            grid.append(list(line.strip()))

    return grid


def tilt_north(grid: list[list[str]]):
    for col_index in range(len(grid[0])):
        north_position = 0
        for row_index in range(len(grid)):
            if grid[row_index][col_index] != EMPTY_CHAR:
                north_position += 1
            else:
                break

        row_index = north_position
        while row_index < len(grid):
            if grid[row_index][col_index] == CUBE_ROCK_CHAR:
                north_position = row_index
                while (
                    row_index < len(grid) and grid[row_index][col_index] != EMPTY_CHAR
                ):
                    north_position += 1
                    row_index += 1

            elif grid[row_index][col_index] == ROUND_ROCK_CHAR:
                grid[north_position][col_index] = ROUND_ROCK_CHAR
                grid[row_index][col_index] = EMPTY_CHAR
                north_position += 1
                row_index += 1

            else:
                row_index += 1


def tilt_south(grid: list[list[str]]):
    for col_index in range(len(grid[0])):
        south_position = len(grid) - 1
        for row_index in range(len(grid) - 1, -1, -1):
            if grid[row_index][col_index] != EMPTY_CHAR:
                south_position -= 1
            else:
                break

        row_index = south_position
        while 0 <= row_index:
            if grid[row_index][col_index] == CUBE_ROCK_CHAR:
                south_position = row_index
                while (
                    row_index < len(grid) and grid[row_index][col_index] != EMPTY_CHAR
                ):
                    south_position -= 1
                    row_index -= 1

            elif grid[row_index][col_index] == ROUND_ROCK_CHAR:
                grid[south_position][col_index] = ROUND_ROCK_CHAR
                grid[row_index][col_index] = EMPTY_CHAR
                south_position -= 1
                row_index -= 1

            else:
                row_index -= 1


def tilt_west(grid: list[list[str]]):
    for row_index in range(len(grid)):
        west_position = 0
        for col_index in range(len(grid[0])):
            if grid[row_index][col_index] != EMPTY_CHAR:
                west_position += 1
            else:
                break

        col_index = west_position
        while col_index < len(grid[0]):
            if grid[row_index][col_index] == CUBE_ROCK_CHAR:
                west_position = col_index
                while (
                    col_index < len(grid[0])
                    and grid[row_index][col_index] != EMPTY_CHAR
                ):
                    west_position += 1
                    col_index += 1

            elif grid[row_index][col_index] == ROUND_ROCK_CHAR:
                grid[row_index][west_position] = ROUND_ROCK_CHAR
                grid[row_index][col_index] = EMPTY_CHAR
                west_position += 1
                col_index += 1

            else:
                col_index += 1


def tile_east(grid: list[list[str]]):
    for row_index in range(len(grid)):
        east_position = len(grid[0]) - 1
        for col_index in range(len(grid[0]) - 1, -1, -1):
            if grid[row_index][col_index] != EMPTY_CHAR:
                east_position -= 1
            else:
                break

        col_index = east_position
        while 0 <= col_index:
            if grid[row_index][col_index] == CUBE_ROCK_CHAR:
                east_position = col_index
                while (
                    col_index < len(grid[0])
                    and grid[row_index][col_index] != EMPTY_CHAR
                ):
                    east_position -= 1
                    col_index -= 1

            elif grid[row_index][col_index] == ROUND_ROCK_CHAR:
                grid[row_index][east_position] = ROUND_ROCK_CHAR
                grid[row_index][col_index] = EMPTY_CHAR
                east_position -= 1
                col_index -= 1

            else:
                col_index -= 1


def part_1():
    grid = get_input()
    result = 0

    tilt_north(grid)

    for row_index in range(len(grid)):
        for ch in grid[row_index]:
            if ch == ROUND_ROCK_CHAR:
                result += len(grid) - row_index

    print(f"Answer is {result}")


def part_2():
    grid = get_input()
    result = 0
    cycle_num = 0
    seen_grid = dict()
    jump_flag = False

    while cycle_num != TARGET_CYCLE_NUM:
        if not jump_flag:
            immutable_grid = tuple(tuple(row) for row in grid)

            if immutable_grid in seen_grid:
                jump_flag = True
                cycle_len = cycle_num - seen_grid[immutable_grid]
                cycle_num += cycle_len * (
                    (TARGET_CYCLE_NUM - cycle_num - 1) // cycle_len
                )

            else:
                seen_grid[immutable_grid] = cycle_num

        cycle_num += 1

        tilt_north(grid)
        tilt_west(grid)
        tilt_south(grid)
        tile_east(grid)

    for row_index in range(len(grid)):
        for ch in grid[row_index]:
            if ch == ROUND_ROCK_CHAR:
                result += len(grid) - row_index

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
