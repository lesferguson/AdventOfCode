from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *

skip_examples = False
override_example_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
override_example_solution = None


def find_path(graph, current_location, score, visited, distinct):
    if not distinct:
        if current_location in visited:
            return score
        visited[current_location] = True
    if graph[current_location] == 9:
        return score + 1
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (
                current_location[0] + direction[0],
                current_location[1] + direction[1],
        ) in graph and graph[
            (current_location[0] + direction[0], current_location[1] + direction[1])
        ] - 1 == graph[
            current_location
        ]:
            score = find_path(
                graph,
                (
                    current_location[0] + direction[0],
                    current_location[1] + direction[1],
                ),
                score,
                visited,
                distinct,
            )

    return score


@timer_func
def part_1(input_data):
    solution = 0
    #

    grid = {
        (i, j): int(v)
        for j, line in enumerate(input_data.splitlines())
        for i, v in enumerate(line)
    }

    for trailhead in [coord for coord in grid.keys() if grid[coord] == 0]:
        solution += find_path(grid, trailhead, 0, {}, False)

    #
    return solution


@timer_func
def part_2(input_data):
    solution = 0
    #

    grid = {
        (i, j): int(v)
        for j, line in enumerate(input_data.splitlines())
        for i, v in enumerate(line)
    }

    for trailhead in [coord for coord in grid.keys() if grid[coord] == 0]:
        solution += find_path(grid, trailhead, 0, {}, True)

    #
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
            print("input: ", example.input_data)
            print("expected answer (B): ", example_solution)
            sol = part_2(example.input_data)
            print("actual answer (B): ", sol)
            assert str(sol) == example_solution
            print("Example Passed")

if not puzzle.answered_a:
    submit(part_1(data))
else:
    submit(part_2(data))
