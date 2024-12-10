from aocd import data, submit
from aocd.models import Puzzle
import os
from collections import defaultdict
from utils.decorators import *


@timer_func
def part_1(input_data):
    max_j = len(input_data.splitlines()) - 1
    max_i = len(input_data.splitlines()[0]) - 1

    lab = {
        (i, j): v
        for j, line in enumerate(input_data.splitlines())
        for i, v in enumerate(line)
    }
    guards_location = list(lab.keys())[list(lab.values()).index("^")]
    visited = defaultdict(bool, {guards_location: True})
    guards_direction = "N"
    directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    direction_order = ["N", "E", "S", "W"]
    lab[guards_location] = "."

    while 0 <= guards_location[0] <= max_i and 0 <= guards_location[1] <= max_j:
        next_step = (
            guards_location[0] + directions[guards_direction][0],
            guards_location[1] + directions[guards_direction][1],
        )
        if next_step not in lab:
            break
        elif lab[next_step] == ".":
            guards_location = next_step
            visited[guards_location] = True
        else:
            guards_direction = direction_order[
                (direction_order.index(guards_direction) + 1) % len(direction_order)
            ]

    return len(visited)


@timer_func
def part_2(input_data):
    solution = 0
    max_j = len(input_data.splitlines()) - 1
    max_i = len(input_data.splitlines()[0]) - 1

    lab = {
        (i, j): v
        for j, line in enumerate(input_data.splitlines())
        for i, v in enumerate(line)
    }
    guards_location = list(lab.keys())[list(lab.values()).index("^")]
    guards_start = guards_location
    visited = defaultdict(str, {guards_location: "N"})
    visited_list = [guards_start]
    visited_list_dirs = ["N"]
    guards_direction = "N"
    directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    direction_order = ["N", "E", "S", "W"]
    lab[guards_location] = "."

    while 0 <= guards_location[0] <= max_i and 0 <= guards_location[1] <= max_j:
        next_step = (
            guards_location[0] + directions[guards_direction][0],
            guards_location[1] + directions[guards_direction][1],
        )
        if next_step not in lab:
            break
        elif lab[next_step] == ".":
            guards_location = next_step
            visited[guards_location] = guards_direction
            visited_list.append(guards_location)
            visited_list_dirs.append(guards_direction)
        else:
            guards_direction = direction_order[
                (direction_order.index(guards_direction) + 1) % len(direction_order)
            ]

    orig_lab = lab.copy()
    for i, node in enumerate(visited_list):
        if node == guards_start:
            continue

        lab = orig_lab.copy()
        lab[node] = "#"
        guards_location = visited_list[i - 1]
        visited = defaultdict(
            str, {visited_list[n]: visited_list_dirs[n] for n in range(i)}
        )
        guards_direction = visited_list_dirs[i - 1]

        while 0 <= guards_location[0] <= max_i and 0 <= guards_location[1] <= max_j:
            next_step = (
                guards_location[0] + directions[guards_direction][0],
                guards_location[1] + directions[guards_direction][1],
            )
            if next_step not in lab:
                break
            elif lab[next_step] == ".":
                guards_location = next_step
                if (
                        guards_location in visited
                        and guards_direction == visited[guards_location]
                ):
                    solution += 1
                    break
                visited[guards_location] = guards_direction
            else:
                guards_direction = direction_order[
                    (direction_order.index(guards_direction) + 1) % len(direction_order)
                ]
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
        assert str(sol) == example.answer_b
        print("Example Passed")
if not puzzle.answered_a:
    submit(part_1(data))
else:
    submit(part_2(data))
