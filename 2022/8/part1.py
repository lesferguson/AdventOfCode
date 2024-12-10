import numpy as np

def run(data):

    vis_trees = 0
    for tree in data:
        visible = True
        for x in range(0, tree[0]):
            if data[(x, tree[1])] >= data[tree]:
                visible = False
                break
        if visible == True:
            vis_trees += 1
            continue
        visible = True
        for x in range(tree[0]+1, int(np.sqrt(len(data)))):
            if data[(x, tree[1])] >= data[tree]:
                visible = False
                break
        if visible == True:
            vis_trees += 1
            continue
        visible = True
        for y in range(0, tree[1]):
            if data[(tree[0], y)] >= data[tree]:
                visible = False
                break
        if visible == True:
            vis_trees += 1
            continue
        visible = True
        for y in range(tree[1]+1, int(np.sqrt(len(data)))):
            if data[(tree[0], y)] >= data[tree]:
                visible = False
                break
        if visible == True:
            vis_trees += 1
            continue

    return vis_trees