FILENAME = "input.txt"


def look_and_say_generator(number: int) -> int:
    number = str(number)
    curr_ch = number[0]
    count = 0

    while True:
        result = ""

        for ch in number:
            if ch == curr_ch:
                count += 1
            else:
                result += str(count) + curr_ch

                curr_ch = ch
                count = 1

        number = result + str(count) + curr_ch

        yield int(number)

        curr_ch = number[0]
        count = 0


def get_input() -> int:
    with open(FILENAME) as file:
        number = int(file.readline())

    return number


def part_1():
    number = get_input()
    gen = look_and_say_generator(number)

    for __ in range(40):
        number = next(gen)

    print(f"The length of the result is {len(str(number))}")


def part_2():  ### NOTE: This part is very slow
    number = get_input()
    gen = look_and_say_generator(number)

    for __ in range(50):
        number = next(gen)

    print(f"The length of the result is {len(str(number))}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
