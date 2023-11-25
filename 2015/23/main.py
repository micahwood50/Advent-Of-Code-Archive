FILENAME = "input.txt"


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def execute(instructions: list[str], registers: dict[str, int]):
    inst_line = 0

    while inst_line < len(instructions):
        opcode, value = instructions[inst_line].split(maxsplit=1)

        match opcode:
            case "hlf":
                registers[value] //= 2
                inst_line += 1

            case "tpl":
                registers[value] *= 3
                inst_line += 1

            case "inc":
                registers[value] += 1
                inst_line += 1

            case "jmp":
                inst_line += int(value)

            case "jie":
                register, offset = value.split(", ")
                if registers[register] % 2 == 0:
                    inst_line += int(offset)

                else:
                    inst_line += 1

            case "jio":
                register, offset = value.split(", ")
                if registers[register] == 1:
                    inst_line += int(offset)

                else:
                    inst_line += 1


def part_1():
    instructions = get_input()

    registers = {
        "a": 0,
        "b": 0,
    }

    execute(instructions, registers)

    result = registers["b"]

    print(f"Answer is {result}")


def part_2():
    instructions = get_input()

    registers = {
        "a": 1,
        "b": 0,
    }

    execute(instructions, registers)

    result = registers["b"]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
