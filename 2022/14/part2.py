from collections import defaultdict
import numpy as np

def run(data):
    caves = defaultdict(lambda: ".")

    for structure in data:
        points = []
        for point in structure.split(" -> "):
            points.append(tuple([int(value) for value in point.split(",")]))
        for i in range(1, len(points)):
            caves[points[i]] = "#"
            caves[points[i-1]] = "#"
            if points[i - 1][0] == points[i][0]:
                for n in range(points[i - 1][1], points[i][1],
                               int(((points[i][1] - points[i - 1][1]) / abs(points[i][1] - points[i - 1][1])))):
                    caves[(points[i][0], n)] = "#"
            elif points[i - 1][1] == points[i][1]:
                for n in range(points[i - 1][0], points[i][0],
                               int(((points[i][0] - points[i - 1][0]) / abs(points[i][0] - points[i - 1][0])))):
                    caves[(n, points[i][1])] = "#"
    max_y = max(coord[1] for coord in caves) + 2
    for n in range(1000):
        caves[(n, max_y)] = "#"
    previous_path = [None]
    current_path = []
    sand_count = -1
    while previous_path != current_path:
        sand_count +=1
        previous_path = current_path
        current_path = [(500, 0)]
        sand = (500, 0)
        while True:
            if caves[tuple(np.add(sand, (0, 1)))] == ".":
                sand = tuple(np.add(sand, (0, 1)))
                current_path.append(sand)
                continue
            elif caves[tuple(np.add(sand, (-1, 1)))] == ".":
                sand = tuple(np.add(sand, (-1, 1)))
                current_path.append(sand)
                continue
            elif caves[tuple(np.add(sand, (1, 1)))] == ".":
                sand = tuple(np.add(sand, (1, 1)))
                current_path.append(sand)
                continue
            else:
                caves[sand] = "o"
                break




    max_x = max([coord[0] for coord in caves])+1


    caves_list = [["."]*max_x for _ in range(max_y+1)]

    for coord in caves:
        if coord[1] <= max_y:
            caves_list[coord[1]][coord[0]] = caves[coord]
    print()
    for line in caves_list:
        print("".join(line))
    return sand_count
