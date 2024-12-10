
def find_sym(rp):
    pattern = {}
    for j, line in enumerate(rp.split("\n")):
        for i, value in enumerate(line.strip()):
            pattern[(i, j)] = value
    # print(pattern)
    max_i = 0
    max_j = 0
    for node in pattern:
        if node[0] > max_i:
            max_i = node[0]
        if node[1] > max_j:
            max_j = node[1]
    for i in range(max_i):
        # left = [pattern[obj] for obj in sorted(pattern.keys()) if obj[0] == i]
        # right = [pattern[obj] for obj in sorted(pattern.keys()) if obj[0] == i + 1]
        left_i = i
        right_i = i + 1
        while 0 <= left_i and right_i <= max_i:
            if [pattern[obj] for obj in sorted(pattern.keys()) if obj[0] == left_i] == [pattern[obj] for obj in
                                                                                        sorted(pattern.keys()) if
                                                                                        obj[0] == right_i]:
                left_i -= 1
                right_i += 1
            else:
                break
        else:
            # print("c" + str(i+1))
            return i + 1

    for j in range(max_j):
        # left = [pattern[obj] for obj in sorted(pattern.keys()) if obj[0] == i]
        # right = [pattern[obj] for obj in sorted(pattern.keys()) if obj[0] == i + 1]
        top_j = j
        bottom_j = j + 1
        while 0 <= top_j and bottom_j <= max_j:
            if [pattern[obj] for obj in sorted(pattern.keys()) if obj[1] == top_j] == [pattern[obj] for obj in
                                                                                       sorted(pattern.keys()) if
                                                                                       obj[1] == bottom_j]:
                top_j -= 1
                bottom_j += 1
            else:
                break
        else:
            # print("r" + str(j+1))
            return 100 * (j + 1)

def run(data):
    result = 0

    raw_patterns = [p for p in data.split("\n\n")]

    for rp in raw_patterns:
        result += find_sym(rp)
    return result
