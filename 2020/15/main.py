from typing import List, Iterator
from collections import defaultdict

INPUT = [13,16,0,12,15,1]

def vaneck(init_seq: List[int]) -> Iterator[int]:
    """ Calculate and yield number in the Van Eck sequence with
        customized starting set

    Args:
        init_seq (List[int]): List of starting numbers

    Yields:
        Iterator[int]: Number spoken for each turn
    """
    for e in init_seq:
        yield e

    # This dictionary take key and pair it with list of length of at most 2
    # The list contains up to last 2 turns when the number was spoken
    spoken_dict = defaultdict(list)

    for i, e in enumerate(init_seq, start = 1):
        if len(spoken_dict[e]) == 2:
            spoken_dict[e] = spoken_dict[e][1:] + [i]

        else:
            spoken_dict[e].append(i)

    prev_num = init_seq[-1]
    turn_num = len(init_seq) + 1

    while True:
        if len(spoken_dict[prev_num]) <= 1:
            # First time spoken
            curr = 0

        else:
            curr = spoken_dict[prev_num][1] - spoken_dict[prev_num][0]

        if len(spoken_dict[curr]) == 2:
            spoken_dict[curr] = spoken_dict[curr][1:] + [turn_num]

        else:
            spoken_dict[curr].append(turn_num)

        prev_num = curr
        turn_num += 1
        yield curr

def part_1():
    vaneck_generator = vaneck(INPUT)

    for turn, num in enumerate(vaneck_generator, start = 1):
        if turn == 2020:
            print(f"Turn {turn}: {num}")
            return

def part_2():
    vaneck_generator = vaneck(INPUT)

    for turn, num in enumerate(vaneck_generator, start = 1):
        if turn == 30_000_000:
            print(f"Turn {turn}: {num}")
            return

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
