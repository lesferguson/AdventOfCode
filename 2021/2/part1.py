

def run(data):

    hor_pos = 0
    vert_pos = 0

    for instruction in data:
        if instruction[0] == "forward":
            hor_pos += int(instruction[1])
        elif instruction[0] == "down":
            vert_pos += int(instruction[1])
        elif instruction[0] == "up":
            vert_pos -= int(instruction[1])
    results = vert_pos*hor_pos

    return results