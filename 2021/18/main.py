FILENAME = "input.txt"


class SnailfishNumber:
    ### WARNING: __add__ type of methods are DESTRUCTIVE!
    def __init__(self, list_num, depth: int = 0, do_reduce: bool = True):
        assert len(list_num) == 2

        if type(list_num[0]) is int:
            self.left = list_num[0]
        elif type(list_num[0]) is SnailfishNumber:
            list_num[0].increase_depth()
            self.left = list_num[0]
        elif type(list_num[0]) is list:
            self.left = SnailfishNumber(list_num[0], depth + 1)
        else:
            raise ValueError()

        if type(list_num[1]) is int:
            self.right = list_num[1]
        elif type(list_num[1]) is SnailfishNumber:
            list_num[1].increase_depth()
            self.right = list_num[1]
        elif type(list_num[1]) is list:
            self.right = SnailfishNumber(list_num[1], depth + 1)
        else:
            raise ValueError()

        self.depth = depth

        if do_reduce:
            self.reduce()

    def __add__(self, other):
        assert isinstance(other, SnailfishNumber)

        result = SnailfishNumber([self, other])
        result.reduce()

        return result

    def __radd__(self, other):
        if isinstance(other, int) and other == 0:
            return self

        assert isinstance(other, SnailfishNumber)

        result = SnailfishNumber([other, self])
        result.reduce()

        return result

    def __str__(self) -> str:
        return f"[{str(self.left)}, {str(self.right)}]"

    def __repr__(self) -> str:
        return f"SnailfishNumber([{str(self.left)}, {str(self.right)}])"

    def increase_depth(self):
        self.depth += 1
        if type(self.left) is SnailfishNumber:
            self.left.increase_depth()

        if type(self.right) is SnailfishNumber:
            self.right.increase_depth()

    def reduce(self):
        S_list = list()

        def reduce_helper(
            num, depth=self.depth, parent_num=None, parent_num_index=None
        ):
            left_num = num.left
            right_num = num.right

            if type(left_num) is int:
                S_list.append((left_num, depth, num, 0, parent_num, parent_num_index))
            else:
                reduce_helper(left_num, depth + 1, num, 0)

            if type(right_num) is int:
                S_list.append((right_num, depth, num, 1, parent_num, parent_num_index))
            else:
                reduce_helper(right_num, depth + 1, num, 1)

        reduce_helper(self)

        while True:
            for index, [
                regular_num,
                depth,
                snail_num,
                snail_index,
                parent_snail,
                parent_index,
            ] in enumerate(S_list):
                if depth >= 4:
                    assert type(snail_num.left) is int
                    assert type(snail_num.right) is int
                    # explode here
                    if index > 0:
                        _, _, snail_num, snail_index, *_ = S_list[index - 1]
                        if snail_index == 0:
                            snail_num.left += regular_num
                        else:
                            snail_num.right += regular_num

                    if index < len(S_list) - 2:
                        regular_num, *_ = S_list[index + 1]
                        _, _, snail_num, snail_index, *_ = S_list[index + 2]
                        if snail_index == 0:
                            snail_num.left += regular_num
                        else:
                            snail_num.right += regular_num

                    if parent_index == 0:
                        parent_snail.left = 0
                    else:
                        parent_snail.right = 0

                    break
            else:
                # No explosion occur; check for split

                for index, [
                    regular_num,
                    depth,
                    snail_num,
                    snail_index,
                    parent_snail,
                    parent_index,
                ] in enumerate(S_list):
                    if regular_num > 9:
                        # split here
                        if regular_num % 2 == 0:
                            new_left = regular_num // 2
                            new_right = regular_num // 2
                        else:
                            new_left = regular_num // 2
                            new_right = regular_num // 2 + 1

                        new_pair = SnailfishNumber(
                            [new_left, new_right], depth + 1, False
                        )

                        if snail_index == 0:
                            snail_num.left = new_pair
                        else:
                            snail_num.right = new_pair

                        break

                else:
                    # No action occur
                    break

            # Reduction action was taken, so prepare the next iteration
            S_list = list()
            reduce_helper(self)

    def calculate_magnitude(self) -> int:
        left_num = (
            self.left if type(self.left) is int else self.left.calculate_magnitude()
        )
        right_num = (
            self.right if type(self.right) is int else self.right.calculate_magnitude()
        )

        return 3 * left_num + 2 * right_num


def get_input() -> list[SnailfishNumber]:
    snailfish_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            snailfish_list.append(SnailfishNumber(eval(line.strip())))

    return snailfish_list


def get_input_str() -> list[str]:
    snailfish_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            snailfish_list.append(line.strip())

    return snailfish_list


def part_1():
    snailfish_list = get_input()

    print(
        f"The magnitude of the final sum is {sum(snailfish_list).calculate_magnitude()}"
    )


def part_2():
    snailfish_list = get_input_str()
    result = 0

    for i, str_i in enumerate(snailfish_list):
        for j, str_j in enumerate(snailfish_list):
            if i == j:
                continue

            snail_i = SnailfishNumber(eval(str_i))
            snail_j = SnailfishNumber(eval(str_j))

            result = max(result, (snail_i + snail_j).calculate_magnitude())

    print(
        f"The largest magnitude of any sum of two different snailfish numbers is {result}"
    )


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
