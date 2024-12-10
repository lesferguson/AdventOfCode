from collections import deque
import re

def run(data):
    result = 0

    permutations_count = 0
    for line in data:
        s_launcher, springs = line.split()
        springs = deque(springs.split(","))
        pattern = r'^\.*'
        for spring in springs:
            pattern += rf'#{{{spring}}}\.+'
        pattern = pattern[:-1]+"*$"
        possible_launchers = [s_launcher]
        # while any(["?" in launcher for launcher in possible_launchers]):
        #     possible_launchers
        #     for i in range(len(launcher)):
        #         if launcher[i] == "?":
        #             possible_launchers.append(launcher[:i] + "#" + launcher[i+1:])
        #     works = re.match(pattern, launcher)
        for i in range(len(s_launcher)):
            new_possible_launchers = []
            if not any(["?" in l for l in possible_launchers]):
                break
            for launcher in possible_launchers:
                if launcher[i] == "?":
                    new_possible_launchers.append(launcher[:i] + "#" + launcher[i + 1:])
                    new_possible_launchers.append(launcher[:i] + "." + launcher[i + 1:])
                else:
                    new_possible_launchers.append(launcher)
            possible_launchers = new_possible_launchers.copy()
        for launcher in possible_launchers:
            if re.match(pattern, launcher):
                permutations_count += 1

    return permutations_count
