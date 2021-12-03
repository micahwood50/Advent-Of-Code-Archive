from hashlib import md5

FILENAME = "input.txt"

def get_input() -> str:
    with open(FILENAME) as file:
        input = file.readline().strip()

    return input

def part_1():
    input = get_input()
    secret_key = 0

    while not md5(f"{input}{secret_key}".encode()).hexdigest().startswith(5 * '0'):
        secret_key += 1

    print(f"The secret key is {secret_key}")

def part_2():
    input = get_input()
    secret_key = 0

    while not md5(f"{input}{secret_key}".encode()).hexdigest().startswith(6 * '0'):
        secret_key += 1

    print(f"The secret key is {secret_key}")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
