FILENAME = "input.txt"


def direction_to_dxdy(direction: str) -> tuple[int, int]:
    if direction == "U":
        return (0, 1)

    if direction == "D":
        return (0, -1)

    if direction == "L":
        return (-1, 0)

    if direction == "R":
        return (1, 0)


class Wire:
    def __init__(self, direction: str, distance: int):
        self.direction = direction
        self.distance = distance

    def __repr__(self) -> str:
        return f'Wire("{self.direction}", {self.distance})'

    def __str__(self) -> str:
        return f"{self.direction}{self.distance})"


def get_input() -> list[list[Wire]]:
    wire_path_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            wire_path_list.append(list())
            wire_str_list = line.strip().split(",")

            for wire_str in wire_str_list:
                wire_path_list[-1].append(Wire(wire_str[0], int(wire_str[1:])))

    return wire_path_list


def part_1():
    wire_paths = get_input()
    graph_dict = dict()
    intersection_set = set()
    result = float("inf")

    for wire_num, wires in enumerate(wire_paths):
        x, y = 0, 0

        for wire in wires:
            dx, dy = direction_to_dxdy(wire.direction)

            for __ in range(wire.distance):
                x += dx
                y += dy

                if (x, y) in graph_dict and graph_dict[(x, y)] != wire_num:
                    intersection_set.add((x, y))
                else:
                    graph_dict[(x, y)] = wire_num

    for x, y in intersection_set:
        result = min(result, abs(x) + abs(y))

    print(f"Answer is {result}")


def part_2():
    wire_paths = get_input()
    graph_dict = dict()
    intersection_dict = dict()

    for wire_num, wires in enumerate(wire_paths):
        x, y = 0, 0
        wire_distance_traveled = 0

        for wire in wires:
            dx, dy = direction_to_dxdy(wire.direction)

            for __ in range(wire.distance):
                x += dx
                y += dy
                wire_distance_traveled += 1

                if (x, y) in graph_dict:
                    if graph_dict[(x, y)][0] != wire_num:
                        intersection_dict[(x, y)] = (
                            wire_distance_traveled + graph_dict[(x, y)][1]
                        )
                else:
                    graph_dict[(x, y)] = (wire_num, wire_distance_traveled)

    print(f"Answer is {min(intersection_dict.values())}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
