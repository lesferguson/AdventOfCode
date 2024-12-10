import string


def run(data):
    priorities = string.ascii_letters
    total = 0
    for i in range(0, int(len(data)), 3):
        elf1 = set(data[i])
        elf2 = set(data[i + 1])
        elf3 = set(data[i + 2])

        total += priorities.index(list(elf1.intersection(elf2.intersection(elf3)))[0]) + 1

    return total
