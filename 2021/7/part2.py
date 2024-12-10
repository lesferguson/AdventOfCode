from collections import defaultdict
import statistics

def run(data):

    positions= defaultdict(int, {})
    for crab in data:
        positions[crab] += 1

    distances = defaultdict(list, {})
    for n in range(max(positions)):
        distance = 0
        for position, count in positions.items():
            distance += (abs(position - n)*(abs(position - n)+1)/2) * count
        distances[distance].append(n)



    return min(distances)