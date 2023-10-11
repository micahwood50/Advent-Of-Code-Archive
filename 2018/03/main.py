import re


FILENAME = "input.txt"


class Claim:
    def __init__(
        self, id: int, left_distance: int, top_distance: int, width: int, height: int
    ):
        self.id = id
        self.left_distance = left_distance
        self.top_distance = top_distance
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"#{self.id} @ {self.left_distance},{self.top_distance}: {self.width}x{self.height}"

    def __repr__(self) -> str:
        return f"Claim({self.id}, {self.left_distance}, {self.top_distance}, {self.width}, {self.height})"


def get_input() -> list[Claim]:
    claim_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            result = re.search(r"#(\d+)+ @ (\d+)+,(\d+)+: (\d+)+x(\d+)", line.strip())
            claim_list.append(Claim(*map(int, result.groups())))

    return claim_list


def part_1():
    claims = get_input()

    square_inch_set = set()
    overlap_set = set()

    for claim in claims:
        for x in range(claim.left_distance, claim.left_distance + claim.width):
            for y in range(claim.top_distance, claim.top_distance + claim.height):
                if (x, y) in square_inch_set:
                    overlap_set.add((x, y))
                else:
                    square_inch_set.add((x, y))

    print(f"Answer is {len(overlap_set)}")


def part_2():
    claims = get_input()

    square_inch_dict = dict()
    overlapped_set = set()
    claim_ids = set()

    for claim in claims:
        claim_ids.add(claim.id)

        for x in range(claim.left_distance, claim.left_distance + claim.width):
            for y in range(claim.top_distance, claim.top_distance + claim.height):
                if (x, y) in square_inch_dict:
                    overlapped_set.add(claim.id)
                    overlapped_set.add(square_inch_dict[(x, y)])
                else:
                    square_inch_dict[(x, y)] = claim.id

    result = next(iter(claim_ids - overlapped_set))
    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
