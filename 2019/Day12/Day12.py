import re
from math import gcd
import numpy as np
data = open("Day12input.txt", "r").read()
import sys
moons = [np.array([int(m[0]), int(m[1]), int(m[2])]) for m in re.findall(r'<x=([\d-]+), y=([\d-]+), z=([\d-]+)>', data)]
velocities = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
c = 0
initial_positions = str((moons.copy(), velocities.copy()))
seen = [set(), set(), set()]
periods = [int(), int(), int()]
while True:
    for i, primary in enumerate(moons):
        for n, secondary in enumerate(moons):
            if i == n:
                continue
            else:
                new_v = []
                for m in range(3):
                    if primary[m] < secondary[m]:
                        new_v.append(velocities[i][m] + 1)
                    elif primary[m] > secondary[m]:
                        new_v.append(velocities[i][m] - 1)
                    else:
                        new_v.append(velocities[i][m])
                velocities[i] = (new_v[0], new_v[1], new_v[2])
    # energy = 0
    for i in range(4):
        moons[i] = np.add(moons[i], velocities[i])
        # energy += (abs(moons[i][0]) + abs(moons[i][1]) + abs(moons[i][2])) * (abs(velocities[i][0]) + abs(velocities[i][1]) + abs(velocities[i][2]))

    for i in range(3):
        if periods[i]:
            continue
        state = []
        for j in range(4):
            state.append(moons[j][i])
            state.append(velocities[j][i])
        state = str(state)
        if state in seen[i]:
            print(f"Seen: {i} - {state}")
            periods[i] = c
            continue
        seen[i].add(state)

    if periods[0] and periods[1] and periods[2]:
        print()
        lcm = periods[0]
        for i in periods[1:]:
            lcm = int(lcm*i/gcd(lcm, i))
        print("LCM", lcm)
        sys.exit()
    c += 1


    if c % 10000 == 0:
        print(c)

