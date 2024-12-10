
def run(data):
    total = 0
    for line in data:
        calibration = [i for i in line if i.isdigit()]
        total += int(calibration[0]+calibration[-1])
    return total
