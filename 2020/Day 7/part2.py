colors = set()
count = 0


def check_bags(outer):
    global count
    for color in rules[outer]:
        if color == "other":
            return
        else:
            for i in range(0, int(rules[outer][color])):
                count += 1
                check_bags(color)


data = [n.strip() for n in open("input.txt").readlines()]

rules = {}
for rule in data:
    outer, inner = rule.split("bags contain")
    inner = [[r.strip() for r in rule.strip(" .").split()] for rule in inner.split(",")]
    inner_d = {}
    for n, c in enumerate(inner):
        inner_d[" ".join(c[1:-1])] = c[0]
    rules[outer.strip()] = inner_d

print(rules)
check_bags("shiny gold")

print(count)
