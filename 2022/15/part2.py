import re
from collections import defaultdict
from scipy.spatial.distance import cityblock
import numpy as np
from tqdm import tqdm
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
        bounds = 4000000
    else:
        bounds = 20

    for sensor in sensors:
        for m_x in tqdm(range(sensors[sensor] + 2)):
            for direction in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
                unobserved = True
                possible_spot = tuple(np.add(np.multiply(direction, (m_x, sensors[sensor] + 1 - m_x)), sensor))
                if not (0 <= possible_spot[0] <= bounds and 0 <= possible_spot[1] <= bounds):
                    continue
                for sensor_check, distance in sensors.items():
                    if (abs(possible_spot[0] - sensor_check[0]) + abs(possible_spot[1] - sensor_check[
                      1])) <= distance or possible_spot in sensors or possible_spot in beacons:
                        unobserved = False
                        break
                if unobserved:
                    print(possible_spot)
                    return possible_spot[0]*4, possible_spot[1]


if __name__ == "__main__":
    # format options: raw, line, tuple, list, grid
    file_format = "line"
    base_type = str
    example_result_1 = 26
    example_result_2 = 56000011

    # if test passed, do the real input
    real_data = ingest("real.input", file_format, base_type=base_type)

    print("\nPart 2 Results\n----------------\n")
    print(run(real_data))
