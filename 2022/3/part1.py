import string


def run(data):
    priorities = string.ascii_letters
    total = 0
    for elf in data:
        comp1 = set([item for item in elf[:int(len(elf) / 2)]])
        comp2 = set([item for item in elf[int(len(elf) / 2):]])
        total += priorities.index(list(comp1.intersection(comp2))[0]) + 1

    return total
