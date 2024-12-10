

def run(data):

    for i in range(14, len(data)):
        if len(set(list(data)[i-14:i])) == 14:
            break

    return i
