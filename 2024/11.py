from collections import defaultdict

from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *
import functools

skip_examples = False
override_example_input = "125 17"
override_example_solution = None


@timer_func
def part_1(input_data):
    solution = 0
    #
    stones = [int(stone) for stone in input_data.split(" ")]
    new_stones = stones.copy()
    for _ in range(25):
        stones = new_stones
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                new_stones.append(int(stone[:int(len(stone)/2)]))
                new_stones.append(int(stone[int(len(stone)/2):]))
            else:
                new_stones.append(stone*2024)

    #
    return len(new_stones)


@timer_func
def part_2(input_data):
    solution = 0
    #
    stones = defaultdict(int)
    for stone in input_data.split(" "):
        stones[int(stone)] += 1
    new_stones = stones.copy()

    for _ in range(75):
        stones = new_stones.copy()
        new_stones = defaultdict(int)
        for stone, n in stones.items():
            if stone == 0:
                new_stones[1] += n
                # stones.append(1)
            elif len(str(stone)) % 2 == 0:
                stone = str(stone)
                new_stones[int(stone[:int(len(stone)/2)])] += n
                new_stones[int(stone[int(len(stone)/2):])] += n
                # stones.append(int(stone[:int(len(stone)/2)]))
                # new_stones.append(int(stone[int(len(stone)/2):]))
            else:
                new_stones[stone*2024] += n
                # new_stones.append(stone*2024)



    #
    return functools.reduce(lambda x, y: x+y, new_stones.values())

year, day = [
    int(param.strip(".py")) for param in os.path.abspath(__file__).split("\\")[-2:]
]
puzzle = Puzzle(year=year, day=day)

if puzzle.answered_b:
    part_1(data)
    part_2(data)
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
            sol = part_1(example_input)
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
            sol = part_2(example_input)
            print("actual answer (B): ", sol)
            assert str(sol) == example_solution
            print("Example Passed")
        elif override_example_solution and override_example_input:
            example_solution = override_example_solution
            print("-----------------")
            print("input: ", example_input)
            print("expected answer (override): ", example_solution)
            sol = part_2(example_input)
            print("actual answer (override): ", sol)
            assert str(sol) == example_solution
            print("Example Passed")

if not puzzle.answered_a:
    submit(part_1(data))
else:
    submit(part_2(data))
