FILENAME = "input.txt"


def sign(n: int) -> int:
    if n > 0:
        return 1

    if n < 0:
        return -1

    return 0


def is_safe(report: list[int]) -> bool:
    this_diff = report[0] - report[1]
    this_sign = sign(this_diff)

    for i in range(len(report) - 1):
        this_diff = report[i] - report[i + 1]

        if sign(this_diff) != this_sign or not (1 <= abs(this_diff) <= 3):
            return False

    return True


def get_input() -> list[list[int]]:
    reports = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            reports.append(list(map(int, line.strip().split())))

    return reports


def part_1():
    reports = get_input()
    result = 0

    for report in reports:
        if is_safe(report):
            result += 1

    print(f"Answer is {result}")


def part_2():
    reports = get_input()
    result = 0

    for report in reports:
        for i in range(len(report)):
            this_report = report[:i] + report[i + 1 :]

            if is_safe(this_report):
                result += 1
                break

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
