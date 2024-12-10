from intcode import intcode

ascii_code = intcode([int(option) for option in open("Day17input.txt", "r").read().split(",")])

layout = {}
i, j = 0, 0

while True:
    loc = ascii_code.loop()
    if loc == "Halt":
        break

    elif loc == 10:
        j += 1
        i = 0

    else:
        layout[(i, j)] = chr(loc)
        i += 1

alignment_params = []
grid = [[" " for col in range(77)] for row in range(41)]
for panel in layout:
    grid[panel[1]][panel[0]] = layout[panel]
    # if 0 < panel[0] < 76 and 0 < panel[1] < 40 and layout[panel] == "#" and layout[(panel[0] + 1, panel[1])] == "#" and \
    #         layout[(panel[0] - 1, panel[1])] == "#" and layout[(panel[0], panel[1] + 1)] == "#" and layout[(panel[0], panel[1] - 1)] == "#":
    #     print(panel)
    #     alignment_params.append(panel[0] * panel[1])
    #     grid[panel[1]][panel[0]] = "O"

for y in range(len(grid)):
    for x in range(len(grid[0])):
        print(grid[y][x], end="")
    print("")


# R, 6, L, 10, R, 8, R, 8, R, 12, L, 8, L, 10, R, 6, L, 10, R, 12, R, 8, R, 12, L, 10, R, 6, L, 10, R, 12, L, 8, L, 10, R, 12, L, 10, R, 6, L,10, R, 6
