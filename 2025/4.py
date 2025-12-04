import os

from aocd import data, submit
from aocd.models import Puzzle

from utils.decorators import *
from utils.input_reader import default_parsers

skip_examples = False
override_example_input = None
override_example_solution = "43"

def parse_input(raw_input):
    """

        file_format types:
        raw: raw
        line: line separated
        tuple: tuple per line
        list: comma seperated list per line, if only 1 line, only return the list for that line
        grid: return a dictionary of coordinate keys, with the value of that coord in the values
        """
    formatted_input = default_parsers(raw_input, "grid", str)


    return formatted_input



@timer_func
def part_1(input_data):
    solution = 0
    #

    adjacent_mod = [(i, j) for i in [-1, 0, 1]  for j in [-1, 0, 1] if (i, j) != (0, 0)]
    for key, value in input_data.items():
        if value==".":
            continue
        adj_rolls = 0
        for adjacent in adjacent_mod:
            adjacent_space = (key[0] + adjacent[0], key[1]+adjacent[1])
            if adjacent_space not in input_data or input_data[adjacent_space]==".":
                continue
            adj_rolls+=1
        if adj_rolls < 4:
            solution+=1

    #
    return solution


@timer_func
def part_2(input_data):
    solution = 0
    #
    next_state = input_data.copy()
    adjacent_mod = [(i, j) for i in [-1, 0, 1]  for j in [-1, 0, 1] if (i, j) != (0, 0)]
    while True:
        removed_rolls = 0
        input_data = next_state
        next_state = input_data.copy()
        for key, value in input_data.items():
            if value==".":
                continue
            adj_rolls = 0
            for adjacent in adjacent_mod:
                adjacent_space = (key[0] + adjacent[0], key[1]+adjacent[1])
                if adjacent_space not in input_data or input_data[adjacent_space]==".":
                    continue
                adj_rolls+=1
            if adj_rolls < 4:
                removed_rolls+=1
                solution+=1
                next_state[key] = "."
        if removed_rolls == 0:
            break

    #
    return solution


year, day = [
    int(param.strip(".py")) for param in os.path.abspath(__file__).split("/")[-2:]
]
puzzle = Puzzle(year=year, day=day)

if puzzle.answered_b:
    part_1(parse_input(data))
    part_2(parse_input(data))
    exit()

examples = puzzle._get_examples()
if not skip_examples:
    for example in examples:
        if override_example_input:
            example_input = override_example_input
        else:
            example_input = example.input_data
        if not puzzle.answered_a and example.answer_a:
            if override_example_solution:
                example_solution = override_example_solution
            else:
                example_solution = example.answer_a
            print("-----------------")
            print("input: ", example_input)
            print("expected answer (A): ", example_solution)
            sol = part_1(parse_input(example_input))
            print("actual answer (A): ", sol)
            assert str(sol) == example_solution
            print("Example Passed")
        elif example.answer_b:
            if override_example_solution:
                example_solution = override_example_solution
            else:
                example_solution = example.answer_b
            print("-----------------")
            print("input: ", example_input)
            print("expected answer (B): ", example_solution)
            sol = part_2(parse_input(example_input))
            print("actual answer (B): ", sol)
            assert str(sol) == example_solution
            print("Example Passed")
        elif override_example_solution and override_example_input:
            example_solution = override_example_solution
            print("-----------------")
            print("input: ", example_input)
            print("expected answer (override): ", example_solution)
            if not puzzle.answered_a:
                sol = part_1(parse_input(example_input))
            else:
                sol = part_2(parse_input(example_input))
            print("actual answer (override): ", sol)
            assert str(sol) == example_solution
            print("Example Passed")
if not puzzle.answered_a:
    submit(part_1(parse_input(data)))
else:
    submit(part_2(parse_input(data)))
