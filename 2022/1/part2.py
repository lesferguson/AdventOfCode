def run(data):
    # elves = []
    # elf = []
    # for item in data:
    #     if not item:
    #         elves.append(sum(elf))
    #         elf = []
    #     else:
    #         elf.append(int(item))
    # elves.append(sum(elf))
    elves = [sum([int(food) for food in elf.split(",")]) for elf in ",".join(data).split(",,")]
    total = 0
    for _ in range(3):
        total += max(elves)
        elves.remove(max(elves))

    return total
