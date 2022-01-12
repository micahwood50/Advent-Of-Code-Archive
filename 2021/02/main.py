FILENAME = "input.txt"

def get_input() -> list[tuple[int, int]]:
    vector_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            direction, unit = line.split()
            unit = int(unit)

            if direction == "forward":
                vector = (unit, 0)

            elif direction == "up":
                vector = (0, -unit)

            elif direction == "down":
                vector = (0, unit)

            else:
                raise ValueError(f"Unknown instruction: {line}")

            vector_list.append(vector)

    return vector_list

def part_1():
    vector_list = get_input()
    horizontal_pos, depth = 0, 0

    for vector in vector_list:
        x, y = vector
        horizontal_pos += x
        depth += y

    print(f"The multiplication of the final horizontal position and the final depth is {horizontal_pos * depth}")

def part_2():
    vector_list = get_input()
    horizontal_pos, depth, aim = 0, 0, 0

    for vector in vector_list:
        x, y = vector

        if x != 0 and y == 0:
            # The instruction was forward X, so multiple the depth by X
            horizontal_pos += x
            depth += aim * x

        else:
            aim += y

    print(f"The multiplication of the final horizontal position and the final depth is {horizontal_pos * depth}")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
