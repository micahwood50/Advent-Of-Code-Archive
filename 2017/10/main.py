from functools import reduce
from operator import xor


FILENAME = "input.txt"
LIST_SIZE = 256


def get_input() -> str:
    with open(FILENAME) as file:
        return file.readline().strip()


def part_1():
    lengths = [int(n) for n in get_input().split(",")]
    nums = list(range(LIST_SIZE))
    index = 0
    skip_size = 0

    for length in lengths:
        to_reverse = list()

        for x in range(length):
            n = (index + x) % LIST_SIZE
            to_reverse.append(nums[n])

        to_reverse.reverse()

        for x in range(length):
            n = (index + x) % LIST_SIZE
            nums[n] = to_reverse[x]

        index += length + skip_size
        index %= LIST_SIZE
        skip_size += 1

    result = nums[0] * nums[1]
    print(f"Answer is {result}")


def part_2():
    lengths = [ord(ch) for ch in get_input()]
    lengths.extend([17, 31, 73, 47, 23])

    nums = list(range(LIST_SIZE))
    index = 0
    skip_size = 0

    for __ in range(64):
        for length in lengths:
            to_reverse = list()

            for block_index in range(length):
                n = (index + block_index) % LIST_SIZE
                to_reverse.append(nums[n])

            to_reverse.reverse()

            for block_index in range(length):
                n = (index + block_index) % LIST_SIZE
                nums[n] = to_reverse[block_index]

            index += length + skip_size
            index %= LIST_SIZE
            skip_size += 1

    result = ""

    for block_index in range(0, 16):
        sub_list = nums[16 * block_index : 16 * block_index + 16]
        result += hex(reduce(xor, sub_list))[2:]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
