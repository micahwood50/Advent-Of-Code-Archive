from collections import defaultdict


FILENAME = "input.txt"


class Program:
    def __init__(self, name: str, weight: int, subprogram_names: list[str]) -> None:
        self.name = name
        self.weight = weight
        self.subprogram_names = subprogram_names

    def __str__(self) -> str:
        if self.subprogram_names:
            return f"{self.name} ({self.weight}) -> {', '.join(self.subprogram_names)}"

        return f"{self.name} ({self.weight})"

    def __repr__(self) -> str:
        if self.subprogram_names:
            list_of_subprograms = '", "'.join(self.subprogram_names)
            return f'Program("{self.name}", {self.weight}, ["{list_of_subprograms}"])'

        return f'Program("{self.name}", {self.weight}, [])'


def get_weight(this_program: str, program_dict: dict[str, Program]) -> int:
    this_program: Program = program_dict[this_program]
    result = this_program.weight

    for subprogram in this_program.subprogram_names:
        result += get_weight(subprogram, program_dict)

    return result


def get_input() -> dict[str, Program]:
    program_dict = dict()

    with open(FILENAME) as file:
        for line in file.readlines():
            this_program, remaining = line.strip().split(" (")
            weight, remaining = remaining.split(")")

            subprograms = list()
            if remaining.startswith(" -> "):
                subprograms = remaining[4:].split(", ")

            program_dict[this_program] = Program(this_program, int(weight), subprograms)

    return program_dict


def part_1():
    program_dict = get_input()

    left_programs = set()
    right_programs = set()

    for program in program_dict.values():
        left_programs.add(program.name)
        for right_program in program.subprogram_names:
            right_programs.add(right_program)

    result = left_programs - right_programs

    if len(result) > 1:
        print("There are multiple answers!")

    else:
        print(f"Answer is {result.pop()}")


def part_2():
    program_dict = get_input()

    left_side_program_set = set()
    right_side_program_set = set()

    weight_dict = dict()

    def get_weight(program_name: str) -> int:
        if program_name in weight_dict:
            return weight_dict[program_name]

        else:
            this_program = program_dict[program_name]
            result = this_program.weight

            for subprogram in this_program.subprogram_names:
                result += get_weight(subprogram)

            weight_dict[program_name] = result
            return result

    for program in program_dict.values():
        left_side_program_set.add(program.name)
        for right_program in program.subprogram_names:
            right_side_program_set.add(right_program)

    result = left_side_program_set - right_side_program_set

    if len(result) > 1:
        print("There are multiple answers!")

    else:
        curr_program_name = result.pop()
        get_weight(curr_program_name)

        weight_to_add = 0

        # Hunting for the first sign of unbalanced

        while len(program_dict[curr_program_name].subprogram_names) == 1:
            curr_program_name = program_dict[curr_program_name].subprogram_names[0]

        # If first node with multiple children has only two children
        if len(program_dict[curr_program_name].subprogram_names) == 2:
            raise NotImplementedError
            # TODO; this doesn't happen in my specific case so I was too lazy to implement this case scenario.

        else:
            subprogram_weight_dict = defaultdict(list)

            for subprogram_name in program_dict[curr_program_name].subprogram_names:
                this_weight = get_weight(subprogram_name)
                subprogram_weight_dict[this_weight].append(subprogram_name)

            # Checking if assumption that only one weight need to be fixed still holds
            assert len(subprogram_weight_dict) == 2

            items = list(subprogram_weight_dict.items())

            k0, v0 = items[0]
            k1, v1 = items[1]

            if len(v0) == 1:
                weight_to_add = k1 - k0

            else:
                # Checking if assumption that only one weight need to be fixed still holds
                assert len(v1) == 1

                weight_to_add = k0 - k1

        # We figured out how unbalance this tree is. Now hunting for the program with wrong weight.

        while True:
            if len(program_dict[curr_program_name].subprogram_names) == 1:
                curr_program_name = program_dict[curr_program_name].subprogram_names[0]

            else:
                subprogram_weight_dict = defaultdict(list)

                for subprogram_name in program_dict[curr_program_name].subprogram_names:
                    this_weight = get_weight(subprogram_name)
                    subprogram_weight_dict[this_weight].append(subprogram_name)

                if len(subprogram_weight_dict) == 1:
                    break

                for v in subprogram_weight_dict.values():
                    if len(v) == 1:
                        curr_program_name = v[0]

        result = program_dict[curr_program_name].weight + weight_to_add
        print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
