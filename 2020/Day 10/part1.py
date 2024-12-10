
input_file = "input.txt"
# input_file = "test.txt"

data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip()] for line in open(input_file).readlines()]
data.sort()
print(data)
device_jolt = max(data)+3
outlet_jolt = 0
data.append(device_jolt)
previous_jolt = outlet_jolt
diffs = {1:0, 2:0, 3:0}
for adapter in data:
    diffs[adapter - previous_jolt] += 1
    previous_jolt = adapter
print(diffs[1]*diffs[3])