from string import ascii_lowercase

FILENAME = "input.txt"


def get_input() -> str:
    with open(FILENAME) as file:
        for line in file.readlines():
            return line.strip()


def is_opposite_polarity(ch1: str, ch2: str) -> bool:
    return ch1.lower() == ch2.lower() and ch1 != ch2


def part_1():
    polymer = get_input()

    while polymer:
        i = 0
        remove_indices = list()
        while i < len(polymer) - 1:
            if is_opposite_polarity(polymer[i], polymer[i + 1]):
                remove_indices.insert(0, i)
                i += 2
            else:
                i += 1

        if remove_indices:
            for remove_index in remove_indices:
                polymer = polymer[:remove_index] + polymer[remove_index + 2 :]
        else:
            break

    print(f"Answer is {len(polymer)}")


def part_2():
    polymer = get_input()
    min_length = len(polymer)

    print("Progress bar: ", end="")

    for letter in ascii_lowercase:
        print(letter, end="")
        polymer_clone = polymer.replace(letter, "").replace(letter.upper(), "")
        while polymer_clone:
            i = 0
            remove_indices = list()
            while i < len(polymer_clone) - 1:
                if is_opposite_polarity(polymer_clone[i], polymer_clone[i + 1]):
                    remove_indices.insert(0, i)
                    i += 2
                else:
                    i += 1

            if remove_indices:
                for remove_index in remove_indices:
                    polymer_clone = (
                        polymer_clone[:remove_index] + polymer_clone[remove_index + 2 :]
                    )
            else:
                break

        if len(polymer_clone) < min_length:
            min_length = len(polymer_clone)

    print(f"\nAnswer is {min_length}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
