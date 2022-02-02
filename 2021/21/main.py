from collections import defaultdict

FILENAME = "input.txt"

DIRAC_DICT = defaultdict(int)
for d1 in range(1, 4):
    for d2 in range(1, 4):
        for d3 in range(1, 4):
            DIRAC_DICT[d1 + d2 + d3] += 1


def generator_dice() -> int:
    n = 0
    while True:
        n = n % 100 + 1
        yield n


def get_input() -> tuple[int, int]:
    with open(FILENAME) as file:
        p1_position, p2_position = int(file.readline().split(":")[1]), int(
            file.readline().split(":")[1]
        )

    return p1_position, p2_position


def part_1():
    positions = list(get_input())
    scores = [0, 0]
    turn = 0

    dice = generator_dice()
    roll_dice_count = 0

    while scores[0] < 1000 and scores[1] < 1000:
        distance = next(dice) + next(dice) + next(dice)

        roll_dice_count += 3

        positions[turn] = (positions[turn] - 1 + distance) % 10 + 1

        scores[turn] += positions[turn]

        turn = 1 - turn

    losing_score = min(scores)

    result = losing_score * roll_dice_count

    print(f"The multiplication is {result}")


def part_2():
    positions = get_input()
    scores = (0, 0)

    universes_dict = {(positions, scores): 1}
    turn = 0

    count_wins = [0, 0]

    while universes_dict:
        universes_temp_dict = defaultdict(int)

        for ((positions, scores), universes_count) in universes_dict.items():
            for dice_result, universes_multiplier in DIRAC_DICT.items():
                positions_list = list(positions)
                scores_list = list(scores)

                new_universes_count = universes_count * universes_multiplier

                positions_list[turn] = (positions_list[turn] - 1 + dice_result) % 10 + 1
                scores_list[turn] += positions_list[turn]

                if scores_list[turn] >= 21:
                    count_wins[turn] += new_universes_count

                else:
                    key = (tuple(positions_list), tuple(scores_list))

                    universes_temp_dict[key] += new_universes_count

        universes_dict = universes_temp_dict
        turn = 1 - turn

    print(f"That player won in {max(count_wins)} universes")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
