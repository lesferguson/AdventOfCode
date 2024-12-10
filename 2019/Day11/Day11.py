from intcode import intcode
from collections import deque

orientations = ["N", "E", "S", "W"]
robot = intcode([int(option) for option in open("Day11input.txt", "r").read().split(",")])
graph = {(0, 0): robot.loop(deque([1]))}
direction = robot.loop()
if direction == 0:
    orientation = "W"
    pos = (-1, 0)
else:
    orientation = "E"
    pos = (1, 0)
while True:
    if pos in graph:
        pos_color = graph[pos]
    else:
        pos_color = 0
    color = robot.loop(deque([pos_color]))
    if color == "Halt":
        print(graph)
        break
    graph[pos] = color
    print(pos, color)
    direction = robot.loop()
    if direction == "Halt":
        break
    elif direction == 0:
        orientation = orientations[orientations.index(orientation) - 1]
    else:
        if orientation == "W":
            orientation = "N"
        else:
            orientation = orientations[orientations.index(orientation) + 1]
    if orientation == "N":
        pos = (pos[0], pos[1] + 1)
    elif orientation == "S":
        pos = (pos[0], pos[1] - 1)
    elif orientation == "E":
        pos = (pos[0] + 1, pos[1])
    elif orientation == "W":
        pos = (pos[0] - 1, pos[1])
    else:
        print("bad direction")
        break

grid = [[" " for col in range(100)] for row in range(100)]

for panel in graph:
    if graph[panel] == 0:
        grid[panel[0]+50][panel[1]+50] = " "
    else:
        grid[panel[0] + 50][panel[1] + 50] = "X"

for y in range(len(grid)):
    for x in range(len(grid[0])):
        print(grid[y][x], end="")
    print("")

pass