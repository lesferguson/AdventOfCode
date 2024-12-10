import re
import time


def run(data):
    # tic = time.perf_counter()
    conversions = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                   "eight": "8", "nine": "9",
                   "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
    # total = 0
    # for line in data:
    #     calibration = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    #     total += int(conversions[calibration[0]] + conversions[calibration[-1]])
    # print(f"{time.perf_counter() - tic:0.4f}")

    # tic = time.perf_counter()
    total = 0
    for line in data:
        total += int(
            conversions[re.search(r'(\d|one|two|three|four|five|six|seven|eight|nine)', line).group()] +
            conversions[re.search(r'(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', line[::-1]).group()[::-1]])
    # print(f"{time.perf_counter() - tic:0.4f}")

    return total
