FILENAME = "input.txt"


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def execute_instruction(instruction_str: str, registers: dict[str, int]):
    r0, i_or_d, v0, _, r1, condition, v1 = instruction_str.split()
    v0 = int(v0)
    v1 = int(v1)

    if eval(f"{registers[r1]} {condition} {v1}"):
        if i_or_d == "inc":
            registers[r0] += v0
        else:
            registers[r0] -= v0


def part_1():
    instructions = get_input()
    registers = dict()

    # Generate registers
    for instruction_str in instructions:
        r0, _, _, _, r1, _, _ = instruction_str.split()
        registers[r0] = 0
        registers[r1] = 0

    # Execute instructions
    for instruction_str in instructions:
        execute_instruction(instruction_str, registers)

    result = max(registers.values())

    print(f"Answer is {result}")


def part_2():
    instructions = get_input()
    registers = dict()

    result = float("-inf")

    # Generate registers
    for instruction_str in instructions:
        r0, _, _, _, r1, _, _ = instruction_str.split()
        registers[r0] = 0
        registers[r1] = 0

    # Execute instructions
    for instruction_str in instructions:
        execute_instruction(instruction_str, registers)
        result = max(result, max(registers.values()))

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
