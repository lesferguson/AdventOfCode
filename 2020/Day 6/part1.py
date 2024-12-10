
data = [n.strip() for n in open("input.txt").readlines()]
# data = open("input.txt").read()
answers = set()
count = 0
for n, line in enumerate(data):

    if n + 1 == len(data) or not line.strip():
        for a in line:
            answers.add(a)
        count += len(answers)
        answers = set()
    else:
        for a in line:
            answers.add(a)

print(count)