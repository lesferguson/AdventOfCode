from copy import deepcopy
import re

input_file = "input.txt"
# input_file = "test.txt"

data = [line.strip() for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

def convert_regex(logic_list, d=0):
    logic_re = str

    for i, logic in enumerate(logic_list):
        for j, step in enumerate(logic):
            if type(step) == list:
                if d != 10:
                    logic_list[i][j] = convert_regex(step, d=d+1)
                else:
                    logic_list[i][j] = ''.join(logic_list[0])

    rule_list = []
    for n in range(len(logic_list)):
        rule_list.append(''.join(logic_list[n]))
    if len(logic_list) > 1:
        need_paren = True
    else:
        need_paren = False
    logic_re = '|'.join(rule_list)
    if need_paren:
        logic_re = "(" + logic_re + ")"

    return logic_re








rules = data[:data.index('')]

messages = data[data.index('')+1:]
rules_dict = {}
for rule in rules:
    if rule.startswith("8:"):
        rule = "8: 42 | 42 8"
    elif rule.startswith("11:"):
        rule = "11: 42 31 | 42 11 31"
    num, logic = rule.split(": ")
    num = int(num)
    logic = logic.split(" | ")
    rules_dict[num] = []
    for log in logic:
        cleaned_logic = ''
        sub_rules = log.split()
        for n, r in enumerate(sub_rules):
            if '"' in r:
                r = r[1: -1]
            else:
                r = int(r)
            sub_rules[n] = r
        rules_dict[num].append(sub_rules)

# print(rules_dict)
simple = False
while not simple:
    simple = True
    for rule in rules_dict:
        if type(rules_dict[rule]) == str:
            continue
        if_base = True
        for i, logic in enumerate(rules_dict[rule]):
            for j, step in enumerate(logic):
                if type(step) == int:
                    if_base = False
                    break
        if if_base:
            rule_list = []
            for n in range(len(rules_dict[rule])):
                rule_list.append(''.join(rules_dict[rule][n]))

            if len(rules_dict[rule]) > 1:
                need_paren = True
            else:
                need_paren = False
            rules_dict[rule] = '|'.join(rule_list)
            if need_paren:
                rules_dict[rule] = "(" + rules_dict[rule] + ")"

    for rule in rules_dict:
        if type(rules_dict[rule]) == str:
            continue
        for i, logic in enumerate(rules_dict[rule]):
            for j, step in enumerate(logic):
                if type(step) == int:
                    if type(rules_dict[step]) == str:

                        rules_dict[rule][i][j] = rules_dict[step]
                        simple = False


for rule in [8, 11]:
    if type(rules_dict[rule]) == str:
        continue
    for i, logic in enumerate(rules_dict[rule]):
        for j, step in enumerate(logic):
            if type(step) == int:
                # if type(rules_dict[step]) == str:

                rules_dict[rule][i][j] = rules_dict[step]

for rule in [8, 11]:
    reg = convert_regex(rules_dict[rule])
    rule_list = []
    for n in range(len(rules_dict[rule])):
        rule_list.append(''.join(rules_dict[rule][n]))

    if len(rules_dict[rule]) > 1:
        need_paren = True
    else:
        need_paren = False
    rules_dict[rule] = '|'.join(rule_list)
    if need_paren:
        rules_dict[rule] = "(" + rules_dict[rule] + ")"
# print(rules_dict)

rules_dict[0] = rules_dict[8]+rules_dict[11]
#
# for i, logic in enumerate(rules_dict[0]):
#     for j, step in enumerate(logic):
#         if type(step) == int:
#             # if type(rules_dict[step]) == str:
#
#             rules_dict[0][i][j] = rules_dict[step]
#
# for n in range(len(rules_dict[0])):
#     rule_list.append(''.join(rules_dict[0][n]))
#
# #
# if len(rules_dict[0]) > 1:
#     need_paren = True
# else:
#     need_paren = False
# rules_dict[0] = '|'.join(rule_list)
# if need_paren:
#     rules_dict[0] = "(" + rules_dict[0] + ")"

# print(42, rules_dict[42])
# print(31, rules_dict[31])
count = 0
for message in messages:
    if re.fullmatch(rules_dict[0], message):
        count += 1
        print(message)

print(count)


