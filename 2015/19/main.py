from random import shuffle


FILENAME = "input.txt"


class Replacement:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def __str__(self) -> str:
        return f"{self.before} => {self.after}"

    def __repr__(self) -> str:
        return f"Replacement({self.before}, {self.after})"


def get_input() -> tuple[list[Replacement], str]:
    replacement_list = list()

    with open(FILENAME) as file:
        lines = file.readlines()
        molecule = lines[-1].strip()

        for replacement_str in lines[:-2]:
            replacement_list.append(Replacement(*replacement_str.strip().split(" => ")))

    return replacement_list, molecule


def part_1():
    replacements, molecule = get_input()
    found_replacement_set = set()

    for replacement in replacements:
        location = -1
        indices = list()

        while True:
            location = molecule.find(replacement.before, location + 1)
            if location != -1:
                indices.append(location)
            else:
                break

        for curr_index in indices:
            found_replacement_set.add(
                molecule[0:curr_index]
                + replacement.after
                + molecule[curr_index + len(replacement.before) :]
            )

    print(f"Answer is {len(found_replacement_set)}")


def part_2():
    replacements, molecule = get_input()
    curr_molecule = molecule
    result = 0

    while curr_molecule != "e":
        prev_molecule = curr_molecule

        for replacement in replacements:
            if replacement.after not in curr_molecule:
                continue

            curr_molecule = curr_molecule.replace(
                replacement.after, replacement.before, 1
            )
            result += 1

        if prev_molecule == curr_molecule:
            curr_molecule = molecule
            result = 0
            shuffle(replacements)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
