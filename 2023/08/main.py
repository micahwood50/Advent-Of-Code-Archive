from math import lcm
from itertools import cycle

FILENAME = "input.txt"


def get_input() -> tuple[str, dict[str, tuple[str, str]]]:
    with open(FILENAME) as file:
        instruction = file.readline().strip()
        node_dict = dict()
        file.readline()

        for line in file.readlines():
            name, tuple_str = line.strip().split(" = ")
            node_dict[name] = tuple_str[1:-1].split(", ")

    return instruction, node_dict


def part_1():
    instruction, node_dict = get_input()
    curr_node = "AAA"
    result = 0

    for step in cycle(instruction):
        if curr_node == "ZZZ":
            print(f"Answer is {result}")
            break

        step_index = 0 if step == "L" else 1

        curr_node = node_dict[curr_node][step_index]

        result += 1


def part_2():
    instruction, node_dict = get_input()
    start_letter, end_letter = "A", "Z"
    starting_list = [node for node in node_dict.keys() if node.endswith(start_letter)]
    step_count_set = set()

    for start_node in starting_list:
        curr_node = start_node
        step_count = 0

        for step in cycle(instruction):
            if curr_node.endswith(end_letter):
                step_count_set.add(step_count)
                break

            step_index = 0 if step == "L" else 1
            curr_node = node_dict[curr_node][step_index]

            step_count += 1

    result = lcm(*step_count_set)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
