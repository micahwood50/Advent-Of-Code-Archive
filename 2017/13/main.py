FILENAME = "input.txt"


def get_input() -> dict[int, int]:
    this_dict = dict()

    with open(FILENAME) as file:
        for line in file.readlines():
            key, val = map(int, line.strip().split(": "))
            this_dict[key] = val

    return this_dict


def part_1():
    layers = get_input()
    result = 0

    for index in range(max(layers.keys()) + 1):
        if index in layers and index % (2 * (layers[index] - 1)) == 0:
            result += index * layers[index]

    print(f"Answer is {result}")


def part_2():
    layers = get_input()
    delay = 0

    while True:
        for pico_sec, index in enumerate(range(max(layers.keys()) + 1), start=delay):
            if index in layers and pico_sec % (2 * (layers[index] - 1)) == 0:
                delay += 1
                break
        else:
            print(f"Answer is {delay}")
            return


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
