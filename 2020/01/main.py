FILENAME = "input.txt"
GOAL_NUM = 2020

def get_input() -> set[int]:
    """ Read the file and generate a set of entries

    Returns:
        set[int]: A set of entries
    """
    entries_set = set()

    with open(FILENAME) as f:
        for line in f.readlines():
            entries_set.add(int(line))

    return entries_set

def part_1():
    entries_set = get_input()

    for entry in entries_set:
        if GOAL_NUM - entry in entries_set:
            print(f"The product of the two entries that sum to 2020 is {entry * (GOAL_NUM - entry)}")
            return

def part_2():
    entries_set = get_input()

    for entry_1 in entries_set:
        for entry_2 in entries_set:
            if entry_1 == entry_2:
                continue

            if GOAL_NUM - entry_1 - entry_2 in entries_set:
                print(f"The product of the three entries that sum to 2020 is {entry_1 * entry_2 * (GOAL_NUM - entry_1 - entry_2)}")
                return

if __name__ == "__main__":
    # part_1()
    part_2()
    pass
