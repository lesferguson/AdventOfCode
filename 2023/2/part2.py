import re
import time
import numpy as np
from collections import defaultdict

def run(data):
    total = 0
    for game in data:
        (game_label, cubes) = game.split(": ")
        game_label = int(game_label.split(" ")[1])
        handfuls = [{color.split(" ")[1]: int(color.split(" ")[0]) for color in handful.split(", ")} for handful in
                    cubes.split("; ")]
        minimum_counts = defaultdict(int, {})

        for handful in handfuls:
            for color in handful:
                if handful[color] >= minimum_counts[color]:
                    minimum_counts[color] = handful[color]
        # print(minimum_counts)

        total += np.prod([count for count in minimum_counts.values()])
        # if check_possible(handfuls, possible_count):
        #     total += game_label
        # print(game_label, handfuls)
    return total


