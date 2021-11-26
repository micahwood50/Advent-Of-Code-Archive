from copy import deepcopy

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'

DIRECTIONS = [
    (-1, 1),  (0, 1),  (1, 1),
    (-1, 0),           (1, 0),
    (-1, -1), (0, -1), (1, -1)
]