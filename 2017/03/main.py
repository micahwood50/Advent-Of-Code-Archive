FILENAME = "input.txt"


def generator_spiral_distance():
    yield 0

    distance = 1
    n = 2

    while True:
        for __ in range(4):
            for __ in range((n - 1) // 2):
                yield distance
                distance -= 1

            for __ in range(n // 2):
                yield distance
                distance += 1

            yield distance
            distance -= 1

        distance += 2
        n += 2


def get_input() -> int:
    with open(FILENAME) as file:
        return int(file.readline())


def part_1():
    num = get_input()

    for k, distance in enumerate(generator_spiral_distance(), start=1):
        if k == num:
            result = distance
            break

    print(f"Answer is {result}")


def part_2():
    num = get_input()
    result = 0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    sq_len = int(num**0.5) + 5
    center = sq_len // 2

    grid = [[0 for __ in range(sq_len)] for __ in range(sq_len)]
    curr_point = (center, center)
    d_index = 2
    n_times = 2
    n = 1
    max_n = 1

    grid[curr_point[0]][curr_point[1]] = 1

    while True:
        dx, dy = directions[d_index]

        curr_x, curr_y = curr_point
        curr_x += dx
        curr_y += dy
        curr_point = (curr_x, curr_y)

        grid[curr_y][curr_x] = (
            grid[curr_y - 1][curr_x - 1]
            + grid[curr_y - 1][curr_x]
            + grid[curr_y - 1][curr_x + 1]
            + grid[curr_y][curr_x - 1]
            + grid[curr_y][curr_x + 1]
            + grid[curr_y + 1][curr_x - 1]
            + grid[curr_y + 1][curr_x]
            + grid[curr_y + 1][curr_x + 1]
        )

        if grid[curr_y][curr_x] > num:
            result = grid[curr_y][curr_x]
            break

        n -= 1

        if n == 0:
            n_times -= 1
            d_index = (d_index + 1) % 4

            if n_times == 0:
                n_times = 2
                max_n += 1

            n = max_n

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
