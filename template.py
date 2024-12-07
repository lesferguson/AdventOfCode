from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *

skip_examples = False


@timer_func
def solve_a(input_data):
    solution = 0
    #

    #
    return solution


@timer_func
def solve_b(input_data):
    solution = 0
    #

    #
    return solution


year, day = [int(param.strip(".py")) for param in os.path.abspath(__file__).split('\\')[-2:]]
puzzle = Puzzle(year=year, day=day)
