import string
from collections import defaultdict
import re
import numpy as np

def run(data):
    result = 0
    non_parts = []
    parts = []
    adjacents = [(i, j) for i in [-1, 0, 1]  for j in [-1, 0, 1] if (i, j) != (0, 0)]
    for i, line in enumerate(data):
        number = ""
        part = False
        for j, value in enumerate(line):
            if value in "0123456789":
                number += value
                for adjacent in adjacents:
                    if 0 <= i + adjacent[0] < len(data) and 0 <= j + adjacent[1] < len(line):
                        # print((i + adjacent[0], j + adjacent[1]))
                        if data[i + adjacent[0]][j + adjacent[1]] not in "0123456789.":
                            part = True
            else:
                if number and part:
                    parts.append(int(number))
                part = False
                number = ""
        else:
            if number and part:
                parts.append(int(number))
            part = False
            number = ""

    # np.prod(non_parts)

    return np.sum(parts)
