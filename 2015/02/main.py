FILENAME = "input.txt"


class Present:
    def __init__(self, length: int, width: int, height: int):
        self.length = length
        self.width = width
        self.height = height

    def calculate_surface_area(self):
        return (
            2 * self.length * self.width
            + 2 * self.width * self.height
            + 2 * self.length * self.height
        )

    def calculate_wrapping_paper(self):
        return self.calculate_surface_area() + min(
            self.length * self.width,
            self.width * self.height,
            self.length * self.height,
        )

    def calculate_ribbon_wrap_length(self):
        return min(
            2 * self.length + 2 * self.width,
            2 * self.width + 2 * self.height,
            2 * self.length + 2 * self.height,
        )

    def calculate_ribbon_bow_length(self):
        return self.length * self.width * self.height

    def calculate_ribbon_length(self):
        return self.calculate_ribbon_wrap_length() + self.calculate_ribbon_bow_length()


def get_input() -> list[Present]:
    present_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            length, width, height = map(int, line.split("x"))

            this_persent = Present(length, width, height)

            present_list.append(this_persent)

    return present_list


def part_1():
    presents = get_input()
    result = 0

    for present in presents:
        result += present.calculate_wrapping_paper()

    print(f"They should order {result} total square feet of wrapping paper")


def part_2():
    presents = get_input()
    result = 0

    for present in presents:
        result += present.calculate_ribbon_length()

    print(f"They should order {result} total feet of ribbon")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
