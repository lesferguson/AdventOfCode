from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *
import numpy as np

skip_examples = True
override_example_input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
override_example_solution = "480"


@timer_func
def part_1(input_data):
    solution = 0
    #
    input_data = input_data.splitlines()
    for i in range(0, len(input_data), 4):
        a_press = [int(num.split("+")[1]) for num in input_data[i].split(": ")[1].split(", ")]
        b_press = [int(num.split("+")[1]) for num in input_data[i + 1].split(": ")[1].split(", ")]
        prize_x, prize_y = [int(num.split("=")[1]) for num in input_data[i + 2].split(": ")[1].split(", ")]
        x = np.array([[a_press[0], b_press[0]], [a_press[1], b_press[1]]])
        y = np.array([[prize_x], [prize_y]])
        a_presses, b_presses = np.linalg.solve(x, y)
        a_presses = a_presses[0]
        b_presses = b_presses[0]
        if a_presses >= 0 and b_presses >= 0 and round(a_presses, 2) % 1 == 0 and round(b_presses,
                                                                                        2) % 1 == 0:
            solution += int(round(a_presses, 2)) * 3 + int(round(b_presses, 2))

    #
    return solution


@timer_func
def part_2(input_data):
    solution = 0
    #
    input_data = input_data.splitlines()
    for i in range(0, len(input_data), 4):
        a_press = [int(num.split("+")[1]) for num in input_data[i].split(": ")[1].split(", ")]
        b_press = [int(num.split("+")[1]) for num in input_data[i + 1].split(": ")[1].split(", ")]
        prize_x, prize_y = [int(num.split("=")[1]) for num in input_data[i + 2].split(": ")[1].split(", ")]
        prize_x += 10000000000000
        prize_y += 10000000000000
        x = np.array([[a_press[0], b_press[0]], [a_press[1], b_press[1]]])
        y = np.array([[prize_x], [prize_y]])
        a_presses, b_presses = np.linalg.solve(x, y)
        a_presses = a_presses[0]
        b_presses = b_presses[0]
        if a_presses >= 0 and b_presses >= 0 and round(a_presses, 2) % 1 == 0 and round(b_presses,
                                                                                        2) % 1 == 0:
            solution += int(round(a_presses, 2)) * 3 + int(round(b_presses, 2))

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
