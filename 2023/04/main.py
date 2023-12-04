# NOTE: I assumed there is no duplicate number on all scratchcards. It did work for my specific puzzle input.

FILENAME = "input.txt"


def get_input() -> list[tuple[set[int], set[int]]]:
    card_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            winning_numbers, our_numbers = line.split(": ")[1].split(" | ")
            winning_numbers = set(map(int, winning_numbers.split()))
            our_numbers = set(map(int, our_numbers.split()))

            card_list.append((winning_numbers, our_numbers))

    return card_list


def part_1():
    card_list = get_input()
    result = 0

    for winning_num_set, our_num_set in card_list:
        matching_set = winning_num_set & our_num_set

        if len(matching_set) != 0:
            result += 1 << (len(matching_set) - 1)

    print(f"Answer is {result}")


def part_2():
    card_list = get_input()

    amount_card_dict = {n: 1 for n in range(1, len(card_list) + 1)}

    for card_id, (winning_num_set, our_num_set) in enumerate(card_list, start=1):
        matching_set = winning_num_set & our_num_set

        for i in range(len(matching_set)):
            this_id = card_id + i + 1

            if this_id in amount_card_dict:
                amount_card_dict[this_id] += amount_card_dict[card_id]

    result = sum(amount_card_dict.values())

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
