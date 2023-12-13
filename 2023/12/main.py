FILENAME = "input.txt"

OPERATIONAL_CHAR = "."
DAMAGED_CHAR = "#"
UNKNOWN_CHAR = "?"


DP = dict()


def count_arrangement(
    condition: str,
    blocks: list[int],
    *,
    index: int = 0,
    block_index: int = 0,
    curr_damaged_count: int = 0,
) -> int:
    key = (index, block_index, curr_damaged_count)

    if key in DP:
        return DP[key]

    if index == len(condition):
        if (block_index == len(blocks) and curr_damaged_count == 0) or (
            block_index == len(blocks) - 1 and curr_damaged_count == blocks[block_index]
        ):
            return 1

        return 0

    result = 0

    for ch in [OPERATIONAL_CHAR, DAMAGED_CHAR]:
        if condition[index] in {ch, UNKNOWN_CHAR}:
            if ch == OPERATIONAL_CHAR:
                if curr_damaged_count == 0:
                    result += count_arrangement(
                        condition,
                        blocks,
                        index=index + 1,
                        block_index=block_index,
                        curr_damaged_count=0,
                    )

                elif (
                    curr_damaged_count > 0
                    and block_index < len(blocks)
                    and blocks[block_index] == curr_damaged_count
                ):
                    result += count_arrangement(
                        condition,
                        blocks,
                        index=index + 1,
                        block_index=block_index + 1,
                        curr_damaged_count=0,
                    )

            else:
                result += count_arrangement(
                    condition,
                    blocks,
                    index=index + 1,
                    block_index=block_index,
                    curr_damaged_count=curr_damaged_count + 1,
                )

    DP[key] = result

    return result


def unfold(condition: str, blocks: list[int]) -> tuple[str, list[int]]:
    condition = UNKNOWN_CHAR.join([condition for __ in range(5)])
    blocks = blocks * 5

    return condition, blocks


def get_input() -> list[tuple[str, list[int]]]:
    record_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            condition, blocks = line.strip().split()
            blocks = list(map(int, blocks.split(",")))

            record_list.append((condition, blocks))

    return record_list


def part_1():
    record_list = get_input()
    result = 0

    for row in record_list:
        DP.clear()
        result += count_arrangement(*row)

    print(f"Answer is {result}")


def part_2():
    record_list = get_input()
    result = 0

    for row in record_list:
        DP.clear()
        result += count_arrangement(*unfold(*row))

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
