FILENAME = "input.txt"


def get_input() -> list[tuple[int]]:
    side_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            side_list.append(tuple(map(int, line.strip().split())))

    return side_list


def isValidTriangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def part_1():
    side_list = get_input()
    result = 0

    for sides in side_list:
        if isValidTriangle(*sides):
            result += 1

    print(f"Answer is {result}")


def part_2():
    side_list = get_input()
    result = 0

    for i in range(len(side_list) // 3):
        t1 = side_list[3 * i]
        t2 = side_list[3 * i + 1]
        t3 = side_list[3 * i + 2]

        for j in range(3):
            if isValidTriangle(t1[j], t2[j], t3[j]):
                result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
