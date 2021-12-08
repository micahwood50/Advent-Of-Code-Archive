FILENAME = "input.txt"

def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list

def part_1():
    string_list = get_input()
    literals_counter = 0
    memory_counter   = 0

    for string in string_list:
        literals_counter += len(string)
        memory_counter   += len(eval(string))

    print(f"The total difference is {literals_counter - memory_counter}")

def part_2():
    string_list = get_input()
    literals_counter = 0
    encode_counter   = 0

    for string in string_list:
        literals_counter += len(string)
        encode_counter   += len(string) + 2

        for ch in string:
            if ch == "\"" or ch == "\\":
                encode_counter += 1

    print(f"The total difference is {encode_counter - literals_counter}")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
