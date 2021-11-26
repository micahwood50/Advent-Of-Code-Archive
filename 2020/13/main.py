from functools import reduce

FILENAME = "input.txt"

class BusTime:
    def __init__(self, depart_time, services):
        self.time = depart_time
        self.bus_services = services

def get_input() -> BusTime:
    lines = list()

    with open(FILENAME) as f:
        for line in f.readlines():
            lines.append(line.strip())

    IDs_temp = lines[1].split(',')
    IDs = list()

    for i, e in enumerate(IDs_temp):
        if e == 'x':
            continue

        else:
            m = (int(e), i)
            IDs.append(m)

    return BusTime(int(lines[0]), IDs)

def CRT_calculator(A_list, N_list) -> int:
    """Solve the simultaneous congruences using Chinese Remainder Theorem (CRT)

    x = a_1 mod (n_1)
    x = a_2 mod (n_2)
    ...
    x = a_k mod (n_k)

    Args:
        A_list (list[int]): List of a_i from 1 to k
        N_list (list[int]): List of n_i from 1 to k

    Note:
        List arguments need to have same length, and every number in N_list need to be co-prime
        to each other.

    Returns:
        int: Smallest positive integer x such that it satisfies all congruences.
    """
    def get_inverse(c, n):
        r = c%n

        if r == 1 or r == n-1:
            return r

        for i in range(2, n-1):
            if (c*i)%n == 1:
                return i

        raise ArithmeticError("No solution!")

    n = reduce(lambda x, y: x*y, N_list)

    C_list = [n//ni for ni in N_list]

    D_list = [get_inverse(ci, ni) for ci, ni in zip(C_list, N_list)]

    result = reduce(lambda x, y: x+y, [a*c*d for a, c, d in zip(A_list, C_list, D_list)]) % n

    return result

def part_1():
    bus_time = get_input()
    earliest_time = 1_000_000
    bus_id_to_take = -1

    for i, _ in bus_time.bus_services:
        if bus_time.time%i == 0:
            return

        if i - bus_time.time%i < earliest_time:
            earliest_time = i - bus_time.time%i
            bus_id_to_take = i

    print("The ID of the earliest bus you can take to the airport "
        "multiplied by the number of minutes you'll need to wait for that bus is "
        f"{earliest_time * bus_id_to_take}"
    )

def part_2():
    bus_time = get_input()

    A_list = list()
    N_list = list()

    for e, i in bus_time.bus_services:
        A_list.append(-i)
        N_list.append(e)

    result = CRT_calculator(A_list, N_list)

    print("the earliest timestamp such that "
        "all of the listed bus IDs depart at offsets matching their positions in the list is "
        f"{result}"
    )

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
