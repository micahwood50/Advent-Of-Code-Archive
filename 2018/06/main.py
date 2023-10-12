from collections import defaultdict


FILENAME = "input.txt"
EQUAL_DISTANCE_LABEL = -1


def manhattan_distance(coord1: tuple[int, int], coord2: tuple[int, int]) -> int:
    x1, y1 = coord1
    x2, y2 = coord2

    return abs(x1 - x2) + abs(y1 - y2)


def get_input() -> list[tuple[int, int]]:
    coord_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            coord_list.append(tuple(map(int, line.strip().split(", "))))

    return coord_list


def part_1():
    coord_list = get_input()
    result = 0

    min_value = float("inf")
    max_value = float("-inf")

    for coord in coord_list:
        this_min_value = min(coord)
        this_max_value = max(coord)

        if this_min_value < min_value:
            min_value = this_min_value

        if this_max_value > max_value:
            max_value = this_max_value

    grid_extra_distance = 10

    low_bound = min_value - grid_extra_distance
    upper_bound = max_value + grid_extra_distance

    grid = dict()
    area_dict = defaultdict(int)

    for x in range(low_bound, upper_bound):
        for y in range(low_bound, upper_bound):
            dist_dict = defaultdict(list)

            for label, curr_coord in enumerate(coord_list):
                this_distance = manhattan_distance((x, y), curr_coord)
                dist_dict[this_distance].append(label)

            min_dist, labels = sorted(list(dist_dict.items()), key=lambda t: t[0])[0]

            if len(labels) > 1:
                grid[(x, y)] = (EQUAL_DISTANCE_LABEL, min_dist)
            else:
                grid[(x, y)] = (labels[0], min_dist)
                area_dict[labels[0]] += 1

    infinite_area_label_set = set()

    for x in range(low_bound, upper_bound):
        this_label_0 = grid[(x, low_bound)][0]
        this_label_1 = grid[(x, upper_bound - 1)][0]

        infinite_area_label_set.add(this_label_0)
        infinite_area_label_set.add(this_label_1)

    for y in range(low_bound, upper_bound):
        this_label_0 = grid[(low_bound, y)][0]
        this_label_1 = grid[(upper_bound - 1, y)][0]

        infinite_area_label_set.add(this_label_0)
        infinite_area_label_set.add(this_label_1)

    for infinite_label in infinite_area_label_set:
        area_dict.pop(infinite_label, None)

    result = max(area_dict.values())

    print(f"Answer is {result}")


def part_2():
    coord_list = get_input()
    max_total_distance = 10_000
    result = 0

    min_value = float("inf")
    max_value = float("-inf")

    for coord in coord_list:
        this_min_value = min(coord)
        this_max_value = max(coord)

        if this_min_value < min_value:
            min_value = this_min_value

        if this_max_value > max_value:
            max_value = this_max_value

    grid_extra_distance = 10

    low_bound = min_value - grid_extra_distance
    upper_bound = max_value + grid_extra_distance

    for x in range(low_bound, upper_bound):
        for y in range(low_bound, upper_bound):
            sum_distance = 0

            for coord in coord_list:
                sum_distance += manhattan_distance((x, y), coord)

            if sum_distance < max_total_distance:
                result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
