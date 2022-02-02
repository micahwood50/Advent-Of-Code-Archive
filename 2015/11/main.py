FILENAME = "input.txt"


def password_generator(password: str) -> str:
    password_array = [ord(ch) - ord("a") for ch in password]

    def check_requirement(password_array: list[int]) -> bool:
        # 1st Requirement
        for i in range(len(password_array) - 2):
            if (
                password_array[i] + 1
                == password_array[i + 1]
                == password_array[i + 2] - 1
            ):
                break

        else:
            return False

        # 2nd Requirement
        if (
            ord("i") - ord("a") in password_array
            or ord("l") - ord("a") in password_array
            or ord("o") - ord("a") in password_array
        ):
            return False

        # 3rd Requirement
        i = 0
        first_ch_pair = None
        while i < len(password_array) - 1:
            if password_array[i] == password_array[i + 1]:
                if first_ch_pair is None:
                    first_ch_pair = password_array[i]
                elif password_array[i] != first_ch_pair:
                    return True
                i += 1
            i += 1

        return False

    def get_next_password(password_array: list[int]) -> list[int]:
        i = 1

        while i <= len(password_array) and password_array[-i] == 25:
            password_array[-i] = 0
            i += 1

        if i <= len(password_array):
            password_array[-i] += 1

        return password_array

    def get_password_str(password_array: list[int]) -> str:
        result = ""

        for num in password_array:
            result += chr(num + ord("a"))

        return result

    while True:
        password_array = get_next_password(password_array)
        if check_requirement(password_array):
            yield get_password_str(password_array)


def get_input() -> str:
    with open(FILENAME) as file:
        password = file.readline().strip()

    return password


def part_1():
    password = get_input()

    gen = password_generator(password)

    print(f"Santa's next password is {next(gen)}")


def part_2():
    password = get_input()

    gen = password_generator(password)

    next(gen)

    print(f"Santa's next new password is {next(gen)}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
