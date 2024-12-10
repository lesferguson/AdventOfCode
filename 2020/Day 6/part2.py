
data = [n.strip() for n in open("input.txt").readlines()]
# data = open("input.txt").read()
answers_group = set()
g = False
count = 0
for n, line in enumerate(data):
    answers_line = set()
    if n + 1 == len(data):
        if g:
            for a in line:
                answers_line.add(a)
            answers_group = answers_group.intersection(answers_line)
        else:
            for a in line:
                answers_group.add(a)
        count += len(answers_group)
        print(answers_group)
        answers_group = set()
        g = False
    elif not line.strip():
        count += len(answers_group)
        print(answers_group)
        answers_group = set()
        g = False
    else:
        if g:

            for a in line:
                answers_line.add(a)
            answers_group = answers_group.intersection(answers_line)
        else:
            g = True
            for a in line:
                answers_line.add(a)
                answers_group.add(a)

print(count)
