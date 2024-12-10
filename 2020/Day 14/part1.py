from copy import deepcopy
import collections
input_file = "input.txt"
# input_file = "test.txt"

data = [line.strip() for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip()] for line in open(input_file).readlines()]

# mask = data[0].split(" = ")[1]
# ops = [ [ val[4:]  if n == 0 else val for n, val in enumerate(line.split("] = "))] for line in data[1:]]

# mem = collections.defaultdict(int)
mem = {}
for line in data:
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
    else:
        op = tuple([int(val[4:]) if n == 0 else int(val) for n, val in enumerate(line.split("] = "))])
        # print(op)
        value = op[1]
        for n, i in enumerate(reversed(mask)):
            if i == '1':
                bit_mask = 1 << n
                value = value | bit_mask
            elif i == '0':
                bit_mask = 1 << n
                value = value & ~bit_mask
        mem[op[0]] = value

summation = 0
for k, v in mem.items():
    summation += v
print(summation)