from itertools import permutations


FILENAME = "input.txt"


class Intcode:
    def __init__(self, input: list[int]):
        self.input = input
        self.is_halted = False
        self.input_history = list()

        self.instruction_pointer = 0
        self.comp_input_pointer = 0
        self.output = 0

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

    def compute(self, comp_input: list[int]):
        if self.is_halted:
            raise ValueError("Cannot execute halted computer!")

        self.input_history.extend(comp_input)

        while self.input[self.instruction_pointer] != 99:
            value = str(self.input[self.instruction_pointer]).rjust(5, "0")

            opcode = value[-2:]
            modes = [int(digit) for digit in value[2::-1].rjust(3, "0")]

            match opcode:
                case "01":  # Add
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, self.instruction_pointer
                    )

                    calc_result = first_parameter + second_parameter

                    self.input[self.input[self.instruction_pointer + 3]] = calc_result

                    self.instruction_pointer += 4

                case "02":  # Multiple
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, self.instruction_pointer
                    )

                    calc_result = first_parameter * second_parameter

                    self.input[self.input[self.instruction_pointer + 3]] = calc_result

                    self.instruction_pointer += 4

                case "03":  # Get input
                    self.input[
                        self.input[self.instruction_pointer + 1]
                    ] = self.input_history[self.comp_input_pointer]

                    self.instruction_pointer += 2
                    self.comp_input_pointer += 1

                case "04":  # Write to output
                    self.output = self.input[self.input[self.instruction_pointer + 1]]
                    self.instruction_pointer += 2
                    return self.output

                case "05":  # jump-if-true
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, self.instruction_pointer
                    )

                    if first_parameter != 0:
                        self.instruction_pointer = second_parameter
                    else:
                        self.instruction_pointer += 3

                case "06":  # jump-if-false
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, self.instruction_pointer
                    )

                    if first_parameter == 0:
                        self.instruction_pointer = second_parameter
                    else:
                        self.instruction_pointer += 3

                case "07":  # less than
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, self.instruction_pointer
                    )

                    self.input[self.input[self.instruction_pointer + 3]] = (
                        1 if first_parameter < second_parameter else 0
                    )
                    self.instruction_pointer += 4

                case "08":  # equals
                    first_parameter, second_parameter = self._get_parameters(
                        modes, 2, self.instruction_pointer
                    )

                    self.input[self.input[self.instruction_pointer + 3]] = (
                        1 if first_parameter == second_parameter else 0
                    )
                    self.instruction_pointer += 4

                case _:
                    raise ValueError(
                        f"Invalid program! Value {self.input[self.instruction_pointer]} at position {self.instruction_pointer}"
                    )

        self.is_halted = True
        return self.output


def get_input() -> list[int]:
    with open(FILENAME) as file:
        return list(map(int, file.readline().split(",")))


def part_1():
    program_input = get_input()
    max_value = float("-inf")

    for ps in permutations(range(5), 5):
        amplifiers = [Intcode(program_input) for __ in range(5)]
        prev_result = 0

        for i in range(5):
            prev_result = amplifiers[i].compute([ps[i], prev_result])

        if max_value < prev_result:
            max_value = prev_result

    print(f"Answer is {max_value}")


def part_2():
    program_input = get_input()
    max_value = float("-inf")

    for ps in permutations(range(5, 10), 5):
        amplifiers: list[Intcode] = [Intcode(program_input) for __ in range(5)]
        prev_result = 0

        for i in range(5):
            try:
                amplifiers[i].compute([ps[i]])
            except IndexError:
                pass

        while not amplifiers[-1].is_halted:
            for i in range(5):
                prev_result = amplifiers[i].compute([prev_result])

        if max_value < prev_result:
            max_value = prev_result

    print(f"Answer is {max_value}")


if __name__ == "__main__":
    part_1()
    part_2()
    pass
