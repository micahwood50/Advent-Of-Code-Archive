FILENAME = "input.txt"


class Intcode:
    def __init__(self, input: list[int]):
        self.input = input

    def compute(self):
        i = 0
        while self.input[i] != 99:
            if self.input[i] == 1:
                self.input[self.input[i + 3]] = (
                    self.input[self.input[i + 1]] + self.input[self.input[i + 2]]
                )
            elif self.input[i] == 2:
                self.input[self.input[i + 3]] = (
                    self.input[self.input[i + 1]] * self.input[self.input[i + 2]]
                )
            else:
                raise ValueError("Invalid program!")

            i += 4


def get_input() -> list[int]:
    with open(FILENAME) as file:
        return list(map(int, file.readline().split(",")))


def part_1():
    this_computer = Intcode(get_input())

    this_computer.input[1] = 12
    this_computer.input[2] = 2

    this_computer.compute()

    result = this_computer.input[0]

    print(f"Answer is {result}")


def part_2():
    program = get_input()
    target = 19690720

    for noun in range(0, 100):
        for verb in range(0, 100):
            this_computer = Intcode(program.copy())

            this_computer.input[1] = noun
            this_computer.input[2] = verb

            this_computer.compute()

            if this_computer.input[0] == target:
                result = 100 * noun + verb
                print(f"Answer is {result}")
                return

    raise ValueError("No such input possible!")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
