FILENAME = "input.txt"


class Expression:
    def __init__(self, expression_str: str):
        expression_list = expression_str.split()

        if len(expression_list) == 1:
            self.parse_expression(None, None, expression_list[0])

        elif len(expression_list) == 2:
            self.parse_expression(None, *expression_list)

        else:
            self.parse_expression(*expression_list)

    def parse_expression(
        self, left_literal: str | None, operator: str | None, right_literal: str
    ):
        try:
            self._left_literal = int(left_literal)
        except:
            self._left_literal = left_literal

        try:
            self._right_literal = int(right_literal)
        except:
            self._right_literal = right_literal

        self._operator = operator

    def eval(self, table) -> int:
        if self._left_literal is not None:
            if isinstance(self._left_literal, int):
                left = self._left_literal
            else:
                left = table.get_value(self._left_literal)

        if isinstance(self._right_literal, int):
            right = self._right_literal
        else:
            right = table.get_value(self._right_literal)

        if self._operator == "AND":
            return left & right

        elif self._operator == "OR":
            return left | right

        elif self._operator == "NOT":
            return 2**16 - right - 1

        elif self._operator == "LSHIFT":
            return left << right

        elif self._operator == "RSHIFT":
            return left >> right

        elif self._operator is None:
            return right

        else:
            raise ValueError(f"Unknown operator: {self._operator}")


class Table:
    def __init__(self):
        self._variable_dict = dict()

    def process_expression(self, variable: str, expression: Expression):
        self._variable_dict[variable] = expression

    def get_value(self, variable: str) -> int:
        result = self._variable_dict[variable].eval(self)

        self._variable_dict[variable] = Expression(str(result))

        return result


def get_input() -> Table:
    table = Table()

    with open(FILENAME) as file:
        for line in file.readlines():
            lhs, rhs = line.strip().split(" -> ")
            table.process_expression(rhs, Expression(lhs))

    return table


def part_1():
    table = get_input()
    WIRE_VAR = "a"

    result = table.get_value(WIRE_VAR)

    print(f"Signal {result} is ultimately provided to wire {WIRE_VAR}")


def part_2():
    table1 = get_input()
    table2 = get_input()
    WIRE_VAR = "a"

    a_signal = table1.get_value(WIRE_VAR)
    table2.process_expression("b", Expression(str(a_signal)))
    result = table2.get_value(WIRE_VAR)

    print(f"Signal {result} is ultimately provided to wire {WIRE_VAR}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
