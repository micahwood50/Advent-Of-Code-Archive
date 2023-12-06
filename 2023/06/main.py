FILENAME = "input.txt"


def calculate_distances(time: int) -> list[int]:
    result = list()

    for ti in range(1, time):
        result.append(ti * (time - ti))

    return result


def get_input(*, is_space=True) -> tuple[list[int], list[int]] | tuple[int, int]:
    with open(FILENAME) as file:
        if is_space:
            time_list = list(map(int, file.readline().split(":")[1].strip().split()))
            dist_list = list(map(int, file.readline().split(":")[1].strip().split()))

            return time_list, dist_list

        else:
            time = int("".join(file.readline().split(":")[1].strip().split()))
            dist = int("".join(file.readline().split(":")[1].strip().split()))

            return time, dist


def part_1():
    time_list, dist_list = get_input()
    result = 1

    for time, record_dist in zip(time_list, dist_list):
        count_ways_beat = 0

        for possible_dist in calculate_distances(time):
            if possible_dist > record_dist:
                count_ways_beat += 1

        result *= count_ways_beat

    print(f"Answer is {result}")


def part_2():
    time, record_dist = get_input(is_space=False)
    result = 0

    for ti in range(time // 2, 0, -1):
        possible_dist = ti * (time - ti)

        if possible_dist > record_dist:
            result += 1

        else:
            result *= 2
            if time % 2 == 0:
                result -= 1
            break

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
