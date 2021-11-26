from collections import namedtuple

FILENAME = "input.txt"

Direction = namedtuple("Direction", ["turn", "distacne"])

def get_input() -> list[Direction]:
    directions = list()

    with open(FILENAME) as f:
        for direction_str in f.readline().strip().split(", "):
            directions.append(Direction(direction_str[0], int(direction_str[1:])))

    return directions

def part_1():
    directions = get_input()

    head_direction = ['N', 'W', 'S', 'E']
    head_direction_index = 0

    x, y = 0, 0

    for turn_direction, distance in directions:
        if turn_direction == 'R':
            head_direction_index += 1
        else:
            head_direction_index -= 1

        head_direction_index %= 4

        if head_direction[head_direction_index] == 'N':
            y += distance

        elif head_direction[head_direction_index] == 'W':
            x -= distance

        elif head_direction[head_direction_index] == 'S':
            y -= distance

        else:
            x += distance

    print(f"Easter Bunny HQ is {abs(x)+abs(y)} blocks away.")

def find_twice_visit() -> tuple[int, int]:
    directions = get_input()

    head_direction = ['N', 'W', 'S', 'E']
    head_direction_index = 0

    x, y = 0, 0
    visited = set()

    for turn_direction, distance in directions:
        if turn_direction == 'R':
            head_direction_index += 1
        else:
            head_direction_index -= 1

        head_direction_index %= 4

        if head_direction[head_direction_index] == 'N':
            for __ in range(distance):
                y += 1
                if (x, y) in visited:
                    return (x, y)

                visited.add((x, y))

        elif head_direction[head_direction_index] == 'W':
            for __ in range(distance):
                x -= 1
                if (x, y) in visited:
                    return (x, y)

                visited.add((x, y))

        elif head_direction[head_direction_index] == 'S':
            for __ in range(distance):
                y -= 1
                if (x, y) in visited:
                    return (x, y)

                visited.add((x, y))

        else:
            for __ in range(distance):
                x += 1
                if (x, y) in visited:
                    return (x, y)

                visited.add((x, y))

    raise ValueError("There is no such location!")

def part_2():
    x, y = find_twice_visit()

    print(f"Easter Bunny HQ is {abs(x)+abs(y)} blocks away.")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
