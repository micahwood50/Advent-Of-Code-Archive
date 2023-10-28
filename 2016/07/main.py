from collections import defaultdict


FILENAME = "input.txt"


def is_abba(s: str) -> bool:
    if len(s) != 4:
        raise ValueError(f"Invalid string: {s}! The string length should be 4.")

    return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]


def is_aba(s: str) -> bool:
    if len(s) != 3:
        raise ValueError(f"Invalid string: {s}! The string length should be 3.")

    return s[0] == s[2] and s[0] != s[1]


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def part_1():
    addresses = get_input()
    result = 0

    for address in addresses:
        in_brackets_flag = False
        is_valid_flag = False

        for i in range(len(address) - 3):
            four_chs = address[i : i + 4]

            if "]" in four_chs:
                in_brackets_flag = False

            elif "[" in four_chs:
                in_brackets_flag = True

            else:
                if is_abba(four_chs):
                    if in_brackets_flag:
                        break
                    else:
                        is_valid_flag = True
        else:
            if is_valid_flag:
                result += 1

    print(f"Answer is {result}")


def part_2():
    addresses = get_input()
    result = 0

    for address in addresses:
        ABA_BAB_dict = defaultdict(set)
        in_brackets_flag = False

        for i in range(len(address) - 2):
            three_chs = address[i : i + 3]

            if "]" in three_chs:
                in_brackets_flag = False

            elif "[" in three_chs:
                in_brackets_flag = True

            else:
                if is_aba(three_chs):
                    this_tuple = tuple(sorted(list(set(three_chs))))
                    ABA_BAB_dict[this_tuple].add((three_chs, in_brackets_flag))

        for value_set in ABA_BAB_dict.values():
            if len(value_set) > 2:
                result += 1
                break

            if len(value_set) == 2:
                t1 = value_set.pop()
                t2 = value_set.pop()
                if t1[0][0] == t2[0][1] and t1[1] != t2[1]:
                    result += 1
                    break

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
