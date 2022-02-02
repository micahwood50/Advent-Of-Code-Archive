from collections import defaultdict

FILENAME = "input.txt"


class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        self.is_horizontal = y1 == y2
        self.is_vertical = x1 == x2
        self.is_diagonal = x1 != x2 and y1 != y2

    def get_coordinate(self) -> tuple[int, int, int, int]:
        return self._x1, self._y1, self._x2, self._y2


def get_input() -> list[Line]:
    line_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            p1, p2 = line.split(" -> ")
            x1, y1 = map(int, p1.split(","))
            x2, y2 = map(int, p2.split(","))

            line_list.append(Line(x1, y1, x2, y2))

    return line_list


def part_1():
    line_list = get_input()
    coordinate_dict = defaultdict(int)

    for line in line_list:
        x1, y1, x2, y2 = line.get_coordinate()

        if not line.is_diagonal:
            if line.is_horizontal:
                y = y1
                x1, x2 = sorted([x1, x2])
                for x in range(x1, x2 + 1):
                    coordinate_dict[(x, y)] += 1

            else:
                x = x1
                y1, y2 = sorted([y1, y2])
                for y in range(y1, y2 + 1):
                    coordinate_dict[(x, y)] += 1

    result = 0

    for overlap_num in coordinate_dict.values():
        if overlap_num > 1:
            result += 1

    print(f"There are {result} points")


def part_2():
    line_list = get_input()
    coordinate_dict = defaultdict(int)

    for line in line_list:
        x1, y1, x2, y2 = line.get_coordinate()

        if not line.is_diagonal:
            if line.is_horizontal:
                y = y1
                x1, x2 = sorted([x1, x2])
                for x in range(x1, x2 + 1):
                    coordinate_dict[(x, y)] += 1

            else:
                x = x1
                y1, y2 = sorted([y1, y2])
                for y in range(y1, y2 + 1):
                    coordinate_dict[(x, y)] += 1

        else:
            slope = (y1 - y2) / (x1 - x2)

            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])

            if slope == 1:
                for i in range(x2 - x1 + 1):
                    coordinate_dict[(x1 + i, y1 + i)] += 1

            elif slope == -1:
                for i in range(x2 - x1 + 1):
                    coordinate_dict[(x1 + i, y2 - i)] += 1

    result = 0

    for overlap_num in coordinate_dict.values():
        if overlap_num > 1:
            result += 1

    print(f"There are {result} points")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
