FILENAME = "input.txt"


def is_low_point(grid: list[list[int]], row_index: int, col_index: int) -> bool:
    point_height = grid[row_index][col_index]

    if row_index == 0:
        if col_index == 0:
            return (
                point_height < grid[row_index][col_index + 1]
                and point_height < grid[row_index + 1][col_index]
            )
        if col_index == len(grid[0]) - 1:
            return (
                point_height < grid[row_index][col_index - 1]
                and point_height < grid[row_index + 1][col_index]
            )
        return (
            point_height < grid[row_index][col_index - 1]
            and point_height < grid[row_index + 1][col_index]
            and point_height < grid[row_index][col_index + 1]
        )

    if row_index == len(grid) - 1:
        if col_index == 0:
            return (
                point_height < grid[row_index][col_index + 1]
                and point_height < grid[row_index - 1][col_index]
            )
        if col_index == len(grid[0]) - 1:
            return (
                point_height < grid[row_index][col_index - 1]
                and point_height < grid[row_index - 1][col_index]
            )
        return (
            point_height < grid[row_index][col_index - 1]
            and point_height < grid[row_index - 1][col_index]
            and point_height < grid[row_index][col_index + 1]
        )

    if col_index == 0:
        return (
            point_height < grid[row_index - 1][col_index]
            and point_height < grid[row_index][col_index + 1]
            and point_height < grid[row_index + 1][col_index]
        )

    if col_index == len(grid[0]) - 1:
        return (
            point_height < grid[row_index - 1][col_index]
            and point_height < grid[row_index][col_index - 1]
            and point_height < grid[row_index + 1][col_index]
        )

    return (
        point_height < grid[row_index - 1][col_index]
        and point_height < grid[row_index][col_index - 1]
        and point_height < grid[row_index + 1][col_index]
        and point_height < grid[row_index][col_index + 1]
    )


def get_basin_area(grid: list[list[int]], row_index: int, col_index: int) -> int:
    visited_set = set()

    queue = [(row_index, col_index)]

    while queue:
        r, c = queue.pop()
        if (r, c) in visited_set:
            continue

        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 9:
            visited_set.add((r, c))

            queue.extend([(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)])

    return len(visited_set)


def get_input() -> list[list[int]]:
    grid = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            grid.append([int(ch) for ch in line.strip()])

    return grid


def part_1():
    grid = get_input()
    result = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_low_point(grid, r, c):
                result += 1 + grid[r][c]

    print(f"The sum of the risk levels is {result}")


def part_2():
    grid = get_input()
    area_list = list()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_low_point(grid, r, c):
                area_list.append(get_basin_area(grid, r, c))

    area_list.sort(reverse=True)

    a, b, c = area_list[:3]

    print(f"The multiplication of the sizes of three largest basins is {a * b * c}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
