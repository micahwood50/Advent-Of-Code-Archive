from collections import Counter


FILENAME = "input.txt"


def get_input() -> list[list[str]]:
    passphrase_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            passphrase_list.append(line.strip().split())

    return passphrase_list


def part_1():
    passphrases = get_input()
    result = 0

    for passphrase in passphrases:
        word_set = set()

        for word in passphrase:
            if word in word_set:
                break

            word_set.add(word)

        else:
            result += 1

    print(f"Answer is {result}")


def part_2():
    passphrases = get_input()
    result = 0

    for passphrase in passphrases:
        word_set = set()

        for word in passphrase:
            this_counter = Counter(word)
            hashable_counter = tuple(
                (k, this_counter[k]) for k in sorted(this_counter.keys())
            )

            if hashable_counter in word_set:
                break

            word_set.add(hashable_counter)

        else:
            result += 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
