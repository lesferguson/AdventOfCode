from copy import deepcopy

input_file = "input.txt"
# input_file = "test.txt"

data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]


loops = 0
key = data[1]
i = 0
value = 1
subject = 7
while value != key:
    i+=1
    value = value * subject
    value = value % 20201227
loops = i


value = 1
subject = data[0]
for _ in range(loops):
    value = value * subject
    value = value % 20201227

print(value)