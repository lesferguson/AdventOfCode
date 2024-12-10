from copy import deepcopy
from collections import defaultdict
import numpy as np
input_file = "input.txt"
# input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
data = [line.strip() for line in open(input_file).readlines()]
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

# False = White/Not Flipped, True = Black/Flipped
# Key = Coordinates in skewed plane
floor = defaultdict(bool, {(0, 0): False})
# data =['nwwswee']
for line in data:
    n = 0
    target = (0, 0)
    while n < len(line):
        if line[n] == "e":
            target = (target[0] + 1, target[1])
            n += 1
        elif line[n] == "w":
            target = (target[0] - 1, target[1])
            n += 1
        elif line[n] == "n":
            if line[n+1] == "e":
                target = (target[0], target[1] + 1)
                n += 2
            elif line[n+1] == "w":
                target = (target[0] - 1, target[1] + 1)
                n += 2
        elif line[n] == "s":
            if line[n+1] == "e":
                target = (target[0] + 1, target[1] - 1)
                n += 2
            elif line[n+1] == "w":
                target = (target[0], target[1] - 1)
                n += 2
    if floor[target]:
        floor[target] = False
    else:
        floor[target] = True


new_floor = deepcopy(floor)

for i in range(100):
    # expand boundaries
    for tile in list(floor.keys()):
        for offset in [(0,1 ), (0,-1 ), (1, 0 ), (-1,0 ), (-1, 1 ), (1, -1 )]:
            if floor[tuple(np.add(tile, offset))]:
                pass


    new_floor = deepcopy(floor)

    # check adjacents
    for tile in list(floor.keys()):
        if floor[tile]:
            # count adjacent blacks
            adj_count = 0
            for offset in [(0,1 ), (0,-1 ), (1, 0 ), (-1,0 ), (-1, 1 ), (1, -1 )]:
                if floor[tuple(np.add(tile, offset))]:
                    adj_count += 1
            if adj_count == 0 or adj_count > 2:
                new_floor[tile] = False
        else:
            adj_count = 0
            for offset in [(0,1 ), (0,-1 ), (1, 0 ), (-1,0 ), (-1, 1 ), (1, -1 )]:
                if floor[tuple(np.add(tile, offset))]:
                    adj_count += 1
            if adj_count == 2:
                new_floor[tile] = True







    black_count = 0
    for tile, state in new_floor.items():
        if state:
            black_count += 1

    print("Day {}: {}".format(i+1, black_count))

    floor = new_floor