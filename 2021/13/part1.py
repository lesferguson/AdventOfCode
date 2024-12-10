from collections import defaultdict


def run(data):
    paper = defaultdict(bool)
    folds = []
    for line in data:
        if line.startswith("fold"):
            folds.append((line.split("=")[0][-1], int(line.split("=")[1])))
        elif line:
            paper[(int(line.split(",")[0]), int(line.split(",")[1]))] = True


    for fold in folds:
        paper_copy = paper.copy()
        for dot in paper:
            if fold[0] == "x" and dot[0] > fold[1]:
                paper_copy[dot] = False
                paper_copy[((2*fold[1]-dot[0]), dot[1])] = True
            elif fold[0] == "y" and dot[1] > fold[1]:
                paper_copy[dot] = False
                paper_copy[(dot[0],(2 * fold[1] - dot[1]))] = True

        paper = {k:v for k,v in paper_copy.items() if v}

        return len(paper)
