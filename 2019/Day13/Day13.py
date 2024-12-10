from intcode import  intcode
from collections import deque


game = intcode([int(option) for option in open("Day13input.txt", "r").read().split(",")])
grid =  [[0 for col in range(42)] for row in range(25)]
x, y, tile, joystick, ball_x, paddle_x = None, None, None, None, None, None
tile_map = [" ", "+", "B", "_", "O"]
joystick = 0

while True:

    x = game.loop(deque([joystick]))
    y = game.loop()
    tile = game.loop()
    if x == -1 and y == 0:
        if ball_x < paddle_x:
            joystick = -1
        elif ball_x > paddle_x:
            joystick = 1
        else:
            joystick = 0
        score = tile
        print(score)
    elif x != "Halt" and y != "Halt" and tile != "Halt":
        grid[y][x] = tile_map[tile]
        if tile == 4:
            ball_x = x
        elif tile == 3:
            paddle_x = x
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                print(grid[y][x], end="")
            print("")
        if ball_x and paddle_x:
            if ball_x < paddle_x:
                joystick = -1
            elif ball_x > paddle_x:
                joystick = 1
            else:
                joystick = 0
    else:
        break

for y in range(len(grid)):
    for x in range(len(grid[0])):
        print(grid[y][x], end="")
    print("")

print(score)