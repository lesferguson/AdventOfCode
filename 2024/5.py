from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *


@timer_func
def part_1(input_data):
    solution = 0

    page_order, manuals = input_data.split("\n\n")
    page_order = page_order.splitlines()
    manuals = manuals.splitlines()

    page_order = [list(map(int, page.split("|"))) for page in page_order]
    manuals = [[int(x) for x in manual.split(",")] for manual in manuals]

    for manual in manuals:
        bad = False
        for rule in page_order:
            if all(page in manual for page in rule):
                if manual.index(rule[0]) < manual.index(rule[1]):
                    continue
                else:
                    bad = True
                    break
        if not bad:
            solution += manual[int((len(manual) - 1) / 2)]

    return solution


@timer_func
def part_2(input_data):
    solution = 0

    page_order, manuals = input_data.split("\n\n")
    page_order = page_order.splitlines()
    manuals = manuals.splitlines()

    page_order = [list(map(int, page.split("|"))) for page in page_order]
    manuals = [[int(x) for x in manual.split(",")] for manual in manuals]

    bad_manuals = []
    for manual in manuals:
        for rule in page_order:
            if all(page in manual for page in rule):
                if manual.index(rule[0]) < manual.index(rule[1]):
                    continue
                else:
                    bad_manuals.append(manual)
                    break

    for manual in bad_manuals:
        for _ in range(2):
            for rule in page_order:
                if all(page in manual for page in rule):
                    if manual.index(rule[0]) > manual.index(rule[1]):
                        manual.remove(rule[0])
                        manual.insert(manual.index(rule[1]), rule[0])
        solution += manual[int((len(manual) - 1) / 2)]
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
