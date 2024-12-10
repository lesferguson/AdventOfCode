from copy import deepcopy
import numpy as np
import collections
input_file = "input.txt"
# input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
data = {(i, j, 0): col for j, line in enumerate(open(input_file).readlines()) for i, col in enumerate(line.strip()) }
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
        adjacents = [(key[0]+i, key[1]+j, key[2]+k) for i in (-1,0,1) for j in (-1,0,1) for k in (-1,0,1) if i!=0 or j!=0 or k!=0]
        for coord in adjacents:
            if coord not in old_space and v == "#":
                new_space[coord] = "."

    # check actives
    space = new_space.copy()
    old_space = space.copy()
    for key,v in space.items():
        adjacents = [(key[0]+i, key[1]+j, key[2]+k) for i in (-1,0,1) for j in (-1,0,1) for k in (-1,0,1) if i!=0 or j!=0 or k!=0]
        active_count = 0
        for coord in adjacents:
            if old_space[coord] == "#":
                active_count += 1
        if v == "#" and active_count != 2 and active_count !=3:
            new_space[key] = "."
        elif v != "#" and active_count == 3:
            new_space[key] = "#"

smallest_i = 0
smallest_j = 0
biggest_i = 0
biggest_j = 0
smallest_k = 0
biggest_k = 0
for k,v in new_space.items():
    if v == "#":
        if k[0] < smallest_i:
            smallest_i = k[0]
        if k[1] < smallest_j:
            smallest_j = k[1]
        if k[0] > biggest_i:
            biggest_i = k[0]
        if k[1] > biggest_j:
            biggest_j = k[1]
        if k[2] < smallest_k:
            smallest_k = k[2]
        if k[2] > biggest_k:
            biggest_k = k[2]

count = 0
for k, v in new_space.items():
    if v == "#":
        count += 1
print(count)

# for z in range(smallest_k, biggest_k+1):
#     plane = np.full((biggest_i - smallest_i+1, biggest_j - smallest_j+1), ".")
#     for k, v in new_space.items():
#         if v == "#" and k[2] == z:
#             rel_coord = np.subtract(k, (smallest_i,smallest_j,0))
#             plane[rel_coord[1]][rel_coord[0]] = v
#     print(z)
#     print(plane)