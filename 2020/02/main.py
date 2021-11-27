import re

FILENAME = "input.txt"

class Policy:
    def __init__(self, num1, num2, letter, password):
        self.num1 = num1
        self.num2 = num2
        self.letter = letter
        self.password = password

    def __str__(self):
        return f"Policy({self.num1}, {self.num2}, '{self.letter}', \"{self.password}\")"

def get_input() -> list[Policy]:
    """ Read the file and generate a list of policies

    Returns:
        list[Policy]: A list of policies
    """
    policies_list = list()

    re_pattern = r"(\d+)-(\d+) ([a-z]): ([a-z]+)"

    with open(FILENAME) as f:
        for line in f.readlines():
            m = re.match(re_pattern, line)
            policies_list.append(
                Policy(
                    int(m.group(1)),
                    int(m.group(2)),
                    m.group(3),
                    m.group(4)
                )
            )

    return policies_list

def part_1():
    policies_list = get_input()
    valid_count = 0

    for policy in policies_list:
        match_letter_count = 0
        for ch in policy.password:
            if ch == policy.letter:
                match_letter_count += 1

        if policy.num1 <= match_letter_count <= policy.num2:
            valid_count += 1

    print(f"There are {valid_count} valid passwords.")

def part_2():
    policies_list = get_input()
    valid_count = 0

    for policy in policies_list:
        if (policy.password[policy.num1-1] == policy.letter) ^ (policy.password[policy.num2-1] == policy.letter):
            valid_count += 1

    print(f"There are {valid_count} valid passwords.")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
