from collections import defaultdict
from pprint import pprint

FILENAME = "input.txt"

MASK_COMMAND = '0'
MEM_COMMAND = '1'

def get_input() -> list[tuple[str]]:
    lines = list()

    mask = 0
    mem_index = -1

    with open(FILENAME) as f:
        for line in f.readlines():
            ls, rs = line.split(" = ")

            if ls == "mask":
                lines.append((MASK_COMMAND, rs.strip(), ""))

            else:
                lines.append((MEM_COMMAND, ls[4:-1], rs.strip()))

    return lines

def mask_num_v1(n: int, mask_str: str) -> int:
    bn = list('0'*len(mask_str) + bin(n)[2:])

    for i in range(-1, -len(mask_str)-1, -1):
        if mask_str[i] == 'X':
            continue

        bn[i] = mask_str[i]

    bn = "".join(bn)

    result = int(bn, 2)

    return result

def floating(string: str) -> set[int]:
    if 'X' not in string:
        return {int(string, 2)}

    index = string.index('X')

    s0 = string[:index] + '0' + string[index+1:]
    s1 = string[:index] + '1' + string[index+1:]

    return floating( s0 ) | floating( s1 )

def mask_num_v2(n: int, mask_str: str) -> set[int]:
    bn = list('0'*len(mask_str) + bin(n)[2:])

    for i in range(-1, -len(mask_str)-1, -1):
        if mask_str[i] == '0':
            continue

        else:
            bn[i] = mask_str[i]

    bn = "".join(bn)

    result = floating(bn)

    return result

def part_1():
    lines = get_input()

    mask = "X"
    mem_index = -1

    memory = defaultdict(int)

    for command, v1, v2 in lines:
        if command == MASK_COMMAND:
            mask = v1

        else:
            memory[int(v1)] = mask_num_v2(int(v2), mask)

    print(f"{sum(memory.values())}")

def part_2():
    lines = get_input()

    mask = "X"
    mem_index = -1

    memory = defaultdict(int)

    for command, v1, v2 in lines:
        if command == MASK_COMMAND:
            mask = v1

        else:
            for m_num in mask_num_v2(int(v1), mask):
                memory[m_num] = int(v2)

    print(f"{sum(memory.values())}")

if __name__ == "__main__":
    # part_1()
    part_2()
    pass
