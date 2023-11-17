FILENAME = "input.txt"


def get_input() -> list[str]:
    with open(FILENAME) as file:
        return file.readline().strip().split(",")


def part_1():
    steps = get_input()
    q, r, s = 0, 0, 0

    # Use Cube coordinates derived by Red Blob Games from the blog "Hexagonal Grids"
    for step in steps:
        match step:
            case "nw":
                q -= 1
                s += 1

            case "n":
                r -= 1
                s += 1

            case "ne":
                q += 1
                r -= 1

            case "sw":
                q -= 1
                r += 1

            case "s":
                r += 1
                s -= 1

            case "se":
                q += 1
                s -= 1

    result = (abs(q) + abs(r) + abs(s)) // 2

    print(f"Answer is {result}")


def part_2():
    steps = get_input()
    result = 0
    q, r, s = 0, 0, 0

    # Use Cube coordinates derived by Red Blob Games from the blog "Hexagonal Grids"
    for step in steps:
        match step:
            case "nw":
                q -= 1
                s += 1

            case "n":
                r -= 1
                s += 1

            case "ne":
                q += 1
                r -= 1

            case "sw":
                q -= 1
                r += 1

            case "s":
                r += 1
                s -= 1

            case "se":
                q += 1
                s -= 1

        result = max(result, (abs(q) + abs(r) + abs(s)) // 2)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
