FILENAME = "input.txt"


def get_fuel_requirement(mass: int) -> int:
    return mass // 3 - 2


def get_real_fuel_requirement(mass: int) -> int:
    result = 0
    mass = mass // 3 - 2

    while mass > 0:
        result += mass
        mass = mass // 3 - 2

    return result


def get_input() -> list[int]:
    int_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            int_list.append(int(line.strip()))

    return int_list


def part_1():
    module_masses = get_input()
    result = 0

    for mass in module_masses:
        result += get_fuel_requirement(mass)

    print(f"Answer is {result}")


def part_2():
    module_masses = get_input()
    result = 0

    for mass in module_masses:
        result += get_real_fuel_requirement(mass)

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
