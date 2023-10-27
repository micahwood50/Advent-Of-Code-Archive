from hashlib import md5


FILENAME = "input.txt"


def get_input() -> str:
    with open(FILENAME) as file:
        return file.readline().strip()


def part_1():
    doorID = get_input()
    password = list()

    index = 0

    while len(password) < 8:
        code_to_hash = doorID + str(index)
        this_hashed = md5(code_to_hash.encode()).hexdigest()

        if this_hashed.startswith("00000"):
            password.append(this_hashed[5])

        index += 1

    print(f"Answer is {''.join(password)}")


def part_2():
    doorID = get_input()
    password = [None] * 8
    index = 0

    while None in password:
        code_to_hash = doorID + str(index)
        this_hashed = md5(code_to_hash.encode("utf-8")).hexdigest()

        if this_hashed.startswith("00000"):
            place = this_hashed[5]
            code_ch = this_hashed[6]
            if "0" <= place < "8":
                int_place = int(place)
                if password[int_place] is None:
                    password[int_place] = code_ch

        index += 1

    print(f"Answer is {''.join(password)}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
