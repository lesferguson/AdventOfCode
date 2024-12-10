


data = [int(n.strip()) for n in open("input.txt").readlines()]

for i, n in enumerate(data):
    for j in range(i, 199):
        for k in range(j, 199):
            if n + data[j] + data[k] == 2020:
                print(n, data[j], data[k])
                print(n*data[j]*data[k])

