FILENAME = "input.txt"
OPEN = '.'
TREE = '#'

def get_input() -> list[str]:
    """ Read the file and generate a grid map (list of strings)
    """
    strMap = list()

    with open(FILENAME) as f:
        for line in f.readlines():
           strMap.append(line.strip())

    return strMap

def count_collision(strMap: list[str], right: int, down: int) -> int:
    """ Read the map and count how many tree would be encountered if someone start from the top left corner    
    """
    mapWidth = len(strMap[0]) # All lines are assumed to have same width
    xCoord, yCoord = right % mapWidth, down
    count = 0

    while yCoord < len(strMap):
        if strMap[yCoord][xCoord] == TREE:
            count += 1

        xCoord = (xCoord + right) % mapWidth
        yCoord += down

    return count

def part_1():
    strMap = get_input()

    answer = count_collision(strMap, 3, 1)

    print(f"{answer} trees will be encountered")

def part_2():
    strMap = get_input()
    
    a1 = count_collision(strMap, 1, 1)
    a2 = count_collision(strMap, 3, 1)
    a3 = count_collision(strMap, 5, 1)
    a4 = count_collision(strMap, 7, 1)
    a5 = count_collision(strMap, 1, 2)

    answer = a1 * a2 * a3 * a4 * a5

    print(f"The result of multiplication of the number of trees encountered on each of the listed slopes is {answer}")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
