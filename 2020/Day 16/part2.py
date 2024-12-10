from copy import deepcopy

input_file = "input.txt"
# input_file = "test.txt"

data = [line.strip() for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

section = 0
possible_values = []
possible_field_values = []
my_ticket = ()
nearby_tickets = []
rule_names = []
for line in data:
    if not line.strip():
        section += 1
        continue
    if section == 0:
        ranges = line.split(": ")[1].split(" or ")
        rule_names.append(line.split(": ")[0])
        parsed_ranges = []
        for r in ranges:
            possible_values.append(tuple(map(int, r.split("-"))))
            parsed_ranges.append(tuple(map(int, r.split("-"))))
        possible_field_values.append(parsed_ranges)
    elif section == 1:
        if line != "your ticket:":
            my_ticket = tuple(map(int, line.split(",")))
    elif section == 2:
        if line != "nearby tickets:":
            nearby_tickets.append(tuple(map(int, line.split(","))))


nearby_tickets_good = nearby_tickets.copy()
for ticket in nearby_tickets:
    for v in ticket:
        valid_v = False
        for r in possible_values:
            if r[0] <= v <= r[1]:
                valid_v = True
                break
        if not valid_v:
            nearby_tickets_good.remove(ticket)
            break

valid_fields = {i: [j for j in range(len(possible_field_values))] for i in range(len(possible_field_values))}
for ticket in nearby_tickets_good:
    for n, v in enumerate(ticket):
        for i, ranges in enumerate(possible_field_values):
            valid_v = False
            if n not in valid_fields[i]:
                continue
            for r in ranges:
                if r[0] <= v <= r[1]:
                    valid_v = True

            if not valid_v:
                valid_fields[i].remove(n)

mapped_rules = []
simple = False
while not simple:
    simple = True
    for k, v in valid_fields.items():
        if len(v) > 1:
            simple = False
            for rule in mapped_rules:
                if rule in v:
                    v.remove(rule)
        elif len(v) == 1 and v[0] not in mapped_rules:
            mapped_rules.append(v[0])

product = 1
for rule, field in valid_fields.items():
    print(rule_names[rule], possible_field_values[rule],  my_ticket[field[0]])
    if rule_names[rule].startswith("departure"):
        product *= my_ticket[field[0]]
print(product)