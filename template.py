from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *

skip_examples = False


@timer_func
def solve_a(input_data):
    solution = 0
    #

    #
    return solution


@timer_func
def solve_b(input_data):
    solution = 0
    #

    #
    return solution


year, day = [int(param.strip(".py")) for param in os.path.abspath(__file__).split('\\')[-2:]]
puzzle = Puzzle(year=year, day=day)

if puzzle.answered_b:
    solve_a(data)
    solve_b(data)
    exit()

examples = puzzle._get_examples()

if not skip_examples:
    for example in examples:
        if not puzzle.answered_a and example.answer_a:
            print("-----------------")
            print("input: ", example.input_data)
            print("expected answer (A): ", example.answer_a)
            sol = solve_a(example.input_data)
            print("actual answer (A): ", sol)
            assert str(sol) == example.answer_a
            print("Example Passed")
        elif example.answer_b:
            print("-----------------")
            print("input: ", example.input_data)
            print("expected answer (B): ", example.answer_b)
            sol = solve_b(example.input_data)
            print("actual answer (B): ", sol)
            assert str(sol) == example.answer_b
            print("Example Passed")

if not puzzle.answered_a:
    submit(solve_a(data))
else:
    submit(solve_b(data))
