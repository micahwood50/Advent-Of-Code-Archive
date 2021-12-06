from enum import Enum, auto
from dataclasses import dataclass
from typing import Callable, Any

FILENAME = "input.txt"

class InstructionType(Enum):
    TURN_ON  = auto()
    TURN_OFF = auto()
    TOGGLE   = auto()

@dataclass
class Instruction:
    command_type: InstructionType
    point_1:       tuple[int, int]
    point_2:       tuple[int, int]

class Grid:
    def __init__(self, *, function_dict: dict[InstructionType, Callable[[Any], Any]]):
        self._grid = [[False for __ in range(1_000)] for __ in range(1_000)]
        self._function_dict = function_dict

    def process_instruction(self, instruction: Instruction):
        x1, y1 = instruction.point_1
        x2, y2 = instruction.point_2

        light_function = self._function_dict[instruction.command_type]

        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                self._grid[y][x] = light_function(self._grid[y][x])

    def sum_all(self) -> int:
        result = 0

        for row in self._grid:
            result += sum(row)

        return result

def get_input() -> list[Instruction]:
    instruction_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            line = line.split()
            p1 = tuple(map(int, line[-3].split(',')))
            p2 = tuple(map(int, line[-1].split(',')))

            if line[0] == "toggle":
                type = InstructionType.TOGGLE
            elif line[1] == "on":
                type = InstructionType.TURN_ON
            else:
                type = InstructionType.TURN_OFF

            instruction_list.append(Instruction(type, p1, p2))

    return instruction_list

def part_1():
    instruction_list = get_input()
    grid = Grid(function_dict = {
        InstructionType.TURN_ON:  lambda bool_val: True,
        InstructionType.TURN_OFF: lambda bool_val: False,
        InstructionType.TOGGLE:   lambda bool_val: not bool_val
    })

    for instruction in instruction_list:
        grid.process_instruction(instruction)

    print(f"{grid.sum_all()} lights are lit")

def part_2():
    instruction_list = get_input()
    grid = Grid(function_dict = {
        InstructionType.TURN_ON:  lambda num: num + 1,
        InstructionType.TURN_OFF: lambda num: num - 1 if num > 0 else 0,
        InstructionType.TOGGLE:   lambda num: num + 2
    })

    for instruction in instruction_list:
        grid.process_instruction(instruction)

    print(f"The total brightness of all lights combined is {grid.sum_all()}")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
