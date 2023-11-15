FILENAME = "input.txt"
LIGHT_OFF = " "
LIGHT_ON = "#"

SCREEN_WIDTH = 50
SCREEN_HEIGHT = 6


def print_screen(screen: list[list[str]]):
    for row in screen:
        for col in row:
            print(col, end="")
        print()


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def part_1():
    operations = get_input()

    screen = [[LIGHT_OFF for __ in range(SCREEN_WIDTH)] for __ in range(SCREEN_HEIGHT)]

    for oper in operations:
        if oper.startswith("rect"):
            width, height = map(int, oper.split()[1].split("x"))

            for row_i in range(height):
                for col_i in range(width):
                    screen[row_i][col_i] = LIGHT_ON

        else:  # rotate operation
            direction, selection_num, _, distance = oper.split()[1:]
            selection_num = int(selection_num.split("=")[1])
            distance = int(distance)

            if direction == "row":
                distance = SCREEN_WIDTH - (distance % SCREEN_WIDTH)
                screen[selection_num] = (
                    screen[selection_num][distance:] + screen[selection_num][:distance]
                )

            else:
                screen_copy = [[pixel for pixel in row] for row in screen]

                for row_i in range(SCREEN_HEIGHT):
                    screen_copy[row_i][selection_num] = screen[
                        (row_i - distance) % SCREEN_HEIGHT
                    ][selection_num]

                screen = screen_copy

    result = sum(screen[i].count(LIGHT_ON) for i in range(6))

    print(f"Answer is {result}")


def part_2():
    operations = get_input()

    screen = [[LIGHT_OFF for __ in range(SCREEN_WIDTH)] for __ in range(SCREEN_HEIGHT)]

    for oper in operations:
        if oper.startswith("rect"):
            width, height = map(int, oper.split()[1].split("x"))

            for row_i in range(height):
                for col_i in range(width):
                    screen[row_i][col_i] = LIGHT_ON

        else:  # rotate operation
            direction, selection_num, _, distance = oper.split()[1:]
            selection_num = int(selection_num.split("=")[1])
            distance = int(distance)

            if direction == "row":
                distance = SCREEN_WIDTH - (distance % SCREEN_WIDTH)
                screen[selection_num] = (
                    screen[selection_num][distance:] + screen[selection_num][:distance]
                )

            else:
                screen_copy = [[pixel for pixel in row] for row in screen]

                for row_i in range(SCREEN_HEIGHT):
                    screen_copy[row_i][selection_num] = screen[
                        (row_i - distance) % SCREEN_HEIGHT
                    ][selection_num]

                screen = screen_copy

    print(f"What the screen displays:\n")
    print_screen(screen)
    print()


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
