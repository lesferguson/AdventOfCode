from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *
from utils.input_reader import default_parsers
import sys
from collections import defaultdict

sys.setrecursionlimit(1500)
skip_examples = False
override_example_input = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
override_example_solution = "64"


def parse_input(raw_input):
    """

        file_format types:
        raw: raw
        line: line separated
        tuple: tuple per line
        list: comma seperated list per line, if only 1 line, only return the list for that line
        grid: return a dictionary of coordinate keys, with the value of that coord in the values
        """
    formatted_input = default_parsers(raw_input, "grid", str)

    return formatted_input


min_score = 100000
min_distances = defaultdict(lambda: 100000)
best_path_tiles = defaultdict(dict)


def path_find(previous_node, current_node, current_score, end_node, visited, grid):
    global min_score
    for node in [(modifier[0] + current_node[0], modifier[1] + current_node[1]) for modifier in
                 [(0, 1), (0, -1), (1, 0), (-1, 0)]]:

        if node == end_node and current_score <= min_score:
            min_score = current_score
            for tile in visited:
                best_path_tiles[min_score][tile] = True
            return
        elif node == end_node:

            return

        if node == previous_node or grid[node] == "#" or node in visited:
            continue
        elif node == (
                current_node[0] + (current_node[0] - previous_node[0]),
                current_node[1] + (current_node[1] - previous_node[1])):
            next_score = 1
        else:
            next_score = 1001

        if current_score + next_score > min_distances[node] + 1001 or current_score + next_score > min_score:
            continue
        else:
            min_distances[node] = current_score + next_score

        visited[node] = True
        try:
            path_find(current_node, node, current_score + next_score, end_node, visited, grid)
        except RecursionError:
            pass
        del visited[node]
    return


@timer_func
def part_1(input_data):
    solution = 0
    global min_score
    #
    start_point = [coord for coord, val in input_data.items() if val == "S"][0]
    end_point = [coord for coord, val in input_data.items() if val == "E"][0]
    path_find((start_point[0] - 1, start_point[1]), start_point, 1, end_point, {start_point: True}, input_data)

    #
    return min_score


@timer_func
def part_2(input_data):
    solution = 0
    #
    global best_path_tiles
    global min_score
    #
    start_point = [coord for coord, val in input_data.items() if val == "S"][0]
    end_point = [coord for coord, val in input_data.items() if val == "E"][0]
    path_find((start_point[0] - 1, start_point[1]), start_point, 1, end_point, {start_point: True}, input_data)
    #
    return len(best_path_tiles[min_score]) + 1


year, day = [
    int(param.strip(".py")) for param in os.path.abspath(__file__).split("\\")[-2:]
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

min_score = 99999999999
min_distances = defaultdict(lambda: 99999999)
best_path_tiles = defaultdict(dict)
if not puzzle.answered_a:
    submit(part_1(parse_input(data)))
else:
    submit(part_2(parse_input(data)))
