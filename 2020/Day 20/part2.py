import collections
from copy import deepcopy
import time
import numpy as np

input_file = "input.txt"
# input_file = "test.txt"


data = [line.strip() for line in open(input_file).readlines()]
# data = [tuple([col for col in line.strip().split()]) for line in open(input_file).readlines()]
# data = open(input_file).read()
# data = [[val for val in line.strip().split(",")] for line in open(input_file).readlines()]

matches = collections.defaultdict(dict, {})
tiles = {}
tile_numbers = []
for line in data:
    if line.startswith("Tile"):
        tile_num = line[5:-1]
        tile_numbers.append(tile_num)
        tiles[tile_num] = {'data': []}
        continue
    elif not line:
        continue
    tiles[tile_num]['data'].append(line)

for tile in tiles:
    tiles[tile]['face1'] = tiles[tile]['data'][0]
    tiles[tile]['face2'] = ''
    tiles[tile]['face3'] = tiles[tile]['data'][-1]
    tiles[tile]['face4'] = ''
    for i in range(len(tiles[tile]['data'])):
        tiles[tile]['face4'] += tiles[tile]['data'][i][0]
        tiles[tile]['face2'] += tiles[tile]['data'][i][-1]

for i, t in enumerate(tile_numbers):
    for k in tiles[t]:
        if k.startswith('face'):
            for tile in tile_numbers:
                if tile == t:
                    continue
                for f in ['face1', 'face2', 'face3', 'face4']:
                    if tiles[t][k] == tiles[tile][f] or tiles[t][k] == ''.join(reversed(tiles[tile][f])):
                        matches[t][k] = tile

corners = []
for tile, match in matches.items():
    if len(match) < 3:
        corners.append(tile)

tile_map = np.full((int(np.sqrt(len(tiles))), int(np.sqrt(len(tiles)))), None)
tile_number_map = np.full((int(np.sqrt(len(tiles))), int(np.sqrt(len(tiles)))), None)
#
# print(corners[0])
start_time = time.process_time()

match_face = list(matches[corners[0]].keys())
tile_data = [[char for char in row] for row in tiles[corners[0]]['data']]
tile = np.array(tile_data)

if "face1" in match_face:
    tile = np.flip(tile, axis=0)
if "face4" in match_face:
    tile = np.flip(tile, axis=1)
tile_map[0][0] = tile
tile_number_map[0][0] = corners[0]

for i in range(len(tile_map)):
    for j in range(len(tile_map[i])):
        if tile_map[i][j] is not None:
            continue
        if j == 0:
            if tile_number_map[i - 1][j]:
                source_face = list(tile_map[i - 1][j][-1])
                for f, t in matches[tile_number_map[i - 1][j]].items():
                    r = 0
                    match = False
                    while r < 4 and not match:
                        new_tile = [[char for char in row] for row in deepcopy(tiles[t]['data'])]
                        new_tile = np.rot90(new_tile, r)
                        face = list(new_tile[0])
                        if source_face == face:
                            match = True
                        if source_face == list(reversed(face)):
                            new_tile = np.flip(new_tile, axis=1)
                            match = True
                        if match:
                            tile_map[i][j] = new_tile
                            tile_number_map[i][j] = t

                        r += 1
                    if match:
                        break
        else:
            if tile_number_map[i][j - 1]:
                source_face = [tile_map[i][j - 1][k][-1] for k in range(len(tile_map[i][j - 1]))]
                # print(source_face)
                for f, t in matches[tile_number_map[i][j - 1]].items():
                    r = 0
                    match = False
                    while r < 4 and not match:
                        new_tile = [[char for char in row] for row in deepcopy(tiles[t]['data'])]
                        new_tile = np.rot90(new_tile, r)
                        face = [new_tile[k][0] for k in range(len(new_tile))]
                        if source_face == face:
                            match = True
                        if source_face == list(reversed(face)):
                            new_tile = np.flip(new_tile, axis=0)
                            match = True
                        if match:
                            tile_map[i][j] = new_tile
                            tile_number_map[i][j] = t

                        r += 1
                    if match:
                        break

picture = ''
for i in range(len(tile_map)):  # len(tile_map)
    row = collections.defaultdict(str, {})
    for j in range(len(tile_map[i])):
        for k in range(len(tile_map[i][j])):
            row[k] += ''.join(tile_map[i][j][k][1:-1])
    for k in range(len(row)):
        if k == 0 or k == len(row) - 1:
            continue
        picture += row[k] + '\n'
picture = picture[:-1]
picture = np.array([[char for char in line] for line in picture.split("\n")])

snek_count = 0
transformations = set()
for r in range(4):
    new_picture = np.rot90(picture, r)
    picture_string = '\n'.join([''.join(line) for line in new_picture])
    transformations.add(picture_string)

flipped_picture = np.flip(picture, axis=0)
for r in range(4):
    new_picture = np.rot90(flipped_picture, r)
    picture_string = '\n'.join([''.join(line) for line in new_picture])
    transformations.add(picture_string)

snake = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
snake_coords = []
for i in range(len(snake)):
    for j in range(len(snake[i])):
        if snake[i][j] == "#":
            snake_coords.append((i, j))

snake_count = 0
for image in transformations:
    image = [[char for char in line] for line in image.split("\n")]
    for i in range(len(image) - len(snake)):
        for j in range(len(image) - len(snake[0])):
            match = True
            for coord in snake_coords:
                coord_check = np.add((i, j), coord)
                if image[coord_check[0]][coord_check[1]] != "#":
                    match = False
                    break
            if match:
                snake_count += 1

print(snake_count)

exclude = snake_count * 15

count = 0
for char in '\n'.join([''.join(line) for line in picture]):
    if char == "#":
        count += 1

print(count - exclude)

print(time.process_time() - start_time)