from collections import defaultdict, deque


def run(data):
    data = deque(data)
    seeds_map = [int(seed) for seed in data.popleft().split(": ")[-1].split(" ")]
    ranges = deque()
    for i in range(0, len(seeds_map), 2):
        ranges.append((seeds_map[i], seeds_map[i]+seeds_map[i+1]))

    data.popleft()
    while len(data) > 0:
        data.popleft()
        next_map = defaultdict(int, {})
        next_ranges = deque()
        while True:
            try:
                soil_calc = data.popleft().split(" ")
            except IndexError:
                break
            if not soil_calc[0]:
                break
            soil_calc = [int(soil) for soil in soil_calc]
            next_map[(soil_calc[1], soil_calc[1] + soil_calc[2])] = soil_calc[0]

        while len(ranges) > 0:
            range_tup = ranges.popleft()
            for key in next_map:
                if key[0] <= range_tup[0] and range_tup[1] < key[1]:
                    next_ranges.append((range_tup[0]-key[0]+next_map[key], range_tup[1]-key[0]+next_map[key]))
                    break
                elif key[0] <= range_tup[0] < key[1] <= range_tup[1]:
                    next_ranges.append((range_tup[0]-key[0]+next_map[key], key[1]-key[0]+next_map[key]))
                    ranges.append((key[1], range_tup[1]))
                    break
                elif range_tup[0] < key[0] < range_tup[1] < key[1]:
                    next_ranges.append((next_map[key], range_tup[1]-key[0]+next_map[key]))
                    ranges.append((range_tup[0], key[0]))
                    break
            else:
                    next_ranges.append(range_tup)
        ranges = next_ranges.copy()


    locations = [range_tup[0] for range_tup in ranges]
    result = min(locations)

    return result
