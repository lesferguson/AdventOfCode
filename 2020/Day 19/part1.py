from copy import deepcopy
import re

input_file = "input.txt"
input_file = "test.txt"

data = [line.strip() for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

rules = data[:data.index('')]

messages = data[data.index('')+1:]
rules_dict = {}
for rule in rules:
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

print(rules_dict)
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
count = 0
for message in messages:
    if re.match("^" + rules_dict[0] + "$", message):
        count += 1

print(count)


