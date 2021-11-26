# Evaluate the expression that is guaranteed to have no parentheses
def aoc_raw_eval(expression: str) -> int:
    num_str = ""
    last_opr = '+'
    result = 0

    for ch in expression:
        if ch.isdigit():
            num_str += ch

        elif ch in "+*":
            if last_opr == '+':
                result += int(num_str)
            else:
                result *= int(num_str)

            last_opr = ch
            num_str = ""

    if last_opr == '+':
        result += int(num_str)
    else:
        result *= int(num_str)

    return result

def aoc_eval(expression: str) -> int:
    if '(' not in expression:
        return aoc_raw_eval(expression)

    num_str = ""
    last_opr = '+'
    result = 0

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

            num_str = str(aoc_eval(expression[i:ri-1]))

            i = ri

        if ch.isdigit():
            num_str += ch

        elif ch in "+*":
            if last_opr == '+':
                result += int(num_str)
            else:
                result *= int(num_str)

            last_opr = ch
            num_str = ""

        i += 1

    if last_opr == '+':
        result += int(num_str)
    else:
        result *= int(num_str)

    return result

def run_solution(expressions: list[str]):
    results_sum = 0

    stack = []

    for expression in expressions:
        results_sum += aoc_eval(expression)

    print(f"The sum of results is {results_sum}")
