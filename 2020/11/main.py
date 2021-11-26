from part1 import run_solution as part_1
from part2 import run_solution as part_2

FILENAME = "input.txt"

def get_input() -> list[list[str]]:
    grid = list()

    with open(FILENAME) as f:
        for line in f.readlines():
            grid.append(list(line.strip()))

    return grid

if __name__ == "__main__":
    grid = get_input()

    part_1(grid)
    part_2(grid)
    pass
