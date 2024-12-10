from collections import defaultdict
import sys
sys.setrecursionlimit(1000)


def getPaths(cave_system, u, path, all_paths, double_cave):


    path.append(u)

    if u == "end":
        all_paths.append(path.copy())
    else:
        for i in cave_system[u]:
            if i.isupper():
                getPaths(cave_system, i, path, all_paths, double_cave)
            else:
                l_case=[n for n in path if n.islower()]
                twice = any([True for j in l_case if l_case.count(j) > 1])
                if (twice and l_case.count(i)<1) or not twice:
                    getPaths(cave_system, i,  path, all_paths, double_cave)




    path.pop()







def run(data):

    cave_system = defaultdict(list)


    for path in data:
        caves = path.split("-")
        if caves[1] != "start" and caves[0] != "end":
            cave_system[caves[0]].append(caves[1])


        if caves[0] != "start" and caves[1] != "end":
            cave_system[caves[1]].append(caves[0])




    path = []
    all_paths = []
    double_cave = ""
    getPaths(cave_system,"start",path, all_paths, double_cave)



    return len(all_paths)






