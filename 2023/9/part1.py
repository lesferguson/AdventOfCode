import numpy as np

def run(data):
    result = 0
    next_values = []
    for history in data:
        values = [int(v) for v in history.split(" ")]
        current_step = values
        edge = [current_step[-1]]
        while not all([value==0 for value in current_step]):
            next_step = []
            for i in range(len(current_step)-1):
                next_step.append(current_step[i+1]-current_step[i])
            current_step = next_step
            edge.append(current_step[-1])

        next_values.append(np.sum(edge))
    # print(next_values)

    return np.sum(next_values)
