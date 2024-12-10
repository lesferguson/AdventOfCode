from collections import defaultdict
from functools import cache

class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))

@cache
def cycle(data):
    max_i = 0
    max_j = 0
    for node in data:
        if node[0] > max_i:
            max_i = node[0]
        if node[1] > max_j:
            max_j = node[1]
    for i in range(max_i + 1):
        column = "".join([data[obj] for obj in sorted(data.keys()) if obj[0] == i])
        groups = column.split("#")
        shifted_groups = []
        for n, group in enumerate(groups):
            group = list(group)
            group.sort()
            shifted_groups.append("".join(group))
        shifted_groups.reverse()
        shifted_column = "#".join(shifted_groups)
        for n, place in enumerate(reversed(shifted_column)):
            data[(i, n)] = place
    for j in range(max_j + 1):
        row = "".join([data[obj] for obj in sorted(data.keys()) if obj[1] == j])
        groups = row.split("#")
        shifted_groups = []
        for n, group in enumerate(groups):
            group = list(group)
            group.sort()
            shifted_groups.append("".join(group))
        shifted_groups.reverse()
        shifted_column = "#".join(shifted_groups)
        for n, place in enumerate(reversed(shifted_column)):
            data[(n, j)] = place
        print("test")
    for i in range(max_i + 1):
        column = "".join([data[obj] for obj in sorted(data.keys()) if obj[0] == i])
        groups = column.split("#")
        shifted_groups = []
        for n, group in enumerate(groups):
            group = list(group)
            group.sort()
            group.reverse()
            shifted_groups.append("".join(group))
        shifted_groups.reverse()
        shifted_column = "#".join(shifted_groups)
        for n, place in enumerate(reversed(shifted_column)):
            data[(i, n)] = place
    for j in range(max_j + 1):
        row = "".join([data[obj] for obj in sorted(data.keys()) if obj[1] == j])
        groups = row.split("#")
        shifted_groups = []
        for n, group in enumerate(groups):
            group = list(group)
            group.sort()
            group.reverse()
            shifted_groups.append("".join(group))
        shifted_groups.reverse()
        shifted_column = "#".join(shifted_groups)
        for n, place in enumerate(reversed(shifted_column)):
            data[(n, j)] = place
    return data

def run(data_raw):
    result = 0
    max_j = 0
    data_raw = hashabledict(data_raw)
    for node in data_raw:
        if node[1] > max_j:
            max_j = node[1]
    for _ in range(1000000000):
        data_raw = cycle(data_raw)
    circle_rocks = [rock for rock in data_raw if data_raw[rock] == "O"]
    for rock in circle_rocks:
        result += max_j - rock[1] + 1
    return result
