FILENAME = "input.txt"


def get_input() -> str:
    with open(FILENAME) as file:
        return file.readline().strip()


def part_1():
    image_str = get_input()

    image_size = 25 * 6

    layers = list()
    this_layer = ""

    for i, ch in enumerate(image_str):
        if i % image_size == 0:
            layers.append(this_layer)
            this_layer = ""

        this_layer += ch

    layers.pop(0)

    min_zeroes = image_size
    result = 0

    for layer in layers:
        this_num_zeroes = layer.count("0")
        if this_num_zeroes < min_zeroes:
            min_zeroes = this_num_zeroes
            result = layer.count("1") * layer.count("2")

    print(f"Answer is {result}")


def part_2():
    image_str = get_input()

    image_size = 25 * 6

    layers = list()
    this_layer = ""

    for i, ch in enumerate(image_str):
        if i % image_size == 0:
            layers.append(this_layer)
            this_layer = ""

        this_layer += ch

    layers.append(this_layer)
    layers.pop(0)

    decoded_image_str = ""

    for layer_chs in zip(*layers):
        for ch in layer_chs:
            if ch != "2":
                decoded_image_str += ch
                break
        else:
            decoded_image_str += "2"

    row = ""
    print(f"The decoded image looks like this:")

    for i, ch in enumerate(decoded_image_str):
        if i % 25 == 0:
            print(row)
            row = ""

        if ch == "0":
            row += " "
        elif ch == "1":
            row += "#"
        else:
            row += "!"

    print(row)
    print()


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
