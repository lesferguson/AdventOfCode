from copy import deepcopy

input_file = "input.txt"
# input_file = "test.txt"

# data = [int(line.strip()) for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
cups_list = [int(cup) for cup in open(input_file).read()]
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

extra_cups = [n for n in range(max(cups_list)+1, 1000001)]
cups_list += extra_cups

cups = {}
cup_index = {}
for i, cup in enumerate(cups_list):
    if i == len(cups_list)-1:
        cups[cup] = (cups_list[i-1], cups_list[0])
    else:
        cups[cup] = (cups_list[i-1], cups_list[i+1])
max_cup = max(cups_list)
current_cup = cups_list[0]


for _ in range(10000000):
    # remove 3 clockwise
    removed1 = cups[current_cup][1]
    removed2 = cups[removed1][1]
    removed3 = cups[removed2][1]
    cups[current_cup] = (cups[current_cup][0], cups[removed3][1])
    cups[cups[removed3][1]] = (current_cup, cups[cups[removed3][1]][1])


    # pick destination cup
    dest_cup = None
    dest = current_cup
    while not dest_cup:
        if dest == 1:
            dest = max_cup
        else:
            dest=dest-1
        if dest not in [removed1, removed2, removed3]:
            dest_cup = dest

    # insert removed cups
    cups[removed3] = (removed2, cups[dest_cup][1])
    cups[removed1] = (dest_cup, removed2)
    cups[cups[dest_cup][1]] = (removed3, cups[cups[dest_cup][1]][1])
    cups[dest_cup] = (cups[dest_cup][0], removed1)

    # move selected cup
    current_cup = cups[current_cup][1]

print(cups[1][1], cups[cups[1][1]][1])
print(cups[1][1] * cups[cups[1][1]][1])