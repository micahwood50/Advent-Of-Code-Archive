FILENAME = "input.txt"


class Bingo:
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.length = len(board)

        self.mark_board = [
            [False for __ in range(len(board))] for __ in range(len(board))
        ]
        self.won = False

    def mark(self, drawn_num: int):
        for ri, row in enumerate(self.board):
            for ci, num in enumerate(row):
                if num == drawn_num:
                    self.mark_board[ri][ci] = True

    def is_win(self) -> bool:
        if self.won:
            return True

        if any(all(row) for row in self.mark_board):
            self.won = True
            return True

        for i in range(len(self.board)):
            if all(self.mark_board[j][i] for j in range(self.length)):
                self.won = True
                return True

        return False

    def calculate_score(self, last_drawn_num: int) -> int:
        result = 0

        for ri, row in enumerate(self.board):
            for ci, num in enumerate(row):
                if not self.mark_board[ri][ci]:
                    result += num

        return last_drawn_num * result


def get_input() -> tuple[list[int], list[Bingo]]:
    bingo_list = list()

    with open(FILENAME) as file:
        draw_nums = list(map(int, file.readline().split(",")))

        bingo_buffer = list()

        for line in file.readlines():
            if not line.strip():
                if not bingo_buffer:
                    continue

                bingo_list.append(Bingo(bingo_buffer))
                bingo_buffer = list()

            else:
                bingo_buffer.append(list(map(int, line.split())))

    bingo_list.append(Bingo(bingo_buffer))

    return draw_nums, bingo_list


def part_1():
    nums, bingo_list = get_input()

    for num in nums:
        for bingo in bingo_list:
            bingo.mark(num)

            if bingo.is_win():
                print(
                    f"The final score of the chosen board is {bingo.calculate_score(num)}"
                )
                return

    raise ValueError("There is no winning board!")


def part_2():
    nums, bingo_list = get_input()

    final_score = -1

    for num in nums:
        for bingo in bingo_list:
            bingo.mark(num)

            if not bingo.won and bingo.is_win():
                final_score = bingo.calculate_score(num)

    if final_score == -1:
        raise ValueError("There is no winning board!")

    print(f"The final score of the last winning board is {final_score}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
