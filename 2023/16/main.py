FILENAME = "input.txt"

DIRECTIONS = {
    "N": (-1, 0),
    "W": (0, -1),
    "E": (0, 1),
    "S": (1, 0),
}


def get_input() -> list[list[str]]:
    grid = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            grid.append(list(line.strip()))

    return grid


def part_1():
    grid = get_input()
    result = 0

    queue = [(0, 0, "E")]
    done_set = set()
    coord_set = set()

    while queue:
        row_index, col_index, direction = queue.pop()

        if (row_index, col_index, direction) in done_set:
            continue

        done_set.add((row_index, col_index, direction))
        coord_set.add((row_index, col_index))

        if grid[row_index][col_index] == "|":
            if direction in {"W", "E"}:
                for dir in {"N", "S"}:
                    dr, dc = DIRECTIONS[dir]
                    next_row = row_index + dr
                    next_col = col_index + dc

                    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                        queue.append((next_row, next_col, dir))

                continue

        elif grid[row_index][col_index] == "-":
            if direction in {"N", "S"}:
                for dir in {"W", "E"}:
                    dr, dc = DIRECTIONS[dir]
                    next_row = row_index + dr
                    next_col = col_index + dc

                    if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                        queue.append((next_row, next_col, dir))

                continue

        elif grid[row_index][col_index] == "/":
            if direction == "N":
                dir = "E"

            elif direction == "W":
                dir = "S"

            elif direction == "E":
                dir = "N"

            elif direction == "S":
                dir = "W"

            dr, dc = DIRECTIONS[dir]
            next_row = row_index + dr
            next_col = col_index + dc

            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                queue.append((next_row, next_col, dir))

            continue

        elif grid[row_index][col_index] == "\\":
            if direction == "N":
                dir = "W"

            elif direction == "W":
                dir = "N"

            elif direction == "E":
                dir = "S"

            elif direction == "S":
                dir = "E"

            dr, dc = DIRECTIONS[dir]
            next_row = row_index + dr
            next_col = col_index + dc

            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                queue.append((next_row, next_col, dir))

            continue

        dr, dc = DIRECTIONS[direction]
        next_row = row_index + dr
        next_col = col_index + dc

        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
            queue.append((next_row, next_col, direction))

    result = len(coord_set)

    print(f"Answer is {result}")


def part_2():
    grid = get_input()
    result = 0

    start_coord_set = set()

    for ri in range(len(grid)):
        start_coord_set.add((ri, 0, "E"))
        start_coord_set.add((ri, len(grid[0]) - 1, "W"))

    for ci in range(len(grid[0])):
        start_coord_set.add((0, ci, "S"))
        start_coord_set.add((len(grid) - 1, ci, "N"))

    for start_coord in start_coord_set:
        copy_grid = [row[:] for row in grid]
        queue = [start_coord]
        done_set = set()
        coord_set = set()

        while queue:
            row_index, col_index, direction = queue.pop()

            if (row_index, col_index, direction) in done_set:
                continue

            done_set.add((row_index, col_index, direction))
            coord_set.add((row_index, col_index))

            if copy_grid[row_index][col_index] == "|":
                if direction in {"W", "E"}:
                    for dir in {"N", "S"}:
                        dr, dc = DIRECTIONS[dir]
                        next_row = row_index + dr
                        next_col = col_index + dc

                        if 0 <= next_row < len(copy_grid) and 0 <= next_col < len(
                            copy_grid[0]
                        ):
                            queue.append((next_row, next_col, dir))

                    continue

            elif copy_grid[row_index][col_index] == "-":
                if direction in {"N", "S"}:
                    for dir in {"W", "E"}:
                        dr, dc = DIRECTIONS[dir]
                        next_row = row_index + dr
                        next_col = col_index + dc

                        if 0 <= next_row < len(copy_grid) and 0 <= next_col < len(
                            copy_grid[0]
                        ):
                            queue.append((next_row, next_col, dir))

                    continue

            elif copy_grid[row_index][col_index] == "/":
                if direction == "N":
                    dir = "E"

                elif direction == "W":
                    dir = "S"

                elif direction == "E":
                    dir = "N"

                elif direction == "S":
                    dir = "W"

                dr, dc = DIRECTIONS[dir]
                next_row = row_index + dr
                next_col = col_index + dc

                if 0 <= next_row < len(copy_grid) and 0 <= next_col < len(copy_grid[0]):
                    queue.append((next_row, next_col, dir))

                continue

            elif copy_grid[row_index][col_index] == "\\":
                if direction == "N":
                    dir = "W"

                elif direction == "W":
                    dir = "N"

                elif direction == "E":
                    dir = "S"

                elif direction == "S":
                    dir = "E"

                dr, dc = DIRECTIONS[dir]
                next_row = row_index + dr
                next_col = col_index + dc

                if 0 <= next_row < len(copy_grid) and 0 <= next_col < len(copy_grid[0]):
                    queue.append((next_row, next_col, dir))

                continue

            dr, dc = DIRECTIONS[direction]
            next_row = row_index + dr
            next_col = col_index + dc

            if 0 <= next_row < len(copy_grid) and 0 <= next_col < len(copy_grid[0]):
                queue.append((next_row, next_col, direction))

        result = max(result, len(coord_set))

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
