from __future__ import annotations

FILENAME = "input.txt"

class CuboidSwitch:
    def __init__(self, switch_bool: bool,
        x_min: int, x_max: int,
        y_min: int, y_max: int,
        z_min: int, z_max: int
    ):
        self.switch_bool = switch_bool
        self.overlapped_cuboids: set[CuboidSwitch] = set()

        self.x_min = x_min
        self.x_max = x_max

        self.y_min = y_min
        self.y_max = y_max

        self.z_min = z_min
        self.z_max = z_max

    def __hash__(self) -> int:
        return hash((
            self.switch_bool,
            self.x_min, self.x_max,
            self.y_min, self.y_max,
            self.z_min, self.z_max
        ))

    def is_in_bounded(self, cube_min: int, cube_max: int) -> bool:
        return not (
            self.x_max < cube_min or self.x_min > cube_max or
            self.y_max < cube_min or self.y_min > cube_max or
            self.z_max < cube_min or self.z_min > cube_max
        )

    def bound(self, cube_min: int, cube_max: int):
        assert self.is_in_bounded(cube_min, cube_max)

        self.x_min = max(self.x_min, cube_min)
        self.x_max = min(self.x_max, cube_max)

        self.y_min = max(self.y_min, cube_min)
        self.y_max = min(self.y_max, cube_max)

        self.z_min = max(self.z_min, cube_min)
        self.z_max = min(self.z_max, cube_max)

    def get_overlap_volume(self, other: CuboidSwitch) -> int:
        if self.is_overlap(other):
            return CuboidSwitch(False,
                max(self.x_min, other.x_min), min(self.x_max, other.x_max),
                max(self.y_min, other.y_min), min(self.y_max, other.y_max),
                max(self.z_min, other.z_min), min(self.z_max, other.z_max)
            ).calculate_volume()

        else:
            return 0

    def is_overlap(self, other: CuboidSwitch):
        result = (
            (other.x_min > self.x_max or self.x_min > other.x_max) and
            (other.y_min > self.y_max or self.y_min > other.y_max) and
            (other.z_min > self.z_max or self.z_min > other.z_max)
        )

        if result:
            self.add_overlapped_cuboid(other)
            other.add_overlapped_cuboid(self)

    def add_overlapped_cuboid(self, cuboid: CuboidSwitch):
        self.overlapped_cuboids.add(cuboid)

    def calculate_volume(self) -> int:
        return (self.x_max - self.x_min + 1) * (self.y_max - self.y_min + 1) * (self.z_max - self.z_min + 1)

def get_input() -> list[CuboidSwitch]:
    cuboid_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            switch_str, cuboid_str = line.strip().split()

            switch_bool = switch_str == "on"

            x_dim, y_dim, z_dim = cuboid_str.split(',')
            x_dim, y_dim, z_dim = x_dim[2:], y_dim[2:], z_dim[2:]

            x_min, x_max = map(int, x_dim.split(".."))
            y_min, y_max = map(int, y_dim.split(".."))
            z_min, z_max = map(int, z_dim.split(".."))

            cuboid_list.append(CuboidSwitch(switch_bool, x_min, x_max, y_min, y_max, z_min, z_max))

    return cuboid_list

def part_1():
    cuboid_list = get_input()
    grid = dict()

    cube_min, cube_max = -50, 50

    for x in range(cube_min, cube_max+1):
        for y in range(cube_min, cube_max+1):
            for z in range(cube_min, cube_max+1):
                grid[(x, y, z)] = False

    for cuboid in cuboid_list:
        if not cuboid.is_in_bounded(cube_min, cube_max):
            continue

        cuboid.bound(cube_min, cube_max)

        for x in range(cuboid.x_min, cuboid.x_max+1):
            for y in range(cuboid.y_min, cuboid.y_max+1):
                for z in range(cuboid.z_min, cuboid.z_max+1):
                    grid[(x, y, z)] = cuboid.switch_bool

    result = 0
    for x in range(cube_min, cube_max+1):
        for y in range(cube_min, cube_max+1):
            for z in range(cube_min, cube_max+1):
                if grid[(x, y, z)]:
                    result += 1

    print(f"{result} cubes are on")

def part_2():
    cuboid_list = get_input()
    result = 0

    visited_cuboid_set: set[CuboidSwitch] = set()

    for i in range(len(cuboid_list)-1):
        for j in range(i+1, len(cuboid_list)):
            cuboid_list[i].is_overlap(cuboid_list[j])

    for cuboid in cuboid_list:
        L = list(cuboid.overlapped_cuboids)
        for i in range(len(L)-1):
            for j in range(i+1, len(L)):
                if L[j] in L[i].overlapped_cuboids or L[i] in L[j].overlapped_cuboids:
                    print("!!!")
                    exit()

    for cuboid in cuboid_list:
        this_result = 0
        if cuboid.switch_bool == True:
            this_result += cuboid.calculate_volume()

        for visited_overlap_cuboid in visited_cuboid_set & cuboid.overlapped_cuboids:
            if visited_overlap_cuboid.switch_bool == True:
                this_result -= cuboid.get_overlap_volume(visited_overlap_cuboid)

        result += this_result
        visited_cuboid_set.add(cuboid)

    print(f"                 {result}")

if __name__ == "__main__":
    # part_1()
    part_2()
    print("Expected answer: 2758514936282235")
    pass
