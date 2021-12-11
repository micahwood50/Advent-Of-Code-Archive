import json
from pprint import pprint

FILENAME = "input.txt"

def flatten_json(json_obj, ignore_red = False):
    result = dict()

    def flatten(obj, name = ""):
        if type(obj) is dict:
            if ignore_red:
                for key in obj:
                    if obj[key] == "red":
                        return

            for key in obj:
                flatten(obj[key], f"{name}{key}_")

        elif type(obj) is list:
            for i, val in enumerate(obj):
                flatten(val, f"{name}{i}_")

        else:
            result[name[:-1]] = obj

    flatten(json_obj)
    return result

def get_input() -> dict:
    with open(FILENAME) as file:
        json_object = json.load(file)

    return json_object

def part_1():
    json_object = get_input()
    result = 0

    json_object = flatten_json(json_object)

    for val in json_object.values():
        if type(val) is int:
            result += val

    print(f"The sum of all numbers in the document is {result}")

def part_2():
    json_object = get_input()
    result = 0

    json_object = flatten_json(json_object, True)

    for val in json_object.values():
        if type(val) is int:
            result += val

    print(f"The right sum of all numbers in the document is {result}")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
