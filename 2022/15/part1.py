import re
from collections import defaultdict
from scipy.spatial.distance import cityblock
import numpy as np
from utils.input_reader import ingest

def run(data):

    sensors = {}
    beacons = set()
    max_y = 0

    for line in data:

        coords = re.findall(r"(x=(-?\d+), y=(-?\d+))", line)
        sensor = (int(coords[0][1]), int(coords[0][2]))
        beacon = (int(coords[1][1]), int(coords[1][2]))
        difference = np.subtract(sensor, beacon)
        distance = abs(difference[0]) + abs(difference[1])
        sensors[sensor] = distance
        beacons.add(beacon)
        max_y = max(max(max_y, sensor[1]), beacon[1])

    if max_y >= 2000000:
        y = 2000000
    else:
        y = 10

    non_beacons = set()
    for sensor in sensors:
        distance = sensors[sensor]
        if sensor[1] + distance >= y >= sensor[1] - distance:
            for i in range(distance-abs(y - sensor[1])+1):
                non_beacons.add((sensor[0] + i, y))
                non_beacons.add((sensor[0] - i, y))

    return len(non_beacons.difference(beacons))