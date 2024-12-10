def run(data):
    rel_low = []
    risk_level = 0
    reference_data = data.copy()
    for coord, height in data.items():
        if height < reference_data[(coord[0] - 1, coord[1])] and \
                height < reference_data[(coord[0] + 1, coord[1])] and \
                height < reference_data[(coord[0], coord[1]-1)] and \
                height < reference_data[(coord[0], coord[1]+1)]:
            rel_low.append(coord)
            risk_level+=1+height
    return risk_level
