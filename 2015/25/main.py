FILENAME = "input.txt"

FIRST_NUM = 20151125
MULTIPLE = 252533
MOD_NUM = 33554393


def get_input() -> tuple[int, int]:
    with open(FILENAME) as file:
        line = file.readline().strip().split("row ")[1]
        row, col = line.split(", column ")
        row = int(row)
        col = int(col[:-1])
        return (row, col)


def T(num: int) -> int:
    return (num * (num + 1)) // 2


def get_num(row: int, col: int) -> int:
    return T(row + col - 2) + col


def part_1():
    row, col = get_input()

    result = FIRST_NUM
    num = get_num(row, col) - 1

    bin_num = bin(num)[2:]
    this_num = MULTIPLE

    for b in reversed(bin_num):
        if b == "1":
            result *= this_num

        this_num *= this_num
        this_num %= MOD_NUM
        result %= MOD_NUM

    print(f"Answer is {result}")


def part_2():
    input = get_input()
    result = 0

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
