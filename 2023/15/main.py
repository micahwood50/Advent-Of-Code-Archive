FILENAME = "input.txt"


def get_input() -> list[str]:
    with open(FILENAME) as file:
        return file.readline().strip().split(",")


def hash(label: str) -> int:
    result = 0

    for ch in label:
        result += ord(ch)
        result *= 17
        result %= 256

    return result


def part_1():
    init_sequence = get_input()
    result = 0

    for step in init_sequence:
        result += hash(step)

    print(f"Answer is {result}")


def part_2():
    init_sequence = get_input()
    result = 0
    boxes = [list() for __ in range(256)]
    name_val_map = dict()

    for step in init_sequence:
        if "=" in step:
            name, val = step.split("=")
            val = int(val)
            box_index = hash(name)

            if name not in boxes[box_index]:
                boxes[box_index].append(name)

            name_val_map[name] = val

        else:
            name = step[:-1]
            box_index = hash(name)

            if name in boxes[box_index]:
                boxes[box_index].remove(name)

    for box_num, name_list in enumerate(boxes, start=1):
        for slot_num, name in enumerate(name_list, start=1):
            result += box_num * slot_num * name_val_map[name]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
