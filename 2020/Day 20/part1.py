from copy import deepcopy
import collections
import time
input_file = "input.txt"
# input_file = "test.txt"

start_time = time.process_time()
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
    # print(tiles[tile])


for i, t in enumerate(tile_numbers):
    for k in tiles[t]:
        if k.startswith('face'):
            for tile in tile_numbers:
                if tile == t:
                    continue
                for f in ['face1', 'face2', 'face3', 'face4']:
                    if tiles[t][k] == tiles[tile][f] or tiles[t][k] == ''.join(reversed(tiles[tile][f])):
                        matches[t][k] = (tile, f)

prod = 1
for tile, match in matches.items():
    if len(match) < 3:
        prod *= int(tile)
        print(tile, match)

print(prod)

print(time.process_time() - start_time)
# print(tiles)