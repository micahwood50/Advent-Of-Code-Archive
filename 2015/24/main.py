FILENAME = "input.txt"


def subset_sum(numbers: list[int], target: int, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial

    if partial_sum >= target:
        return

    for i, n in enumerate(numbers):
        remaining = numbers[i + 1 :]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


def product(numbers: list[int]) -> int:
    result = 1

    for n in numbers:
        result *= n

    return result


def get_input() -> list[int]:
    int_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            int_list.append(int(line))

    return int_list


def part_1():
    int_list = get_input()
    result = product(int_list)
    target = sum(int_list) // 3

    comb = list(subset_sum(int_list, target))
    min_len = len(int_list)

    for c in comb:
        min_len = min(len(c), min_len)

    for c in comb:
        if len(c) == min_len:
            result = min(result, product(c))

    print(f"Answer is {result}")


def part_2():
    int_list = get_input()
    result = product(int_list)
    target = sum(int_list) // 4

    comb = list(subset_sum(int_list, target))
    min_len = len(int_list)

    for c in comb:
        min_len = min(len(c), min_len)

    for c in comb:
        if len(c) == min_len:
            result = min(result, product(c))

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
