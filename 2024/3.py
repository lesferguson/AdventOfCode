from aocd import data, submit
from aocd.models import Puzzle
import os
import re
from utils.decorators import *


@timer_func
def part_1(input_data):
    solution = 0

    matches = re.findall(r"mul\(\d+,\d+\)", input_data)
    for match in matches:
        match = match.strip("mul(").strip(")")
        a, b = match.split(",")
        solution += int(a) * int(b)

    return solution


@timer_func
def part_2(input_data):
    solution = 0

    matches = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", input_data)
    do = True
    for match in matches:
        if match == "do()":
            do = True
            continue
        elif match == "don't()":
            do = False
            continue
        elif do:
            match = match.strip("mul(").strip(")")
            a, b = match.split(",")
            solution += int(a) * int(b)

    return solution


year, day = [
    int(param.strip(".py")) for param in os.path.abspath(__file__).split("\\")[-2:]
]
puzzle = Puzzle(year=year, day=day)

if puzzle.answered_b:
    part_1(data)
    part_2(data)
    exit()

examples = puzzle._get_examples()

for example in examples:
    if not puzzle.answered_a and example.answer_a:
        print("-----------------")
        print("input: ", example.input_data)
        print("example a answer: ", example.answer_a)
        sol = part_1(example.input_data)
        print("solution a answer: ", sol)
        print(sol)
        assert str(sol) == example.answer_a
        print("Example Passed")
    elif example.answer_b:
        print("-----------------")
        print("input: ", example.input_data)
        print("example b answer: ", example.answer_b)
        sol = part_2(example.input_data)
        print("solution b answer: ", sol)
        # print(example.extra)
        assert str(sol) == example.answer_b
        print("Example Passed")
if not puzzle.answered_a:
    submit(part_1(data))
else:
    submit(part_2(data))
