from collections import defaultdict

def run(data):
    result = 0
    max_i = 0
    max_j = 0
    for node in data:
        if node[0] > max_i:
            max_i = node[0]
        if node[1] > max_j:
            max_j = node[1]

    for i in range(max_i+1):
        column = "".join([data[obj] for obj in sorted(data.keys()) if obj[0] == i])
        groups = column.split("#")
        shifted_groups = []
        for n, group in enumerate(groups):
            group = list(group)
            group.sort()
            shifted_groups.append("".join(group))
        shifted_groups.reverse()
        shifted_column = "." + "#".join(shifted_groups)
        for n, place in enumerate(shifted_column):
            if place == "O":
                result += n
    return result
