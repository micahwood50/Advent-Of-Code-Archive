FILENAME = "input.txt"


def get_input() -> list[int]:
    with open(FILENAME) as file:
        return list(map(int, file.readline().split("\t")))


def part_1():
    banks = get_input()
    steps = 0

    state_set = set()
    state_tuple = (0,)

    while state_tuple not in state_set:
        state_set.add(state_tuple)
        steps += 1

        max_block_index = 0

        for i in range(len(banks)):
            if banks[i] > banks[max_block_index]:
                max_block_index = i

        new_banks = banks[:]
        new_banks[max_block_index] = 0

        redistribution_amount = banks[max_block_index] // len(banks)
        remaining_amount = banks[max_block_index] % len(banks)

        for index in range(len(banks)):
            new_banks[index] += redistribution_amount

        for i in range(remaining_amount):
            this_index = (i + max_block_index + 1) % len(banks)
            new_banks[this_index] += 1

        banks = new_banks[:]

        state_tuple = tuple(banks)

    print(f"Answer is {steps}")


def part_2():
    banks = get_input()
    steps = 0

    state_set = set()
    state_tuple = (0,)
    target_set_flag = False

    loop_flag = False
    target = (0,)

    while not loop_flag:
        if target_set_flag:
            steps += 1

        max_block_index = 0

        for i in range(len(banks)):
            if banks[i] > banks[max_block_index]:
                max_block_index = i

        new_banks = banks[:]
        new_banks[max_block_index] = 0

        redistribution_amount = banks[max_block_index] // len(banks)
        remaining_amount = banks[max_block_index] % len(banks)

        for index in range(len(banks)):
            new_banks[index] += redistribution_amount

        for i in range(remaining_amount):
            this_index = (i + max_block_index + 1) % len(banks)
            new_banks[this_index] += 1

        banks = new_banks[:]
        state_tuple = tuple(banks)

        if state_tuple in state_set:
            if not target_set_flag:
                target_set_flag = True
                target = state_tuple

            else:
                if state_tuple == target:
                    break

        else:
            state_set.add(state_tuple)

    print(f"Answer is {steps}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
