FILENAME = "input.txt"


class MapFunction:
    def __init__(self, name: str):
        self.name = name
        self.list_intervals = list()

    def add_interval(self, dest_start: int, source_start: int, range_length: int):
        self.list_intervals.append((dest_start, source_start, range_length))

    def get_map_value(self, n: int) -> int:
        for dest, source, range_len in self.list_intervals:
            if source <= n < source + range_len:
                return n - source + dest

        return n

    def get_map_intervals(self, interval: tuple[int, int]) -> list[tuple[int, int]]:
        raise NotImplementedError("Not finished with this function!")

        result = list()

        interval_queue = [interval]

        while interval_queue:
            curr_interval = interval_queue.pop()

            for dest, source, range_len in self.list_intervals:
                if source <= curr_interval[0] < source + range_len:
                    this_interval_start = curr_interval[0] - source + dest

                    if curr_interval[1] < source + range_len:
                        this_interval_end = curr_interval[1] - source + dest

                    else:
                        this_interval_end = source + range_len
                        next_interval_start = curr_interval[0] + range_len

        return result

    def __str__(self) -> str:
        result = f"{self.name} map:\n"

        for dest, source, range_len in self.list_intervals:
            result += f"{dest} {source} {range_len}\n"

        return result


def get_input() -> tuple[list[int], list[MapFunction]]:
    seed_list = list()
    map_func_list = list()

    with open(FILENAME) as file:
        seed_list = list(map(int, file.readline().split(": ")[1].split()))

        file.readline()

        while True:
            try:
                this_map_function = MapFunction(file.readline().split()[0])
                while line := file.readline().strip():
                    this_map_function.add_interval(*map(int, line.split()))

                map_func_list.append(this_map_function)

            except IndexError:
                break

    return seed_list, map_func_list


def part_1():
    seed_list, map_func_list = get_input()
    result = float("inf")

    for seed in seed_list:
        this_num = seed

        for map_f in map_func_list:
            this_num = map_f.get_map_value(this_num)

        result = min(result, this_num)

    print(f"Answer is {result}")


def part_2():
    seed_list, map_func_list = get_input()
    result = float("inf")

    for seed_start, seed_range in zip(seed_list[0::2], seed_list[1::2]):
        print(seed_range)
        for seed in range(seed_start, seed_start + seed_range):
            this_num = seed

            for map_f in map_func_list:
                this_num = map_f.get_map_value(this_num)

            result = min(result, this_num)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
