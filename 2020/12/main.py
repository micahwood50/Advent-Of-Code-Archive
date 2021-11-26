from collections import namedtuple
import numpy as np
from pprint import pprint

FILENAME = "input.txt"

D = ['N', 'E', 'S', 'W']

Direction = namedtuple("Direction", ["direction", "unit"])

def rotate(position, degree):
    rad = degree * np.pi/180
    cos_val = np.cos(rad)
    sin_val = np.sin(rad)

    R = np.array([[cos_val, sin_val],[-sin_val, cos_val]])

    return np.dot(position, R)

def get_input() -> list[str]:
    directions = list()

    with open(FILENAME) as f:
        for line in f.readlines():
            directions.append(Direction(line[0], int(line[1:])))

    return directions

def part_1():
    directions = get_input()
    position = np.array([0, 0])
    head_direction_index = 1

    for direction, unit in directions:
        if direction == 'R':
            head_direction_index = (head_direction_index + unit//90)%4

        elif direction == 'L':
            head_direction_index = (head_direction_index - unit//90)%4

        else:
            if direction == 'F':
                direction = D[head_direction_index]

            if direction == 'N':
                position += np.array([0, unit])

            elif direction == 'W':
                position -= np.array([unit, 0])

            elif direction == 'E':
                position += np.array([unit, 0])

            else:
                position -= np.array([0, unit])

    result = abs(position[0]) + abs(position[1])

    print(f"Distance: {result}")

def part_2():
    directions = get_input()
    ship_position = np.array([0, 0], float)
    waypoint_position = np.array([10, 1], float)
    head_direction_index = 1

    for direction, unit in directions:
        if direction == 'R':
            waypoint_position = rotate(waypoint_position, -unit)

        elif direction == 'L':
            waypoint_position = rotate(waypoint_position, unit)

        elif direction == 'F':
            ship_position += unit*waypoint_position

        elif direction == 'N':
            waypoint_position += np.array([0, unit])

        elif direction == 'W':
            waypoint_position -= np.array([unit, 0])

        elif direction == 'E':
            waypoint_position += np.array([unit, 0])

        else:
            waypoint_position -= np.array([0, unit])

    result = abs(ship_position[0]) + abs(ship_position[1])

    print(f"Distance: {result}")

if __name__ == "__main__":
    # part_1()
    part_2()

    pass
