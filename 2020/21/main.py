FILENAME = "input.txt"

class Food:
    def __init__(self, ingredients: set[str], allergens: set[str]):
        self.ingredients = ingredients
        self.allergens = allergens

def get_input() -> list[Food]:
    foods = list()

    with open(FILENAME) as f:
        for line in f.readlines():
            line = line.strip()

            ing_str, aller_str = line.split(' (contains ')

            ing_set = set(ing_str.split())
            aller_set = set(aller_str[:-1].split(", "))

            foods.append(Food(ing_set, aller_set))

    return foods

def part_1():
    food_list = get_input()

    all_ing = set()
    all_aller = set()

    possible_ing = dict()

    for food in food_list:
        all_ing |= food.ingredients
        all_aller |= food.allergens

        for aller in food.allergens:
            if aller in possible_ing:
                possible_ing[aller] &= food.ingredients
            else:
                possible_ing[aller] = food.ingredients.copy()

    ing_no_aller = all_ing

    for ing_s in possible_ing.values():
        ing_no_aller -= ing_s

    count = 0

    for food in food_list:
        for ing in food.ingredients:
            if ing in ing_no_aller:
                count += 1

    print(f"Ingredients that can't contain any of the allergens appear {count} times.")

def part_2():
    food_list = get_input()

    all_ing = set()
    all_aller = set()

    possible_ing = dict()

    for food in food_list:
        all_ing |= food.ingredients
        all_aller |= food.allergens

        for aller in food.allergens:
            if aller in possible_ing:
                possible_ing[aller] &= food.ingredients
            else:
                possible_ing[aller] = food.ingredients.copy()

    discovered_aller = set()

    while not all(len(s) == 1 for s in possible_ing.values()):
        for value in possible_ing.values():
            if len(value) == 1:
                discovered_aller |= value

            else:
                value -= discovered_aller

    print("The canonical dangerous ingredient list is:")
    print(",".join(list(possible_ing[aller])[0] for aller in sorted(possible_ing.keys())))


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
