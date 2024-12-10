from copy import deepcopy
import collections
input_file = "input.txt"
# input_file = "test.txt"

data = [line.strip() for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

menu = []
mapping = collections.defaultdict(set)
all_ingredients = set([])
all_allergens = set([])
for line in data:
    ingredients, allergens = line.split("(contains ")
    ingredients = ingredients.strip().split(" ")
    allergens = allergens.rstrip(")").split(", ")
    all_ingredients.update(ingredients.copy())
    all_allergens.update(allergens.copy())
    menu.append((ingredients, allergens))

for row in menu:
    for allergen in row[1]:
        if allergen not in mapping:
            mapping[allergen] = row[0].copy()
        else:
            for ingredient in mapping[allergen].copy():
                if ingredient not in row[0]:
                    mapping[allergen].remove(ingredient)
for i in range(3):
    for k,v in mapping.copy().items():
        if len(v) == 1:
            for k1,v1 in mapping.items():
                if k1 == k:
                    continue
                if v[0] in v1:
                    v1.remove(v[0])

allergens = list(mapping.keys())
allergens.sort()
output = ''
for allergen in allergens:
    output += "," + mapping[allergen][0]
output = output.lstrip(",")
print(mapping)
print(output)
