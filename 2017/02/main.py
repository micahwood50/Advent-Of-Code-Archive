FILENAME = "input.txt"


def get_input() -> list[list[int]]:
    spreadsheet = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            spreadsheet.append(list(map(int, line.split())))

    return spreadsheet


def part_1():
    spreadsheet = get_input()
    result = 0

    for row in spreadsheet:
        min_val = float("inf")
        max_val = float("-inf")

        for n in row:
            if n < min_val:
                min_val = n
            if n > max_val:
                max_val = n

        result += max_val - min_val

    print(f"Answer is {result}")


def part_2():
    spreadsheet = get_input()
    result = 0

    for row in spreadsheet:
        row.sort()

        for i in range(len(row) - 1):
            for j in range(i + 1, len(row)):
                if row[j] % row[i] == 0:
                    result += row[j] // row[i]
                    break
            else:
                continue

            break

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
