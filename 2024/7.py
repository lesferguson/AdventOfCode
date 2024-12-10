from aocd import data, submit
from aocd.models import Puzzle
import os

positions = 0

from utils.decorators import *


def next_operation(current, remaining_operands, target):
    global positions
    if current > target:
        return
    if not remaining_operands and current == target:
        positions += target
        raise ValueError
    elif not remaining_operands:
        return
    else:
        next_operation(
            current + remaining_operands[0], remaining_operands[1:].copy(), target
        )
        next_operation(
            current * remaining_operands[0], remaining_operands[1:].copy(), target
        )
        next_operation(
            int(str(current) + str(remaining_operands[0])),
            remaining_operands[1:].copy(),
            target,
        )


@timer_func
def part_1(input_data):
    global positions
    for line in input_data.splitlines():
        test_value, operands = line.split(": ")
        operands = [int(operand) for operand in operands.split(" ")]
        try:
            next_operation(operands[0], operands[1:].copy(), int(test_value))
        except ValueError:
            continue

    return positions


@timer_func
def part_2(input_data):
    global positions
    for line in input_data.splitlines():
        test_value, operands = line.split(": ")
        operands = [int(operand) for operand in operands.split(" ")]
        try:
            next_operation(operands[0], operands[1:].copy(), int(test_value))
        except ValueError:
            continue

    return positions


year, day = [
    int(param.strip(".py")) for param in os.path.abspath(__file__).split("\\")[-2:]
]
puzzle = Puzzle(year=year, day=day)

if puzzle.answered_b:
    part_1(data)
    part_2(data)
    exit()


examples = puzzle._get_examples()
skip_examples = False
if not skip_examples:
    for example in examples:
        if not puzzle.answered_a and example.answer_a:
            print("-----------------")
            print("input: ", example.input_data)
            print("expected answer (A): ", example.answer_a)
            sol = part_1(example.input_data)
            print("actual answer (A): ", sol)
            print(sol)
            assert str(sol) == example.answer_a
            print("Example Passed")
        elif example.answer_b:
            print("-----------------")
            print("input: ", example.input_data)
            print("expected answer (B): ", example.answer_b)
            sol = part_2(example.input_data)
            print("actual answer (B): ", sol)
            # print(example.extra)
            assert str(sol) == example.answer_b
            print("Example Passed")
positions = 0
if not puzzle.answered_a:
    submit(part_1(data))
else:
    submit(part_2(data))
