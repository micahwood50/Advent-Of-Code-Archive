from collections import defaultdict

FILENAME = "input.txt"


class Reindeer:
    def __init__(self, name: str, speed: int, run_duration: int, rest_duration: int):
        self.name = name
        self.speed = speed
        self.run_duration = run_duration
        self.rest_duration = rest_duration
        self._position = 0
        self._time = 0
        self._is_rest = False

    @property
    def distance_traveled(self):
        return self._position

    def next_tick(self):
        if self._is_rest:
            if self._time >= self.rest_duration:
                self._is_rest = False
                self._time = 1
                self._position += self.speed
            else:
                self._time += 1

        else:
            if self._time >= self.run_duration:
                self._is_rest = True
                self._time = 1

            else:
                self._time += 1
                self._position += self.speed

    def __str__(self) -> str:  # For debug purpose
        return f"{self.name}:\n\tCan fly {self.speed} km/s for {self.run_duration} seconds, but then must rest for {self.rest_duration} seconds."

    def __repr__(self) -> str:
        return (
            f"Reindeer({self.name, self.speed, self.run_duration, self.rest_duration})"
        )


def get_input() -> dict[str, dict[str, int]]:
    reindeer_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            name, rest = line.strip().split(" can fly ")
            speed, rest = rest.strip().split(" km/s for ")
            run_duration, rest = rest.strip().split(" seconds, but then must rest for ")
            rest_duration, _ = rest.strip().split(" sec")

            reindeer_list.append(
                Reindeer(name, int(speed), int(run_duration), int(rest_duration))
            )

    return reindeer_list


def part_1():
    reindeer_list = get_input()

    T = 2503

    for __ in range(T):
        for r in reindeer_list:
            r.next_tick()

    print(
        f"The winning reindeer traveled {max(r.distance_traveled for r in reindeer_list)} km."
    )


def part_2():
    reindeer_list = get_input()
    scoreboard = defaultdict(int)

    T = 2503

    for __ in range(T):
        for r in reindeer_list:
            r.next_tick()

        lead_distance = max(r.distance_traveled for r in reindeer_list)

        for r in reindeer_list:
            if r.distance_traveled == lead_distance:
                scoreboard[r.name] += 1

    print(f"The winning reindeer has {max(scoreboard.values())} points.")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
