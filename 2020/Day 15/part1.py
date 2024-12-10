from copy import deepcopy

input_file = "input.txt"
input_file = "test.txt"

data = [int(line.strip()) for line in open(input_file).read().split(",")]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

ran = 2020
# ran = 10

for n in range(len(data), ran):
    if data[n-1] in data[:n-1]:
        i = list(reversed(data[:n-1])).index(data[n-1])+1
        data.append(i)
    else:
        data.append(0)
print(data[-1])