from copy import deepcopy
import numpy as np
import collections
input_file = "input.txt"
# input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
data = {(i, j, 0, 0): col for j, line in enumerate(open(input_file).readlines()) for i, col in enumerate(line.strip()) }
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]
space = collections.defaultdict(str, data)
old_space = space.copy()
new_space = space.copy()

for n in range(6):
    space = new_space.copy()
    old_space = space.copy()

    # expand space
    for key,v in space.items():
        adjacents = [(key[0]+i, key[1]+j, key[2]+k, key[3]+w) for i in (-1,0,1) for j in (-1,0,1) for k in (-1,0,1) for w in (-1,0,1) if i!=0 or j!=0 or k!=0 or w!=0]
        for coord in adjacents:
            if coord not in old_space and v == "#":
                new_space[coord] = "."

    # check actives
    space = new_space.copy()
    old_space = space.copy()
    for key,v in space.items():
        adjacents = [(key[0]+i, key[1]+j, key[2]+k, key[3]+w) for i in (-1,0,1) for j in (-1,0,1) for k in (-1,0,1) for w in (-1,0,1) if i!=0 or j!=0 or k!=0 or w!=0]
        active_count = 0
        for coord in adjacents:
            if old_space[coord] == "#":
                active_count += 1
        if v == "#" and active_count != 2 and active_count !=3:
            new_space[key] = "."
        elif v != "#" and active_count == 3:
            new_space[key] = "#"


count = 0
for k, v in new_space.items():
    if v == "#":
        count += 1
print(count)

