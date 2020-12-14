FILENAME = "input.txt"

def get_input() -> str:
    with open(FILENAME) as f:
        return f.readline().strip()

def part_1():
    input = get_input()
    result = 0

    for ch in input:
        if ch == '(':
            result += 1

        else:
            result -= 1

    print(f"The instructions take Santa to floor {result}")

def part_2():
    input = get_input()
    floor = 0

    for i, ch in enumerate(input, start = 1):
        if ch == '(':
            floor += 1

        if ch == ')':
            if floor == 0:
                print(f"Santa first enter the basement at position {i}")
                return

            else:
                floor -= 1

    print(f"Something went wrong!")

if __name__ == "__main__":
    part_1()
    part_2()
    pass
