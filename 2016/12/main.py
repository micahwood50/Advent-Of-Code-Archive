FILENAME = "input.txt"


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def part_1():
    instructions = get_input()
    registers = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
    }

    inst_line = 0

    while inst_line < len(instructions):
        this_inst = instructions[inst_line]

        inst_code, rest = this_inst.split(maxsplit=1)

        match inst_code:
            case "cpy":
                first_val, second_val = rest.split()

                try:
                    first_val = int(first_val)
                except ValueError:
                    first_val = registers[first_val]

                registers[second_val] = first_val

            case "inc":
                registers[rest] += 1

            case "dec":
                registers[rest] -= 1

            case "jnz":
                first_val, second_val = rest.split()

                try:
                    first_val = int(first_val)
                except ValueError:
                    first_val = registers[first_val]

                if first_val != 0:
                    inst_line += int(second_val) - 1

        inst_line += 1

    result = registers["a"]

    print(f"Answer is {result}")


def part_2():
    instructions = get_input()
    registers = {
        "a": 0,
        "b": 0,
        "c": 1,
        "d": 0,
    }

    inst_line = 0

    while inst_line < len(instructions):
        this_inst = instructions[inst_line]

        inst_code, rest = this_inst.split(maxsplit=1)

        match inst_code:
            case "cpy":
                first_val, second_val = rest.split()

                try:
                    first_val = int(first_val)
                except ValueError:
                    first_val = registers[first_val]

                registers[second_val] = first_val

            case "inc":
                registers[rest] += 1

            case "dec":
                registers[rest] -= 1

            case "jnz":
                first_val, second_val = rest.split()

                try:
                    first_val = int(first_val)
                except ValueError:
                    first_val = registers[first_val]

                if first_val != 0:
                    inst_line += int(second_val) - 1

        inst_line += 1

    result = registers["a"]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
