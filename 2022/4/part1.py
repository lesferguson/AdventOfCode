def run(data):
    subsets = 0
    for pair in data:
        pair = [ elf.split("-") for elf in pair.split(",")]
        sections1 = set(
            [sect for sect in range(int(pair[0][0]), int(pair[0][1]) + 1)])
        sections2 = set(
            [sect for sect in range(int(pair[1][0]), int(pair[1][1]) + 1)])
        if sections2.issubset(sections1) or sections1.issubset(sections2):
            subsets += 1
    return subsets
