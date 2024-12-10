

def run(data):

    increased_count = 0
    for i in range(1, len(data)):
        if data[i-1] < data[i]:
            increased_count+=1

    results = increased_count

    return results