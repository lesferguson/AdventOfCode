
data = [[space for space in row.strip()] for row in open("input.txt").readlines()]
# data = open("input.txt").read()
tree_counts_prod = 1
for slope in [1, 3, 5, 7]:
    tree_count = 0
    for n in range(1, len(data)):
        # slope of 3
        if data[n][(n*slope) % len(data[n])] == "#":
            tree_count += 1
    tree_counts_prod *= tree_count
    print(slope, tree_count)

tree_count = 0
for n in range(2, len(data), 2):
    # slope of 3
    if data[n][int(n/2) % len(data[n])] == "#":
        tree_count += 1
tree_counts_prod *= tree_count
print(".5", tree_count)

print(tree_counts_prod)