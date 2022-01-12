FILENAME = "input.txt"

def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list

def part_1():
    input = get_input()
    result = 0

    print(f"Answer is {result}")

def part_2():
    input = get_input()
    result = 0

    print(f"Answer is {result}")

if __name__ == "__main__":
    part_1()
    # part_2()
    pass
