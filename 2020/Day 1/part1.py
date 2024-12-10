


data = [int(n.strip()) for n in open("input.txt").readlines()]

for i, n in enumerate(data):
    for j in range(i, 199):
        if n + data[j] == 2020:
            print(n*data[j])

