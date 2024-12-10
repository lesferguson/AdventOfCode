from collections import defaultdict


def run(data):
    polymer = defaultdict(int)
    template = data.pop(0)
    data.pop(0)
    for i in range(len(template) - 1):
        polymer[template[i] + template[i + 1]] += 1
    rules = {}
    for line in data:
        pair, insert = line.split(" -> ")
        rules[pair] = (pair[0] + insert, insert + pair[1])

    for _ in range(40):
        polymer_copy = polymer.copy()
        for pair, new_pair in rules.items():
            if polymer[pair] > 0:
                polymer_copy[pair] -= polymer[pair]
                polymer_copy[new_pair[0]] += polymer[pair]
                polymer_copy[new_pair[1]] += polymer[pair]
        polymer = defaultdict(int, {k: v for k, v in polymer_copy.items() if v > 0})
        polymer_len = 1
        for pair in polymer:
            polymer_len += polymer[pair]
    mol_count = defaultdict(int, {template[-1]:1})
    for pair in polymer:
        mol_count[pair[0]] += polymer[pair]


    return mol_count[max(mol_count, key=mol_count.get)] - mol_count[min(mol_count, key=mol_count.get)]
