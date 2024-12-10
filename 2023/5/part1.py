from collections import defaultdict, deque


def run(data):
    data = deque(data)
    seeds_map = {int(seed):int(seed) for seed in data.popleft().split(": ")[-1].split(" ")}
    data.popleft()
    while len(data) > 0:
        data.popleft()
        next_map = defaultdict(int, {})
        while True:
            try:
                soil_calc = data.popleft().split(" ")
            except IndexError:
                break
            if not soil_calc[0]:
                break
            soil_calc = [int(soil) for soil in soil_calc]
            next_map[(soil_calc[1], soil_calc[1] + soil_calc[2])] = soil_calc[0]

        for seed, value in seeds_map.items():
            for key in next_map:
                if key[0] <= value < key[1]:
                    seeds_map[seed] = (value - key[0]) + next_map[key]
                    break
            else:
                seeds_map[seed] = value

    locations = {location:seed for seed, location in seeds_map.items()}
    result = min(locations.keys())

    return result
