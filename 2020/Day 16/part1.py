from copy import deepcopy

input_file = "input.txt"
# input_file = "test.txt"

data = [line.strip() for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

section = 0
possible_values = []
my_ticket = ()
nearby_tickets = []
for line in data:
    if not line.strip():
        section += 1
        continue
    if section == 0:
        ranges = line.split(": ")[1].split(" or ")
        parsed_ranges = []
        for r in ranges:
            possible_values.append(tuple(map(int, r.split("-"))))
            # parsed_ranges.append(tuple(map(int, r.split("-"))))
        # possible_values.append(parsed_ranges)
    elif section == 1:
        if line != "your ticket:":
            my_ticket = tuple(map(int, line.split(",")))
    elif section == 2:
        if line != "nearby tickets:":
            nearby_tickets.append(tuple(map(int, line.split(","))))

print(possible_values)
print(my_ticket)
print(nearby_tickets)
bad_tickets = []
error_rate = 0
for ticket in nearby_tickets:
    valid = True
    for v in ticket:
        valid_v = False
        for r in possible_values:
            if r[0] <= v <= r[1]:
                valid_v = True
                break
        if not valid_v:
            error_rate += v
            valid = False
            print(ticket)
            bad_tickets.append(ticket)


print(bad_tickets)
print(error_rate)