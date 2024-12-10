import string
from collections import defaultdict
import re
import numpy as np
from collections import defaultdict


def run(data):
    result = 0
    non_parts = []
    parts = []
    gears = defaultdict(list, {})
    adjacents = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]
    for i, line in enumerate(data):
        number = ""
        # part = False

        gear = ()
        for j, value in enumerate(line):
            if value in "0123456789":
                number += value
                for adjacent in adjacents:
                    if 0 <= i + adjacent[0] < len(data) and 0 <= j + adjacent[1] < len(line):
                        # # print((i + adjacent[0], j + adjacent[1]))
                        # if data[i + adjacent[0]][j + adjacent[1]] not in "0123456789.":
                        #     part = True
                        if data[i + adjacent[0]][j + adjacent[1]] == "*":
                            gear = (i + adjacent[0], j + adjacent[1])
            else:
                if number and gear:
                    # parts.append(int(number))

                    gears[gear].append(int(number))
                gear = ()
                number = ""
        else:
            if number and gear:
                gears[gear].append(int(number))
            gear = ()
            number = ""

    # np.prod(non_parts)
    for gear, ratio_calc in gears.items():
        if len(ratio_calc) == 2:
            result += np.prod(ratio_calc)

    return result
