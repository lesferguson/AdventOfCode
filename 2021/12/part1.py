from collections import defaultdict

def getPaths(cave_system, u, visited, path, all_paths):
    visited[u] = True
    path.append(u)

    if u == "end":
        all_paths.append(path)
    else:
        for i in cave_system[u]:
            if not visited[i] or i.isupper():
                getPaths(cave_system, i, visited, path, all_paths)


    path.pop()
    visited[u] = False




def run(data):

    cave_system = defaultdict(list)
    v = 0
    visited = defaultdict(bool)
    for path in data:
        caves = path.split("-")
        visited[caves[1]] = False
        visited[caves[0]] = False
        if caves[1] != "start" and caves[0] != "end":
            cave_system[caves[0]].append(caves[1])
            v+=1

        if caves[0] != "start" and caves[1] != "end":
            cave_system[caves[1]].append(caves[0])
            v+=1



    path = []
    all_paths = []
    getPaths(cave_system,"start",visited, path, all_paths)



    return len(all_paths)
