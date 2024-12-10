from aocd import data, submit
from aocd.models import Puzzle
import os
import re
def solve_a(input_data):
    solution = 0
    for line in input_data.splitlines():
        vowel_count = sum([line.count(vowel) for vowel in ['a', 'e', 'i', 'o', 'u'] ])
        if not vowel_count >= 3:
            continue
        double = False
        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                double = True
                break
        if not double == True:
            continue
        naughty_string = False
        for string in ["ab", "cd", "pq", "xy"]:
            if string in line:
                naughty_string = True
                break
        if not naughty_string == True:
            solution += 1
    return solution


def solve_b(input_data):
    solution = 0
    for line in input_data.splitlines():
        double = False
        for i in range(len(line) - 1):
            # if line[i] == line[i + 1]:
            #     double = True
            #     break
            pair = line[i] + line[i+1]
            if pair in line[i+2:]:
                double = True
                break

        if not double == True:
            continue
        repeated = False
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                repeated = True
                break
        if repeated:
            solution += 1
    return solution





year, day = [ int(param.strip(".py")) for param in os.path.abspath(__file__).split('\\')[-2:]]
puzzle = Puzzle(year=year, day=day)

for example in puzzle._get_examples():
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
if not example.answer_b:
    submit(solve_a(data))
else:
    submit(solve_b(data))