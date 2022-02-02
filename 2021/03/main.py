from collections import Counter

FILENAME = "input.txt"


def get_input() -> list[str]:
    diagnostic_report = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            diagnostic_report.append(line.strip())

    return diagnostic_report


def calculate_oxygen_rating(diagnostic_report: list[str]) -> int:
    filter_list = diagnostic_report

    for index in range(len(diagnostic_report[0])):
        zero_counter = 0
        for num in filter_list:
            if num[index] == "0":
                zero_counter += 1

        most_common_bit = "0" if zero_counter > len(filter_list) / 2 else "1"

        new_filter_list = list()

        for num in filter_list:
            if num[index] == most_common_bit:
                new_filter_list.append(num)

        filter_list = new_filter_list

        if len(filter_list) == 1:
            break

    return int(filter_list[0], 2)


def calculate_CO2_scrubber_rating(diagnostic_report: list[str]) -> int:
    filter_list = diagnostic_report

    for index in range(len(diagnostic_report[0])):
        zero_counter = 0
        for num in filter_list:
            if num[index] == "0":
                zero_counter += 1

        least_common_bit = "0" if zero_counter <= len(filter_list) / 2 else "1"

        new_filter_list = list()

        for num in filter_list:
            if num[index] == least_common_bit:
                new_filter_list.append(num)

        filter_list = new_filter_list

        if len(filter_list) == 1:
            break

    return int(filter_list[0], 2)


def part_1():
    diagnostic_report = get_input()

    gamma_binary = "0"
    epsilon_binary = "0"

    for bits in zip(*diagnostic_report):
        most_common_bit = Counter(bits).most_common(1)[0][0]

        gamma_binary += most_common_bit
        epsilon_binary += "0" if most_common_bit == "1" else "1"

    gamma_rate = int(gamma_binary, 2)
    epsilon_rate = int(epsilon_binary, 2)

    print(f"The power consumption of the submarine is {gamma_rate * epsilon_rate}")


def part_2():
    diagnostic_report = get_input()

    oxygen_rating = calculate_oxygen_rating(diagnostic_report)
    CO2_scrubber_rating = calculate_CO2_scrubber_rating(diagnostic_report)

    print(
        f"The life support rating of the submarine is {oxygen_rating * CO2_scrubber_rating}"
    )


if __name__ == "__main__":
    part_1()
    # part_2()
    pass
