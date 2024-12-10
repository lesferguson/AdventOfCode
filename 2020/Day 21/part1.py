from copy import deepcopy
import collections
input_file = "input.txt"
input_file = "test.txt"

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
print(menu)
print(all_ingredients)
print(all_allergens)
for row in menu:
    for allergen in row[1]:
        if allergen not in mapping:
            mapping[allergen] = row[0].copy()
        else:
            for ingredient in mapping[allergen].copy():
                if ingredient not in row[0]:
                    mapping[allergen].remove(ingredient)


for k,v in mapping.items():
    for ingredient in v:
        all_ingredients.discard(ingredient)

count = 0
for row in menu:
    for ingredient in row[0]:
        if ingredient in all_ingredients:
            count += 1


print(count)