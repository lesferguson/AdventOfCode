from collections import defaultdict
import re


def run(data):
    data_split = data.split("\n")
    yard = defaultdict(list, {})
    for _ in range(len(data_split)):
        row = data_split.pop(0)
        if row.startswith(" 1"):
            num_of_stacks = int(row[-1])
            data_split.pop(0)
            break
        else:
            for i in range(int(len(row) / 4) + 1):
                crate = row[i * 4 + 1]
                if crate != " ":
                    yard[i + 1].insert(0, crate)

    for command in data_split:
        command = [int(param) for param in re.findall(r"(\d+)", command)]

        move_cache = []
        for n in range(command[0]):
            move_cache.append(yard[command[1]].pop(-1))
        for i in range(len(move_cache)):
            yard[command[2]].append(move_cache.pop(-1))

    tops = ""
    for stack_num in range(num_of_stacks):
        stack_num += 1
        tops += yard[stack_num][-1]
    return tops
