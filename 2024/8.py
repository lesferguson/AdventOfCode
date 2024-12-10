from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *
from collections import defaultdict
import itertools

skip_examples = True


@timer_func
def part_1(input_data):
    solution = defaultdict(str, {})
    #
    max_j = len(input_data.splitlines()) - 1
    max_i = len(input_data.splitlines()[0]) - 1

    grid = {
        (i, j): v
        for j, line in enumerate(input_data.splitlines())
        for i, v in enumerate(line)
    }

    frequency_map = defaultdict(list, {})
    for location, frequency in grid.items():
        if frequency != ".":
            frequency_map[frequency].append(location)
    for frequency in frequency_map.values():
        for combination in itertools.combinations(frequency, r=2):
            a1 = (
                combination[1][0] - (combination[0][0] - combination[1][0]),
                combination[1][1] - (combination[0][1] - combination[1][1]),
            )
            if 0 <= a1[0] <= max_i and 0 <= a1[1] <= max_j:
                solution[a1] = "#"
            a2 = (
                (combination[0][0] - combination[1][0]) + combination[0][0],
                (combination[0][1] - combination[1][1]) + combination[0][1],
            )
            if 0 <= a2[0] <= max_i and 0 <= a2[1] <= max_j:
                solution[a2] = "#"

    return len(solution)


@timer_func
def part_2(input_data):
    solution = defaultdict(str, {})
    #
    max_j = len(input_data.splitlines()) - 1
    max_i = len(input_data.splitlines()[0]) - 1

    grid = {
        (i, j): v
        for j, line in enumerate(input_data.splitlines())
        for i, v in enumerate(line)
    }

    frequency_map = defaultdict(list, {})
    for location, frequency in grid.items():
        if frequency != ".":
            frequency_map[frequency].append(location)
    for frequency in frequency_map.values():
        for combination in itertools.combinations(frequency, r=2):
            offset = (
                (combination[0][0] - combination[1][0]),
                (combination[0][1] - combination[1][1]),
            )
            for m in range(max([abs(max_i // offset[0]), abs(max_j // offset[1])])):
                a1 = (
                    combination[1][0] - offset[0] * m,
                    combination[1][1] - offset[1] * m,
                )
                if 0 <= a1[0] <= max_i and 0 <= a1[1] <= max_j:
                    solution[a1] = "#"
                a2 = (
                    offset[0] * m + combination[0][0],
                    offset[1] * m + combination[0][1],
                )
                if 0 <= a2[0] <= max_i and 0 <= a2[1] <= max_j:
                    solution[a2] = "#"

    return len(solution)


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

if not puzzle.answered_a:
    submit(part_1(data))
else:
    submit(part_2(data))
