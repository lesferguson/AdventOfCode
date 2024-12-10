

def run(data):

    hor_pos = 0
    vert_pos = 0
    aim = 0

    for instruction in data:
        if instruction[0] == "forward":
            hor_pos += int(instruction[1])
            vert_pos += aim*int(instruction[1])
        elif instruction[0] == "down":
            aim += int(instruction[1])
        elif instruction[0] == "up":
            aim -= int(instruction[1])
    results = vert_pos*hor_pos

    return results