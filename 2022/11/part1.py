import operator
import math

def operation(item, function):
    ops = {"+": operator.add, "*": operator.mul}
    if function[0] == "old":
        p1 = item
    else:
        p1 = int(function[0])
    if function[2] == "old":
        p2 = item
    else:
        p2 = int(function[2])
    return ops[function[1]](p1, p2)

def run(data):

    monkeys_raw = data.split("\n\n")
    monkeys = []
    for monkey_raw in monkeys_raw:
        monkey = {}
        description = monkey_raw.split("\n")
        # monkey_id = description[0].split()[1][:-1]
        monkey["items"] = [int(item.strip()) for item in description[1].split(":")[1].split(",")]
        monkey["operation"] = [x for x in description[2].split("=")[1].strip().split(" ")]
        monkey["test"] = int(description[3].split()[3])
        monkey["true"] = int(description[4].split()[5])
        monkey["false"] = int(description[5].split()[5])

        monkeys.append(monkey)
    inspected = [0] * len(monkeys)
    for _ in range(20):
        for i, monkey in enumerate(monkeys):

            for _ in range(len(monkey["items"])):
                item = monkey["items"].pop(0)
                item = operation(item, monkey["operation"])
                item = int(item / 3)
                if item % monkey["test"] == 0:
                    monkeys[monkey["true"]]["items"].append(item)
                else:
                    monkeys[monkey["false"]]["items"].append(item)
                inspected[i] += 1


    return math.prod(sorted(inspected, reverse=True)[0:2])