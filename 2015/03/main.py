FILENAME = "input.txt"


def get_input() -> str:
    with open(FILENAME) as file:
        directions = file.readline().strip()

    return directions


def part_1():
    directions = get_input()

    visited_set = set()
    visited_again_set = set()
    coordinate = (0, 0)

    visited_set.add(coordinate)

    for direction in directions:
        x, y = coordinate

        if direction == ">":
            x += 1

        elif direction == "<":
            x -= 1

        elif direction == "^":
            y += 1

        elif direction == "v":
            y -= 1

        else:
            raise ValueError("Unusual character detected!")

        coordinate = (x, y)

        if coordinate in visited_set:
            if coordinate not in visited_again_set:
                visited_again_set.add(coordinate)

        else:
            visited_set.add(coordinate)

    result = len(visited_set)

    print(f"Answer is {result}")


def part_2():
    directions = get_input()

    visited_set = set()
    visited_again_set = set()
    real_santa_coordinate = (0, 0)
    robot_santa_coordinate = (0, 0)
    turn = 0

    visited_set.add(real_santa_coordinate)

    for direction in directions:
        if turn == 0:
            x, y = real_santa_coordinate
        else:
            x, y = robot_santa_coordinate

        if direction == ">":
            x += 1

        elif direction == "<":
            x -= 1

        elif direction == "^":
            y += 1

        elif direction == "v":
            y -= 1

        else:
            raise ValueError("Unusual character detected!")

        coordinate = (x, y)

        if turn == 0:
            real_santa_coordinate = coordinate
        else:
            robot_santa_coordinate = coordinate

        if coordinate in visited_set:
            if coordinate not in visited_again_set:
                visited_again_set.add(coordinate)

        else:
            visited_set.add(coordinate)

        turn = 1 - turn

    result = len(visited_set)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
