

def run(data):

    for i in range(4, len(data)):
        if len(set(list(data)[i-4:i])) == 4:
            break

    return i
