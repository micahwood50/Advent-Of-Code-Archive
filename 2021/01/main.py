FILENAME = "input.txt"


def get_input() -> list[int]:
    depth_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            depth_list.append(int(line))

    return depth_list


def part_1():
    depth_list = get_input()
    result = 0

    # Assume the depth list is not empty, otherwise this will throw IndexError
    prev_depth = depth_list[0]

    for depth in depth_list[1:]:
        if depth > prev_depth:
            result += 1

        prev_depth = depth

    print(
        f"There are {result} measurements that are larger than the previous measurement"
    )


def part_2():
    depth_list = get_input()
    window_size = 3
    result = 0

    # Assume the depth list is longer than window size, otherwise this will throw IndexError
    prev_sum = sum(depth_list[i] for i in range(window_size))

    for index, depth in enumerate(depth_list[window_size:], start=window_size):
        curr_sum = prev_sum - depth_list[index - window_size] + depth

        if curr_sum > prev_sum:
            result += 1

        prev_sum = curr_sum

    print(f"There are {result} sums that are larger than the previous sum")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
