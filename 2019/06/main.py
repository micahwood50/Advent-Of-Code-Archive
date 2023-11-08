from collections import defaultdict


FILENAME = "input.txt"


def get_input() -> dict[str, set[str]]:
    dict_input = defaultdict(set)

    with open(FILENAME) as file:
        for line in file.readlines():
            first_obj, second_obj = line.strip().split(")")
            dict_input[first_obj].add(second_obj)

    return dict_input


def part_1():
    dict_input = get_input()
    stack = [("COM", 0)]
    result = 0

    while stack:
        this_object, this_depth = stack.pop()
        result += this_depth

        for obj_orbit in dict_input[this_object]:
            stack.append((obj_orbit, this_depth + 1))

    print(f"Answer is {result}")


def part_2():
    dict_input = get_input()
    result = 0

    neighborhood_dict = defaultdict(set)

    for k, v in dict_input.items():
        neighborhood_dict[k] |= v
        for vv in v:
            neighborhood_dict[vv].add(k)

    visited_set = set()
    queue = [("YOU", 0)]

    while queue:
        this_object, this_depth = queue.pop(0)
        if this_object in visited_set:
            continue

        visited_set.add(this_object)

        if this_object == "SAN":
            result = this_depth - 2
            break

        for n in neighborhood_dict[this_object]:
            queue.append((n, this_depth + 1))

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
