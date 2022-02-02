from itertools import permutations

FILENAME = "input.txt"


def get_distance(routes: dict[frozenset, int], city1: str, city2: str) -> int:
    return routes[frozenset([city1, city2])]


def get_input() -> tuple[set[str], dict[frozenset, int]]:
    routes = dict()
    cities = set()

    with open(FILENAME) as file:
        for line in file.readlines():
            locations, distance = line.split(" = ")
            distance = int(distance)
            loc_A, loc_B = locations.split(" to ")

            cities.add(loc_A)
            cities.add(loc_B)

            routes[frozenset([loc_A, loc_B])] = distance

    return cities, routes


def part_1():
    cities, routes = get_input()
    result = float("inf")

    for city_perm in permutations(cities):
        this_route_distance = 0

        for i in range(len(cities) - 1):
            this_route_distance += get_distance(routes, city_perm[i], city_perm[i + 1])

        result = min(result, this_route_distance)

    print(f"The distance of the shortest route is {result}")


def part_2():
    cities, routes = get_input()
    result = 0

    for city_perm in permutations(cities):
        this_route_distance = 0

        for i in range(len(cities) - 1):
            this_route_distance += get_distance(routes, city_perm[i], city_perm[i + 1])

        result = max(result, this_route_distance)

    print(f"The distance of the longest route is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
