import json
from collections import deque

# def find_shortest_path(graph, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     if start not in graph:
#         return None
#     shortest = None
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_shortest_path(graph, node, end, path)
#             if newpath:
#                 if not shortest or len(newpath) < len(shortest):
#                     shortest = newpath
#     return shortest

def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist[end]


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

data = [line.strip() for line in open("Day6input.txt", "r").readlines()]
orbits = {}

for orbit in data:
    primary, secondary = orbit.split(")")
    if primary in orbits:
        if secondary in orbits[primary]:
            continue
        else:
            orbits[primary].append(secondary)
    else:
        orbits[primary] = [secondary]

# count = 0
# for key, value in orbits.items():
#     for v in value:
#         path = find_shortest_path(orbits, "COM", v)
#         count += len(path) - 1

count = len(find_shortest_path(orbits, "ZCZ", "SAN")) + len(find_shortest_path(orbits, "ZCZ", "YOU"))

print(count)

