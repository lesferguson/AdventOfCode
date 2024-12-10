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
        addr = op[0]
        value = op[1]

        for n, i in enumerate(reversed(mask)):
            if i == '1':
                bit_mask = 1 << n
                addr = addr | bit_mask

        possible_addr = {addr}
        for n, i in enumerate(reversed(mask)):
            if i == 'X':
                bit_mask = 1 << n
                possible_addr_copy = set()
                for address in possible_addr:
                    possible_addr_copy.add(address | bit_mask)
                    possible_addr_copy.add(address & ~bit_mask)
                possible_addr = possible_addr.union(possible_addr_copy)
        for address in possible_addr:
            mem[address] = value

summation = 0
for k, v in mem.items():
    summation += v
print(summation)