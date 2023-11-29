FILENAME = "input.txt"

GOAL_X = 31
GOAL_Y = 39


def get_input() -> int:
    with open(FILENAME) as file:
        return int(file.readline())


def f(x: int, y: int) -> int:
    return x * x + 3 * x + 2 * x * y + y + y * y


def part_1():
    designer_num = get_input()

    visited_coord = set()
    queue = [(1, 1, 0)]

    while queue:
        this_x, this_y, this_dist = queue.pop(0)

        if (
            (this_x, this_y) in visited_coord
            or this_x < 0
            or this_y < 0
            or (f(this_x, this_y) + designer_num).bit_count() % 2 == 1
        ):
            continue

        visited_coord.add((this_x, this_y))

        if this_x == GOAL_X and this_y == GOAL_Y:
            print(f"Answer is {this_dist}")
            return

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            queue.append((this_x + dx, this_y + dy, this_dist + 1))

    print("Destination is unreachable!")


def part_2():
    designer_num = get_input()

    visited_coord = set()
    queue = [(1, 1, 0)]

    while queue:
        this_x, this_y, this_dist = queue.pop(0)

        if (
            (this_x, this_y) in visited_coord
            or this_x < 0
            or this_y < 0
            or (f(this_x, this_y) + designer_num).bit_count() % 2 == 1
            or this_dist > 50
        ):
            continue

        visited_coord.add((this_x, this_y))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            queue.append((this_x + dx, this_y + dy, this_dist + 1))

    result = len(visited_coord)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
