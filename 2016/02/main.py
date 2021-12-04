FILENAME = "input.txt"

class Keypad:
    def __init__(self, board: list[list[str]], coordinate: tuple[int, int]):
        self._board = board
        self._coordinate = coordinate

    def _get_button(self):
        x, y = self._coordinate

        return self._board[y][x]

    def _move(self, direction: str):
        x, y = self._coordinate

        if direction == 'L':
                x -= 1

        elif direction == 'R':
                x += 1

        elif direction == 'U':
                y -= 1

        elif direction == 'D':
                y += 1

        else:
            raise ValueError(f"Unknown instruction: {direction}")

        try:
            if x < 0 or y < 0 or self._board[y][x] is None:
                return

        except IndexError:
            return

        self._coordinate = (x, y)

    def process_instruction(self, instruction: str) -> int:
        for direction in instruction:
            self._move(direction)

        return self._get_button()

def get_input() -> list[str]:
    instruction_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            instruction_list.append(line.strip())

    return instruction_list

def part_1():
    instruction_list = get_input()
    keypad = Keypad([
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ], (1, 1))
    code = ""

    for instruction in instruction_list:
        code += keypad.process_instruction(instruction)

    print(f"The bathroom code is {code}")

def part_2():
    instruction_list = get_input()
    keypad = Keypad([
        [None, None, '1', None, None],
        [None,  '2', '3',  '4', None],
        [ '5',  '6', '7',  '8',  '9'],
        [None,  'A', 'B',  'C', None],
        [None, None, 'D', None, None]
    ], (2, 0))
    code = ""

    for instruction in instruction_list:
        code += keypad.process_instruction(instruction)

    print(f"The bathroom code is {code}")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
