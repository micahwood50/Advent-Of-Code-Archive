from collections import defaultdict

FILENAME = "input.txt"

def get_input() -> list[int]:
    with open(FILENAME) as file:
        lanternfish_timers = list(map(int, file.readline().split(',')))

    return lanternfish_timers

def simulate(lanternfish_timers: list[int], days: int):
    timers_dict = defaultdict(int)

    for timer in lanternfish_timers:
        timers_dict[timer] += 1

    for __ in range(days):
        temp_dict = defaultdict(int)

        for timer_num in range(1, 9):
            temp_dict[timer_num-1] = timers_dict[timer_num]

        temp_dict[6] += timers_dict[0]
        temp_dict[8] += timers_dict[0]

        timers_dict = temp_dict

    print(f"After {days} days, there would be {sum(timers_dict.values())} lanternfishes")

def part_1():
    lanternfish_timers = get_input()
    simulate(lanternfish_timers, 80)

def part_2():
    lanternfish_timers = get_input()
    simulate(lanternfish_timers, 256)

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
