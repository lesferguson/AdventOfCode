import re

def run(data):
    result = 1
    time_data = int(re.sub(r"\s", "", data[0].split(": ")[1]))
    distance_data = int(re.sub(r"\s", "", data[1].split(": ")[1]))


    possible_wins = 0
    for i in range(time_data):
        distance = i * (time_data - i)
        if distance_data < distance:
            possible_wins += 1

    return possible_wins
