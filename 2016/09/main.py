from itertools import takewhile, islice


FILENAME = "input.txt"


def get_input() -> str:
    with open(FILENAME) as file:
        return file.readline().strip()


def decompress_len(file_str, *, recursive_decompress=True):
    result = 0
    chars = iter(file_str)

    for ch in chars:
        if ch == "(":
            subseq_len, repeat_num = map(
                int,
                ["".join(takewhile(lambda c: c not in "x)", chars)) for __ in range(2)],
            )

            s = "".join(islice(chars, subseq_len))

            result += (
                decompress_len(s) if recursive_decompress else len(s)
            ) * repeat_num

        else:
            result += 1

    return result


def part_1():
    file_str = get_input()

    result = decompress_len(file_str, recursive_decompress=False)

    print(f"Answer is {result}")


def part_2():
    file_str = get_input()

    result = decompress_len(file_str)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
