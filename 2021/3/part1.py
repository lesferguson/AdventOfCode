from collections import defaultdict

def run(data):



    ones= [0]*len(data[0])

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "1":
                ones[j] += 1

    gamma = ["0"] * len(data[0])

    for k,v in enumerate(ones):
        if v>len(data)/2:
            gamma[k] = "1"
    epsilon = ""

    for digit in gamma:
        if digit == "1":
            epsilon += "0"
        else:
            epsilon += "1"

    results = int(''.join(epsilon),2)*int(''.join(gamma),2)
    return results