from copy import deepcopy

input_file = "input.txt"
input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
timestamp, buses = [[int(val)  if val != "x" else val for val in line.strip().split(",")] for line in open(input_file).readlines()]
timestamp = timestamp[0]
print(timestamp, buses)
next_bus = (0, timestamp)
for bus in buses:
    if bus == "x":
        continue
    dep_time = bus - timestamp % bus
    if dep_time < next_bus[1]:
        next_bus = (bus, dep_time)

print(next_bus[0] * next_bus[1])
