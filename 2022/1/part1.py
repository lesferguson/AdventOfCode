import numpy as np


def run(data):
    # elves = []
    # elf = []

    # elves =

    # for item in data:
    #     if not item:
    #         elves.append(sum(elf))
    #         elf = []
    #     else:
    #         elf.append(int(item))
    # elves.append(sum(elf))

    return max([sum([int(food) for food in elf.split(",")]) for elf in ",".join(data).split(",,")])
