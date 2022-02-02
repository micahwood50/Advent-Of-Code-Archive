FILENAME = "input.txt"


class DigitSegments:
    def __init__(self, pattern_list: list[str]):
        #
        # Generate sets according
        #

        S2, S3, S4, S5, S6 = list(), list(), list(), list(), list()

        for pattern in pattern_list:
            if len(pattern) == 2:
                S2.append(set(pattern))

            elif len(pattern) == 3:
                S3.append(set(pattern))

            elif len(pattern) == 4:
                S4.append(set(pattern))

            elif len(pattern) == 5:
                S5.append(set(pattern))

            elif len(pattern) == 6:
                S6.append(set(pattern))

        S5_intersection = set("abcdefg")
        S6_intersection = set("abcdefg")

        for set_pattern in S5:
            S5_intersection &= set_pattern

        for set_pattern in S6:
            S6_intersection &= set_pattern

        #
        # Now we deduce everything...
        #
        # Variables a, b, ..., g represent segments from seven-segment display according to this:
        #
        #   aaaa
        #  b    c
        #  b    c
        #   dddd
        #  e    f
        #  e    f
        #   gggg
        #
        # Each of those variables will be equal to one of those character: a, b, ..., g; basically a random permutation.

        # Step 1: deduce a, d, and f

        a = list(S5_intersection & S3[0])[0]
        d = list(S5_intersection & S4[0])[0]
        f = list(S6_intersection & S2[0])[0]

        # Step 2: deduce c

        c = list(S2[0] - {f})[0]

        # Step 3: deduce g

        for s5_element in S5:
            if len(s5_element - {a, c, d, f}) == 1:
                g = list(s5_element - {a, c, d, f})[0]

        # Step 4: deduce b and e

        for s5_element in S5:
            if (
                c in s5_element and f in s5_element
            ):  # All segments in digit 3 are already deduced
                continue

            if c in s5_element:  # Digit 2
                e = list(s5_element - {a, c, d, g})[0]

            else:  # f is in s5_element; Digit 5
                b = list(s5_element - {a, d, f, g})[0]

        #
        # We successfully deduced everything. Now we populate the _digit_dict variable
        #

        # We use frozenset as a hashable set
        self._digit_dict = {
            frozenset(a + b + c + e + f + g): 0,
            frozenset(c + f): 1,
            frozenset(a + c + d + e + g): 2,
            frozenset(a + c + d + f + g): 3,
            frozenset(b + c + d + f): 4,
            frozenset(a + b + d + f + g): 5,
            frozenset(a + b + d + e + f + g): 6,
            frozenset(a + c + f): 7,
            frozenset(a + b + c + d + e + f + g): 8,
            frozenset(a + b + c + d + f + g): 9,
        }

    def get_digit(self, digit_pattern: str):
        digit_set = frozenset(digit_pattern)

        if digit_set not in self._digit_dict:
            raise ValueError(f"Unknown pattern: {digit_pattern}")

        return self._digit_dict[digit_set]


def get_input() -> tuple[list[list[str]], list[list[str]]]:
    patterns_list = list()
    outputs_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            pattern_line, output_line = line.split(" | ")
            patterns_list.append(pattern_line.split())
            outputs_list.append(output_line.split())

    return patterns_list, outputs_list


def part_1():
    _, outputs_list = get_input()
    result = 0

    for outputs in outputs_list:
        for output_digit in outputs:
            if len(output_digit) in {2, 3, 4, 7}:
                result += 1

    print(f"Digits 1, 4, 7, or 8 appear {result} times")


def part_2():
    patterns_list, outputs_list = get_input()
    result = 0

    for patterns, outputs in zip(patterns_list, outputs_list):
        digit_class = DigitSegments(patterns)

        num = 0
        for output_digit in outputs:
            num = 10 * num + digit_class.get_digit(output_digit)

        result += num

    print(f"The sum of all the output values is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
