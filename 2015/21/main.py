from itertools import combinations


FILENAME = "input.txt"


class Item:
    def __init__(self, name: str, cost: int, damage: int, armor: int):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor


class Character:
    def __init__(self, hitpoint: int = 100, damage: int = 0, armor: int = 0):
        self.hitpoint = hitpoint
        self.damage = damage
        self.armor = armor
        self.items = list()

    def use_item(self, item: Item):
        self.damage += item.damage
        self.armor += item.armor
        self.items.append(item)


WEAPONS = [
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0),
]

ARMORS = [
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5),
]

RINGS = [
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3),
]


def get_input() -> tuple[int, int, int]:
    info_list = list()

    with open(FILENAME) as file:
        for __ in range(3):
            info_list.append(int(file.readline().strip().split()[-1]))

    return tuple(info_list)


def part_1():
    boss_info = get_input()
    result = 100_000

    for weapon in WEAPONS:
        for armor_num in range(2):
            for armors in combinations(ARMORS, armor_num):
                for ring_num in range(3):
                    for rings in combinations(RINGS, ring_num):
                        this_player = Character()
                        this_boss = Character(*boss_info)

                        this_player.use_item(weapon)
                        this_cost = weapon.cost

                        for armor in armors:
                            this_player.use_item(armor)
                            this_cost += armor.cost

                        for ring in rings:
                            this_player.use_item(ring)
                            this_cost += ring.cost

                        while True:
                            this_boss.hitpoint -= max(
                                1, this_player.damage - this_boss.armor
                            )

                            if this_boss.hitpoint <= 0:
                                result = min(result, this_cost)
                                break

                            this_player.hitpoint -= max(
                                1, this_boss.damage - this_player.armor
                            )

                            if this_player.hitpoint <= 0:
                                break

    print(f"Answer is {result}")


def part_2():
    boss_info = get_input()
    result = 0

    for weapon in WEAPONS:
        for armor_num in range(2):
            for armors in combinations(ARMORS, armor_num):
                for ring_num in range(3):
                    for rings in combinations(RINGS, ring_num):
                        this_player = Character()
                        this_boss = Character(*boss_info)

                        this_player.use_item(weapon)
                        this_cost = weapon.cost

                        for armor in armors:
                            this_player.use_item(armor)
                            this_cost += armor.cost

                        for ring in rings:
                            this_player.use_item(ring)
                            this_cost += ring.cost

                        while True:
                            this_boss.hitpoint -= max(
                                1, this_player.damage - this_boss.armor
                            )

                            if this_boss.hitpoint <= 0:
                                break

                            this_player.hitpoint -= max(
                                1, this_boss.damage - this_player.armor
                            )

                            if this_player.hitpoint <= 0:
                                result = max(result, this_cost)
                                break

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
