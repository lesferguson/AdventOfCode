from collections import deque
from math import floor

layers = []
zero_counts = []
encoded_data = deque([digit for digit in open("Day8input.txt", "r").read()])
while encoded_data:
    layer = [[], [], [], [], [], []]

    for i in range(0, 150):
        d = encoded_data.popleft()
        layer[floor(i / 25)].append(d)
    layers.append(layer)


grid = [[2 for col in range(25)] for row in range(6)]

for x in range(len(layers[0][0])):
    for y in range(len(layers[0])):
        for z in range(len(layers)):
            color = layers[z][y][x]
            if color == "2":
                continue
            elif color == "1":
                grid[y][x] = "."
                break
            else:
                grid[y][x] = " "
                break


for y in range(len(grid)):
    for x in range(len(grid[0])):
        print(grid[y][x], end="")
    print("")