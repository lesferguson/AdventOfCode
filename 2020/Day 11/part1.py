from copy import deepcopy

input_file = "input.txt"
# input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
data = [[val for val in line.strip()] for line in open(input_file).readlines()]

print(data)
empty = [".", "L"]
current_state = []
next_state = deepcopy(data)
while True:

    for i, row in enumerate(current_state):
        for j, seat in enumerate(row):
            if seat == "L" and (i == 0 or (i > 0 and current_state[i - 1][j] in empty)) and (
                    j == 0 or (j > 0 and current_state[i][j - 1] in empty)) and (
                    i == len(current_state) - 1 or (
                    i < len(current_state) - 1 and current_state[i + 1][j] in empty)) and (
                    j == len(row) - 1 or (j < len(row) - 1 and current_state[i][j + 1] in empty)) and (
                    (i == 0 or j == 0) or (i > 0 and j > 0 and current_state[i - 1][j - 1] in empty)) and (
                    (i == 0 or j == len(row) - 1) or (
                    i > 0 and j < len(row) - 1 and current_state[i - 1][j + 1] in empty)) and (
                    (i == len(current_state) - 1 or j == 0) or (
                    i < len(current_state) - 1 and j > 0 and current_state[i + 1][j - 1] in empty)) and (
                    (i == len(current_state) - 1 or j == len(row) - 1) or (
                    i < len(current_state) - 1 and j < len(row) - 1 and current_state[i + 1][j + 1] in empty)):
                next_state[i][j] = "X"
            if seat == "X":
                occ_count = 0
                if i > 0 and current_state[i - 1][j] == "X":
                    occ_count += 1
                if j > 0 and current_state[i][j - 1] == "X":
                    occ_count += 1
                if i < len(current_state) - 1 and current_state[i + 1][j] == "X":
                    occ_count += 1
                if j < len(row) - 1 and current_state[i][j + 1] == "X":
                    occ_count += 1
                if i > 0 and j > 0 and current_state[i - 1][j - 1] == "X":
                    occ_count += 1
                if i > 0 and j < len(row) - 1 and current_state[i - 1][j + 1] == "X":
                    occ_count += 1
                if i < len(current_state) - 1 and j > 0 and current_state[i + 1][j - 1] == "X":
                    occ_count += 1
                if i < len(current_state) - 1 and j < len(row) - 1 and current_state[i + 1][j + 1] == "X":
                    occ_count += 1
                if occ_count >= 4:
                    next_state[i][j] = "L"
    for n in range(len(current_state)):
        print(current_state[n])
    print()
    for n in range(len(current_state)):
        print(next_state[n])
    print()
    if current_state == next_state:
        break
    else:
        current_state = deepcopy(next_state)

print("done")
total_count = 0
for n in range(len(current_state)):
    print(current_state[n])
    total_count += current_state[n].count("X")
print(total_count)