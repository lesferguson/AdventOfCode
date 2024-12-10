from time import process_time
from copy import deepcopy
import collections
input_file = "input.txt"
# input_file = "test.txt"

data = [int(line.strip()) for line in open(input_file).read().split(",")]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]
start_time = process_time()
ran = 30000000
# ran = 2020
start_len = len(data)
initial_data = data.copy()
last_seen = collections.defaultdict(list, {v:[n] for n,v in enumerate(data)})
next_num = data[-1]
print(last_seen, next_num)
for n in range(start_len, ran):
    # if n % 1000 == 0:
    #     print(n)
    if next_num in last_seen and last_seen[next_num][-1] != n-1:
        i = n - last_seen[next_num][-1]
        next_num = i
        last_seen[i].append(n)
    elif next_num in last_seen and len(last_seen[next_num]) > 1:
        i = n - last_seen[next_num][-2] - 1
        next_num = i
        last_seen[i].append(n)
        if len(last_seen[i]) > 2:
            last_seen[i] = last_seen[i][1:]
    else:
        next_num = 0
        last_seen[next_num].append(n)

# print(last_seen)

print(next_num, process_time() - start_time)