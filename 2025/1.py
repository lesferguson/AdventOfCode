import os

from aocd import data, submit
from aocd.models import Puzzle

from utils.decorators import *
from utils.input_reader import default_parsers

skip_examples = False
override_example_input = None
override_example_solution = None

def parse_input(raw_input):
    """

        file_format types:
        raw: raw
        line: line separated
        tuple: tuple per line
        list: comma seperated list per line, if only 1 line, only return the list for that line
        grid: return a dictionary of coordinate keys, with the value of that coord in the values
        """
    formatted_input = default_parsers(raw_input, "line", str)
    formatted_input = [(-1 * int(distance[1:])) if distance[0]=="L" else (1 * int(distance[1:])) for distance in formatted_input]
    print(formatted_input)

    return formatted_input



@timer_func
def part_1(input_data):
    solution = 0
    #
    z_mod = 100
    current_setting = 50
    password = 0
    for move in input_data:
        current_setting = (current_setting + move) % z_mod
        if current_setting == 0:
            password += 1

    #
    return password


@timer_func
def part_2(input_data):
    solution = 0
    #
    z_mod = 100
    current_setting = 50
    password = 0
    for move in input_data:
        if move > z_mod:
            password +=  abs(move) // z_mod
            move = move % z_mod
        elif move < -1 * z_mod:
            password +=  abs(move) // z_mod
            move =  (move % z_mod) - z_mod

        previous_setting = current_setting
        current_setting = (current_setting + move) % z_mod
        if current_setting == 0 or ((previous_setting + move) != current_setting and previous_setting!=0):
            password += 1
    #
    return password


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
