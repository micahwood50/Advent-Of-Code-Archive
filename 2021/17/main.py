FILENAME = "input.txt"


class Hoop:
    def __init__(
        self,
        x_low_target: int,
        x_high_target: int,
        y_low_target: int,
        y_high_target: int,
    ):
        self.x_low_target = x_low_target
        self.x_high_target = x_high_target
        self.y_low_target = y_low_target
        self.y_high_target = y_high_target

    def velocity(self, vx: int, vy: int) -> tuple[int, int, int]:
        x, y = 0, 0

        max_y = 0

        while x <= self.x_high_target and self.y_low_target <= y:
            x += vx
            y += vy

            max_y = max(max_y, y)

            if vx > 0:
                vx -= 1
            elif vx < 0:
                vx += 1
            vy -= 1

            if (
                self.x_low_target <= x <= self.x_high_target
                and self.y_low_target <= y <= self.y_high_target
            ):
                return (x, y, max_y)

        return (0, 0, 0)


def get_input() -> Hoop:
    with open(FILENAME) as file:
        line = file.readline().strip()
        _, x_side, y_side = line.split("=")
        low_x, high_x = x_side.split("..")
        low_y, high_y = y_side.split("..")
        hoop = Hoop(*[int(n) for n in [low_x, high_x[:-3], low_y, high_y]])

    return hoop


def part_1():
    hoop = get_input()

    result = 0

    for vx in range(1, hoop.x_high_target + 1):
        for vy in range(0, 1000):
            result = max(result, hoop.velocity(vx, vy)[2])

    print(f"The highest y position it reaches on this trajectory is {result}")


def part_2():
    hoop = get_input()

    result = 0

    for vx in range(1, hoop.x_high_target + 1):
        for vy in range(hoop.y_low_target - 1, 1000):
            shot = hoop.velocity(vx, vy)
            if shot != (0, 0, 0):
                result += 1

    print(
        f"There are {result} distinct initial velocity values cause the probe to be within the target area after any step"
    )


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
