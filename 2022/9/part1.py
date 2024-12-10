import numpy as np
from collections import defaultdict

def run(data):

    tail_history = defaultdict(bool, {(0, 0): True})
    h_loc = (0, 0)
    t_loc = (0, 0)
    movements = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    for move in data:
        for step in range(int(move[1])):
            h_loc = np.add(h_loc, movements[move[0]])
            diff = np.subtract(h_loc, t_loc)
            if abs(diff[0]) == 2 and abs(diff[1]) == 1:
                t_loc = np.add(t_loc, (int(diff[0]/2), diff[1]))
            elif abs(diff[0]) == 1 and abs(diff[1]) == 2:
                t_loc = np.add(t_loc, (diff[0], int(diff[1]/2)))
            else:
                t_loc = np.add(t_loc, np.fix(diff/2).astype(int))
            tail_history[tuple(t_loc)] = True



    return len(tail_history)