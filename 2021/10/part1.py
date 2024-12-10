from collections import defaultdict
from queue import LifoQueue
closers = {"}": "{", ">": "<", "]": "[", ")": "("}
closer_values = ["}", ">", "]", ")"]


# def capture_chunk(opener, remaining_line):
#     if remaining_line[0] == closers[opener]:
#         return
#     elif remaining_line[0] in closer_values:
#         raise ValueError
#     else:
#


def run(data):
    errors = 0
    error_weight = {"}": 1197, ">": 25137, "]": 57, ")": 3}
    for line in data:
        # try:
        #     capture_chunk()
        # except ValueError:
        #     errors.append(line)
        command = LifoQueue()
        for c in line:
            if c not in closers:
                command.put(c)
            else:
                opener = command.get()
                if opener != closers[c]:
                    errors+=error_weight[c]
                    break




    return errors
