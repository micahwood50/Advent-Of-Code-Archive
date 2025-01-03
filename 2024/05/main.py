FILENAME = "input.txt"


def get_input() -> tuple[set[tuple[int, int]], list[list[int]]]:
    page_orderings = set()
    pages = list()
    section_flag = True

    with open(FILENAME) as file:
        for line in file.readlines():
            line = line.strip()

            if len(line) == 0:
                section_flag = False
                continue

            if section_flag:
                page_orderings.add((tuple(map(int, line.split("|")))))

            else:
                pages.append(list(map(int, line.split(","))))

    return page_orderings, pages


def part_1():
    page_orderings, pages_list = get_input()

    result = 0

    for pages in pages_list:
        for i in range(len(pages) - 1):
            for j in range(i + 1, len(pages)):
                if (pages[j], pages[i]) in page_orderings:
                    break

            else:
                continue

            break

        else:
            result += pages[(len(pages) - 1) // 2]

    print(f"Answer is {result}")


def part_2():
    page_orderings, pages_list = get_input()

    result = 0
    incorrectly_ordered_list = list()

    for pages in pages_list:
        for i in range(len(pages) - 1):
            for j in range(i + 1, len(pages)):
                if (pages[j], pages[i]) in page_orderings:
                    incorrectly_ordered_list.append(pages)
                    break

            else:
                continue

            break

    for pages in incorrectly_ordered_list:
        for i in range(1, len(pages)):
            key = pages[i]
            j = i - 1

            while j >= 0 and (key, pages[j]) in page_orderings:
                pages[j + 1] = pages[j]
                j -= 1

            pages[j + 1] = key

        result += pages[(len(pages) - 1) // 2]

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
