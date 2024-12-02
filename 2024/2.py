from aocd import data, submit
from aocd.models import Puzzle
import os


def solve_a(input_data):
    solution = 0




    return solution


def solve_b(input_data):
    solution = 0




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