from collections import defaultdict
from scipy.spatial.distance import cityblock

def run(data):
    result = 0
    translation_map_x = {}
    translation_map_y = {}
    max_i = 0
    max_j = 0

    for node in data:
        if node[0] > max_i:
            max_i = node[0]
        if node[1] > max_j:
            max_j = node[1]
    expansion = 99 if max_j < 20 else 999999
    blank_columns = 0
    for i in range(max_i+1):
        if all([data[(i, j)] == "." for j in range(max_j+1)]):
            blank_columns += expansion
        else:
            translation_map_x[i] = i + blank_columns
    blank_rows = 0
    for j in range(max_j+1):
        if all([data[(i, j)] == "." for i in range(max_i+1)]):
            blank_rows += expansion
        else:
            translation_map_y[j] = j + blank_rows
    expanded = {}
    for galaxy in data:
        if data[galaxy] == "#":
            expanded[(translation_map_x[galaxy[0]], translation_map_y[galaxy[1]])] = "#"

    node_map = defaultdict(list, {})
    expanded_todel = expanded.copy()
    shortest_distances_total = float(0)
    for src_galaxy in expanded:
        del expanded_todel[src_galaxy]
        for dest_galaxy in expanded_todel:
            node_map[src_galaxy].append((dest_galaxy, cityblock(src_galaxy, dest_galaxy)))
            shortest_distances_total += cityblock(src_galaxy, dest_galaxy)

    return shortest_distances_total
