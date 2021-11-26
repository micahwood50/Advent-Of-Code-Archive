from part1 import run_solution as part_1
from part2 import run_solution as part_2

FILENAME = "input.txt"

def get_input() -> list[str]:
    expressions = list()

    with open(FILENAME) as f:
        for line in f.readlines():
            expressions.append(line.strip())

    return expressions

if __name__ == "__main__":
    expressions = get_input()

    # part_1(expressions)
    # part_2(expressions)
    pass
