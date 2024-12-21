from aocd import data, submit
from aocd.models import Puzzle
import os
from utils.decorators import *

skip_examples = False
override_example_input = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
override_example_solution = "9021"


def parse_input(raw_input):
    warehouse_raw, robot_raw = raw_input.split("\n\n")
    warehouse = {
        (i, j): v
        for j, line in enumerate(warehouse_raw.splitlines())
        for i, v in enumerate(line)
    }
    robot_raw = robot_raw.replace("\n", "")
    robot = [command for command in robot_raw]
    formatted_input = (warehouse, robot)
    return formatted_input


@timer_func
def part_1(input_data):
    solution = 0
    #
    warehouse = input_data[0]
    robot_location = [coord for coord, val in warehouse.items() if val == "@"][0]

    direction = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}
    for command in input_data[1]:
        # print(command)
        in_contact_with = ["@"]
        in_contact_with_coords = []
        current_location = robot_location

        while True:
            next_step = (current_location[0] + direction[command][0], current_location[1] + direction[command][1])
            in_contact_with.append(warehouse[next_step])
            in_contact_with_coords.append((next_step))
            if warehouse[next_step] != "O":
                break
            else:
                current_location = next_step

        if "#" in in_contact_with:
            continue
        else:
            warehouse[robot_location] = "."
            robot_location = in_contact_with_coords[0]
            for i in range(len(in_contact_with_coords)):
                warehouse[in_contact_with_coords[i]] = in_contact_with[i]

        # temp_x = max([cord[1] for cord in warehouse.keys()])
        # temp_y = max([cord[0] for cord in warehouse.keys()])
        # res = [[0] * (temp_y + 1) for ele in range(temp_x + 1)]
        #
        # for (i, j), val in warehouse.items():
        #     res[j][i] = str(val)
        # for row in res:
        #     print("".join(row))

    for tile, val in warehouse.items():
        if val == "O":
            solution += tile[0] + tile[1] * 100
        #

    return solution


@timer_func
def part_2(input_data):
    solution = 0
    #

    input_data = parse_input(input_data.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))

    warehouse = input_data[0]
    robot_location = [coord for coord, val in warehouse.items() if val == "@"][0]

    direction = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}

    # temp_x = max([cord[1] for cord in warehouse.keys()])
    # temp_y = max([cord[0] for cord in warehouse.keys()])
    # res = [[0] * (temp_y + 1) for ele in range(temp_x + 1)]

    # for (i, j), val in warehouse.items():
    #     res[j][i] = str(val)
    # for row in res:
    #     print("".join(row))
    for command in input_data[1]:
        # print(command)
        in_contact_with = ["@"]
        tiles_to_check = [(robot_location[0] + direction[command][0], robot_location[1] + direction[command][1])]
        wall = False
        blocks_new_locations = {
            (robot_location[0] + direction[command][0], robot_location[1] + direction[command][1]): "@"}
        blocks_old_locations = [robot_location]
        while True:
            if not tiles_to_check:
                break
            checking_tile = tiles_to_check.pop()
            in_contact_with.append(warehouse[checking_tile])
            if warehouse[checking_tile] == "#":
                break
            elif warehouse[checking_tile] == ".":
                continue
            elif command in ["^", "v"] and warehouse[checking_tile] == "]" and (
            checking_tile[0] - 1, checking_tile[1]) not in blocks_old_locations:
                tiles_to_check.append((checking_tile[0] - 1, checking_tile[1]))
            elif command in ["^", "v"] and warehouse[checking_tile] == "[" and (
            checking_tile[0] + 1, checking_tile[1]) not in blocks_old_locations:
                tiles_to_check.append((checking_tile[0] + 1, checking_tile[1]))

            blocks_old_locations.append(checking_tile)
            tiles_to_check.append((checking_tile[0] + direction[command][0], checking_tile[1] + direction[command][1]))
            blocks_new_locations[(checking_tile[0] + direction[command][0], checking_tile[1] + direction[command][1])] = \
                warehouse[checking_tile]

            #
        if "#" in in_contact_with:
            continue
        else:
            robot_location = (robot_location[0] + direction[command][0], robot_location[1] + direction[command][1])
            for tile in blocks_old_locations:
                warehouse[tile] = "."
            for tile, value in blocks_new_locations.items():
                warehouse[tile] = value

        # temp_x = max([cord[1] for cord in warehouse.keys()])
        # temp_y = max([cord[0] for cord in warehouse.keys()])
        # res = [[0] * (temp_y + 1) for ele in range(temp_x + 1)]
        #
        # for (i, j), val in warehouse.items():
        #     res[j][i] = str(val)
        # for row in res:
        #     print("".join(row))

    for tile, val in warehouse.items():
        if val == "[":
            solution += tile[0] + tile[1] * 100
        #
    #
    return solution


year, day = [
    int(param.strip(".py")) for param in os.path.abspath(__file__).split("\\")[-2:]
]
puzzle = Puzzle(year=year, day=day)

if puzzle.answered_b:
    part_1(parse_input(data))
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
            sol = part_2(example_input)
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
                sol = part_2(example_input)
            print("actual answer (override): ", sol)
            assert str(sol) == example_solution
            print("Example Passed")
if not puzzle.answered_a:
    submit(part_1(parse_input(data)))
else:
    submit(part_2(data))
