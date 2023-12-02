FILENAME = "input.txt"

COLORS = ["red", "green", "blue"]


class Game:
    def __init__(self, game_id: int, cubes: dict[str, int]):
        self.game_id = game_id
        self.cubes = cubes

    def get_power(self) -> int:
        result = 1

        for v in self.cubes.values():
            result *= v

        return result


def get_input() -> list[Game]:
    game_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            game_str, cube_str = line.strip().split(": ")
            game_id = int(game_str.split()[1])

            cubes = dict()

            for cube_reveal_str in cube_str.split("; "):
                if "," in cube_reveal_str:
                    for cube_type_str in cube_reveal_str.split(", "):
                        cube_num, cube_color = cube_type_str.split()
                        cubes[cube_color] = max(cubes.get(cube_color, 0), int(cube_num))

                else:
                    cube_num, cube_color = cube_reveal_str.split()
                    cubes[cube_color] = max(cubes.get(cube_color, 0), int(cube_num))

            game_list.append(Game(game_id, cubes))

    return game_list


def part_1():
    games = get_input()
    result = 0

    target_dict = {"red": 12, "green": 13, "blue": 14}

    for game in games:
        for color in COLORS:
            if game.cubes[color] > target_dict[color]:
                break
        else:
            result += game.game_id

    print(f"Answer is {result}")


def part_2():
    games = get_input()
    result = 0

    for game in games:
        result += game.get_power()

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
