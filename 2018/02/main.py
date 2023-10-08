from collections import Counter as counter

FILENAME = "input.txt"


def hamming_distance(str1, str2):
    result = 0

    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            result += 1

    return result + abs(len(str1) - len(str2))


def get_input() -> list[str]:
    string_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            string_list.append(line.strip())

    return string_list


def part_1():
    boxIDs = get_input()

    count_two = 0
    count_three = 0

    for boxID in boxIDs:
        list_values = counter(boxID).values()
        count_two += int(2 in list_values)
        count_three += int(3 in list_values)

    result = count_two * count_three

    print(f"Answer is {result}")


def part_2():
    boxIDs = get_input()

    for i in range(len(boxIDs) - 1):
        for j in range(i + 1, len(boxIDs)):
            if hamming_distance(boxIDs[i], boxIDs[j]) == 1:
                for remove_index, (ch1, ch2) in enumerate(zip(boxIDs[i], boxIDs[j])):
                    if ch1 != ch2:
                        result = (
                            boxIDs[i][:remove_index] + boxIDs[i][remove_index + 1 :]
                        )
                        print(f"Answer is {result}")
                        return


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
