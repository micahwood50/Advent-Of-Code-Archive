FILENAME = "input.txt"

def get_next_step(grid: list[list[int]]) -> tuple[list[list[int]], int]:
    visited_set = set()

    def flash(ri: int, ci: int):
        if (ri, ci) in visited_set or not (0 <= ri < len(grid)) or not (0 <= ci < len(grid[0])):
            return

        grid[ri][ci] += 1

        if grid[ri][ci] > 9:
            visited_set.add((ri, ci))

            for dri in [-1, 0, 1]:
                for dci in [-1, 0, 1]:
                    flash(ri + dri, ci + dci)

    for ri in range(len(grid)):
        for ci in range(len(grid[0])):
            if grid[ri][ci] == 9:
                flash(ri, ci)

            else:
                grid[ri][ci] += 1

    for ri in range(len(grid)):
        for ci in range(len(grid[0])):
            if grid[ri][ci] > 9:
                grid[ri][ci] = 0

    return grid, len(visited_set)

def is_all_flash(grid: list[list[int]]) -> bool:
    for row in grid:
        for num in row:
            if num != 0:
                return False

    return True

def get_input() -> list[list[int]]:
    grid = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            grid.append(list(int(ch) for ch in line.strip()))

    return grid

def part_1():
    grid = get_input()
    result = 0
    N = 100

    for __ in range(N):
        grid, count = get_next_step(grid)
        result += count

    print(f"There are {result} total flashes after {N} steps")

def part_2():
    grid = get_input()
    step_count = 0

    while True:
        grid, _ = get_next_step(grid)
        step_count += 1
        if is_all_flash(grid):
            break

    print(f"The first step during which all octopuses flash is {step_count}")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
