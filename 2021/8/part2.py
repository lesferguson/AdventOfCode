from collections import defaultdict


def run(data):
    normal_seg = {0: {"a", "b", "c", "e", "f", "g"},
                  1: {"c", "f"},
                  2: {"a", "c", "d", "e", "g"},
                  3: {"a", "c", "d", "f", "g"},
                  4: {"b", "c", "d", "f"},
                  5: {"a", "b", "d", "f", "g"},
                  6: {"a", "b", "d", "e", "f", "g"},
                  7: {"a", "c", "f"},
                  8: {"a", "b", "c", "d", "e", "f", "g"},
                  9: {"a", "b", "c", "d", "f", "g"}}

    total = 0
    for display in data:
        pattern, output = display.split(" | ")
        patterns = pattern.split()
        outputs = output.split()
        mappings = defaultdict(set, {})

        seg_counts = defaultdict(int, {})
        for digit in patterns:
            for seg in digit:
                seg_counts[seg] += 1
            if len(digit) == 2:
                mappings[1] = set(digit)
            elif len(digit) == 3:
                mappings[7] = set(digit)
            elif len(digit) == 4:
                mappings[4] = set(digit)
            elif len(digit) == 7:
                mappings[8] = set(digit)

        seg_map = {}
        seg_map[list(mappings[1].symmetric_difference(mappings[7]))[0]] = "a"
        for seg, count in seg_counts.items():
            if count == 9:
                seg_map[seg] = "f"
            elif count == 6:
                seg_map[seg] = "b"
            elif count == 4:
                seg_map[seg] = "e"

        for seg in mappings[1]:
            if seg not in seg_map:
                seg_map[seg] = "c"

        for seg in mappings[4]:
            if seg not in seg_map:
                seg_map[seg] = "d"

        for seg in mappings[8]:
            if seg not in seg_map:
                seg_map[seg] = "g"

        out = []
        for digit in outputs:
            if len(digit) == 2:
                out.append("1")
            elif len(digit) == 3:
                out.append("7")
            elif len(digit) == 4:
                out.append("4")
            elif len(digit) == 7:
                out.append("8")
            else:
                num = normal_seg.copy()
                num2 = normal_seg.copy()
                for n in num:
                    if len(digit) != len(num[n]):
                        num2.pop(n)
                for seg in digit:
                    for n in num:
                        if n in num2 and seg_map[seg] not in num[n]:
                            num2.pop(n)
                            continue
                out.append([str(n) for n in num2][0])
        total += int("".join(out))

    return total
