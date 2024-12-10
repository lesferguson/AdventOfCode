from collections import defaultdict
from queue import LifoQueue
import statistics
closers = {"}": "{", ">": "<", "]": "[", ")": "("}
openers = {"{": "}", "<": ">", "[": "]", "(": ")"}
closer_weight = {"}": 3, ">": 4, "]": 2, ")": 1}
def run(data):
    clean_data = data.copy()
    scores = []
    for line in data:
        corrupted = False
        command = LifoQueue()
        for c in line:
            if c not in closers:
                command.put(c)
            else:
                opener = command.get()
                if opener != closers[c]:
                    clean_data.remove(line)
                    corrupted = True
                    break
        if corrupted:
            continue
        line_score = 0
        while not command.empty():
            o = command.get()
            closer=openers[o]
            line_score*=5
            line_score+=closer_weight[closer]
        scores.append(line_score)






    return statistics.median(scores)
