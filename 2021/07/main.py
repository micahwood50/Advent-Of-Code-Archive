from statistics import mean, median

FILENAME = "input.txt"

def triangular_number(num: int) -> int:
    return num*(num+1)//2

def get_input() -> list[int]:
    position_list = list()

    with open(FILENAME) as file:
        position_list = list(map(int, file.readline().split(',')))

    return position_list

def part_1():
    position_list = get_input()
    fuel_total = 0
    desired_position = round(median(position_list))

    for position in position_list:
        fuel_total += abs(desired_position - position)

    print(f"They need to spend {fuel_total} fuels")

def part_2():
    position_list = get_input()
    fuel_total = float("inf")

    mean_position = round(mean(position_list))

    for i in range(-1, 2):
        this_fuel_total = 0
        for position in position_list:
            this_fuel_total += triangular_number(abs(mean_position + i - position))

        fuel_total = min(fuel_total, this_fuel_total)

    print(f"They need to spend {fuel_total} fuels")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
