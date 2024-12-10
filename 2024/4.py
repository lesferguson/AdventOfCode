from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *
from numpy.f2py.crackfortran import word_pattern


@timer_func
def part_1(input_data):
    solution = 0

    word_search = {
        (i, j): v
        for j, line in enumerate(input_data.splitlines())
        for i, v in enumerate(line)
    }

    start_offsets = [
        [(1, 0), (2, 0), (3, 0)],
        [(-1, 0), (-2, 0), (-3, 0)],
        [(0, 1), (0, 2), (0, 3)],
        [(0, -1), (0, -2), (0, -3)],
        [(-1, -1), (-2, -2), (-3, -3)],
        [(1, 1), (2, 2), (3, 3)],
        [(1, -1), (2, -2), (3, -3)],
        [(-1, 1), (-2, 2), (-3, 3)],
    ]

    for coord, letter in word_search.items():
        if letter == "X":
            for offset in start_offsets:
                if all(
                        word_search.get((coord[0] + offset[n][0], coord[1] + offset[n][1]))
                        == ["M", "A", "S"][n]
                        for n in range(3)
                ):
                    solution += 1

    return solution


@timer_func
def part_2(input_data):
    solution = 0

    word_search = {
        (i, j): v
        for j, line in enumerate(input_data.splitlines())
        for i, v in enumerate(line)
    }

    start_offsets = [
        ([(-1, -1), (1, 1)], [(1, -1), (-1, 1)]),
        ([(-1, -1), (1, 1)], [(-1, 1), (1, -1)]),
        ([(1, 1), (-1, -1)], [(1, -1), (-1, 1)]),
        ([(1, 1), (-1, -1)], [(-1, 1), (1, -1)]),
    ]

    for coord, letter in word_search.items():
        if letter == "A":
            for offset in start_offsets:
                if all(
                        word_search.get(
                            (coord[0] + offset[i][n][0], coord[1] + offset[i][n][1])
                        )
                        == ["M", "S"][n]
                        for n in range(2)
                        for i in range(2)
                ):
                    solution += 1
    return solution


year, day = [
    int(param.strip(".py")) for param in os.path.abspath(__file__).split("\\")[-2:]
]
puzzle = Puzzle(year=year, day=day)

if puzzle.answered_b:
    part_1(data)
    part_2(data)
    exit()

if not puzzle.answered_a:
    submit(part_1(data))
else:
    submit(part_2(data))
