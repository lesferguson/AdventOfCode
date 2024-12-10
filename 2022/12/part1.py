import math
from collections import defaultdict
import numpy as np
import string
#
# def getPaths(graph, u, visited, path, all_paths):
#     visited[u] = True
#     path.append(u)
#
#     if u == end:
#         all_paths.append(path.copy())
#     else:
#         for i in graph[u]:
#             if not visited[i]:
#                 getPaths(graph, i, visited, path, all_paths)
#
#     path.pop()
#     visited[u] = False
global shortest_path
# Python implementation to find the
# shortest path in the graph using
# dictionaries

# Function to find the shortest
# path between two nodes of a graph
def BFS_SP(graph, start, goal):
    global shortest_path
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    shortest_path = new_path
                    return
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting" \
          "path doesn't exist :(")
    return

def run(data):
    global end
    start = list(data.keys())[list(data.values()).index("S")]
    end = list(data.keys())[list(data.values()).index("E")]
    data[start] = "a"
    data[end] = "z"
    graph = defaultdict(list)

    for point in data:
        data[point] = string.ascii_lowercase.index(data[point])

    for point in data:
        neighbors = {}
        for adj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

            neighbor = tuple(np.add(point, adj))
            if neighbor not in data:
                continue

            if data[neighbor] - data[point] <= 1:
                neighbors[neighbor] = math.dist(neighbor, end)
        graph[point] = [neigh for neigh in dict(sorted(neighbors.items(), key=lambda item: item[1])).keys()]

                #graph[point].append(neighbor)


    path = []
    all_paths = []
    visited = defaultdict(bool)
    # getPaths(graph, start, visited, path, all_paths)
    global shortest_path
    BFS_SP(graph, start, end)
    # shortest_path = min([len(path) for path in all_paths]) - 1
    return len(shortest_path) -1