from aocd import data, submit
from aocd.models import Puzzle
import os
from collections import defaultdict

def solve_a(input_data):
    solution = 0
    wires = {}
    lines = input_data.splitlines()
    circuit = {}
    for line in lines:
        pre, post = line.split(" -> ")
        circuit[post] = pre
    still_needs = {}

    new_lines=lines
    while(len(lines) > 0):
        lines = new_lines.copy()
        new_lines = []
        for line in lines:
            pre, post = line.split(" -> ")
            try:
                if "AND" in pre:
                    left, right = pre.split(" AND ")
                    wires[post] = wires[left] & wires[right]
                elif "OR" in pre:
                    left, right = pre.split(" OR ")
                    wires[post] = wires[left] | wires[right]
                elif "LSHIFT" in pre:
                    left, right = pre.split(" LSHIFT ")
                    wires[post] = wires[left] << int(right)
                elif "RSHIFT" in pre:
                    left, right = pre.split(" RSHIFT ")
                    wires[post] = wires[left] >> int(right)
                elif "NOT" in pre:
                    wire = pre.split("NOT ")[1]
                    wires[post] = ~int(wires[wire])
                else:
                    try:
                        wires[post] = int(pre)
                    except ValueError:
                        wires[post] = wires[pre]
            except KeyError:
                new_lines.append(line)



    return wires["a"]


def solve_b(input_data):
    solution = 0




    return solution





year, day = [ int(param.strip(".py")) for param in os.path.abspath(__file__).split('\\')[-2:]]
puzzle = Puzzle(year=year, day=day)

# for example in puzzle._get_examples():
#     if not puzzle.answered_a and example.answer_a:
#         print("-----------------")
#         print("input: ", example.input_data)
#         print("example a answer: ", example.answer_a)
#         sol = solve_a(example.input_data)
#         print("solution a answer: ", sol)
#         print(sol)
#         assert str(sol) == example.answer_a
#         print("Example Passed")
#     elif example.answer_b:
#         print("-----------------")
#         print("input: ", example.input_data)
#         print("example b answer: ", example.answer_b)
#         sol = solve_b(example.input_data)
#         print("solution b answer: ", sol)
#         # print(example.extra)
#         assert str(sol) == example.answer_b
#         print("Example Passed")
if not puzzle.answered_a:
    submit(solve_a(data))
else:
    submit(solve_b(data))