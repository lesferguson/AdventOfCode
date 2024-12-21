from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *
import re

skip_examples = True
override_example_input = None
override_example_solution = None

def parse_input(raw_input):
    formatted_input = []

    for robot in raw_input.splitlines():
        robot_meta = re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", robot)
        formatted_input.append(((int(robot_meta[1]), int(robot_meta[2])),(int(robot_meta[3]), int(robot_meta[4]))))

    return formatted_input


@timer_func
def part_1(input_data):
    solution = 0
    #
    if not len(input_data) > 15:
        x_size = 11
        y_size = 7
    else:
        x_size = 101
        y_size = 103
    lab = {(i,j): [] for i in range(x_size) for j in range(y_size)}
    for robot in input_data:
        lab[robot[0]].append(robot[1])

    new_lab = lab.copy()
    for n in range(100):
        lab = new_lab.copy()
        # temp_x = max([cord[1] for cord in new_lab.keys()])
        # temp_y = max([cord[0] for cord in new_lab.keys()])
        # res = [[0] * (temp_y + 1) for ele in range(temp_x + 1)]
        #
        # for (i, j), val in lab.items():
        #     res[j][i] = str(len(val))
        # for row in res:
        #     print("".join(row))
        new_lab = {(i, j): [] for i in range(x_size) for j in range(y_size)}
        for tile, robots in lab.items():
            for robot in robots:
                new_x = (robot[0]+tile[0]) % x_size
                new_y = (robot[1]+tile[1]) % y_size

                new_lab[(new_x,new_y)].append(robot)

        # print(n)
    lab = new_lab.copy()
    # temp_x = max([cord[1] for cord in new_lab.keys()])
    # temp_y = max([cord[0] for cord in new_lab.keys()])
    # res = [[0] * (temp_y + 1) for ele in range(temp_x + 1)]
    #
    # for (i, j), val in lab.items():
    #     res[j][i] = str(len(val))
    # for row in res:
    #     print("".join(row))
    quad1=0
    quad2=0
    quad3=0
    quad4=0

    for tile, robots in lab.items():
            if tile[0] < (x_size-1)/2 and tile[1] < (y_size-1)/2:
                quad1 += len(robots)
            elif tile[0] > (x_size-1)/ 2 and tile[1] < (y_size-1) / 2:
                quad2 += len(robots)
            elif tile[0] < (x_size-1)/ 2 and tile[1] > (y_size-1) / 2:
                quad3 += len(robots)
            elif tile[0] > (x_size-1)/ 2 and tile[1] > (y_size-1) / 2:
                quad4 += len(robots)
    #
    return quad1*quad2*quad3*quad4


@timer_func
def part_2(input_data):
    solution = 0
    #
    if not len(input_data) > 15:
        x_size = 11
        y_size = 7
    else:
        x_size = 101
        y_size = 103
    lab = {(i,j): [] for i in range(x_size) for j in range(y_size)}
    for robot in input_data:
        lab[robot[0]].append(robot[1])

    new_lab = lab.copy()
    for n in range(100000):
        lab = new_lab.copy()

        new_lab = {(i, j): [] for i in range(x_size) for j in range(y_size)}
        for tile, robots in lab.items():
            for robot in robots:
                new_x = (robot[0]+tile[0]) % x_size
                new_y = (robot[1]+tile[1]) % y_size

                new_lab[(new_x,new_y)].append(robot)
        temp_x = max([cord[1] for cord in new_lab.keys()])
        temp_y = max([cord[0] for cord in new_lab.keys()])
        res = [[0] * (temp_y + 1) for ele in range(temp_x + 1)]

        for (i, j), val in lab.items():
            res[j][i] = "#" if len(val) > 0 else "."
        for row in res:
            # print("".join(row))
            if "#######" in "".join(row):
                return n

        #
    return solution


year, day = [
    int(param.strip(".py")) for param in os.path.abspath(__file__).split("\\")[-2:]
]
puzzle = Puzzle(year=year, day=day)

data = parse_input(data)

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
    submit(part_1(data))
else:
    submit(part_2(data))
