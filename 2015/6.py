from aocd import data, submit
from aocd.models import Puzzle
import os
from collections import defaultdict
import re

def solve_a(input_data):
    solution = 0
    grid = defaultdict(bool)
    for line in input_data.splitlines():
        command = re.search(r"(?P<command>turn on|turn off|toggle) (?P<x1>\d+),(?P<y1>\d+) through (?P<x2>\d+),(?P<y2>\d+)", line)
        x1 = int(command.group("x1"))
        y1 = int(command.group("y1"))
        x2 = int(command.group("x2"))+1
        y2 = int(command.group("y2"))+1
        command = command.group("command")
        if command == "turn on":
            for x in range(x1, x2):
                for y in range(y1, y2):
                    grid[(x,y)] = True
        elif command == "turn off":
            for x in range(x1, x2):
                for y in range(y1, y2):
                    grid[(x, y)] = False
        elif command == "toggle":
            for x in range(x1, x2):
                for y in range(y1, y2):
                    grid[(x, y)] = False if grid[(x,y)] else True
        else:
            raise Exception("Unknown command")
    for light in grid.values():
        if light:
            solution += 1


    return solution


def solve_b(input_data):
    solution = 0
    grid = defaultdict(int)
    for line in input_data.splitlines():
        command = re.search(
            r"(?P<command>turn on|turn off|toggle) (?P<x1>\d+),(?P<y1>\d+) through (?P<x2>\d+),(?P<y2>\d+)", line)
        x1 = int(command.group("x1"))
        y1 = int(command.group("y1"))
        x2 = int(command.group("x2")) + 1
        y2 = int(command.group("y2")) + 1
        command = command.group("command")
        if command == "turn on":
            for x in range(x1, x2):
                for y in range(y1, y2):
                    grid[(x, y)] += 1
        elif command == "turn off":
            for x in range(x1, x2):
                for y in range(y1, y2):
                    grid[(x, y)] -= 1 if grid[(x,y)]>0 else 0
        elif command == "toggle":
            for x in range(x1, x2):
                for y in range(y1, y2):
                    grid[(x, y)] += 2
        else:
            raise Exception("Unknown command")
    for light in grid.values():
        if light:
            solution += light

    return solution





year, day = [ int(param.strip(".py")) for param in os.path.abspath(__file__).split('\\')[-2:]]
puzzle = Puzzle(year=year, day=day)

for example in puzzle._get_examples():
    if not puzzle.answered_a and example.answer_a:
        if example.input_data == 'turn off 499,499 through 500,500':
            continue
        print("-----------------")
        print("input: ", example.input_data)
        print("example a answer: ", example.answer_a)
        sol = solve_a(example.input_data)
        print("solution a answer: ", sol)
        print(sol)

        assert str(sol) == example.answer_a
        print("Example Passed")
    elif example.answer_b:
        print("-----------------")
        print("input: ", example.input_data)
        print("example b answer: ", example.answer_b)
        sol = solve_b(example.input_data)
        print("solution b answer: ", sol)
        # print(example.extra)
        assert str(sol) == example.answer_b
        print("Example Passed")
if not puzzle.answer_a:
    submit(solve_a(data))
else:
    submit(solve_b(data))