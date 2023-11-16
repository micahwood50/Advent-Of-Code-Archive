from icecream import ic


FILENAME = "input.txt"


class Bot:
    def __init__(self, num: int):
        self.num = num
        self.inputs = list()

    def set_chip_given(
        self, low_type: str, low_num: int, high_type: str, high_num: int
    ):
        self.low_type = low_type
        self.low_num = low_num
        self.high_type = high_type
        self.high_num = high_num

    def add_value(self, value: int):
        self.inputs.append(value)


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def part_1():
    instructions = get_input()

    low_goal = 17
    high_goal = 61

    bot_dict = dict()
    output_dict = dict()

    value_instructions = list()

    for inst in instructions:
        if inst.startswith("value"):
            value_instructions.append(inst)

        else:
            (
                _,
                this_bot_num,
                _,
                _,
                _,
                low_type,
                low_num,
                _,
                _,
                _,
                high_type,
                high_num,
            ) = inst.split()
            this_bot_num = int(this_bot_num)
            low_num = int(low_num)
            high_num = int(high_num)

            this_bot = Bot(this_bot_num)
            this_bot.set_chip_given(low_type, low_num, high_type, high_num)

            bot_dict[this_bot_num] = this_bot

            if low_type == "output":
                output_dict[low_num] = list()

            if high_type == "output":
                output_dict[high_num] = list()

    for inst in value_instructions:
        _, value, _, _, _, bot_num = inst.split()
        value = int(value)
        bot_num = int(bot_num)

        if bot_num not in bot_dict:
            raise ValueError(f"Bot #{bot_num} does not exist!")

        curr_bot = bot_dict[bot_num]

        curr_bot.add_value(value)

        if len(curr_bot.inputs) == 2:
            queue = [
                (low_val := min(curr_bot.inputs), curr_bot.low_type, curr_bot.low_num),
                (
                    high_val := max(curr_bot.inputs),
                    curr_bot.high_type,
                    curr_bot.high_num,
                ),
            ]

            if low_val == low_goal and high_val == high_goal:
                print(f"Answer is {bot_num}")

            curr_bot.inputs = list()

            while queue:
                this_val, dest_type, dest_num = queue.pop(0)

                if dest_type == "bot":
                    bot_dict[dest_num].add_value(this_val)

                    if len(bot_dict[dest_num].inputs) == 2:
                        this_bot = bot_dict[dest_num]

                        queue += [
                            (
                                low_val := min(this_bot.inputs),
                                this_bot.low_type,
                                this_bot.low_num,
                            ),
                            (
                                high_val := max(this_bot.inputs),
                                this_bot.high_type,
                                this_bot.high_num,
                            ),
                        ]

                        if low_val == low_goal and high_val == high_goal:
                            print(f"Answer is {dest_num}")

                        bot_dict[dest_num].inputs = list()

                else:
                    output_dict[dest_num].append(this_val)


def part_2():
    instructions = get_input()

    bot_dict = dict()
    output_dict = dict()

    value_instructions = list()

    for inst in instructions:
        if inst.startswith("value"):
            value_instructions.append(inst)

        else:
            (
                _,
                this_bot_num,
                _,
                _,
                _,
                low_type,
                low_num,
                _,
                _,
                _,
                high_type,
                high_num,
            ) = inst.split()
            this_bot_num = int(this_bot_num)
            low_num = int(low_num)
            high_num = int(high_num)

            this_bot = Bot(this_bot_num)
            this_bot.set_chip_given(low_type, low_num, high_type, high_num)

            bot_dict[this_bot_num] = this_bot

            if low_type == "output":
                output_dict[low_num] = list()

            if high_type == "output":
                output_dict[high_num] = list()

    for inst in value_instructions:
        _, value, _, _, _, bot_num = inst.split()
        value = int(value)
        bot_num = int(bot_num)

        if bot_num not in bot_dict:
            raise ValueError(f"Bot #{bot_num} does not exist!")

        curr_bot = bot_dict[bot_num]

        curr_bot.add_value(value)

        if len(curr_bot.inputs) == 2:
            queue = [
                (min(curr_bot.inputs), curr_bot.low_type, curr_bot.low_num),
                (max(curr_bot.inputs), curr_bot.high_type, curr_bot.high_num),
            ]

            curr_bot.inputs = list()

            while queue:
                this_val, dest_type, dest_num = queue.pop(0)

                if dest_type == "bot":
                    bot_dict[dest_num].add_value(this_val)

                    if len(bot_dict[dest_num].inputs) == 2:
                        this_bot = bot_dict[dest_num]

                        queue += [
                            (min(this_bot.inputs), this_bot.low_type, this_bot.low_num),
                            (
                                max(this_bot.inputs),
                                this_bot.high_type,
                                this_bot.high_num,
                            ),
                        ]

                        bot_dict[dest_num].inputs = list()

                else:
                    output_dict[dest_num].append(this_val)

    result = 1

    for i in range(3):
        result *= output_dict[i][0]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
