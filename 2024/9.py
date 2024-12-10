from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *
from collections import defaultdict, deque

skip_examples = False


@timer_func
def part_1(input_data):
    solution = 0
    #

    disk = {}
    free_space = deque()
    block_number = 0

    for i in range(len(input_data)):
        if i % 2 == 0:
            for n in range(int(input_data[i])):
                disk[block_number] = int(i / 2)
                block_number += 1
        else:
            for n in range(int(input_data[i])):
                free_space.append(block_number)
                block_number += 1

    for block in sorted(disk.copy().keys(), reverse=True):
        empty_spot = free_space.popleft()
        if empty_spot > block:
            break

        disk[empty_spot] = disk[block]
        del disk[block]

    for block, file_id in disk.items():
        solution += block * file_id

    #
    return solution


@timer_func
def part_2(input_data):
    solution = 0
    #
    disk = {}
    free_space = []
    block_number = 0
    files = {}
    for i in range(len(input_data)):
        if i % 2 == 0:
            files[int(i / 2)] = (block_number, int(input_data[i]))
            for n in range(int(input_data[i])):
                disk[block_number] = int(i / 2)
                block_number += 1
        else:
            for n in range(int(input_data[i])):
                free_space.append(block_number)
                block_number += 1

    for file in sorted(files.copy().keys(), reverse=True):
        for i in range(len(free_space)):
            if free_space[i] > files[file][0]:
                break
            elif len(free_space) > files[file][1] + i and [free_space[n] for n in range(i, i + files[file][1])] == [
                free_space[i] + n for n in range(files[file][1])]:
                for j in range(free_space[i], free_space[i] + files[file][1]):
                    disk[j] = file
                    free_space.pop(i)
                for j in range(files[file][1]):
                    del disk[files[file][0] + j]
                break

    for block, file_id in disk.items():
        solution += block * file_id
    #
    return solution


year, day = [int(param.strip(".py")) for param in os.path.abspath(__file__).split('\\')[-2:]]
puzzle = Puzzle(year=year, day=day)

if puzzle.answered_b:
    part_1(data)
    part_2(data)
    exit()

examples = puzzle._get_examples()

if not skip_examples:
    for example in examples:
        if not puzzle.answered_a and example.answer_a:
            print("-----------------")
            print("input: ", example.input_data)
            print("expected answer (A): ", example.answer_a)
            sol = part_1(example.input_data)
            print("actual answer (A): ", sol)
            assert str(sol) == example.answer_a
            print("Example Passed")
        elif example.answer_b:
            print("-----------------")
            print("input: ", example.input_data)
            print("expected answer (B): ", example.answer_b)
            sol = part_2(example.input_data)
            print("actual answer (B): ", sol)
            assert str(sol) == example.answer_b
            print("Example Passed")

if not puzzle.answered_a:
    submit(part_1(data))
else:
    submit(part_2(data))
