import numpy as np


def run(data):
    vis_trees = {}

    x_range = [x for x in range(int(np.sqrt(len(data))))]
    y_range = [y for y in range(int(np.sqrt(len(data))))]

    for tree in data:
        scenery_score = 1
        seen_trees = 0
        left = x_range[:tree[0]]
        left.reverse()
        for x in left:
            seen_trees += 1
            if data[(x, tree[1])] >= data[tree]:
                break
        scenery_score *= seen_trees
        seen_trees = 0
        right = x_range[tree[0]+1:]
        for x in right:
            seen_trees += 1
            if data[(x, tree[1])] >= data[tree]:
                break
        scenery_score *= seen_trees
        seen_trees = 0
        up = y_range[:tree[1]]
        up.reverse()
        for y in up:
            seen_trees += 1
            if data[(tree[0], y)] >= data[tree]:
                break
        scenery_score *= seen_trees
        seen_trees = 0
        down = y_range[tree[1]+1:]
        for y in down:
            seen_trees += 1
            if data[(tree[0], y)] >= data[tree]:
                break
        scenery_score *= seen_trees

        vis_trees[tree] = scenery_score

    return max(vis_trees.values())
