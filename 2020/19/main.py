from typing import Union
import re

FILENAME = "input.txt"

def get_input() -> tuple[dict[int, Union[str, list[list[int]]]], list[str]]:
    rules = dict()
    messages = list()

    isReadingRule = True

    with open(FILENAME) as f:
        for line in f.readlines():
            line = line.strip()

            if not line:
                isReadingRule = False
                continue

            if isReadingRule:
                lside, rside = line.split(": ")

                if '"' in rside:
                    rules[int(lside)] = rside.strip()[1]

                else:
                    rules[int(lside)] = \
                        [list(map(int, v.split())) for v in rside.split(" | ")]

            else:
                messages.append(line)

    return rules, messages

def generate_grammar(rules, curr_num: int = 0, depth: int = 0) -> str:
    if depth > 50:
        return ""

    if type(rules[curr_num]) is str:
        return rules[curr_num]

    result = "(("
    sub_results = list()

    for L in rules[curr_num]:
        this_rule = ""
        for num in L:
            this_rule += generate_grammar(rules, num, depth + 1)

        sub_results.append(this_rule)

    result += ")|(".join(sub_results) + "))"

    return result

def part_1():
    rules, messages = get_input()
    count = 0

    grammar_str = '^' + generate_grammar(rules) + '$'
    grammar = re.compile(grammar_str)

    for message in messages:
        if grammar.match(message):
            count += 1

    print(f"{count} messages completely match rule 0.")

def part_2():
    rules, messages = get_input()

    # Fix the rules manually as per the requirement
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    count = 0

    grammar_str = '^' + generate_grammar(rules) + '$'
    grammar = re.compile(grammar_str)

    for message in messages:
        if grammar.match(message):
            count += 1

    print(f"{count} messages completely match rule 0.")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
