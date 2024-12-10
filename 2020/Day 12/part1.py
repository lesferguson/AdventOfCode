from copy import deepcopy
import collections
import numpy
input_file = "input.txt"
input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
data = [(line[0], int(line[1:])) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip()] for line in open(input_file).readlines()]
print(data)
ordinal_dirs = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
rel_dirs = {"L": 1, "R": -1}
coords = (0, 0)
heading = 0

for move in data:
    direction = move[0]
    distance = move[1]
    if direction in ordinal_dirs:
        coords = numpy.add(coords, numpy.multiply(distance, ordinal_dirs[direction]))


    elif direction in rel_dirs:
        heading += rel_dirs[direction] * distance

    elif direction == "F":
        coords = numpy.add(coords, (int(distance*numpy.cos(numpy.deg2rad(heading))), int(distance*numpy.sin(numpy.deg2rad(heading)))))
    print(move, heading, coords)
print(abs(coords[0]) + abs(coords[1]))