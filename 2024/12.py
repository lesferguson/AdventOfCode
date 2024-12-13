import itertools
from collections import defaultdict

from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *

skip_examples = False
override_example_input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
override_example_solution = None


@timer_func
def part_1(input_data):
    solution = 0
    #
    max_j = len(input_data.splitlines()) - 1
    max_i = len(input_data.splitlines()[0]) - 1

    farm = {
        (i, j): v
        for j, line in enumerate(input_data.splitlines())
        for i, v in enumerate(line)
    }
    gardens= defaultdict(list)
    adjacent_plots = [(i, j) for i in [-1,0,1] for j in [-1,0,1] if abs(i)+abs(j)==1]
    for plant_type in set(farm.values()):
        plant_plots = {plot: plant for plot, plant in farm.items() if plant == plant_type}

        for plant in plant_plots:
            plant_gardens = [garden for garden in gardens if garden.startswith(plant_type)]
            connected = False
            for garden in plant_gardens:
                if any((plant[0]+adjacent_plot[0], plant[1]+adjacent_plot[1]) in gardens[garden] for adjacent_plot in adjacent_plots):
                    connected=True
                    gardens[garden].append(plant)
            if not connected:
                i = 0
                while f"{plant_type}{i}" in gardens:
                    i +=1
                gardens[f"{plant_type}{i}"].append(plant)

        plant_gardens = [garden for garden in gardens if garden.startswith(plant_type)]
        for combo in itertools.combinations(plant_gardens, 2):
            g1 = set(gardens[combo[0]])
            g2 = set(gardens[combo[1]])
            if not g1.isdisjoint(g2):
                gardens[combo[0]] = list(g1.union(g2))
                del gardens[combo[1]]
        plant_gardens = [garden for garden in gardens if garden.startswith(plant_type)]
        for combo in itertools.combinations(plant_gardens, 2):
            g1 = set(gardens[combo[0]])
            g2 = set(gardens[combo[1]])
            if not g1.isdisjoint(g2):
                gardens[combo[0]] = list(g1.union(g2))
                del gardens[combo[1]]

    gardens = {garden: plots for garden, plots in gardens.items() if plots}
    for garden, plots in gardens.items():
        perimeter = 0
        for plot in plots:
            for adjacent_plot in adjacent_plots:
                if (plot[0] + adjacent_plot[0], plot[1] + adjacent_plot[1]) not in plots:
                    perimeter+=1
        solution += perimeter * len(plots)
    #
    return solution


@timer_func
def part_2(input_data):
    solution = 0
    #
    max_j = len(input_data.splitlines()) - 1
    max_i = len(input_data.splitlines()[0]) - 1

    farm = {
        (i, j): v
        for j, line in enumerate(input_data.splitlines())
        for i, v in enumerate(line)
    }
    gardens= defaultdict(list)
    adjacent_plots = [(i, j) for i in [-1,0,1] for j in [-1,0,1] if abs(i)+abs(j)==1]
    for plant_type in set(farm.values()):
        plant_plots = {plot: plant for plot, plant in farm.items() if plant == plant_type}

        for plant in plant_plots:
            plant_gardens = [garden for garden in gardens if garden.startswith(plant_type)]
            connected = False
            for garden in plant_gardens:
                if any((plant[0]+adjacent_plot[0], plant[1]+adjacent_plot[1]) in gardens[garden] for adjacent_plot in adjacent_plots):
                    connected=True
                    gardens[garden].append(plant)
            if not connected:
                i = 0
                while f"{plant_type}{i}" in gardens:
                    i +=1
                gardens[f"{plant_type}{i}"].append(plant)

        for _ in range(2):
            plant_gardens = [garden for garden in gardens if garden.startswith(plant_type)]
            for combo in itertools.combinations(plant_gardens, 2):
                g1 = set(gardens[combo[0]])
                g2 = set(gardens[combo[1]])
                if not g1.isdisjoint(g2):
                    gardens[combo[0]] = list(g1.union(g2))
                    del gardens[combo[1]]

            gardens = defaultdict(list, {garden: plots for garden, plots in gardens.items() if plots})
    for garden, plots in gardens.items():
        edges = {"N": set(), "E": set(), "S": set(), "W": set()}
        for plot in plots:
            if (plot[0]+0, plot[1]-1) not in plots:
                edges["N"].add(plot)
            if (plot[0]+1, plot[1]+0) not in plots:
                edges["E"].add(plot)
            if (plot[0]+0, plot[1]+1) not in plots:
                edges["S"].add(plot)
            if (plot[0]-1, plot[1]+0) not in plots:
                edges["W"].add(plot)
        for direction in edges:
            sides = []
            while len(edges[direction]):
                edge = edges[direction].pop()
                for i, side in enumerate(sides):
                    if direction in ["N", "S"] and ((edge[0]-1, edge[1]) in side or (edge[0]+1, edge[1]) in side):
                        sides[i].append(edge)
                        edge = None
                    elif direction in ["E", "W"] and ((edge[0], edge[1]-1) in side or (edge[0], edge[1]+1) in side):
                        sides[i].append(edge)
                        edge = None
                if edge:
                    sides.append([edge])
            print(sides)


    # for garden, plots in gardens.items():
    #     perimeter = 0
    #     for plot in plots:
    #         for adjacent_plot in adjacent_plots:
    #             if (plot[0] + adjacent_plot[0], plot[1] + adjacent_plot[1]) not in plots:
    #                 perimeter+=1
    #     solution += perimeter * len(plots)
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
