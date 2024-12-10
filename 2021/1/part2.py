

def run(data):
    increased_count = 0
    for i in range(3, len(data)):
        if data[i - 3]+data[i - 2]+data[i - 1] < data[i]+data[i - 1]+data[i - 2]:
            increased_count += 1

    results = increased_count

    return results