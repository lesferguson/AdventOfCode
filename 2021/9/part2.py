def calc_basin(data, coord, basin):

    if (coord[0]-1, coord[1]) not in basin and data[(coord[0]-1, coord[1])] != 9:
        basin.add((coord[0]-1, coord[1]))
        calc_basin(data, (coord[0]-1, coord[1]), basin)
    if (coord[0]+1, coord[1]) not in basin and data[(coord[0]+1, coord[1])] != 9:
        basin.add((coord[0]+1, coord[1]))
        calc_basin(data, (coord[0]+1, coord[1]), basin)
    if (coord[0], coord[1]-1) not in basin and data[(coord[0], coord[1]-1)] != 9:
        basin.add((coord[0], coord[1]-1))
        calc_basin(data, (coord[0], coord[1]-1), basin)
    if (coord[0], coord[1]+1) not in basin and data[(coord[0], coord[1]+1)] != 9:
        basin.add((coord[0], coord[1]+1))
        calc_basin(data, (coord[0], coord[1]+1), basin)



def run(data):
    rel_low = []

    basin_sizes = []
    reference_data = data.copy()
    for coord, height in data.items():
        if height < reference_data[(coord[0] - 1, coord[1])] and \
                height < reference_data[(coord[0] + 1, coord[1])] and \
                height < reference_data[(coord[0], coord[1]-1)] and \
                height < reference_data[(coord[0], coord[1]+1)]:
            rel_low.append(coord)


    for low in rel_low:
        basin = set()
        calc_basin(data.copy(), low, basin)

        basin_sizes.append(len(basin))
        basin_sizes.sort()

    return basin_sizes[-3]*basin_sizes[-2]*basin_sizes[-1]
