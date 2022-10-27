from itertools import product

FILENAME = "input.txt"


class Ingredient:
    def __init__(
        self,
        name: str,
        capacity: int,
        durability: int,
        flavor: int,
        texture: int,
        calories: int,
    ):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __str__(self) -> str:  # For debug purpose
        return f"{self.name}: capacity {self.capacity}, durability {self.durability}, flavor {self.flavor}, texture {self.texture}, calories {self.calories}"

    def __repr__(self) -> str:
        return f"Ingredient({self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories})"

    def __mul__(self, n: int):
        return Ingredient(
            self.name,
            n * self.capacity,
            n * self.durability,
            n * self.flavor,
            n * self.texture,
            n * self.calories,
        )

    def __rmul__(self, n: int):
        return self.__mul__(n)


def get_score(*ingredients) -> int:
    def get_vector(ingredient: Ingredient) -> list[int]:
        return [
            ingredient.capacity,
            ingredient.durability,
            ingredient.flavor,
            ingredient.texture,
        ]

    score = 1

    for properties in zip(*map(get_vector, ingredients)):
        score *= max(0, sum(properties))

    return score


def get_calorie(*ingredients) -> int:
    return sum(ingredient.calories for ingredient in ingredients)


def get_input() -> list[Ingredient]:
    ingredient_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            name, rest = line.strip().split(":")
            capacity, durability, flavor, texture, calories = [
                int(info.split()[1]) for info in rest.strip().split(", ")
            ]

            ingredient_list.append(
                Ingredient(name, capacity, durability, flavor, texture, calories)
            )

    return ingredient_list


def part_1():
    ingredient_list = get_input()

    best_score = 0
    i1, i2, i3, i4 = ingredient_list

    for a1, a2, a3 in product(range(101), repeat=3):
        a4 = 100 - a1 - a2 - a3

        if a4 < 0:
            continue

        ti1 = a1 * i1
        ti2 = a2 * i2
        ti3 = a3 * i3
        ti4 = a4 * i4

        best_score = max(best_score, get_score(ti1, ti2, ti3, ti4))

    print(f"The total score of the highest-scoring cookie we can make is {best_score}")


def part_2():
    ingredient_list = get_input()

    best_score = 0
    i1, i2, i3, i4 = ingredient_list

    for a1, a2, a3 in product(range(101), repeat=3):
        a4 = 100 - a1 - a2 - a3

        if a4 < 0:
            continue

        ti1 = a1 * i1
        ti2 = a2 * i2
        ti3 = a3 * i3
        ti4 = a4 * i4

        if get_calorie(ti1, ti2, ti3, ti4) == 500:
            best_score = max(best_score, get_score(ti1, ti2, ti3, ti4))

    print(
        f"The total score of the highest-scoring cookie we can make with a calorie total of 500 is {best_score}"
    )


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
