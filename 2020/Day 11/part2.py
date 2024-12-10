from copy import deepcopy

input_file = "input.txt"
# input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
data = [[val for val in line.strip()] for line in open(input_file).readlines()]

empty = [".", "L"]

current_state = []
next_state = deepcopy(data)
while True:
    for i, row in enumerate(current_state):
        for j, seat in enumerate(row):
            if seat == ".":
                continue
            adj_seats = []

            if i > 0:
                n = 1
                while n < len(current_state) - (len(current_state) - i - 1) and current_state[i - n][j] == ".":
                    n += 1
                if n < len(current_state) - (len(current_state) - i - 1):
                    adj_seats.append(current_state[i - n][j])
            if j > 0:
                n = 1
                while n < len(row) - (len(row) - j - 1) and current_state[i][j - n] == "."  :
                    n += 1
                if n < len(row) - (len(row) - j - 1):
                    adj_seats.append(current_state[i][j - n])
            if i < len(current_state) - 1:
                n = 1
                while n < (len(current_state) - i ) and current_state[i + n][j] == "."  :
                    n += 1
                if n < (len(current_state) - i ):
                    adj_seats.append(current_state[i + n][j])
            if j < len(row) - 1:
                n = 1
                while n < (len(row) - j ) and current_state[i][j + n] == "."  :
                    n += 1
                if n < (len(row) - j ):
                    adj_seats.append(current_state[i][j + n])
            if i > 0 and j > 0:
                n = 1
                while n < len(current_state) - (len(current_state) - i - 1) and n < len(row) - (len(row) - j - 1) and current_state[i - n][j - n] == ".":
                    n += 1
                if n < len(current_state) - (len(current_state) - i - 1) and n < len(row) - (len(row) - j - 1):
                    adj_seats.append(current_state[i - n][j - n])
            if i > 0 and j < len(row) - 1:
                n = 1
                while n < len(current_state) - (len(current_state) - i - 1) and n < (len(row) - j ) and current_state[i - n][j + n] == ".":
                    n += 1
                if n < len(current_state) - (len(current_state) - i - 1) and n < (len(row) - j ):
                    adj_seats.append(current_state[i - n][j + n])
            if i < len(current_state) - 1 and j > 0:
                n = 1
                while n < (len(current_state) - i ) and n < len(row) - (len(row) - j - 1) and current_state[i + n][j - n] == ".":
                    n += 1
                if n < (len(current_state) - i ) and n < len(row) - (len(row) - j - 1):
                    adj_seats.append(current_state[i + n][j - n])
            if i < len(current_state) - 1 and j < len(row) - 1:
                n = 1
                while n < (len(current_state) - i ) and n < (len(row) - j ) and current_state[i + n][j + n] == ".":
                    n += 1
                if (n < (len(current_state) - i ) and n < (len(row) - j )):
                    adj_seats.append(current_state[i + n][j + n])
            if seat == "L" and "#" not in adj_seats:
                next_state[i][j] = "#"
            elif seat == "#" and adj_seats.count("#") >= 5:
                next_state[i][j] = "L"
    # for n in range(len(current_state)):
    #     print(current_state[n])
    # print()
    # for n in range(len(current_state)):
    #     print(next_state[n])
    # print()
    if current_state == next_state:
        break
    else:
        current_state = deepcopy(next_state)

print("done")
total_count = 0
for n in range(len(current_state)):
    print(current_state[n])
    total_count += current_state[n].count("#")
print(total_count)