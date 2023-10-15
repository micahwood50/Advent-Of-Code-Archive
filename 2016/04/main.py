from collections import Counter
import re


FILENAME = "input.txt"


class Room:
    def __init__(self, name: str, sectorID: int, checksum: str) -> None:
        self.name = name
        self.sectorID = sectorID
        self.checksum = checksum

        c = Counter(name)
        del c["-"]
        c = list(c.items())
        c.sort(key=lambda t: (-t[1], t[0]))

        self.is_real = "".join(t[0] for t in c).startswith(checksum)

    def decrypt(self):
        shift_times = self.sectorID % 26
        result = ""

        for ch in self.name:
            if ch == "-":
                result += " "
            else:
                alphabet_index = (ord(ch) - ord("a") + shift_times) % 26
                decrypted_ch = chr(alphabet_index + ord("a"))

                result += decrypted_ch

        return result


def get_input() -> list[Room]:
    room_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            result = re.search(r"([a-z-]+)(\d+)\[([a-z]+)\]", line)
            name, sectorID, checksum = result.groups()
            sectorID = int(sectorID)

            room_list.append(Room(name, sectorID, checksum))

    return room_list


def part_1():
    rooms = get_input()
    result = 0

    for room in rooms:
        if room.is_real:
            result += room.sectorID

    print(f"Answer is {result}")


def part_2():
    rooms = get_input()

    for room in rooms:
        if room.is_real:
            real_name = room.decrypt()
            if "north" in real_name:
                print(f"Answer is {room.sectorID}")
    return


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
