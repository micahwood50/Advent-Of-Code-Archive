FILENAME = "input.txt"

ROOT_NAME = "root"
HUMAN_NAME = "humn"


def get_input() -> dict[str, int | str]:
    monkey_list = dict()

    with open(FILENAME) as file:
        for line in file.readlines():
            name, num = line.strip().split(": ")

            try:
                num = int(num)
            except ValueError:
                pass

            monkey_list[name] = num

    return monkey_list


def calculate_all_monkeys(monkeys: dict[str, int | str]) -> dict[str, int]:
    def helper(name: str) -> int:
        if type(monkeys[name]) == int:
            return monkeys[name]

        left_monkey, operation, right_monkey = monkeys[name].split()

        left_num = helper(left_monkey)
        right_num = helper(right_monkey)

        monkeys[left_monkey] = left_num
        monkeys[right_monkey] = right_num

        monkeys[name] = int(eval(f"{left_num} {operation} {right_num}"))

        return monkeys[name]

    for name in monkeys.keys():
        monkeys[name] = helper(name)

    return monkeys


def part_1():
    monkeys = get_input()

    monkeys = calculate_all_monkeys(monkeys)

    result = monkeys[ROOT_NAME]

    print(f"Answer is {result}")


def part_2():
    monkeys = get_input()

    monkey_all_children = dict()
    monkey_direct_children = dict()

    def get_all_children(name: str) -> set[str]:
        if isinstance(monkeys[name], int):
            monkey_all_children[name] = set()
            return set()

        else:
            left_name, _, right_name = monkeys[name].split()

            monkey_all_children[name] = (
                {left_name, right_name}
                | get_all_children(left_name)
                | get_all_children(right_name)
            )
            monkey_direct_children[name] = {left_name, right_name}

            return monkey_all_children[name]

    get_all_children(ROOT_NAME)

    int_monkey_dict = calculate_all_monkeys(monkeys.copy())

    for name in monkey_direct_children[ROOT_NAME]:
        if HUMAN_NAME in monkey_all_children[name]:
            curr_name = name

        else:
            result = int_monkey_dict[name]

    while HUMAN_NAME not in monkeys[curr_name]:
        this_left_name, operation, this_right_name = monkeys[curr_name].split()

        if HUMAN_NAME in monkey_all_children[this_left_name]:
            curr_val = int_monkey_dict[this_right_name]
            curr_name = this_left_name

            match operation:
                case "+":
                    result -= curr_val
                case "-":
                    result += curr_val
                case "*":
                    result //= curr_val
                case "/":
                    result *= curr_val

        else:
            curr_val = int_monkey_dict[this_left_name]
            curr_name = this_right_name

            match operation:
                case "+":
                    result -= curr_val
                case "-":
                    result -= curr_val
                    result = -result
                case "*":
                    result //= curr_val
                case "/":
                    result = curr_val // result

    final_left, final_operation, final_right = monkeys[curr_name].split()

    if final_left == HUMAN_NAME:
        final_val = int_monkey_dict[final_right]

    else:
        final_val = int_monkey_dict[final_left]

    match final_operation:
        case "+":
            result -= final_val
        case "-":
            result += final_val
        case "*":
            result /= final_val
        case "/":
            result *= final_val

    print(f"Answer is {result}")


if __name__ == "__main__":
    part_1()
    part_2()
    pass
