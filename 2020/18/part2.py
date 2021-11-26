# Evaluate the expression that is guaranteed to have no parentheses
def aoc_raw_eval(expression: str) -> int:
    S = expression.split('*')
    result = 1

    for s in S:
        sm = map(int, s.split('+'))
        ss = sum(sm)
        result *= ss

    return result

def aoc_eval(expression: str) -> int:
    new_expression = ""

    i = 0

    while i < len(expression):
        ch = expression[i]

        if ch == '(':
            lp = 1
            i += 1

            ri = i

            while lp > 0:
                if expression[ri] == '(':
                    lp += 1

                elif expression[ri] == ')':
                    lp -= 1

                ri += 1

            new_expression += str(aoc_eval(expression[i:ri-1]))
            i = ri-1

        else:
            new_expression += ch

        i += 1

    return aoc_raw_eval(new_expression)


def run_solution(expressions: list[str]):
    results_sum = 0

    stack = []

    for expression in expressions:
        results_sum += aoc_eval(expression)

    print(f"The sum of results is {results_sum}")
