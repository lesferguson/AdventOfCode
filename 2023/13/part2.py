
def find_sym(pattern, orig):

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
            summ = i +1
            if summ != orig:
                return summ

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
            summ = 100 * (j + 1)
            if summ != orig:
                return summ

    return

def run(data):
    result = 0

    raw_patterns = [p for p in data.split("\n\n")]

    for rp in raw_patterns:
        pattern = {}

        for j, line in enumerate(rp.split("\n")):
            for i, value in enumerate(line.strip()):
                pattern[(i, j)] = value
        summary_orig = find_sym(pattern, -1)
        for obj in sorted(pattern):
            quantum_pattern = pattern.copy()
            if pattern[obj] == ".":
                quantum_pattern[obj] = "#"
            else:
                quantum_pattern[obj] = "."

            summary = find_sym(quantum_pattern, summary_orig)
            if summary:
                result += summary
                break
    return result
