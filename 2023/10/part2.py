from collections import deque
import re


def run(data):
    result = 0
    max_i = 0
    max_j = 0
    for node in data:
        if node[0] > max_i:
            max_i = node[0]
        if node[1] > max_j:
            max_j = node[1]
    node_map = {}
    for node in data:
        if node == (15, 4):
            print(node)
        if data[node] == "S":
            node_map[node] = []
            if node[0] > 0 and (data[(node[0] - 1, node[1])] == "F" or data[(node[0] - 1, node[1])] == "L"):
                node_map[node].append((node[0] - 1, node[1]))
            if node[0] < max_i and (data[(node[0] + 1, node[1])] == "J" or data[(node[0] + 1, node[1])] == "7"):
                node_map[node].append((node[0] + 1, node[1]))
            if node[1] > 0 and (data[(node[0], node[1] - 1)] == "F" or data[(node[0], node[1] - 1)] == "7"):
                node_map[node].append((node[0], node[1] - 1))
            if node[1] < max_j and (data[(node[0], node[1] + 1)] == "J" or data[(node[0], node[1] + 1)] == "L"):
                node_map[node].append((node[0], node[1] + 1))
            # node_map[node] = [(node[0] + i, node[1] + j) for j in [-1, 0, 1] for i in [-1, 0, 1] if
            #                   0 <= node[0] + i <= max_i and 0 <= node[1] + j <= max_j and abs(i) != abs(j) and
            #                   data[(node[0] + i, node[1] + j)] != "."]
            start_node = node
        elif data[node] == "|":
            node_map[node] = [(node[0], node[1] + j) for j in [-1, 1] if 0 <= node[1] + j <= max_j]
        elif data[node] == "-":
            node_map[node] = [(node[0] + i, node[1]) for i in [-1, 1] if 0 <= node[0] + i <= max_i]
        elif data[node] == "L":
            node_map[node] = [(node[0] + i, node[1] + j) for (i, j) in [(0, -1), (1, 0)] if
                              0 <= node[0] + i <= max_i and 0 <= node[1] + j <= max_j]
        elif data[node] == "J":
            node_map[node] = [(node[0] + i, node[1] + j) for (i, j) in [(0, -1), (-1, 0)] if
                              0 <= node[0] + i <= max_i and 0 <= node[1] + j <= max_j]
        elif data[node] == "7":
            node_map[node] = [(node[0] + i, node[1] + j) for (i, j) in [(0, 1), (-1, 0)] if
                              0 <= node[0] + i <= max_i and 0 <= node[1] + j <= max_j]
        elif data[node] == "F":
            node_map[node] = [(node[0] + i, node[1] + j) for (i, j) in [(0, 1), (1, 0)] if
                              0 <= node[0] + i <= max_i and 0 <= node[1] + j <= max_j]

    for start_d in node_map[start_node]:
        current_node = start_node
        visited = deque([current_node])
        next_node = start_d
        while next_node not in visited:
            previous_node = current_node
            current_node = next_node
            visited.append(current_node)
            try:
                next_node = [node for node in node_map[current_node] if node != previous_node][0]
            except IndexError as e:
                print(e)
        if next_node == start_node:
            # print(visited)
            break
    min_i_path = 9999999999
    max_i_path = 0
    min_j_path = 9999999999
    max_j_path = 0

    for node in visited:
        if node[0] > max_i_path:
            max_i_path = node[0]
        if node[0] < min_i_path:
            min_i_path = node[0]
        if node[1] > max_j_path:
            max_j_path = node[1]
        if node[1] < min_j_path:
            min_j_path = node[1]

    possible_in = [node for node in data if
                   min_i_path < node[0] < max_i_path and min_j_path < node[1] < max_i_path and node not in visited]

    inside = []
    for ground in possible_in:
        # intersects = [(i, node[1]) for i in range(min_i_path, ground[0]) if
        #               (i, node[1]) in visited and (data[(i, node[1])] == "|" or )]
        left_ray = ''.join([data[(i, ground[1])] for i in range(min_i_path, ground[0]) if (i, ground[1]) in visited])
        intersects = re.findall(r'(\||L-*7|F-*J)', left_ray)

        if len(intersects) % 2 == 1:
            inside.append(ground)
    # definitely_in = []
    # for ground in possible_in.copy():
    #     left_ray = [data[(i, ground[1])] for i in range(min_i_path, ground[0])]
    #     right_ray = [data[(i, ground[1])] for i in range(ground[0], max_i_path)]
    #     up_ray = [data[(ground[0], j)] for j in range(min_j_path, ground[1])]
    #     down_ray = [data[(ground[0], j)] for j in range(ground[1], max_j_path)]
    #
    #     if "|" not in left_ray or ("7" not in left_ray and "L" not in left_ray) or (
    #             "F" not in left_ray and "J" not in left_ray):
    #         possible_in.remove(ground)
    #     elif "|" not in right_ray or ("7" not in right_ray and "L" not in right_ray) or (
    #             "F" not in right_ray and "J" not in right_ray):
    #         possible_in.remove(ground)
    #     elif "|" not in right_ray or ("7" not in right_ray and "L" not in right_ray) or (
    #             "F" not in right_ray and "J" not in right_ray):
    #         possible_in.remove(ground)
    #
    #
    #     if "|" not in [data[(i, ground[1])] for i in range(min_i_path, ground[0])] or \
    #             "|" not in [data[(i, ground[1])] for i in range(ground[0], max_i_path)] or \
    #             "-" not in [data[(ground[0], j)] for j in range(min_j_path, ground[1])] or \
    #             "-" not in [data[(ground[0], j)] for j in range(ground[1], max_j_path)]:
    #         possible_in.remove(ground)
    return len(inside)
