FILENAME = "input.txt"


def get_input() -> dict[int, list[int]]:
    dict_ints = dict()

    with open(FILENAME) as file:
        for line in file.readlines():
            this_program, connected_programs = line.strip().split(" <-> ")

            dict_ints[int(this_program)] = list(
                map(int, connected_programs.split(", "))
            )

    return dict_ints


def part_1():
    program_dict = get_input()
    result = 1
    visited_set = {0}

    queue = program_dict[0]

    while queue:
        this_program = queue.pop(0)

        if this_program in visited_set:
            continue

        visited_set.add(this_program)
        result += 1

        queue.extend(program_dict[this_program])

    print(f"Answer is {result}")


def part_2():
    program_dict = get_input()
    result = 0

    visited_set = set()

    for k in program_dict.keys():
        if k in visited_set:
            continue

        result += 1
        queue = [k]

        while queue:
            this_program = queue.pop(0)

            if this_program in visited_set:
                continue

            visited_set.add(this_program)
            queue.extend(program_dict[this_program])

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
