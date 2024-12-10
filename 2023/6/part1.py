

def run(data):
    result = 1
    time_data = [int(v) for v in data[0].split(": ")[1].split(" ") if v]
    distance_data = [int(v) for v in data[1].split(": ")[1].split(" ") if v]

    for race in range(len(time_data)):
        possible_wins = 0
        for i in range(time_data[race]):
            distance = i * (time_data[race] - i)
            if distance_data[race] < distance:
                possible_wins += 1
        result *= possible_wins
    return result
