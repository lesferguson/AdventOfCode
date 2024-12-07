from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *


@timer_func
def solve_a(input_data):
    solution = 0
    a_list = []
    b_list = []
    for line in input_data.splitlines():
        a, b = line.split("   ")
        a_list.append(int(a))
        b_list.append(int(b))
    a_list.sort()
    b_list.sort()
    for i in range(len(a_list)):
        solution += abs(a_list[i] - b_list[i])

    return solution


@timer_func
def solve_b(input_data):
    solution = 0

    a_list = []
    b_list = []
    for line in input_data.splitlines():
        a, b = line.split("   ")
        a_list.append(int(a))
        b_list.append(int(b))
    for a in a_list:
        num = b_list.count(a)
        solution += num * a

    return solution


year, day = [
    int(param.strip(".py")) for param in os.path.abspath(__file__).split("\\")[-2:]
]
puzzle = Puzzle(year=year, day=day)

if puzzle.answered_b:
    print(str(year) + " day " + str(day))
    solve_a(data)
    solve_b(data)
    exit()

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
