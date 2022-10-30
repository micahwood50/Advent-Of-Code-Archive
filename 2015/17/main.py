FILENAME = "input.txt"


def get_input() -> list[int]:
    containers_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            containers_list.append(int(line))

    return containers_list


def part_1():
    containers_list = get_input()

    def count_combinations(amount: int, index: int = 0):
        if amount == 0:
            return 1

        if amount < 0 or index >= len(containers_list):
            return 0

        return count_combinations(
            amount - containers_list[index], index + 1
        ) + count_combinations(amount, index + 1)

    print(f"Answer is {count_combinations(150)}")


def part_2():
    containers_list = get_input()
    count_num_containers = list()

    def count_combinations(amount: int, index: int = 0, count_containers=0):
        if amount == 0:
            count_num_containers.append(count_containers)
            return 1

        if amount < 0 or index >= len(containers_list):
            return 0

        return count_combinations(
            amount - containers_list[index], index + 1, count_containers + 1
        ) + count_combinations(amount, index + 1, count_containers)

    count_combinations(150)

    print(f"Answer is {count_num_containers.count(min(count_num_containers))}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
