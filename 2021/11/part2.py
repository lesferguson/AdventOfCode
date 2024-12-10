from collections import defaultdict


def findAdjPoint(ele, sub=[]):
    if not ele:
        yield sub
    else:
        yield from [idx for j in range(ele[0] - 1, ele[0] + 2)
                    for idx in findAdjPoint(ele[1:], sub + [j])]


def run(data):
    steps = 0
    while len(list(set(list(data.values())))) > 1:
        steps += 1
        for octo in data:
            data[octo] += 1
        while any([True for k, v in data.items() if v > 9]):
            for octo in data:
                if data[octo] > 9:
                    data[octo] = 0
                    for adj_octo in findAdjPoint(octo):
                        if tuple(adj_octo) in data and data[tuple(adj_octo)] != 0:
                            data[tuple(adj_octo)] += 1

    return steps
