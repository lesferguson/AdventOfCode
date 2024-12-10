import numpy as np
from collections import defaultdict


def run(data):
    tail_history = defaultdict(bool, {(0, 0): True})
    rope = [(0, 0)] * 10
    movements = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    for move in data:
        for step in range(int(move[1])):
            rope[0] = np.add(rope[0], movements[move[0]])
            for knot in range(1, len(rope)):
                diff = np.subtract(rope[knot-1], rope[knot])
                if abs(diff[0]) == 2 and abs(diff[1]) == 1:
                    rope[knot] = np.add(rope[knot], (int(diff[0] / 2), diff[1]))
                elif abs(diff[0]) == 1 and abs(diff[1]) == 2:
                    rope[knot] = np.add(rope[knot], (diff[0], int(diff[1] / 2)))
                else:
                    rope[knot] = np.add(rope[knot], np.fix(diff / 2).astype(int))
                tail_history[tuple(rope[-1])] = True

    return len(tail_history)
