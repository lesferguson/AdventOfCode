from aocd import data, submit
from aocd.models import Puzzle


def run_day(puzzle, solve_a, solve_b, skip_examples):
    examples = puzzle._get_examples()

    if not skip_examples:
        for example in examples:
            if not puzzle.answered_a and example.answer_a:
                print("-----------------")
                print("input: ", example.input_data)
                print("expected answer (A): ", example.answer_a)
                sol = solve_a(example.input_data)
                print("actual answer (A): ", sol)
                print(sol)
                assert str(sol) == example.answer_a
                print("Example Passed")
            elif example.answer_b:
                print("-----------------")
                print("input: ", example.input_data)
                print("expected answer (B): ", example.answer_b)
                sol = solve_b(example.input_data)
                print("actual answer (B): ", sol)
                # print(example.extra)
                assert str(sol) == example.answer_b
                print("Example Passed")

    if not puzzle.answered_a:
        submit(solve_a(data))
    else:
        submit(solve_b(data))
