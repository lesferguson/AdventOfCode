from copy import deepcopy

input_file = "input.txt"
# input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
cups = [int(cup) for cup in open(input_file).read()]
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

print(cups)

for _ in range(100):
    # remove 3 clockwise
    removed_cups = []
    for _ in range(3):
        removed_cups.append(cups.pop(1))

    # pick destination cup
    destination_cup = cups[0] - 1
    while destination_cup not in cups:
        if destination_cup < min(cups):
            destination_cup = max(cups)
        else:
            destination_cup -= 1
    dest = cups.index(destination_cup) + 1

    # insert removed cups
    cups[dest:dest] = removed_cups

    # move selected cup
    cups.append(cups.pop(0))

print(''.join([str(cup) for cup in cups[cups.index(1)+1:]])+''.join([str(cup) for cup in cups[:cups.index(1)]]))
