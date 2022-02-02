from collections import Counter, defaultdict

FILENAME = "input.txt"


def get_input() -> tuple[str, dict[str, str]]:
    insertion_dict = dict()

    with open(FILENAME) as file:
        template = file.readline().strip()
        file.readline()

        for line in file.readlines():
            lhs, rhs = line.strip().split(" -> ")
            insertion_dict[lhs] = rhs

    return template, insertion_dict


def part_1():
    polymer, insertion_dict = get_input()
    result = 0

    for __ in range(10):
        this_polymer = ""

        for i in range(len(polymer) - 1):
            this_polymer += polymer[i] + insertion_dict[polymer[i : i + 2]]

        polymer = this_polymer + polymer[-1]

    C = Counter(polymer)
    result = max(C.values()) - min(C.values())

    print(f"Answer is {result}")


def part_2():
    template, insertion_dict = get_input()
    result = 0

    pair_counters = defaultdict(int)

    for i in range(len(template) - 1):
        pair_counters[template[i : i + 2]] += 1

    for __ in range(40):
        temp_dict = defaultdict(int)

        for key, val in pair_counters.items():
            element = insertion_dict[key]
            p1, p2 = key[0] + element, element + key[1]
            temp_dict[p1] += val
            temp_dict[p2] += val

        pair_counters = temp_dict

    char_counters = defaultdict(int)

    for key, val in pair_counters.items():
        char_counters[key[0]] += val
        char_counters[key[1]] += val

    char_counters[template[0]] += 1
    char_counters[template[-1]] += 1

    for key in char_counters:
        char_counters[key] //= 2

    result = max(char_counters.values()) - min(char_counters.values())

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
