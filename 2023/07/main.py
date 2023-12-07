from collections import Counter

FILENAME = "input.txt"

STRENGTH_DICT = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}

STRENGTH_JOKER_DICT = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 11,
    "K": 12,
    "A": 13,
}


class Hand:
    def __init__(self, hand_str: str):
        self.hand = hand_str
        self.joker_rule = False

    def _get_type_helper(self, hand_counter: Counter[str, int]) -> int:
        if len(hand_counter) == 1:
            return 7  # Five of a kind

        if len(hand_counter) == 2:
            if sorted(hand_counter.values()) == [1, 4]:
                return 6  # Four of a kind
            return 5  # Full House

        if len(hand_counter) == 3:
            if sorted(hand_counter.values()) == [1, 1, 3]:
                return 4  # Three of a kind
            return 3  # Two pair

        if len(hand_counter) == 4:
            return 2  # One pair

        return 1  # High card

    def _get_type(self) -> int:
        return self._get_type_helper(Counter(self.hand))

    def _get_type_with_joker(self) -> int:
        hand_counter = Counter(self.hand)

        if "J" in hand_counter:
            if self.hand == "JJJJJ":
                hand_counter = Counter("AAAAA")

            else:
                counter_list = list(hand_counter.items())
                counter_list.sort(key=lambda t: (-t[1], -STRENGTH_JOKER_DICT[t[0]]))

                if counter_list[0][0] == "J":
                    counter_list.pop(0)

                hand_counter[counter_list[0][0]] += hand_counter["J"]
                del hand_counter["J"]

        return self._get_type_helper(hand_counter)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            raise TypeError(
                f"'==' not supported between instances of 'Hand' and '{type(other)}'"
            )

        return self.hand == other.hand

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Hand):
            raise TypeError(
                f"'<' not supported between instances of 'Hand' and '{type(other)}'"
            )

        self_type_val = (
            self._get_type() if not self.joker_rule else self._get_type_with_joker()
        )
        other_type_val = (
            other._get_type() if not other.joker_rule else other._get_type_with_joker()
        )

        if self_type_val == other_type_val:
            this_strength_dict = (
                STRENGTH_JOKER_DICT if self.joker_rule else STRENGTH_DICT
            )

            for self_ch, other_ch in zip(self.hand, other.hand):
                if this_strength_dict[self_ch] < this_strength_dict[other_ch]:
                    return True

                if this_strength_dict[self_ch] > this_strength_dict[other_ch]:
                    return False

            return False

        else:
            return self_type_val < other_type_val

    def __str__(self) -> str:
        return self.hand

    def __repr__(self) -> str:
        return f"Hand({self.hand})"


def get_input(*, joker_rule=False) -> list[tuple[Hand, int]]:
    hand_bid_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            hand_str, bid = line.strip().split()
            bid = int(bid)

            hand = Hand(hand_str)
            hand.joker_rule = joker_rule

            hand_bid_list.append((hand, bid))

    return hand_bid_list


def part_1():
    hand_bid_list = get_input()
    result = 0

    hand_bid_list.sort(key=lambda t: t[0])

    for rank, (_, bid) in enumerate(hand_bid_list, start=1):
        result += rank * bid

    print(f"Answer is {result}")


def part_2():
    hand_bid_list = get_input(joker_rule=True)
    result = 0

    hand_bid_list.sort(key=lambda t: t[0])

    for rank, (_, bid) in enumerate(hand_bid_list, start=1):
        result += rank * bid

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
