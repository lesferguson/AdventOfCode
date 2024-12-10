colors = set()


def chain_up(color):
    if not color == "shiny gold":
        colors.add(color)
    if color not in parents:
        return
    for parent in parents[color]:
        chain_up(parent)


data = [n.strip() for n in open("input.txt").readlines()]

parents = {}
for rule in data:
    outer, inner = rule.split("bags contain")
    inner = [[r.strip() for r in rule.strip(" .").split()] for rule in inner.split(",")]
    inner_d = {}
    for n, c in enumerate(inner):
        inner_color = " ".join(c[1:-1])
        inner_count = c[0]
        if inner_color in parents:
            parents[inner_color].append(outer.strip())
        else:
            parents[inner_color] = [outer.strip()]

print(parents)
chain_up("shiny gold")
print(colors)
print(len(colors))
