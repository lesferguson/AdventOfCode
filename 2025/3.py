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


    return [[int(battery) for battery in bank] for bank in formatted_input]



@timer_func
def part_1(input_data):
    solution = 0
    #
    for bank in input_data:
        max_joltage = 1
        i = 0
        j = 1
        while j <= len(bank)-2:
            if bank[i] < bank[j]:
                i = j
                max_joltage = i+1
            elif bank[j] > bank[max_joltage]:
                max_joltage=j
            j += 1
        if j == len(bank)-1 and bank[max_joltage] < bank[j]:
            max_joltage=j
        solution += bank[i]*10 + bank[max_joltage]

    #
    return solution

@timer_func
def part_2(input_data):
    solution = 0
    #
    for bank in input_data:
        max_joltage=[]
        for battery in range(-12,0):
            if battery < -1:
                max_batt = max(bank[:battery+1])
            else:
                max_batt = max(bank)
            bank = bank[bank.index(max_batt)+1:]
            max_joltage.append(max_batt)
        solution += int("".join([str(battery) for battery in max_joltage]))
    # #
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
