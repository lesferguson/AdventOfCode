import itertools
from copy import deepcopy
test_field = [
    [1,1,1,1,1,1],
    [1,0,1,0,0,1],
    [1,1,1,1,0,1],
    [1,0,0,1,1,1],
    [1,1,1,1,1,1],
]
connection_directions = {
    'left': ["┓", "┛", "┫", "┳", "┻", "╋", "━"],
    'right': ["┏", "┗", "┣", "┳", "┻", "╋", "━"],
    'up': ["┃", "┗", "┛", "┣", "┫", "┻", "╋"],
    'down': ["┃", "┏", "┓", "┣", "┫", "┳", "╋"]
}

field_dirs = deepcopy(test_field)

for i, row in enumerate(field_dirs):
    for j, col in enumerate(row):
        if field_dirs[i][j] == 0:
            field_dirs[i][j] = " "
            continue
        directions = []
        if i > 0 and field_dirs[i-1][j] == 1:
            directions.append("up")
        if j > 0 and field_dirs[i][j-1] == 1:
            directions.append("left")
        if i < len(field_dirs)-1 and field_dirs[i+1][j] == 1:
            directions.append("down")
        if j < len(field_dirs[i])-1 and field_dirs[i][j+1] == 1:
            directions.append("right")
        # if j == 0 and i == 0:
        #     directions = ["left", "up"]
        # if j == 0 and i == len(field_dirs)-1:
        #     directions = ["left", "down"]
        # if j == len(field_dirs[i])-1 and i == 0:
        #     directions = ["right", "up"]
        # if j == len(field_dirs[i])-1 and i == len(field_dirs)-1:
        #     directions = ["right", "down"]
        if not directions:
            continue
        missing_dir = ["left", "right", "up", "down"]
        missing_dir.remove(directions[0])
        wall = set(connection_directions[directions[0]])

        for n in range(1, len(directions)):
            missing_dir.remove(directions[n])
            wall = wall.intersection(set(connection_directions[directions[n]]))
        for direction in missing_dir:
            wall = wall - set(connection_directions[direction])
        field_dirs[i][j] = wall
print(field_dirs)



pieces = ["┃", "┏", "┓", "┗", "┛", "┣", "┫", "┳", "┻", "╋", "━"]



directions = ["left", "right", "up", "down"]

for r in range(2, 4):
    for combo in itertools.combinations(directions, r):
        missing_dir = ["left", "right", "up", "down"]
        missing_dir.remove(combo[0])
        wall = set(connection_directions[combo[0]])

        for n in range(1, len(combo)):
            missing_dir.remove(combo[n])
            wall = wall.intersection(set(connection_directions[combo[n]]))
        for direction in missing_dir:
            wall = wall - set(connection_directions[direction])
        print(combo, wall, missing_dir)
