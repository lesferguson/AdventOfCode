import collections

input_file = "input.txt"
# input_file = "test.txt"

adapters = [int(line.strip()) for line in open(input_file).readlines()]
adapters.sort()
# combinations = collections.defaultdict(int, {0: 1})
combinations = {0: 1}
for adapter in adapters:
    # combinations[adapter] = combinations[adapter - 1] + combinations[adapter - 2] + combinations[adapter - 3]
    local_combo = 0
    if (adapter - 1) in combinations:
        local_combo += combinations[adapter - 1]
    if (adapter - 2) in combinations:
        local_combo += combinations[adapter - 2]
    if (adapter - 3) in combinations:
        local_combo += combinations[adapter - 3]
    combinations[adapter] = local_combo

print(combinations[adapters[-1]])

