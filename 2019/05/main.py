FILENAME = "input.txt"


class Intcode:
    def __init__(self, input: list[int]):
        self.input = input

    def _get_parameters(
        self, modes: list[int], num_parameter: int, instruction_pointer: int
    ) -> list[int]:
        parameter_list = list()

        for i in range(1, num_parameter + 1):
            if modes[i - 1] == 0:
                this_parameter = self.input[self.input[instruction_pointer + i]]
            else:
                this_parameter = self.input[instruction_pointer + i]

            parameter_list.append(this_parameter)

        return parameter_list

    def compute(self, comp_input: int = 0):
        instruction_pointer = 0
        output = 0

        while self.input[instruction_pointer] != 99:
            value = str(self.input[instruction_pointer]).rjust(5, "0")

            opcode = value[-2:]
            modes = [int(digit) for digit in value[2::-1].rjust(3, "0")]

            match opcode:
                case "01":  # Add
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, instruction_pointer
                    )

                    calc_result = first_parameter + second_parameter

                    self.input[self.input[instruction_pointer + 3]] = calc_result

                    instruction_pointer += 4

                case "02":  # Multiple
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, instruction_pointer
                    )

                    calc_result = first_parameter * second_parameter

                    self.input[self.input[instruction_pointer + 3]] = calc_result

                    instruction_pointer += 4

                case "03":  # Get input
                    self.input[self.input[instruction_pointer + 1]] = comp_input
                    instruction_pointer += 2

                case "04":  # Write to output
                    output = self.input[self.input[instruction_pointer + 1]]
                    instruction_pointer += 2

                case "05":  # jump-if-true
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, instruction_pointer
                    )

                    if first_parameter != 0:
                        instruction_pointer = second_parameter
                    else:
                        instruction_pointer += 3

                case "06":  # jump-if-false
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, instruction_pointer
                    )

                    if first_parameter == 0:
                        instruction_pointer = second_parameter
                    else:
                        instruction_pointer += 3

                case "07":  # less than
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, instruction_pointer
                    )

                    self.input[self.input[instruction_pointer + 3]] = (
                        1 if first_parameter < second_parameter else 0
                    )
                    instruction_pointer += 4

                case "08":  # equals
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, instruction_pointer
                    )

                    self.input[self.input[instruction_pointer + 3]] = (
                        1 if first_parameter == second_parameter else 0
                    )
                    instruction_pointer += 4

                case _:
                    raise ValueError(
                        f"Invalid program! Value {self.input[instruction_pointer]} at position {instruction_pointer}"
                    )

        return output


def get_input() -> list[int]:
    with open(FILENAME) as file:
        return list(map(int, file.readline().split(",")))


def part_1():
    this_computer = Intcode(get_input())

    result = this_computer.compute(1)

    print(f"Answer is {result}")


def part_2():
    this_computer = Intcode(get_input())

    result = this_computer.compute(5)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
