
data = [[space for space in row.strip()] for row in open("input.txt").readlines()]
# data = open("input.txt").read()

tree_count = 0
for n in range(1, len(data)):
    # slope of 3
    if data[n][(n*3) % len(data[n])] == "#":
        tree_count += 1

print(tree_count)