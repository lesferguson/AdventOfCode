from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *


@timer_func
def part_1(input_data):
    solution = 0

    for line in input_data.splitlines():
        reports = [int(a) for a in line.split(" ")]
        if sorted(reports) == reports or sorted(reports, reverse=True) == reports:
            gradual = True
            for i in range(len(reports) - 1):
                if 1 <= abs(reports[i] - reports[i + 1]) <= 3:
                    continue
                else:
                    gradual = False
                    break
            if gradual:
                solution += 1

    return solution


@timer_func
def part_2(input_data):
    solution = 0

    unsafe_reports = []
    for line in input_data.splitlines():
        reports = [int(a) for a in line.split(" ")]
        if sorted(reports) == reports or sorted(reports, reverse=True) == reports:
            gradual = True
            for i in range(len(reports) - 1):
                if 1 <= abs(reports[i] - reports[i + 1]) <= 3:
                    continue
                else:
                    gradual = False
                    unsafe_reports.append(reports)
                    break
            if gradual:
                solution += 1
        else:
            unsafe_reports.append(reports)
    for unsafe_report in unsafe_reports:
        for i in range(len(unsafe_report)):
            reports = unsafe_report.copy()
            del reports[i]
            if sorted(reports) == reports or sorted(reports, reverse=True) == reports:
                gradual = True
                for i in range(len(reports) - 1):
                    if 1 <= abs(reports[i] - reports[i + 1]) <= 3:
                        continue
                    else:
                        gradual = False
                        break
                if gradual:

                    solution += 1
                    break

    return solution


year, day = [
    int(param.strip(".py")) for param in os.path.abspath(__file__).split("\\")[-2:]
]
puzzle = Puzzle(year=year, day=day)

if puzzle.answered_b:
    part_1(data)
    part_2(data)
    exit()

examples = puzzle._get_examples()
for example in examples:
    if not puzzle.answered_a and example.answer_a:
        print("-----------------")
        print("input: ", example.input_data)
        print("example a answer: ", example.answer_a)
        sol = part_1(example.input_data)
        print("solution a answer: ", sol)
        print(sol)
        assert str(sol) == example.answer_a
        print("Example Passed")
    elif example.answer_b:
        print("-----------------")
        print("input: ", example.input_data)
        print("example b answer: ", example.answer_b)
        sol = part_2(example.input_data)
        print("solution b answer: ", sol)
        # print(example.extra)
        assert str(sol) == example.answer_b
        print("Example Passed")
if not puzzle.answered_a:
    submit(part_1(data))
else:
    submit(part_2(data))
