from aocd import data, submit
from aocd.models import Puzzle
import os


def solve_a(input_data):
    solution = 0

    for line in input_data.splitlines():
        reports = [int(a) for a in line.split(' ')]
        if sorted(reports) == reports or sorted(reports, reverse=True) == reports:
            gradual=True
            for i in range(len(reports)-1):
                if 1 <= abs(reports[i] - reports[i+1]) <= 3:
                    continue
                else:
                    gradual=False
                    break
            if gradual:
                solution+=1


    return solution


def solve_b(input_data):
    solution = 0
    # for line in input_data.splitlines():
    #     reports = [int(a) for a in line.split(' ')]
    #     popped=False
    #     n = 0
    #     ascending = True
    #     for i in range(len(reports) - 1):
    #         if 1 <= abs(reports[i] - reports[i + 1]) <= 3:
    #             n = n+1
    #             continue
    #         else:
    #             if popped:
    #                 gradual = False
    #                 break
    #             else:
    #                 popped = True
    #                 n = n+2
    #     if gradual:
    #         solution += 1
    unsafe_reports = []
    for line in input_data.splitlines():
        reports = [int(a) for a in line.split(' ')]
        if sorted(reports) == reports or sorted(reports, reverse=True) == reports:
            gradual=True
            for i in range(len(reports)-1):
                if 1 <= abs(reports[i] - reports[i+1]) <= 3:
                    continue
                else:
                    gradual=False
                    unsafe_reports.append(reports)
                    break
            if gradual:
                solution+=1
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
                    print(reports)
                    solution += 1
                    break

    return solution





year, day = [ int(param.strip(".py")) for param in os.path.abspath(__file__).split('\\')[-2:]]
puzzle = Puzzle(year=year, day=day)
examples = puzzle._get_examples()
for example in examples:
    if not puzzle.answered_a and example.answer_a:
        print("-----------------")
        print("input: ", example.input_data)
        print("example a answer: ", example.answer_a)
        sol = solve_a(example.input_data)
        print("solution a answer: ", sol)
        print(sol)
        assert str(sol) == example.answer_a
        print("Example Passed")
    elif example.answer_b:
        print("-----------------")
        print("input: ", example.input_data)
        print("example b answer: ", example.answer_b)
        sol = solve_b(example.input_data)
        print("solution b answer: ", sol)
        # print(example.extra)
        assert str(sol) == example.answer_b
        print("Example Passed")
if not puzzle.answered_a:
    submit(solve_a(data))
else:
    submit(solve_b(data))