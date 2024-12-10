from collections import defaultdict


def run(data):
    normal_seg = {0: ["a", "b", "c", "e", "f", "g"],
                  1: ["c", "f"],
                  2: ["a", "c", "d", "e", "g"],
                  3: ["a", "c", "d", "f", "g"],
                  4: ["b", "c", "d", "f"],
                  5: ["a", "b", "d", "f", "g"],
                  6: ["a", "b", "d", "e", "f", "g"],
                  7: ["a", "c", "f"],
                  8: ["a", "b", "c", "d", "e", "f", "g"],
                  9: ["a", "b", "c", "d", "f", "g"]}

    count = 0
    for display in data:
        pattern, output = display.split(" | ")
        patterns = pattern.split()
        outputs = output.split()
        mappings = defaultdict(str, {})
        for digit in outputs:
            if len(digit) == 2:
                count += 1
            elif len(digit) == 3:
                count += 1
            elif len(digit) == 4:
                count += 1
            elif len(digit) == 7:
                count += 1

    return count
