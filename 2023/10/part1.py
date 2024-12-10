from collections import deque


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
        if data[node] == "S":
            node_map[node] = [(node[0] + i, node[1] + j) for j in [-1, 0, 1] for i in [-1, 0, 1] if
                              0 <= node[0] + i <= max_i and 0 <= node[1] + j <= max_j and abs(i) != abs(j) and
                              data[(node[0] + i, node[1] + j)] != "."]
            start_node = node
        elif data[node] == "|":
            node_map[node] = [(node[0], node[1] + j) for j in [-1, 1] if 0 <= node[1] + j <= max_j]
        elif data[node] == "-":
            node_map[node] = [(node[0] + i, node[1]) for i in [-1, 1] if 0 <= node[1] + i <= max_j]
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
            next_node = [node for node in node_map[current_node] if node != previous_node][0]
        if next_node == start_node:
            # print(visited)
            break

    return int(len(visited)/2)
