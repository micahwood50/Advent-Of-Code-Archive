FILENAME = "input.txt"

START_CHAR = "S"
GROUND_CHAR = "."
OUTSIDE_CHAR = "O"
INSIDE_CHAR = "I"

DIRECTIONS = [
    ((0, 1), "W"),
    ((0, -1), "E"),
    ((1, 0), "N"),
    ((-1, 0), "S"),
]

TO_NORTH_POSSIBLE_PIPE = {"|", "7", "F"}
TO_SOUTH_POSSIBLE_PIPE = {"|", "J", "L"}
TO_WEST_POSSIBLE_PIPE = {"-", "L", "F"}
TO_EAST_POSSIBLE_PIPE = {"-", "7", "J"}


def get_input() -> list[list[str]]:
    grid = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            grid.append([ch for ch in line.strip()])

    return grid


def part_1():
    grid = get_input()
    result = 0

    for ri, row in enumerate(grid):
        for ci, ch in enumerate(row):
            if ch == START_CHAR:
                sr, sc = ri, ci
                break
        else:
            continue
        break

    queue = list()
    visited_set = {(sr, sc)}

    for (dr, dc), from_direction in DIRECTIONS:
        queue.append((sr + dr, sc + dc, 1, from_direction))

    while queue:
        ri, ci, dist, from_direction = queue.pop(0)

        if (
            0 <= ri < len(grid)
            and 0 <= ci < len(grid[0])
            and (ri, ci) not in visited_set
        ):
            match grid[ri][ci]:
                case ".":
                    continue

                case "|":
                    if from_direction == "W" or from_direction == "E":
                        continue

                    if from_direction == "N":
                        direction_index = 2

                    else:
                        direction_index = 3

                case "-":
                    if from_direction == "N" or from_direction == "S":
                        continue

                    if from_direction == "W":
                        direction_index = 0

                    else:
                        direction_index = 1

                case "L":
                    if from_direction == "W" or from_direction == "S":
                        continue

                    if from_direction == "N":
                        direction_index = 0

                    else:
                        direction_index = 3

                case "J":
                    if from_direction == "E" or from_direction == "S":
                        continue

                    if from_direction == "N":
                        direction_index = 1

                    else:
                        direction_index = 3

                case "7":
                    if from_direction == "N" or from_direction == "E":
                        continue

                    if from_direction == "W":
                        direction_index = 2

                    else:
                        direction_index = 1

                case "F":
                    if from_direction == "N" or from_direction == "W":
                        continue

                    if from_direction == "E":
                        direction_index = 2

                    else:
                        direction_index = 0

                case _:
                    continue

            visited_set.add((ri, ci))
            result = max(result, dist)

            (dr, dc), this_from_direction = DIRECTIONS[direction_index]
            next_ri = ri + dr
            next_ci = ci + dc

            if 0 <= next_ri < len(grid) and 0 <= next_ci < len(grid[0]):
                queue.append((next_ri, next_ci, dist + 1, this_from_direction))

    print(f"Answer is {result}")


def part_2():
    grid = get_input()

    for ri, row in enumerate(grid):
        for ci, ch in enumerate(row):
            if ch == START_CHAR:
                sr, sc = ri, ci
                break
        else:
            continue
        break

    queue = list()
    visited_set = {(sr, sc)}

    for (dr, dc), from_direction in DIRECTIONS:
        queue.append((sr + dr, sc + dc, 1, from_direction))

    while queue:
        ri, ci, dist, from_direction = queue.pop(0)

        if (
            0 <= ri < len(grid)
            and 0 <= ci < len(grid[0])
            and (ri, ci) not in visited_set
        ):
            match grid[ri][ci]:
                case ".":
                    continue

                case "|":
                    if from_direction == "W" or from_direction == "E":
                        continue

                    if from_direction == "N":
                        direction_index = 2

                    else:
                        direction_index = 3

                case "-":
                    if from_direction == "N" or from_direction == "S":
                        continue

                    if from_direction == "W":
                        direction_index = 0

                    else:
                        direction_index = 1

                case "L":
                    if from_direction == "W" or from_direction == "S":
                        continue

                    if from_direction == "N":
                        direction_index = 0

                    else:
                        direction_index = 3

                case "J":
                    if from_direction == "E" or from_direction == "S":
                        continue

                    if from_direction == "N":
                        direction_index = 1

                    else:
                        direction_index = 3

                case "7":
                    if from_direction == "N" or from_direction == "E":
                        continue

                    if from_direction == "W":
                        direction_index = 2

                    else:
                        direction_index = 1

                case "F":
                    if from_direction == "N" or from_direction == "W":
                        continue

                    if from_direction == "E":
                        direction_index = 2

                    else:
                        direction_index = 0

                case _:
                    continue

            visited_set.add((ri, ci))

            (dr, dc), this_from_direction = DIRECTIONS[direction_index]
            next_ri = ri + dr
            next_ci = ci + dc

            if 0 <= next_ri < len(grid) and 0 <= next_ci < len(grid[0]):
                queue.append((next_ri, next_ci, dist + 1, this_from_direction))

    if (
        1 <= sc < len(grid[0]) - 1
        and grid[sr][sc - 1] in TO_WEST_POSSIBLE_PIPE
        and grid[sr][sc + 1] in TO_EAST_POSSIBLE_PIPE
    ):
        grid[sr][sc] = "-"

    elif (
        1 <= sr < len(grid) - 1
        and grid[sr - 1][sc] in TO_NORTH_POSSIBLE_PIPE
        and grid[sr + 1][sc] in TO_SOUTH_POSSIBLE_PIPE
    ):
        grid[sr][sc] = "|"

    elif (
        sr < len(grid) - 1
        and sc < len(grid[0]) - 1
        and grid[sr + 1][sc] in TO_SOUTH_POSSIBLE_PIPE
        and grid[sr][sc + 1] in TO_EAST_POSSIBLE_PIPE
    ):
        grid[sr][sc] = "F"

    elif (
        sr < len(grid) - 1
        and 1 <= sc
        and grid[sr + 1][sc] in TO_SOUTH_POSSIBLE_PIPE
        and grid[sr][sc - 1] in TO_WEST_POSSIBLE_PIPE
    ):
        grid[sr][sc] = "7"

    elif (
        1 <= sr
        and 1 <= sc
        and grid[sr - 1][sc] in TO_SOUTH_POSSIBLE_PIPE
        and grid[sr][sc - 1] in TO_WEST_POSSIBLE_PIPE
    ):
        grid[sr][sc] = "J"

    elif (
        1 <= sr
        and sc < len(grid[0]) - 1
        and grid[sr - 1][sc] in TO_SOUTH_POSSIBLE_PIPE
        and grid[sr][sc + 1] in TO_EAST_POSSIBLE_PIPE
    ):
        grid[sr][sc] = "L"

    for ri in range(len(grid)):
        for ci in range(len(row)):
            if (ri, ci) not in visited_set:
                grid[ri][ci] = GROUND_CHAR

    result = 0

    for ri, row in enumerate(grid):
        curr_side = OUTSIDE_CHAR
        on_pipe = False

        for ci, ch in enumerate(row):
            if ch == GROUND_CHAR:
                if curr_side == INSIDE_CHAR:
                    result += 1

                grid[ri][ci] = curr_side

            else:
                if on_pipe == False:
                    if ch in {"F", "L"}:
                        on_pipe = True
                        collision_ch = ch

                    else:
                        if curr_side == OUTSIDE_CHAR:
                            curr_side = INSIDE_CHAR

                        else:
                            curr_side = OUTSIDE_CHAR

                else:
                    if ch != "-":
                        on_pipe = False

                        if ch == "J":
                            if collision_ch == "L":
                                continue

                        if ch == "7":
                            if collision_ch == "F":
                                continue

                        if curr_side == OUTSIDE_CHAR:
                            curr_side = INSIDE_CHAR

                        else:
                            curr_side = OUTSIDE_CHAR

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
