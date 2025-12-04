import os
import textwrap

from aocd import data, submit
from aocd.models import Puzzle

from utils.decorators import *
from utils.input_reader import default_parsers

skip_examples = False
override_example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

override_example_solution = None
from functools import reduce

def factors(n):
    f = set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    f.remove(n)
    return f



def parse_input(raw_input):
    """

        file_format types:
        raw: raw
        line: line separated
        tuple: tuple per line
        list: comma seperated list per line, if only 1 line, only return the list for that line
        grid: return a dictionary of coordinate keys, with the value of that coord in the values
        """
    formatted_input = default_parsers(raw_input, "list", str)
    formatted_input = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in formatted_input]
    return formatted_input



@timer_func
def part_1(input_data):
    solution = 0
    #
    for r in input_data:
        for n in range(r[0],r[1]+1):
            n = str(n)
            if n[:int(len(n)/2)] == n[int(len(n)/2):]:
                solution += int(n)
    #
    return solution


@timer_func
def part_2(input_data):
    solution = 0

    common_factors = { i:factors(i) for i in range(1, 20)}
    #
    for r in input_data:
        for n in range(r[0],r[1]+1):
            n = str(n)
            # print(n)
            f = common_factors[len(n)]
            # print(f)
            for factor in f:
                sub_s = textwrap.wrap(n, factor)
                # print(sub_s)
                if len(set(sub_s)) == 1:
                    # print(n)
                    solution += int(n)
                    break
            # if n[:int(len(n)/2)] == n[int(len(n)/2):]:
            #     solution += int(n)
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
