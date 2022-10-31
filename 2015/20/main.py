FILENAME = "input.txt"


def get_input() -> int:
    with open(FILENAME) as file:
        return int(file.readline())


def sum_div(num: int) -> int:
    result = 1 + num

    i = 2
    while i**2 <= num:
        if num % i == 0:
            if i**2 == num:
                result += i
            else:
                result += i + num // i
        i += 1

    return result


def elf_sum_div(num: int) -> int:
    if num <= 50:
        return sum_div(num)

    result = num

    i = 2
    while i**2 <= num:
        if num % i == 0:
            if i**2 != num:
                j = num // i

                if 50 * j >= num:
                    result += j

            if 50 * i >= num:
                result += i

        i += 1

    return result


def part_1():
    input = get_input()

    result = 2
    while 10 * sum_div(result) < input:
        result += 1

    print(f"Answer is {result}")


def part_2():
    input = get_input()

    result = 2
    while 11 * elf_sum_div(result) < input:
        result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
