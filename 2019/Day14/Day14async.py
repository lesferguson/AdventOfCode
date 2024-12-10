import asyncio
import sys

def create_chemical(chemical):
    global ore_count
    global materials

    for reactant in reactions[chemical]:
        if reactant == "quantity":
            continue
        elif reactant == "ORE":
            if materials[reactant] < reactions[chemical][reactant]:
                print(materials)
                sys.exit(materials["FUEL"])
        else:
            while materials[reactant] < reactions[chemical][reactant]:
                create_chemical(reactant)
        materials[reactant] += -reactions[chemical][reactant]
    materials[chemical] += reactions[chemical]["quantity"]



reactions = {}
materials = {"ORE": 1000000000000}
ore_count = 0

reactions_list = [equation.strip() for equation in open("Day14input.txt", "r").readlines()]
for reaction in reactions_list:
    reaction = reaction.split(" => ")
    product_str = reaction[1]
    reactions[product_str.split(" ")[1]] = {reactant: int(quantity) for reactant, quantity in [(reactant_raw.split(" ")[1], reactant_raw.split(" ")[0]) for reactant_raw in reaction[0].split(", ")]}
    reactions[product_str.split(" ")[1]]["quantity"] = int(product_str.split(" ")[0])
    materials[product_str.split(" ")[1]] = 0



print(materials)
material_loop = {}
loop_counts = []
while True:
    create_chemical("FUEL")
    # print(materials)
    if materials["FUEL"] % 1000 == 0:
        print(materials["ORE"], materials["FUEL"])

