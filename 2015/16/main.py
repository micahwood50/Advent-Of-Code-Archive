from dataclasses import dataclass
from typing_extensions import Self

FILENAME = "input.txt"


@dataclass
class Sue:
    ### -1 indicates unknown value
    id: int
    children: int = -1
    cats: int = -1
    samoyeds: int = -1
    pomeranians: int = -1
    akitas: int = -1
    vizslas: int = -1
    goldfish: int = -1
    trees: int = -1
    cars: int = -1
    perfumes: int = -1

    @classmethod
    def get_compounds(cls):
        return [
            attr
            for attr in dir(cls)
            if not callable(getattr(cls, attr))
            and not attr.startswith("_")
            and attr != "id"
        ]

    def get_var(self, var_name: str):
        return getattr(self, var_name, -1)

    def is_sub(self, other_sue: Self) -> bool:
        for var in self.get_compounds():
            if self.get_var(var) != -1 and self.get_var(var) != other_sue.get_var(var):
                return False

        return True

    def is_actual_sub(self, other_sue: Self) -> bool:
        for var in self.get_compounds():
            if self.get_var(var) != -1:
                if var == "cats" or var == "trees":
                    if self.get_var(var) <= other_sue.get_var(var):
                        return False

                elif var == "pomeranians" or var == "goldfish":
                    if self.get_var(var) >= other_sue.get_var(var):
                        return False

                else:
                    if self.get_var(var) != other_sue.get_var(var):
                        return False

        return True


GOAL_SUE = Sue(
    **{
        "id": 0,
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
)


def get_input() -> list[Sue]:
    sue_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            this_line_dict = dict()

            sue_str_id, var_info = line.strip().split(": ", 1)

            this_line_dict["id"] = int(sue_str_id.split()[1])
            for var_str in var_info.split(", "):
                var_name, var_str_int = var_str.strip().split(": ")
                this_line_dict[var_name] = int(var_str_int)

            sue_list.append(Sue(**this_line_dict))

    return sue_list


def part_1():
    sue_list = get_input()

    result = list()

    for sue in sue_list:
        if sue.is_sub(GOAL_SUE):
            result.append(sue.id)

    print(f"The number of the Sue that got us the gift is ", end="")
    print(*result, sep=", ", end=".\n")


def part_2():
    sue_list = get_input()

    result = list()

    for sue in sue_list:
        if sue.is_actual_sub(GOAL_SUE):
            result.append(sue.id)

    print(f"The number of the Sue that got us the gift is ", end="")
    print(*result, sep=", ", end=".\n")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
