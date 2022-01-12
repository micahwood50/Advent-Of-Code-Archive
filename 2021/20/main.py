FILENAME = "input.txt"

LIGHT_PIXEL = '#'
DARK_PIXEL  = '.'

def get_input() -> tuple[str, list[list[str]]]:
    grid = list()

    with open(FILENAME) as file:
        image_enhancement = file.readline().strip()
        file.readline()

        for row in file.readlines():
            grid.append(row.strip())

    return image_enhancement, grid

def convert_grid_to_set(grid: list[list[str]]) -> set[tuple[int, int]]:
    light_set = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == LIGHT_PIXEL:
                light_set.add((c, r))

    return light_set

def get_output_pixel(grid: list[list[str]], image_enhancement: str) -> str:
    binary_str = ""

    for row in grid:
        for ch in row:
            binary_str += '0' if ch == DARK_PIXEL else '1'
    index = int(binary_str, 2)

    return image_enhancement[index]

def get_nine_input_grid(input_image: set[tuple[int, int]], set_ch: str, x: int, y: int) -> list[list[str]]:
    grid = list()

    not_set_ch = LIGHT_PIXEL if set_ch == DARK_PIXEL else DARK_PIXEL

    for dy in [-1, 0, 1]:
        row = list()
        for dx in [-1, 0, 1]:
            row.append(set_ch if (x+dx, y+dy) in input_image else not_set_ch)

        grid.append(row)

    return grid

def get_output_image(input_image: set[tuple[int, int]], set_ch: str, image_enhancement: str) -> set[tuple[int, int]]:
    visited_set = set()
    output_set = set()

    index = 0 if set_ch == LIGHT_PIXEL else 511

    if image_enhancement[index] == LIGHT_PIXEL:
        pixel_flag = DARK_PIXEL
    else:
        pixel_flag = LIGHT_PIXEL

    for px, py in input_image:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                coord = (px+dx, py+dy)

                if coord in visited_set:
                    continue

                visited_set.add(coord)

                pixel = get_output_pixel(get_nine_input_grid(input_image, set_ch, *coord), image_enhancement)

                if pixel == pixel_flag:
                    output_set.add(coord)

    return output_set

def get_reverse_image_enhancement(image_enhancement: str) -> str:
    result = ""

    for ch in image_enhancement:
        if ch == LIGHT_PIXEL:
            result += DARK_PIXEL
        else:
            result += LIGHT_PIXEL

    return result

def part_1():
    image_enhancement, grid = get_input()
    light_pixel_set = convert_grid_to_set(grid)

    result = len(get_output_image(get_output_image(light_pixel_set, LIGHT_PIXEL, image_enhancement), DARK_PIXEL, image_enhancement))

    print(f"{result} pixels are lit in the resulting image")

def part_2():
    image_enhancement, grid = get_input()
    pixel_set = convert_grid_to_set(grid)
    ch_list = [LIGHT_PIXEL, DARK_PIXEL]

    for i in range(50):
        pixel_set = get_output_image(pixel_set, ch_list[i%2], image_enhancement)

    print(f"{len(pixel_set)} pixels are lit in the resulting image")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
